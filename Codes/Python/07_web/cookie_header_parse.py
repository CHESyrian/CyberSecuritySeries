#!/usr/bin/env python3
"""Phase-2/Track-1 — Parse Set-Cookie-like header strings from stdin or args (educational)."""
from __future__ import annotations

import sys


def analyze(set_cookie: str) -> None:
    parts = [p.strip() for p in set_cookie.split(";")]
    name_val = parts[0] if parts else ""
    flags = {p.lower() for p in parts[1:]}
    print(f"Pair: {name_val}")
    for flag in ("secure", "httponly"):
        print(f"  {flag}: {'yes' if flag in flags else 'no'}")
    samesite = next((p for p in parts[1:] if p.lower().startswith("samesite")), None)
    print(f"  samesite: {samesite.split('=', 1)[-1] if samesite and '=' in samesite else (samesite or 'not set')}")


def main() -> None:
    if len(sys.argv) > 1:
        analyze(" ".join(sys.argv[1:]))
    else:
        data = sys.stdin.read().strip()
        if not data:
            print("Usage: cookie_header_parse.py 'name=value; Secure; HttpOnly; SameSite=Lax'")
            print("   or: echo 'session=abc; HttpOnly' | cookie_header_parse.py")
            return
        for line in data.splitlines():
            if line.strip():
                analyze(line.strip())
                print()


if __name__ == "__main__":
    main()
