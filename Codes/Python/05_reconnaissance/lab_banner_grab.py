#!/usr/bin/env python3
"""
Phase-2 · Stage 5 — Simple TCP banner grab (lab targets only)
Connects, reads a short banner, disconnects. No exploitation.
"""
from __future__ import annotations

import argparse
import socket


def grab(ip: str, port: int, timeout: float = 3.0) -> str:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        try:
            data = s.recv(256)
        except socket.timeout:
            data = b""
        return data.decode("utf-8", errors="replace").strip()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Grab a short TCP banner from a LAB service only."
    )
    parser.add_argument("ip", help="Lab target IP")
    parser.add_argument("port", type=int, help="TCP port")
    parser.add_argument("-t", "--timeout", type=float, default=3.0)
    args = parser.parse_args()

    print(f"Target: {args.ip}:{args.port}  (lab use only)")
    try:
        banner = grab(args.ip, args.port, args.timeout)
        if banner:
            print("Banner:")
            print(banner)
        else:
            print("(no banner received within timeout)")
    except (socket.timeout, ConnectionRefusedError, OSError) as exc:
        print(f"Connection failed: {exc}")

    print("SAFETY: Only use against systems inside your laboratory.")


if __name__ == "__main__":
    main()
