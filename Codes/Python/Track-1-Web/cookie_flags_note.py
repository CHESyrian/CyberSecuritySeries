#!/usr/bin/env python3
"""Track 1 — Print a checklist of cookie security flags to look for in lab apps."""
print(
    """
Cookie flag checklist (lab observation)
=======================================
[ ] Secure     — sent only over HTTPS
[ ] HttpOnly   — not readable from JavaScript
[ ] SameSite   — Lax / Strict / None (None requires Secure)

How to check in the lab:
  1. Open the lab app in a browser
  2. DevTools → Application (or Storage) → Cookies
  3. Or DevTools → Network → login response → Set-Cookie headers
  4. Record findings in your notebook with the lab URL and date

SAFETY: Lab / training applications only.
"""
)
