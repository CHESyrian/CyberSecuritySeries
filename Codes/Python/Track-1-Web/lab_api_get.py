#!/usr/bin/env python3
"""Track 1 — Simple GET against a LAB API/URL; print status and JSON/text preview."""
from __future__ import annotations

import argparse
import json
import urllib.request


def main() -> None:
    p = argparse.ArgumentParser(description="GET a lab URL — training targets only")
    p.add_argument("url", help="http://lab-host/api/...")
    args = p.parse_args()
    if not args.url.startswith(("http://", "https://")):
        raise SystemExit("URL must start with http:// or https://")
    print("SAFETY: Lab applications only.\n")
    req = urllib.request.Request(args.url, headers={"User-Agent": "Phase3-Track1-ApiGet/1.0"})
    with urllib.request.urlopen(req, timeout=8) as resp:
        body = resp.read(2000)
        print(f"Status: {resp.status}")
        ct = resp.headers.get("Content-Type", "")
        print(f"Content-Type: {ct}")
        text = body.decode("utf-8", errors="replace")
        if "json" in ct.lower():
            try:
                print(json.dumps(json.loads(text), indent=2)[:1500])
            except json.JSONDecodeError:
                print(text[:800])
        else:
            print(text[:800])


if __name__ == "__main__":
    main()
