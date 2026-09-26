#!/usr/bin/env bash
# Phase-2 · Stage 10 — Basic evidence collection helper (lab only)
# Creates a timestamped folder with common host artifacts.
set -euo pipefail

STAMP=$(date +%Y%m%d_%H%M%S)
OUT="ir_lab_evidence_${STAMP}"
mkdir -p "$OUT"

echo "=== Lab evidence collection ==="
echo "Output directory: $OUT"
echo "Host: $(hostname)"
echo "Date: $(date -Is)"
echo

{
  echo "hostname: $(hostname)"
  echo "date: $(date -Is)"
  echo "user: $(whoami)"
  echo "uptime: $(uptime)"
} > "$OUT/meta.txt"

echo "[*] Process list"
ps aux > "$OUT/ps_aux.txt" 2>/dev/null || true

echo "[*] Listening sockets"
ss -tulnp > "$OUT/ss_tulnp.txt" 2>/dev/null || netstat -tulnp > "$OUT/ss_tulnp.txt" 2>/dev/null || true

echo "[*] Network addresses"
ip addr > "$OUT/ip_addr.txt" 2>/dev/null || ifconfig > "$OUT/ip_addr.txt" 2>/dev/null || true

echo "[*] Recent auth lines (if readable)"
if [[ -r /var/log/auth.log ]]; then
  tail -n 100 /var/log/auth.log > "$OUT/auth_tail.txt" 2>/dev/null || true
elif [[ -r /var/log/secure ]]; then
  tail -n 100 /var/log/secure > "$OUT/auth_tail.txt" 2>/dev/null || true
fi

echo "[*] Journal snippet (if available)"
journalctl -n 50 --no-pager > "$OUT/journal_tail.txt" 2>/dev/null || true

echo
echo "Collection finished. Review files under: $OUT"
echo "Remember: this is a learning helper, not a full forensic process."
