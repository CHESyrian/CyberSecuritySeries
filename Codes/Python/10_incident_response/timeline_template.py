#!/usr/bin/env python3
"""
Phase-2 · Stage 10 — Print a simple IR timeline template
Helps structure lab incident-response notes.
"""
from __future__ import annotations

from datetime import datetime, timezone


TEMPLATE = """
# Lab Incident Timeline
Generated: {now}

## Scenario (one sentence)
- 

## Scope
- Systems involved:
- Network:
- Out of scope:

## Timeline
| Time (UTC) | Phase              | Action / Observation | Evidence |
|------------|--------------------|----------------------|----------|
| T+0        | Detection          |                      |          |
| T+?        | Analysis           |                      |          |
| T+?        | Containment        |                      |          |
| T+?        | Eradication        |                      |          |
| T+?        | Recovery           |                      |          |
| T+?        | Lessons learned    |                      |          |

## Evidence collected
- [ ] Process list
- [ ] Listening sockets
- [ ] Auth log excerpt
- [ ] Packet capture (if relevant)
- [ ] Snapshots / notes

## Lessons / improvements
1. 
2. 

## Cleanup
- Restored from snapshot: yes / no
"""


def main() -> None:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(TEMPLATE.format(now=now))


if __name__ == "__main__":
    main()
