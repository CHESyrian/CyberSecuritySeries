#!/usr/bin/env python3
from scapy.all import rdpcap, TCP, Raw

pkts = rdpcap("capture.pcap")
for p in pkts:
    if p.haslayer(TCP) and p.haslayer(Raw):
        data = p[Raw].load
        try:
            print(data.decode('utf-8', errors='replace')[:200])  # مثال: أول 200 حرف
        except:
            pass
