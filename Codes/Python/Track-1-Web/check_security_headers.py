#!/usr/bin/env python3
"""Track 1 — Observe security-related HTTP headers from a LAB URL only."""
from __future__ import annotations

import argparse
import urllib.request

INTERESTING = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Set-Cookie",
]


def main() -> None:
    p = argparse.ArgumentParser(description="Security header check — lab URLs only")
    p.add_argument("url", help="http://lab-host/... ")
    args = p.parse_args()
    if not args.url.startswith(("http://", "https://")):
        raise SystemExit("URL must start with http:// or https://")
    print("SAFETY: Use only against lab / training applications you control.\n")
    req = urllib.request.Request(args.url, headers={"User-Agent": "Phase3-Track1-HeaderCheck/1.0"})
    with urllib.request.urlopen(req, timeout=8) as resp:
        print(f"Status: {resp.status}")
        headers = {k.lower(): v for k, v in resp.headers.items()}
        for name in INTERESTING:
            val = headers.get(name.lower())
            print(f"{name}: {val if val else '(missing)'}")


if __name__ == "__main__":
    main()
