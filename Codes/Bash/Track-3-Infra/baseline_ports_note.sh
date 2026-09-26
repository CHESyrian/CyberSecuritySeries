#!/usr/bin/env bash
# Track 3 — Snapshot listening ports for baseline notes (lab VM)
set -euo pipefail
OUT="${1:-baseline_ports_$(date +%Y%m%d).txt}"
{
  echo "Host: $(hostname)"
  echo "Date: $(date -Is)"
  echo "---"
  ss -tulnp 2>/dev/null || netstat -tuln
} > "$OUT"
echo "Wrote $OUT — review and reduce unnecessary listeners on lab VMs only."
