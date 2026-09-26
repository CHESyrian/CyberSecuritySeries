#!/usr/bin/env python3
"""
Track 2 — Score sources by failure bursts in a simple timestamp-free list.
Input: lines containing an IP and FAIL/SUCCESS keywords (stdin or demo).
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict

IP_RE = re.compile(r"(?:\d{1,3}\.){3}\d{1,3}")

DEMO = """
FAIL 10.0.0.5
FAIL 10.0.0.5
FAIL 10.0.0.5
FAIL 10.0.0.5
FAIL 10.0.0.5
FAIL 10.0.0.5
SUCCESS 10.0.0.8
FAIL 10.0.0.8
"""


def main() -> None:
    data = sys.stdin.read() if not sys.stdin.isatty() else DEMO
    fails: dict[str, int] = defaultdict(int)
    for line in data.splitlines():
        if not re.search(r"fail|invalid|failure", line, re.I):
            continue
        for ip in IP_RE.findall(line):
            fails[ip] += 1
    print("Failure burst scores (lab teaching):")
    for ip, n in sorted(fails.items(), key=lambda x: -x[1]):
        level = "high" if n >= 5 else "medium" if n >= 3 else "low"
        print(f"  {ip:16} failures={n:3d}  burst={level}")


if __name__ == "__main__":
    main()
