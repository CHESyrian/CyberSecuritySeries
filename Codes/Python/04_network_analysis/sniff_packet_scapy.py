#!/usr/bin/env python3
from scapy.all import sniff, wrpcap

def pkt_handler(pkt):
    print(pkt.summary())

pkts = sniff(filter="tcp and port 80", iface="wlp2s0", timeout=10, prn=pkt_handler) 
wrpcap("http_capture.pcap", pkts)
