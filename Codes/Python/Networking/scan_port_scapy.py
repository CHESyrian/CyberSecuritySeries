#!/usr/bin/env python3
from scapy.all import IP, TCP, sr1

target = "127.0.0.1"
ports = [22, 80, 443]
for p in ports:
    syn = IP(dst=target)/TCP(dport=p,flags="S")
    resp = sr1(syn, timeout=1, verbose=0)
    if resp is None:
        print(p, "no response")
    elif resp.haslayer(TCP) and resp[TCP].flags == 0x12:  # SYN+ACK
        print(p, "open (SYN/ACK)")
        # إرسال RST لإغلاق الاتصال
        rst = IP(dst=target)/TCP(dport=p,flags="R")
        sr1(rst, timeout=0.5, verbose=0)
    elif resp.haslayer(TCP) and resp[TCP].flags == 0x14:  # RST
        print(p, "closed (RST)")
    else:
        print(p, "filtered/other")
