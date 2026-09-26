#!/usr/bin/env python3
"""Track 2 — Print an alert triage table template for lab notes."""
print(
    """
Alert triage template (lab)
===========================
Date:
Analyst:

| Alert ID / title | Source host | Confidence (H/M/L) | TP/FP/Unknown | Reason | Next action |
|------------------|-------------|--------------------|---------------|--------|-------------|
|                  |             |                    |               |        |             |
|                  |             |                    |               |        |             |
|                  |             |                    |               |        |             |

Notes:
- Confidence ≠ severity
- Document FP causes so rules can be tuned
- Generate activity only against lab systems you control
"""
)
