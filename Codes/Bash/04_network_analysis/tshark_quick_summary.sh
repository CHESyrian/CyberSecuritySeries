#!/usr/bin/env bash
# Phase-2 · Stage 4 — Quick tshark PCAP summary
# Educational. Works on captures taken inside the lab.
set -euo pipefail

PCAP="${1:-}"
if [[ -z "$PCAP" || ! -f "$PCAP" ]]; then
  echo "Usage: $0 <capture.pcap>"
  exit 1
fi

if ! command -v tshark >/dev/null 2>&1; then
  echo "tshark not found. Install Wireshark/tshark in the lab VM."
  exit 1
fi

echo "=== PCAP summary: $PCAP ==="
echo "Date: $(date -Is)"
echo

echo "--- Packet count ---"
tshark -r "$PCAP" -q -z io,stat,0 2>/dev/null | tail -n 5 || tshark -r "$PCAP" 2>/dev/null | wc -l

echo
echo "--- Protocol hierarchy (top) ---"
tshark -r "$PCAP" -q -z io,phs 2>/dev/null | head -n 40 || true

echo
echo "--- First 15 packet summaries ---"
tshark -r "$PCAP" -c 15 2>/dev/null || true

echo
echo "Tip: tshark -r $PCAP -Y 'dns or http' "
