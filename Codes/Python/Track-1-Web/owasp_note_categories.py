#!/usr/bin/env python3
"""Track 1 — Print OWASP-style category checklist for lab note-taking (not a scanner)."""
cats = [
    ("A01", "Broken Access Control", "IDOR, privilege issues on lab app objects"),
    ("A02", "Cryptographic Failures", "HTTP vs HTTPS, weak cookie flags"),
    ("A03", "Injection", "Lab SQLi/command challenges only"),
    ("A04", "Insecure Design", "Missing rate limits / business logic notes"),
    ("A05", "Security Misconfiguration", "Default creds, directory listing, headers"),
    ("A06", "Vulnerable Components", "Known outdated lab stacks (document versions)"),
    ("A07", "Auth Failures", "Session fixation, weak logout"),
    ("A08", "Data Integrity Failures", "Unchecked updates (conceptual)"),
    ("A09", "Logging Failures", "Failed logins not logged in lab app"),
    ("A10", "SSRF", "Only if intentional lab endpoint exists"),
]
print("Lab finding categories (map observations — do not attack production)\n")
for code, name, hint in cats:
    print(f"[ ] {code}  {name}")
    print(f"      note: {hint}\n")
