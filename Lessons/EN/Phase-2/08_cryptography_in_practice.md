# Stage 8: Cryptography in Practice

## Why This Stage Matters

Phase-1 introduced cryptographic ideas at a conceptual level (confidentiality, integrity, authenticity, hashing, symmetric and asymmetric encryption).  
This stage connects those ideas to the artifacts and tools you actually encounter: certificates, TLS handshakes, hash utilities, and common configuration mistakes.

You will not become a cryptographer. You will become someone who can inspect real cryptographic objects and recognize when they are being used correctly or poorly.

---

## Learning Objectives

By the end of this stage you will be able to:

- Explain the practical role of hash functions, certificates, and TLS in everyday systems
- Use common command-line tools to compute hashes and inspect certificates
- Read the main fields of an X.509 certificate
- Describe what a TLS handshake achieves at a high level
- Recognize frequent real-world cryptographic misconfigurations
- Apply these skills only to systems and files inside your laboratory or other authorized scope

---

## Safety Checkpoint

Cryptographic inspection tools are generally passive and safe.  
 nevertheless:

- Only examine certificates and services that belong to your lab or for which you have authorization.
- Do not attempt to break or attack cryptographic implementations.
- Treat any private keys you encounter in lab materials as sensitive even inside the lab.

---

## 1. Hash Functions in Daily Work

A cryptographic hash function takes arbitrary input and produces a fixed-size digest. Practical properties:

- Deterministic (same input → same output)
- Fast to compute
- Hard to invert (pre-image resistance)
- Hard to find collisions for secure algorithms

Common uses you will see:

- Verifying file integrity (download checksums)
- Storing password representations (with salt and proper algorithms)
- Digital signatures and certificate operations
- Detecting changes in forensic or monitoring contexts

Useful tools:

```bash
sha256sum file.bin
sha256sum file.bin > file.bin.sha256
sha256sum -c file.bin.sha256
```

Older algorithms such as MD5 and SHA-1 are no longer considered secure for collision resistance. Prefer SHA-256 or stronger for new work.

---

## 2. Certificates and Public-Key Infrastructure (PKI) — Practical View

An **X.509 certificate** binds a public key to an identity (for example a domain name) and is signed by a trusted issuer (Certificate Authority).

When you connect to an HTTPS site, your browser typically:

1. Receives the server’s certificate.
2. Checks that it is signed by a CA it trusts.
3. Checks that the name matches the site you requested.
4. Checks validity dates and revocation status (when possible).
5. Uses the public key to help establish a secure session.

Key fields worth recognizing when you inspect a certificate:

- Subject (who the certificate is for)
- Issuer (who signed it)
- Validity period (Not Before / Not After)
- Public key algorithm and size
- Subject Alternative Names (SANs)
- Signature algorithm

---

## 3. Inspecting Certificates with Command-Line Tools

```bash
# Fetch and show a server certificate (lab or authorized target)
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | openssl x509 -noout -text

# Inspect a certificate file
openssl x509 -in cert.pem -noout -subject -issuer -dates
openssl x509 -in cert.pem -noout -text
```

Practice on lab services or on public sites only for passive learning (viewing the certificate that is offered to everyone). Never attempt to interfere with production TLS.

---

## 4. TLS at a High Level

**TLS** (Transport Layer Security) provides confidentiality, integrity, and authentication for data in transit.

Simplified handshake goals:

- Agree on cryptographic algorithms (cipher suite)
- Authenticate the server (and optionally the client) using certificates
- Establish shared secret key material for the session
- Protect application data from eavesdropping and tampering

From a defensive and assessment perspective you care about:

- Whether TLS is used at all for sensitive channels
- Whether outdated protocol versions or weak cipher suites are enabled
- Whether certificates are valid, correctly named, and properly chained
- Whether mixed content or downgrade opportunities exist

Deep cryptanalysis is out of scope; configuration awareness is in scope.

---

## 5. Common Real-World Misconfigurations

| Issue | Why it matters |
|-------|----------------|
| Expired or not-yet-valid certificates | Clients reject the connection or users click through warnings |
| Name mismatch (certificate does not cover the hostname) | Breaks authentication of the server identity |
| Self-signed certificates in production | No trusted third-party attestation; easy to impersonate if users ignore warnings |
| Weak or deprecated protocols/ciphers (SSLv3, old TLS, RC4, etc.) | Known attacks become practical |
| Missing or incorrect certificate chains | Some clients cannot validate the certificate |
| Private keys stored insecurely or reused across many systems | Compromise of one system affects many |
| Hashing passwords with outdated algorithms or without salt | Credential theft becomes far more damaging |

In the lab you can intentionally misconfigure a service (wrong certificate, expired cert, weak ciphers) and observe how clients and scanners react. This is one of the safest ways to build intuition.

---

## 6. Linking Cryptography to Earlier Stages

- Stage 4 (Network analysis): You can capture a TLS handshake and observe the certificate messages (even if the application data remains encrypted).
- Stage 6 (Vulnerability assessment): Many scanner findings relate to weak crypto configuration or outdated cryptographic libraries.
- Stage 7 (Web applications): HTTPS configuration, cookie Secure/HttpOnly flags, and transport of session tokens are direct applications of these ideas.

---

## Common Mistakes

| Mistake | Consequence | Better practice |
|---------|-------------|-----------------|
| Treating “HTTPS is present” as “cryptography is done correctly” | Missed weak ciphers or invalid certificates | Inspect configuration and certificate details |
| Using MD5 or SHA-1 for security-sensitive integrity checks | Collision risks | Prefer SHA-256 or stronger |
| Ignoring certificate validity dates in lab experiments | Unrealistic mental model | Notice and document expiration behavior |
| Confusing encryption with hashing | Wrong tool for the job | Hash for integrity; encrypt for confidentiality |
| Storing lab private keys carelessly | Bad habits that transfer to real work | Treat keys as sensitive even in training |

---

## Best Practices

- Verify published checksums when you download security tools or lab images.
- Practice reading certificates until the main fields feel familiar.
- Prefer TLS 1.2+ and modern cipher suites in any service you configure.
- Document cryptographic findings with evidence (certificate text, scanner output, or packet capture references).
- Remember that cryptography is only as strong as its implementation, configuration, and key management.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/Python/08_cryptography/hash_file.py` | Compute MD5/SHA-1/SHA-256/SHA-512 of a file |
| `Codes/Bash/08_cryptography/hash_and_cert_check.sh` | Hash a file or inspect a certificate (file or live TLS endpoint) |

```bash
python3 Codes/Python/08_cryptography/hash_file.py /path/to/file
chmod +x Codes/Bash/08_cryptography/hash_and_cert_check.sh
./Codes/Bash/08_cryptography/hash_and_cert_check.sh hash /path/to/file
./Codes/Bash/08_cryptography/hash_and_cert_check.sh certfile lab.crt
# Passive view of a certificate offered by a service (lab or public learning only):
./Codes/Bash/08_cryptography/hash_and_cert_check.sh cert example.com:443
```


1. Compute the SHA-256 hash of a file in your lab and verify it.
2. Use `openssl` to inspect the certificate presented by a lab HTTPS service (or, for passive learning only, a public site).
3. Record the Subject, Issuer, and validity dates.
4. (Optional) Capture a TLS handshake with Wireshark and locate the certificate message.
5. List two cryptographic misconfigurations you would consider high priority if found on a real internet-facing service.
6. Write a short notebook entry summarizing what you inspected and what you observed.

**Success criteria:** You can obtain and read a certificate, compute a hash, and explain at least two common crypto-related weaknesses.

---

## Review Questions

1. What practical problem does a cryptographic hash solve when distributing files?
2. Name three fields you should examine when inspecting an X.509 certificate.
3. What high-level goals does a TLS handshake achieve?
4. Why is an expired certificate a problem?
5. Give one example of a weak cryptographic configuration that scanners often report.
6. How does cryptography knowledge improve the interpretation of findings from Stages 6 and 7?

---

## Summary

- Hash functions provide integrity checking; certificates bind identities to public keys; TLS protects data in transit.
- Command-line tools (`sha256sum`, `openssl`) let you inspect these objects directly.
- Most real-world cryptographic failures are configuration and operational problems, not broken algorithms.
- Passive inspection and lab misconfiguration experiments are safe ways to build skill.
- Cryptography appears throughout network analysis, vulnerability assessment, and web security — this stage connects those threads.

**Next stage:** Logging, Detection, and Blue Team Basics — shifting perspective from finding weaknesses to noticing and responding to activity.
