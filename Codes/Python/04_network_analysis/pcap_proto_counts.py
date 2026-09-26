#!/usr/bin/env python3
"""
Phase-2 Stage 4 — Count rough protocol layers from a PCAP using Scapy (lab PCAPs).
Requires: pip install scapy (in lab VM)
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter


def main() -> None:
    p = argparse.ArgumentParser(description="Protocol summary for a lab PCAP")
    p.add_argument("pcap", help="Path to .pcap/.pcapng captured in lab")
    args = p.parse_args()
    try:
        from scapy.all import rdpcap, IP, TCP, UDP, ICMP, DNS, ARP  # type: ignore
    except ImportError:
        print("scapy not installed. In the lab VM: pip install scapy")
        sys.exit(1)

    pkts = rdpcap(args.pcap)
    c: Counter[str] = Counter()
    for pkt in pkts:
        if pkt.haslayer(ARP):
            c["ARP"] += 1
        if pkt.haslayer(IP):
            c["IP"] += 1
        if pkt.haslayer(TCP):
            c["TCP"] += 1
        if pkt.haslayer(UDP):
            c["UDP"] += 1
        if pkt.haslayer(ICMP):
            c["ICMP"] += 1
        if pkt.haslayer(DNS):
            c["DNS"] += 1
    print(f"File: {args.pcap}  packets={len(pkts)}")
    for name, n in c.most_common():
        print(f"  {name:8} {n}")


if __name__ == "__main__":
    main()
