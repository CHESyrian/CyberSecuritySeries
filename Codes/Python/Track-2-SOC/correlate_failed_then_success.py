#!/usr/bin/env python3
"""
Track 2 — Teaching helper: given lines with FAILED/SUCCESS and an IP,
flag sources that show failures followed later by success (simple offline demo).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict

IP_RE = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")

# Demo input if stdin empty
DEMO = """
FAILED from 10.0.0.5
FAILED from 10.0.0.5
FAILED from 10.0.0.8
SUCCESS from 10.0.0.5
FAILED from 10.0.0.9
SUCCESS from 10.0.0.9
"""


def main() -> None:
    data = sys.stdin.read() if not sys.stdin.isatty() else DEMO
    events: dict[str, list[str]] = defaultdict(list)
    for line in data.splitlines():
        line_u = line.upper()
        ips = IP_RE.findall(line)
        if not ips:
            continue
        ip = ips[0]
        if "FAIL" in line_u or "INVALID" in line_u:
            events[ip].append("F")
        elif "SUCCESS" in line_u or "ACCEPTED" in line_u:
            events[ip].append("S")
    print("Sources with failure(s) then success (demo logic):")
    found = False
    for ip, seq in events.items():
        if "F" in seq and "S" in seq:
            # success appears after at least one failure in list order
            if seq.index("S") > seq.index("F"):
                print(f"  {ip}  sequence={''.join(seq)}")
                found = True
    if not found:
        print("  (none in input)")
    print("\nTeaching only — real correlation uses time windows and more context.")


if __name__ == "__main__":
    main()
