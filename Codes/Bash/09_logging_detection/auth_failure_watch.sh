#!/usr/bin/env bash
# Phase-2 · Stage 9 — Simple auth-failure watcher (lab)
# Follows auth log and highlights failure lines. Ctrl+C to stop.
set -euo pipefail

if [[ -r /var/log/auth.log ]]; then
  LOG=/var/log/auth.log
elif [[ -r /var/log/secure ]]; then
  LOG=/var/log/secure
else
  echo "No readable auth log. On systemd systems try:"
  echo "  journalctl -u ssh -f"
  exit 0
fi

echo "Watching $LOG for failure-related lines (Ctrl+C to stop)..."
echo "Date: $(date -Is)"
echo
tail -n 0 -F "$LOG" 2>/dev/null | grep --line-buffered -iE "failed|invalid|failure|accepted"
