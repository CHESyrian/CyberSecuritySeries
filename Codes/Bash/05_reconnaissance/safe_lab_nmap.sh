#!/usr/bin/env bash
# Phase-2 · Stage 5 — Safe lab-oriented Nmap wrapper
# ONLY use against IPs inside your isolated laboratory.
set -euo pipefail

TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "Usage: $0 <lab-target-ip>"
  echo "Example: $0 192.168.56.10"
  echo
  echo "SAFETY: Do not point this at the public Internet or systems you do not own."
  exit 1
fi

if ! command -v nmap >/dev/null 2>&1; then
  echo "nmap not found. Install it in your attacker lab VM."
  exit 1
fi

OUTDIR="${OUTDIR:-./nmap_lab_output}"
mkdir -p "$OUTDIR"
BASENAME="$OUTDIR/scan_${TARGET}_$(date +%Y%m%d_%H%M%S)"

echo "=== Safe lab Nmap scan ==="
echo "Target : $TARGET"
echo "Output : $BASENAME.*"
echo "Date   : $(date -Is)"
echo
echo "Confirm this IP is inside YOUR lab network. Continuing in 3 seconds..."
sleep 3

# Host discovery style + version detection, moderate timing
nmap -sS -sV -T3 --top-ports 100 -oA "$BASENAME" "$TARGET"

echo
echo "Scan finished. Review:"
echo "  $BASENAME.nmap"
echo "  $BASENAME.xml"
echo "  $BASENAME.gnmap"
