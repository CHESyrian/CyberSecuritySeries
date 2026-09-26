#!/usr/bin/env bash
# Phase-2 · Stage 1 — Pre-change checklist reminder
# Prints a short safety checklist before lab experiments.
set -euo pipefail

cat << 'EOF'
========================================
  LAB SAFETY CHECKLIST (Stage 1)
========================================
[ ] Working only on VMs I own / control
[ ] Target IPs are inside the lab network
[ ] Snapshots taken for attacker + targets
[ ] Host-only / internal network isolation OK
[ ] No scans pointed at home router or Internet
[ ] Lab notebook ready for notes

If any box is unchecked — stop and fix it first.
========================================
EOF
