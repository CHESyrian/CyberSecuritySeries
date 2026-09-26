#!/usr/bin/env bash
# Phase-2 · Stage 2 — Linux host inspection helper
# Educational. Run on lab VMs you control.
set -euo pipefail

echo "=== Linux security-oriented inspection ==="
echo "Date : $(date -Is)"
echo "Host : $(hostname)"
echo "User : $(whoami) (UID=$(id -u))"
echo

echo "--- Identity ---"
id
echo

echo "--- Listening TCP/UDP sockets ---"
if command -v ss >/dev/null 2>&1; then
  ss -tulnp 2>/dev/null || ss -tuln
else
  netstat -tulnp 2>/dev/null || netstat -tuln
fi
echo

echo "--- Top processes by CPU (snapshot) ---"
ps aux --sort=-%cpu 2>/dev/null | head -n 8 || ps aux | head -n 8
echo

echo "--- Recent authentication-related lines (if readable) ---"
if [[ -r /var/log/auth.log ]]; then
  tail -n 15 /var/log/auth.log
elif [[ -r /var/log/secure ]]; then
  tail -n 15 /var/log/secure
elif command -v journalctl >/dev/null 2>&1; then
  journalctl -u ssh -n 15 --no-pager 2>/dev/null || journalctl -n 15 --no-pager 2>/dev/null || true
else
  echo "(no standard auth log readable with current privileges)"
fi

echo
echo "Inspection complete. Review output in your lab notebook."
