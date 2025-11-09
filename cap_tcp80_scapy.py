#!/usr/bin/env python3
from scapy.all import sniff, TCP, IP, Raw

def handle(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].dport == 80 and pkt.haslayer(Raw):
        payload = pkt[Raw].load
        try:
            text = payload.decode('utf-8', errors='ignore')
            
            # extract request raw HTTP
            if text.startswith("GET") or text.startswith("POST"):
                first_line = text.splitlines()[0]
                host = ""
                for line in text.splitlines():
                    if line.lower().startswith("host:"):
                        host = line.split(":",1)[1].strip()
                        break
                print(f"{pkt[IP].src} -> {pkt[IP].dst} : {first_line} Host: {host}")
        except Exception as e:
            pass

sniff(iface="wlp2s0", prn=handle, filter="tcp port 80", store=0)
