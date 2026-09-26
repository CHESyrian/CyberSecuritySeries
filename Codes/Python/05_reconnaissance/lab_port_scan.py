#!/usr/bin/env python3
"""
Phase-2 · Stage 5 — Minimal educational TCP port scanner
LAB TARGETS ONLY. Prefer the Bash Nmap wrapper for real lab work;
this script teaches the socket concept.
"""
from __future__ import annotations

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def is_open(ip: str, port: int, timeout: float) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            s.connect((ip, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Educational TCP port scan — lab IPs only.")
    parser.add_argument("ip", help="Lab target IP")
    parser.add_argument(
        "-p",
        "--ports",
        default="22,80,443,8080,3306,445,139",
        help="Comma-separated ports",
    )
    parser.add_argument("-t", "--timeout", type=float, default=0.8)
    parser.add_argument("-w", "--workers", type=int, default=32)
    args = parser.parse_args()

    ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]
    print(f"Scanning {args.ip} ports={ports} (lab only)")
    print("-" * 40)

    open_ports: list[int] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(is_open, args.ip, p, args.timeout): p for p in ports}
        for fut in as_completed(futures):
            port = futures[fut]
            if fut.result():
                open_ports.append(port)
                print(f"  {args.ip}:{port} open")

    print("-" * 40)
    print(f"Open: {sorted(open_ports) if open_ports else 'none in list'}")
    print("SAFETY: Do not scan systems outside your laboratory.")


if __name__ == "__main__":
    main()
