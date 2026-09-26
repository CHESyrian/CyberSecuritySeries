#!/usr/bin/env bash
# Track 1 — Fetch response headers from a LAB URL (observation only)
set -euo pipefail
URL="${1:-}"
if [[ -z "$URL" ]]; then
  echo "Usage: $0 http://lab-host/path"
  exit 1
fi
echo "SAFETY: Lab / training URLs only."
echo "URL: $URL"
echo "---"
curl -sI "$URL" | head -n 40
