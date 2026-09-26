#!/usr/bin/env python3
"""
Phase-2 · Stage 9 — Simple detection logic demo
Reads a text log (or stdin) and flags repeated failed logons by source IP.
Teaching example — not a production IDS.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

IP_RE = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")
FAIL_RE = re.compile(r"failed|invalid|failure", re.I)


def main() -> None:
    parser = argparse.ArgumentParser(description="Flag sources with many failed logons.")
    parser.add_argument(
        "logfile",
        nargs="?",
        help="Path to log file (default: stdin)",
    )
    parser.add_argument(
        "-t",
        "--threshold",
        type=int,
        default=5,
        help="Alert if failures from one IP >= threshold (default 5)",
    )
    args = parser.parse_args()

    counts: dict[str, int] = defaultdict(int)

    if args.logfile:
        path = Path(args.logfile)
        if not path.is_file():
            print(f"Cannot read {path}")
            sys.exit(1)
        lines = path.read_text(errors="replace").splitlines()
    else:
        lines = sys.stdin.read().splitlines()

    for line in lines:
        if not FAIL_RE.search(line):
            continue
        for ip in IP_RE.findall(line):
            counts[ip] += 1

    print(f"Threshold: {args.threshold} failures per source")
    print("-" * 40)
    alerts = [(ip, n) for ip, n in counts.items() if n >= args.threshold]
    alerts.sort(key=lambda x: x[1], reverse=True)
    if not alerts:
        print("No sources exceeded threshold.")
    else:
        print("ALERT candidates:")
        for ip, n in alerts:
            print(f"  {n:4d} failures  from  {ip}")
    print("-" * 40)
    print("This is a teaching detector. Real SIEM rules add time windows, allow-lists, and context.")


if __name__ == "__main__":
    main()
