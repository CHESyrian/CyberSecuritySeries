#!/usr/bin/env python3
# requires: pip install scapy
from scapy.all import sniff, wrpcap

# callback for each packet
packets = []

def pkt_handler(pkt):
    print(pkt.summary())   # ملخص سريع
    packets.append(pkt)

# start caprture
# NOTE : maybe your iface not 'wlp2s0', check it using : 'ifconfig'
sniff(iface="wlp2s0", prn=pkt_handler, count=10, timeout=15)

# save packets in pcap file
wrpcap("capture.pcap", packets)
print("Saved capture.pcap")
