#!/usr/bin/env python3
from scapy.all import rdpcap, Raw, TCP

pkts = rdpcap("capture_2.pcap")
for p in pkts:
    if p.haslayer(TCP):
        print(f" Summary : {p.summary()}")
        if p.haslayer(Raw):
            data = p[Raw].load
            try:
                print(f"Decode : {data.decode('utf-8', errors='replace')[:200]}")  # أول 200 حرف
            except:
                pass
