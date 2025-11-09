#!/usr/bin/env python3
"""
net_capture_report.py
Simple packet capture + report tool using Scapy.

Requirements:
    pip install scapy
On Windows: install Npcap and run as Administrator.
On Linux/macOS: run with sudo/root.

Usage examples:
    sudo python3 net_capture_report.py --iface eth0 --timeout 30 --out capture.pcap
    sudo python3 net_capture_report.py --iface wlan0 --count 500 --bpf "tcp" --out capture.pcap

Note:
  By AI (ChatGPT)
"""

import argparse
import time
import json
from collections import Counter, defaultdict
from scapy.all import sniff, wrpcap, IP, IPv6, Raw

def parse_args():
    p = argparse.ArgumentParser(description="Capture packets, save pcap and produce a simple report.")
    p.add_argument("--iface", "-i", required=True, help="Interface to capture on (e.g. eth0, wlan0)")
    p.add_argument("--timeout", "-t", type=int, default=None, help="Capture duration in seconds (mutually exclusive with --count)")
    p.add_argument("--count", "-c", type=int, default=None, help="Number of packets to capture (mutually exclusive with --timeout)")
    p.add_argument("--bpf", "-f", default=None, help="BPF filter (e.g. 'tcp port 80')")
    p.add_argument("--out", "-o", default="capture.pcap", help="Output pcap filename")
    p.add_argument("--report", "-r", default="report.json", help="Output JSON report filename")
    p.add_argument("--portscan-threshold", type=int, default=100, help="Distinct destination-port threshold to flag a host as scanning")
    return p.parse_args()

def key_ip(pkt):
    """Return tuple (src, dst) of IP addresses where possible."""
    if IP in pkt:
        return pkt[IP].src, pkt[IP].dst
    if IPv6 in pkt:
        return pkt[IPv6].src, pkt[IPv6].dst
    return None, None

def proto_name(pkt):
    """Return a simple protocol name (IP/TCP/UDP/ICMP/OTHER)."""
    if pkt.haslayer("TCP"):
        return "TCP"
    if pkt.haslayer("UDP"):
        return "UDP"
    if pkt.haslayer("ICMP") or pkt.haslayer("ICMPv6"):
        return "ICMP"
    if IP in pkt or IPv6 in pkt:
        return "IP"
    return pkt.name or "OTHER"

def human_bytes(n):
    for unit in ("B","KB","MB","GB","TB"):
        if n < 1024.0:
            return f"{n:.1f}{unit}"
        n /= 1024.0
    return f"{n:.1f}PB"

def main():
    args = parse_args()
    print(f"Starting capture on iface={args.iface} "
          f"{'(timeout='+str(args.timeout)+'s)' if args.timeout else ''} "
          f"{'(count='+str(args.count)+')' if args.count else ''} "
          f"{'(bpf='+args.bpf+')' if args.bpf else ''}")
    start = time.time()

    packets = []  # will be written to pcap at the end

    # analytics structures
    bytes_per_ip = Counter()          # ip -> bytes (sum of len(pkt))
    proto_counts = Counter()          # protocol -> count
    portscan_tracker = defaultdict(set)  # src_ip -> set(dst_ports)
    tcp_flags_counter = Counter()     # optional: track some TCP flags counts

    def pkt_handler(pkt):
        # store
        packets.append(pkt)

        pkt_len = len(bytes(pkt))
        src, dst = key_ip(pkt)
        if src:
            bytes_per_ip[src] += pkt_len
        if dst:
            bytes_per_ip[dst] += 0  # ensure key exists (optional)
        proto = proto_name(pkt)
        proto_counts[proto] += 1

        # track dest ports for port-scan detection (simple heuristic)
        try:
            if pkt.haslayer("TCP"):
                dport = pkt["TCP"].dport
                sport = pkt["TCP"].sport
                if src:
                    portscan_tracker[src].add(int(dport))
                # capture some tcp flags
                flags = pkt["TCP"].flags
                tcp_flags_counter[str(flags)] += 1
            elif pkt.haslayer("UDP"):
                dport = pkt["UDP"].dport
                if src:
                    portscan_tracker[src].add(int(dport))
        except Exception:
            pass

    # call sniff
    sniff_kwargs = dict(iface=args.iface, prn=pkt_handler, store=False)
    if args.bpf:
        sniff_kwargs['filter'] = args.bpf
    if args.count:
        sniff_kwargs['count'] = args.count
    if args.timeout:
        sniff_kwargs['timeout'] = args.timeout

    try:
        sniff(**sniff_kwargs)
    except PermissionError:
        print("Permission denied: run as root/Administrator or install required drivers (Npcap on Windows).")
        return
    except Exception as e:
        print("Error during capture:", e)
        return

    duration = time.time() - start
    print(f"Capture finished — captured {len(packets)} packets in {duration:.1f}s. Saving pcap to {args.out} ...")
    try:
        wrpcap(args.out, packets)
    except Exception as e:
        print("Failed to write pcap:", e)
        # still continue to report analytics

    # Produce report
    top_ips = bytes_per_ip.most_common(10)
    proto_summary = proto_counts.most_common()
    # detect port scanners (simple heuristic: many distinct dst ports)
    scanners = []
    for src, ports in portscan_tracker.items():
        if len(ports) >= args.portscan_threshold:
            scanners.append({"src": src, "unique_dst_ports": len(ports)})

    report = {
        "capture_interface": args.iface,
        "capture_duration_seconds": round(duration, 2),
        "packets_captured": len(packets),
        "pcap_file": args.out,
        "top_ips_by_bytes": [{"ip": ip, "bytes": bytes} for ip, bytes in top_ips],
        "protocol_counts": [{"protocol": p, "count": c} for p, c in proto_summary],
        "tcp_flags_summary": [{"flags": f, "count": c} for f, c in tcp_flags_counter.items()],
        "portscan_threshold": args.portscan_threshold,
        "detected_scanners": scanners,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start))
    }

    # Print human-friendly report
    print("\n==== Report ====")
    print(f"Interface: {report['capture_interface']}")
    print(f"Duration: {report['capture_duration_seconds']} s")
    print(f"Packets captured: {report['packets_captured']}")
    print("\nTop IPs by bytes:")
    for entry in report['top_ips_by_bytes']:
        print(f"  {entry['ip']:>20}  {entry['bytes']:>10} bytes  ({human_bytes(entry['bytes'])})")
    print("\nProtocols:")
    for p,c in proto_summary:
        print(f"  {p:>6} : {c}")
    if scanners:
        print("\nPossible port-scanners detected:")
        for s in scanners:
            print(f"  {s['src']} -> {s['unique_dst_ports']} unique destination ports (threshold {args.portscan_threshold})")
    else:
        print("\nNo hosts exceeded the port-scan threshold.")

    # write JSON report
    try:
        with open(args.report, "w") as fh:
            json.dump(report, fh, indent=2)
        print(f"\nJSON report written to {args.report}")
    except Exception as e:
        print("Failed to write report file:", e)

if __name__ == "__main__":
    main()
