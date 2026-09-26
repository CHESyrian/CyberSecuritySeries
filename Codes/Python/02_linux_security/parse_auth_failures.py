#!/usr/bin/env python3
"""
Phase-2 · Stage 2 / 9 — Parse failed auth lines from a log file
Educational log helper for lab environments.
"""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

IP_RE = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")
FAIL_RE = re.compile(r"failed|invalid|failure", re.I)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize failed auth lines in a log file.")
    parser.add_argument(
        "logfile",
        nargs="?",
        default="/var/log/auth.log",
        help="Path to auth log (default: /var/log/auth.log)",
    )
    parser.add_argument("-n", "--top", type=int, default=15, help="Top N sources")
    args = parser.parse_args()

    path = Path(args.logfile)
    if not path.is_file():
        print(f"File not readable or missing: {path}")
        print("Try another path (e.g. /var/log/secure) or copy a lab log locally.")
        return

    sources: Counter[str] = Counter()
    fail_lines = 0
    with path.open("r", errors="replace") as f:
        for line in f:
            if not FAIL_RE.search(line):
                continue
            fail_lines += 1
            ips = IP_RE.findall(line)
            for ip in ips:
                sources[ip] += 1

    print(f"Log file     : {path}")
    print(f"Failure lines: {fail_lines}")
    print(f"Top sources  :")
    for ip, count in sources.most_common(args.top):
        print(f"  {count:5d}  {ip}")
    if not sources:
        print("  (no IPs parsed — log format may differ)")


if __name__ == "__main__":
    main()
