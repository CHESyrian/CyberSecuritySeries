#!/usr/bin/env bash
# Phase-2 · Stage 2 / 9 — Summarize failed authentication attempts
# Lab use only. Requires readable auth logs.
set -euo pipefail

echo "=== Failed logon summary ==="
echo "Date: $(date -Is)"
echo

if [[ -r /var/log/auth.log ]]; then
  LOG=/var/log/auth.log
elif [[ -r /var/log/secure ]]; then
  LOG=/var/log/secure
else
  echo "No readable /var/log/auth.log or /var/log/secure"
  echo "Try: sudo journalctl -u ssh --no-pager | grep -i fail"
  exit 0
fi

echo "Source log: $LOG"
echo
echo "--- Counts by apparent source (best-effort parse) ---"
grep -iE "failed|invalid|failure" "$LOG" 2>/dev/null \
  | grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' \
  | sort | uniq -c | sort -nr \
  | head -n 20 || echo "(no matching lines or no IPs parsed)"

echo
echo "--- Last 10 failure-related lines ---"
grep -iE "failed|invalid|failure" "$LOG" 2>/dev/null | tail -n 10 || true
