#!/usr/bin/env bash
# Phase-2 · Stage 1 — Lab connectivity helper
# Educational use only. Run inside your isolated laboratory.
set -euo pipefail

TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "Usage: $0 <lab-target-ip>"
  echo "Example: $0 192.168.56.10"
  exit 1
fi

echo "=== Lab connectivity check ==="
echo "Date : $(date -Is)"
echo "Host : $(hostname)"
echo "Target: $TARGET"
echo

echo "--- Local interfaces ---"
ip -brief addr 2>/dev/null || ifconfig 2>/dev/null || true
echo

echo "--- Reachability (3 probes) ---"
if ping -c 3 -W 2 "$TARGET"; then
  echo "[OK] Target responded to ICMP"
else
  echo "[!] No ICMP response (may be filtered; not necessarily down)"
fi
echo

echo "--- Quick TCP probe on common lab ports ---"
for port in 22 80 443 8080; do
  if timeout 1 bash -c "echo >/dev/tcp/$TARGET/$port" 2>/dev/null; then
    echo "  port $port : open (TCP connect succeeded)"
  else
    echo "  port $port : closed/filtered"
  fi
done

echo
echo "Done. Use only against systems you own or have explicit permission to test."
