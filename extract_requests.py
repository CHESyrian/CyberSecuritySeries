"""
extract_requests.py

Capture packets and extract:
 - HTTP requests (method, host, uri) from plain HTTP (port 80 or unencrypted payloads)
 - DNS queries (name, qtype)
 - TLS SNI (Server Name Indication) when pyshark/tshark is available

Usage examples:
  sudo python3 extract_requests.py --iface eth0 --timeout 30
  sudo python3 extract_requests.py --iface wlan0 --count 500 --out capture.pcap
  # Or analyze existing pcap:
  python3 extract_requests.py --pcap capture.pcap

Requirements:
  pip install scapy
  Optional (better TLS/SNI + dissected HTTP): pip install pyshark  and install tshark (Wireshark CLI)
  On Windows, install Npcap and run as Administrator.
"""

import argparse
import time
import json
from collections import Counter, defaultdict

# scapy imports
from scapy.all import sniff, wrpcap, rdpcap, IP, IPv6, TCP, UDP, Raw, DNS, DNSQR

# try import pyshark (optional)
try:
    import pyshark
    HAS_PYSHARK = True
except Exception:
    HAS_PYSHARK = False

def parse_args():
    p = argparse.ArgumentParser(description="Capture + extract HTTP/DNS/SNI info.")
    p.add_argument("--iface", "-i", help="Interface to capture on (e.g. eth0)")
    p.add_argument("--timeout", "-t", type=int, default=None, help="Capture duration seconds")
    p.add_argument("--count", "-c", type=int, default=None, help="Number of packets to capture")
    p.add_argument("--bpf", "-f", default=None, help="BPF filter (e.g. 'tcp port 80 or udp port 53')")
    p.add_argument("--out", "-o", default="capture.pcap", help="save captured pcap")
    p.add_argument("--pcap", help="analyze existing pcap file instead of live capture")
    p.add_argument("--use-pyshark", action="store_true", help="Prefer pyshark for SNI/HTTP fields if available")
    return p.parse_args()

def extract_from_scapy(pkt, results):
    """
    Try to extract HTTP (plain), DNS queries, and simple TLS heuristics (not SNI)
    """
    # DNS
    if pkt.haslayer(DNS) and pkt.getlayer(DNS).qdcount > 0:
        try:
            for i in range(pkt[DNS].qdcount):
                q = pkt[DNS].qd[i]
                qname = q.qname.decode() if isinstance(q.qname, bytes) else str(q.qname)
                qtype = q.qtype
                results['dns_queries'].append({
                    'src': pkt[IP].src if pkt.haslayer(IP) else (pkt[IPv6].src if pkt.haslayer(IPv6) else None),
                    'query_name': qname.rstrip('.'),
                    'qtype': qtype,
                    'time': pkt.time
                })
        except Exception:
            pass

    # HTTP (very simple): look for plain-text HTTP requests in TCP payload
    if pkt.haslayer(Raw) and pkt.haslayer(TCP):
        payload = bytes(pkt[Raw].load)
        # quick check for methods at start
        for method in (b"GET", b"POST", b"PUT", b"DELETE", b"HEAD", b"OPTIONS", b"PATCH"):
            if payload.startswith(method + b" "):
                try:
                    text = payload.split(b"\r\n\r\n", 1)[0].decode('utf-8', errors='ignore')
                    lines = text.splitlines()
                    request_line = lines[0] if lines else ""
                    method_part, uri_part, _ = request_line.split(" ", 2)
                    host = ""
                    for line in lines[1:]:
                        if line.lower().startswith("host:"):
                            host = line.split(":",1)[1].strip()
                            break
                    results['http_requests'].append({
                        'src': pkt[IP].src if pkt.haslayer(IP) else (pkt[IPv6].src if pkt.haslayer(IPv6) else None),
                        'dst': pkt[IP].dst if pkt.haslayer(IP) else (pkt[IPv6].dst if pkt.haslayer(IPv6) else None),
                        'method': method_part,
                        'uri': uri_part,
                        'host': host,
                        'time': pkt.time
                    })
                except Exception:
                    pass
                break

def analyze_with_pyshark_from_live(interface, bpf, count, timeout, results):
    """
    Use pyshark LiveCapture to get dissected HTTP and TLS fields (SNI).
    Requires tshark in PATH.
    """
    if not HAS_PYSHARK:
        print("pyshark not available. Install pyshark and tshark for better TLS/HTTP extraction.")
        return

    capture = pyshark.LiveCapture(interface=interface, bpf_filter=bpf)
    # sniff_continuously yields Packet objects with high-level fields
    start = time.time()
    try:
        for i, pkt in enumerate(capture.sniff_continuously(packet_count=count, timeout=timeout)):
            # DNS
            try:
                if hasattr(pkt, 'dns') and int(pkt.dns.count) > 0:
                    # pyshark dns may provide queries as multiple fields; handle gracefully
                    qname = getattr(pkt.dns, 'qry_name', None) or getattr(pkt.dns, 'qry_name_len', None)
                    results['dns_queries'].append({
                        'src': getattr(pkt.ip, 'src', None),
                        'query_name': qname,
                        'qtype': getattr(pkt.dns, 'qry_type', None),
                        'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
                    })
            except Exception:
                pass

            # HTTP
            try:
                if hasattr(pkt, 'http') and hasattr(pkt.http, 'request_method'):
                    results['http_requests'].append({
                        'src': getattr(pkt.ip, 'src', None),
                        'dst': getattr(pkt.ip, 'dst', None),
                        'method': getattr(pkt.http, 'request_method', None),
                        'uri': getattr(pkt.http, 'request_uri', None),
                        'host': getattr(pkt.http, 'host', None),
                        'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
                    })
            except Exception:
                pass

            # TLS SNI (server_name)
            try:
                # many tshark versions expose it under ssl.handshake.extensions_server_name or tls.handshake.extensions_server_name
                sni = None
                if hasattr(pkt, 'ssl') and hasattr(pkt.ssl, 'handshake_extensions_server_name'):
                    sni = pkt.ssl.handshake_extensions_server_name
                elif hasattr(pkt, 'tls') and hasattr(pkt.tls, 'handshake_extensions_server_name'):
                    sni = pkt.tls.handshake_extensions_server_name
                if sni:
                    results['tls_sni'].append({
                        'src': getattr(pkt.ip, 'src', None),
                        'dst': getattr(pkt.ip, 'dst', None),
                        'sni': str(sni),
                        'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
                    })
            except Exception:
                pass

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("pyshark capture error:", e)
    finally:
        capture.close()

def analyze_with_scapy_live(interface, bpf, count, timeout, results, out_pcap):
    packets = []

    def handler(pkt):
        packets.append(pkt)
        extract_from_scapy(pkt, results)

    sniff_kwargs = dict(iface=interface, prn=handler, store=False)
    if bpf:
        sniff_kwargs['filter'] = bpf
    if count:
        sniff_kwargs['count'] = count
    if timeout:
        sniff_kwargs['timeout'] = timeout

    sniff(**sniff_kwargs)

    # write pcap
    if out_pcap and packets:
        try:
            wrpcap(out_pcap, packets)
        except Exception as e:
            print("Failed to write pcap:", e)

def analyze_pcap_file(path, use_pyshark, results):
    # If using pyshark and available, prefer it for better TLS/HTTP fields
    if use_pyshark and HAS_PYSHARK:
        try:
            cap = pyshark.FileCapture(path)
            for pkt in cap:
                # DNS
                try:
                    if hasattr(pkt, 'dns') and getattr(pkt.dns, 'qry_name', None):
                        results['dns_queries'].append({
                            'src': getattr(pkt.ip, 'src', None),
                            'query_name': getattr(pkt.dns, 'qry_name', None),
                            'qtype': getattr(pkt.dns, 'qry_type', None),
                            'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
                        })
                except Exception:
                    pass
                # HTTP
                try:
                    if hasattr(pkt, 'http') and hasattr(pkt.http, 'request_method'):
                        results['http_requests'].append({
                            'src': getattr(pkt.ip, 'src', None),
                            'dst': getattr(pkt.ip, 'dst', None),
                            'method': getattr(pkt.http, 'request_method', None),
                            'uri': getattr(pkt.http, 'request_uri', None),
                            'host': getattr(pkt.http, 'host', None),
                            'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
                        })
                except Exception:
                    pass
                # TLS SNI
                try:
                    sni = None
                    if hasattr(pkt, 'ssl') and hasattr(pkt.ssl, 'handshake_extensions_server_name'):
                        sni = pkt.ssl.handshake_extensions_server_name
                    elif hasattr(pkt, 'tls') and hasattr(pkt.tls, 'handshake_extensions_server_name'):
                        sni = pkt.tls.handshake_extensions_server_name
                    if sni:
                        results['tls_sni'].append({
                            'src': getattr(pkt.ip, 'src', None),
                            'dst': getattr(pkt.ip, 'dst', None),
                            'sni': str(sni),
                            'time': float(pkt.sniff_timestamp) if hasattr(pkt, 'sniff_timestamp') else None
                        })
                except Exception:
                    pass
            cap.close()
            return
        except Exception as e:
            print("pyshark failed to read pcap:", e)
            # fallback to scapy

    # fallback: scapy read pcap and simple extraction
    try:
        pkts = rdpcap(path)
        for pkt in pkts:
            extract_from_scapy(pkt, results)
    except Exception as e:
        print("Failed reading pcap with scapy:", e)

def main():
    args = parse_args()

    results = {
        'http_requests': [],
        'dns_queries': [],
        'tls_sni': []
    }

    start = time.time()

    if args.pcap:
        print(f"Analyzing pcap file: {args.pcap} (use_pyshark={args.use_pyshark})")
        analyze_pcap_file(args.pcap, args.use_pyshark, results)
    else:
        if not args.iface:
            print("Live capture requires --iface. Use --pcap to analyze a file instead.")
            return
        # If user asked for pyshark and it's available, try it for improved fields
        if args.use_pyshark and HAS_PYSHARK:
            print("Starting live capture with pyshark (dissected fields)...")
            analyze_with_pyshark_from_live(args.iface, args.bpf, args.count, args.timeout, results)
        else:
            # Do scapy live capture (works without tshark)
            print("Starting live capture with scapy...")
            analyze_with_scapy_live(args.iface, args.bpf, args.count, args.timeout, results, args.out)

    duration = time.time() - start

    # Simple summaries
    http_count = len(results['http_requests'])
    dns_count = len(results['dns_queries'])
    sni_count = len(results['tls_sni'])

    print("\n==== Extraction Summary ====")
    print(f"Duration: {duration:.1f}s")
    print(f"HTTP requests found: {http_count}")
    print(f"DNS queries found: {dns_count}")
    print(f"TLS SNI entries found: {sni_count}")

    # Show top hosts/URIs
    if http_count:
        from collections import Counter
        hosts = Counter([h.get('host') or '<no-host>' for h in results['http_requests']])
        uris = Counter([h.get('uri') for h in results['http_requests']])
        print("\nTop HTTP hosts:")
        for host, c in hosts.most_common(10):
            print(f"  {host:40} {c}")
        print("\nTop requested URIs (sample):")
        for uri, c in uris.most_common(10):
            print(f"  {uri:60} {c}")

    if dns_count:
        from collections import Counter
        qnames = Counter([q.get('query_name') for q in results['dns_queries']])
        print("\nTop DNS queries:")
        for name, c in qnames.most_common(10):
            print(f"  {name:50} {c}")

    if sni_count:
        from collections import Counter
        snis = Counter([s.get('sni') for s in results['tls_sni']])
        print("\nTop TLS SNI names:")
        for name, c in snis.most_common(10):
            print(f"  {name:50} {c}")

    # Save JSON output
    out_json = "extracted_requests.json"
    try:
        with open(out_json, "w") as fh:
            json.dump(results, fh, default=str, indent=2)
        print(f"\nSaved full extraction to {out_json}")
    except Exception as e:
        print("Failed to write JSON:", e)

if __name__ == "__main__":
    main()
