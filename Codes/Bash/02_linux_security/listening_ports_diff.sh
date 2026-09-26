#!/usr/bin/env bash
# Phase-2 / Track-3 — Compare two saved ss/netstat snapshots (baseline vs current)
set -euo pipefail
A="${1:-}"
B="${2:-}"
if [[ -z "$A" || -z "$B" || ! -f "$A" || ! -f "$B" ]]; then
  echo "Usage: $0 baseline.txt current.txt"
  echo "Create snapshots with: Codes/Bash/Track-3-Infra/baseline_ports_note.sh"
  exit 1
fi
echo "=== Only in current ($B) ==="
comm -13 <(sort -u "$A") <(sort -u "$B") || true
echo "=== Only in baseline ($A) ==="
comm -23 <(sort -u "$A") <(sort -u "$B") || true
