#!/usr/bin/env bash
# Track 2 — Count failure-like lines in a lab auth log (educational)
set -euo pipefail
LOG="${1:-/var/log/auth.log}"
if [[ ! -r "$LOG" ]]; then
  echo "Cannot read $LOG — copy a lab log locally or use journalctl"
  exit 0
fi
echo "Scanning $LOG for failure-related lines..."
grep -icE 'failed|invalid|failure' "$LOG" || true
