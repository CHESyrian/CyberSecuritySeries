#!/usr/bin/env python3
"""Track 2 — Demo threshold detection on a simple event list (offline teaching)."""
from __future__ import annotations

from collections import Counter

# Simulated lab events: source -> failure count
SAMPLE = ["10.0.0.5"] * 3 + ["10.0.0.8"] * 12 + ["10.0.0.9"] * 1


def main() -> None:
    threshold = 5
    counts = Counter(SAMPLE)
    print(f"Threshold = {threshold} failures per source\n")
    for src, n in counts.most_common():
        flag = "ALERT" if n >= threshold else "ok"
        print(f"  {src:16} {n:4d}  {flag}")


if __name__ == "__main__":
    main()
