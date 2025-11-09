#!/usr/bin/env python3
from scapy.all import sr1, IP, ICMP

pkt = IP(dst="8.8.8.8")/ICMP()
res = sr1(pkt, timeout=2)   # إرسال وانتظار إجابة لمدة ثانيتين
if res:
    res.show()
else:
    print("No reply")
