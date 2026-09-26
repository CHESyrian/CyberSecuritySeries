#!/usr/bin/env python3
"""
Phase-2 · Stage 1 — Quick lab port check
Educational only. Use solely against hosts inside your isolated lab.
"""
from __future__ import annotations

import argparse
import socket
import sys


def check_port(ip: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check common ports on a LAB target only."
    )
    parser.add_argument("ip", help="Lab target IP (e.g. 192.168.56.10)")
    parser.add_argument(
        "-p",
        "--ports",
        default="22,80,443,8080",
        help="Comma-separated ports (default: 22,80,443,8080)",
    )
    parser.add_argument("-t", "--timeout", type=float, default=1.0)
    args = parser.parse_args()

    ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]
    print(f"Target (lab only): {args.ip}")
    print(f"Ports: {ports}")
    print("-" * 40)
    for port in ports:
        status = "open" if check_port(args.ip, port, args.timeout) else "closed/filtered"
        print(f"  {args.ip}:{port} -> {status}")
    print("-" * 40)
    print("SAFETY: Do not use against systems outside your laboratory.")


if __name__ == "__main__":
    main()
