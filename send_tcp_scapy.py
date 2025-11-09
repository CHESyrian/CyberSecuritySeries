#!/usr/bin/env python3
from scapy.all import IP, TCP, send

pkt = IP(dst="192.168.1.10")/TCP(dport=9999, sport=12345, flags="PA")/b"Hello-From-Scapy\n"
send(pkt)
