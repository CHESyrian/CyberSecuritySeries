# 08 — Authentication and Authorization in Detail

## Introduction

**Authentication** answers “Who are you?”  
**Authorization** answers “What are you allowed to do?”

These two concepts are often conflated but must be designed and reviewed separately. This module covers common authentication mechanisms, session and token patterns, authorization models, and practical considerations for network and application security.

---

## Learning Objectives

- Clearly distinguish authentication from authorization
- Describe common authentication factors and protocols
- Explain password-based, key-based, token-based, and federated authentication patterns
- Outline major authorization models (ACLs, RBAC, ABAC)
- Relate AAA (Authentication, Authorization, Accounting) to network access control
- Identify typical failure modes and defensive practices

---

## Core Concepts

### 1. Definitions

| Term | Meaning |
|------|---------|
| Authentication | Verifying a claimed identity |
| Authorization | Determining permitted actions or resources for an authenticated (or anonymous) principal |
| Accounting / Auditing | Recording what happened for accountability and forensics |
| AAA | Combined framework used especially in network access (RADIUS, TACACS+, etc.) |

A principal may be a user, a service account, a device, or a process.

### 2. Authentication Factors

| Factor type | Examples |
|-------------|----------|
| Something you know | Password, PIN, recovery answers |
| Something you have | Hardware token, phone (OTP app / push), smart card, private key |
| Something you are | Biometrics (fingerprint, face) |
| Somewhere you are | Network location, geofencing (supplementary) |

**Multi-factor authentication (MFA)** combines at least two different types. MFA significantly raises the cost of account takeover.

### 3. Common Authentication Mechanisms

#### Passwords

- Still widespread; quality depends on length, uniqueness, and storage.
- Servers must store **password hashes** with a slow, salted algorithm (e.g. Argon2, bcrypt, scrypt) — never plaintext or reversible encryption.
- Transmission must be protected (TLS).
- Complementary controls: rate limiting, lockout or progressive delays, breach detection, password managers.

#### Public-key / Certificate authentication

- SSH keys, mutual TLS (mTLS), smart cards.
- Client proves possession of a private key without sending it.
- Strong when private keys are protected (passphrase, hardware token, TPM).

#### One-time passwords (OTP) and push

- TOTP (time-based), HOTP (counter-based), vendor push notifications.
- Phishing-resistant alternatives (FIDO2/WebAuthn) are preferred where possible.

#### Token-based and federated patterns

| Pattern | Description |
|---------|-------------|
| Session cookie | Server-side session keyed by opaque ID (see module 07) |
| Bearer token (API) | Client sends `Authorization: Bearer <token>` |
| JWT (JSON Web Token) | Self-contained, signed (and optionally encrypted) claims; validate signature, issuer, audience, expiry |
| OAuth 2.0 | Delegation framework — access tokens for APIs; not primarily an authentication protocol by itself |
| OpenID Connect (OIDC) | Identity layer on OAuth 2.0 — ID tokens for authentication |
| SAML | XML-based federated identity, common in enterprise SSO |

### 4. Authorization Models

#### Access Control Lists (ACLs)

- Per-object list of principals and permitted operations.
- Simple and explicit; can become hard to manage at scale.

#### Role-Based Access Control (RBAC)

- Users are assigned roles; roles carry permissions.
- Widely used in applications and cloud IAM.
- Risk: role explosion and overly broad roles.

#### Attribute-Based Access Control (ABAC)

- Decisions based on attributes of the user, resource, action, and environment (time, location, device posture).
- Flexible; requires a policy language and reliable attribute sources.

#### Other related concepts

- **Least privilege** — grant only the permissions required.
- **Separation of duties** — split critical tasks across roles.
- **Mandatory vs discretionary** controls (MAC vs DAC) — more common in specialised OS and military systems.

### 5. Network AAA

In network access control:

- **Authentication** — who is connecting (802.1X, captive portal, VPN credentials).
- **Authorization** — which VLAN, ACL, or resources the session receives.
- **Accounting** — session start/stop, bandwidth, timestamps.

Common protocols: RADIUS, TACACS+, Diameter. Cloud analogues appear as IAM policies and security groups.

### 6. Typical Failure Modes (Defensive Awareness)

| Failure | Example consequence |
|---------|---------------------|
| Broken authentication | Credential stuffing succeeds; session fixation |
| Missing function-level access control | User can invoke admin API endpoints |
| Insecure direct object reference | Changing an ID in the URL accesses another user’s data |
| Over-privileged service accounts | Compromise of one service yields broad access |
| Long-lived tokens without revocation | Stolen token remains valid |
| Improper certificate validation | MITM against TLS clients |

---

## Practical Examples

```bash
# HTTP Basic (lab only — prefer stronger methods)
curl -u user:pass https://httpbin.org/basic-auth/user/pass

# Bearer token pattern
curl -H "Authorization: Bearer eyJhbGciOi..." https://api.example.com/resource

# SSH public-key authentication (see module 05)
ssh -i ~/.ssh/id_ed25519_lab user@server
```

Inspect application login flows with browser developer tools: watch for redirects, `Set-Cookie`, and token responses (authorized targets only).

---

## Common Mistakes

| Mistake | Better practice |
|---------|-----------------|
| Rolling a custom crypto or token format | Use proven libraries and standards (OIDC, WebAuthn, well-reviewed JWT libraries) |
| Storing passwords in reversible form | Use modern password hashing |
| Authorizing only in the UI | Enforce authorization on every server-side request |
| Sharing service-account credentials across many systems | Unique credentials, short lifetime, rotation |
| Treating OAuth access tokens as proof of user identity alone | Understand the difference between access tokens and ID tokens |

---

## Best Practices

- Separate authentication and authorization logic clearly in design and code review.
- Prefer phishing-resistant MFA (FIDO2/WebAuthn) for high-value accounts.
- Enforce least privilege and review roles periodically.
- Protect credentials and tokens in transit (TLS) and at rest.
- Implement revocation or short expiry for tokens and sessions.
- Log authentication successes and failures, and authorization denials, with enough context for investigation.
- In labs, deliberately test both positive and negative authorization cases (access allowed vs denied).

---

## Hands-on Exercise

1. Map a login flow you use (web or SSH) and label each step as authentication, session establishment, or authorization.
2. Using browser tools on a lab application, identify how the session or token is presented after login.
3. Write a short policy in plain language for an RBAC system with roles “viewer”, “editor”, and “admin” on a document resource.
4. List three attributes you might use in an ABAC decision for remote access (user, device, environment).
5. (Optional) Configure a lab service to require key-based SSH authentication only and verify password login is rejected.

---

## Review Questions

1. What question does authentication answer? What question does authorization answer?
2. Name the three classic authentication factor types.
3. Why should password hashes be slow and salted?
4. What is the main idea of RBAC?
5. What does the “Accounting” component of AAA provide?

---

## Summary

Authentication establishes identity; authorization enforces policy on what that identity may do. Modern systems combine passwords, keys, tokens, federation, and MFA with models such as RBAC and ABAC. Network AAA extends the same ideas to network access. Clear separation of the two concerns, least privilege, and strong credential protection are foundational security practices.

---

## Sources

- NIST SP 800-63 Digital Identity Guidelines (concepts)
- OWASP Authentication and Access Control Cheat Sheets
- OAuth 2.0 / OpenID Connect specifications (high-level understanding)
- RADIUS / TACACS+ operational documentation
