#!/usr/bin/env python3
# requires: pip install pyshark
# also requires tshark installed
import pyshark

cap = pyshark.LiveCapture(interface='wlp2s0', bpf_filter='tcp port 80')
for pkt in cap.sniff_continuously(packet_count=10):
    try:
        if 'HTTP' in pkt:
            host = pkt.http.host
            uri  = pkt.http.request_uri
            src  = pkt.ip.src
            dst  = pkt.ip.dst
            print(f"{src} -> {dst}  {host}{uri}")
    except AttributeError:
        pass
