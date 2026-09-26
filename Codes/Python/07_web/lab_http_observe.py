#!/usr/bin/env python3
"""
Phase-2 · Stage 7 — Observe HTTP response metadata from a LAB web app
Safe observation only (headers, status). No exploitation payloads.
Point only at intentionally vulnerable lab apps (DVWA, Juice Shop, etc.).
"""
from __future__ import annotations

import argparse
import sys

try:
    import urllib.request
except ImportError:
    print("urllib not available")
    sys.exit(1)


def observe(url: str, timeout: float = 5.0) -> None:
    req = urllib.request.Request(url, method="GET", headers={"User-Agent": "Phase2-LabObserver/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        print(f"URL           : {url}")
        print(f"Status        : {resp.status} {resp.reason}")
        print(f"Final URL     : {resp.geturl()}")
        print("--- Headers ---")
        for k, v in resp.headers.items():
            print(f"  {k}: {v}")
        body_preview = resp.read(200)
        print("--- Body preview (first 200 bytes) ---")
        print(body_preview.decode("utf-8", errors="replace"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Observe HTTP metadata from a LAB web application only."
    )
    parser.add_argument(
        "url",
        help="Lab URL, e.g. http://192.168.56.10/dvwa/ or http://127.0.0.1:3000/",
    )
    parser.add_argument("-t", "--timeout", type=float, default=5.0)
    args = parser.parse_args()

    if not args.url.startswith(("http://", "https://")):
        print("URL must start with http:// or https://")
        sys.exit(1)

    print("SAFETY: Use only against lab / intentionally vulnerable apps you control.\n")
    try:
        observe(args.url, args.timeout)
    except Exception as exc:  # noqa: BLE001 — educational script
        print(f"Request failed: {exc}")


if __name__ == "__main__":
    main()
