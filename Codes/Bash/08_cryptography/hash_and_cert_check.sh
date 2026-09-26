#!/usr/bin/env bash
# Phase-2 · Stage 8 — Hash file + optional certificate peek
# Educational cryptography helpers for the lab.
set -euo pipefail

usage() {
  echo "Usage:"
  echo "  $0 hash <file>"
  echo "  $0 cert <host:port>     # e.g. lab.local:443 or example.com:443 (passive view)"
  echo "  $0 certfile <cert.pem>"
  exit 1
}

CMD="${1:-}"
ARG="${2:-}"

case "$CMD" in
  hash)
    [[ -n "$ARG" && -f "$ARG" ]] || usage
    echo "=== SHA-256 ==="
    sha256sum "$ARG"
    if command -v sha1sum >/dev/null 2>&1; then
      echo "=== SHA-1 (legacy, not recommended for security) ==="
      sha1sum "$ARG"
    fi
    ;;
  cert)
    [[ -n "$ARG" ]] || usage
    if ! command -v openssl >/dev/null 2>&1; then
      echo "openssl not found"
      exit 1
    fi
    HOSTPORT="$ARG"
    echo "=== Certificate from $HOSTPORT (passive) ==="
    echo | openssl s_client -connect "$HOSTPORT" -servername "${HOSTPORT%%:*}" 2>/dev/null \
      | openssl x509 -noout -subject -issuer -dates 2>/dev/null \
      || echo "Could not retrieve certificate (TLS required / host unreachable)"
    ;;
  certfile)
    [[ -n "$ARG" && -f "$ARG" ]] || usage
    openssl x509 -in "$ARG" -noout -subject -issuer -dates -fingerprint -sha256 2>/dev/null \
      || openssl x509 -in "$ARG" -noout -text | head -n 40
    ;;
  *)
    usage
    ;;
esac
