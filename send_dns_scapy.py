#!/usr/bin/env python3
from scapy.all import sr1, IP, UDP, DNS, DNSQR

q = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com"))
ans = sr1(q, timeout=2)
if ans and ans.haslayer(DNS):
    ans.show()
