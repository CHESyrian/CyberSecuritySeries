# 07 — Sessions and Cookies in Detail

## Introduction

HTTP is a stateless protocol: each request is independent. Applications need a way to recognise the same client across multiple requests — for login state, shopping carts, preferences, and more. **Sessions** and **cookies** are the primary mechanisms used on the Web. This module explains how they work, the important cookie attributes, and the main risks and defences from a security perspective.

---

## Learning Objectives

- Explain why HTTP is described as stateless and how sessions restore continuity
- Describe how session identifiers are typically created, stored, and validated
- List and interpret the major cookie attributes (Secure, HttpOnly, SameSite, Path, Domain, Max-Age/Expires)
- Distinguish session cookies from persistent cookies
- Recognise common session-related risks (fixation, hijacking, CSRF interaction) and defensive controls
- Inspect cookies in a browser and in HTTP headers

---

## Core Concepts

### 1. Stateless Protocol, Stateful Applications

Without extra mechanisms, a server cannot know that request N+1 comes from the same user as request N. State must be carried either:

- In the client (cookies, local storage, hidden form fields), or
- On the server (session store keyed by an identifier the client presents), or
- In a self-contained token the client presents (e.g. signed JWT).

### 2. Sessions (Server-Side Model)

Typical flow:

1. Client authenticates (or otherwise starts a session).
2. Server creates a **session record** (user id, expiry, CSRF token, …) in memory, database, or cache.
3. Server sends a **session identifier** to the client (almost always in a cookie).
4. Client includes the identifier on subsequent requests.
5. Server looks up the session record and restores context.
6. Session is destroyed on logout or timeout.

Properties of a good session ID:

- Long, unpredictable (cryptographically random)
- Transmitted only over protected channels
- Bound to client attributes where practical (optional IP or User-Agent checks — with care)
- Rotated after privilege changes (login, elevation)

### 3. Cookies

A cookie is a small name–value pair that the server asks the browser to store and return.

**Set by the server:**

```
Set-Cookie: sessionid=abc123; Path=/; HttpOnly; Secure; SameSite=Lax
```

**Sent by the client on later requests:**

```
Cookie: sessionid=abc123; other=value
```

#### Important attributes

| Attribute | Purpose |
|-----------|---------|
| `Expires` / `Max-Age` | Lifetime. Session cookies omit these and die when the browser session ends. |
| `Domain` | Which hosts receive the cookie. Defaults to the setting host (no subdomains) if omitted carefully. |
| `Path` | URL path prefix that must match. |
| `Secure` | Cookie only sent over HTTPS. |
| `HttpOnly` | Cookie not accessible to JavaScript (`document.cookie`). Mitigates some XSS impact. |
| `SameSite` | Controls cross-site sending: `Strict`, `Lax`, or `None` (requires `Secure`). Important for CSRF defence. |
| `Prefix __Host-` / `__Secure-` | Extra restrictions enforced by browsers. |

### 4. Session Cookies vs Persistent Cookies

- **Session cookie** — no `Expires`/`Max-Age`; expected to disappear when the browser closes (implementation varies with “restore session” features).
- **Persistent cookie** — has an explicit lifetime; survives browser restarts until expiry or deletion.

### 5. Client-Side Storage Alternatives

- `localStorage` / `sessionStorage` — accessible to JavaScript; not automatically sent with requests; XSS can read them.
- Tokens in memory only — better for some SPA patterns; lost on refresh unless refreshed via a secure cookie.

### 6. Security Risks and Controls (Defensive View)

| Risk | Description | Primary controls |
|------|--------------|------------------|
| Session hijacking | Attacker obtains a valid session ID | HTTPS everywhere, `Secure` + `HttpOnly`, short lifetime, regenerate on login, monitor anomalies |
| Session fixation | Attacker forces a known session ID on the victim | Issue a new session ID after authentication |
| Cross-site request forgery (CSRF) | Browser attaches cookies to cross-site requests | `SameSite` cookies, anti-CSRF tokens, prefer non-simple requests |
| XSS reading session | Malicious script exfiltrates ID | `HttpOnly`, strong CSP, output encoding |
| Weak session IDs | Predictable or short identifiers | Cryptographically secure random generation, adequate length |

### 7. Inspecting Cookies

Browser developer tools → Application / Storage → Cookies.

Command-line / capture:

```bash
curl -v -c cookies.txt -b cookies.txt https://example.com/
```

In a packet capture you will see `Set-Cookie` in responses and `Cookie` in subsequent requests (on cleartext HTTP; on HTTPS the payload is encrypted).

---

## Practical Examples

```bash
# Save and replay cookies with curl
curl -c /tmp/cj -b /tmp/cj -v https://httpbin.org/cookies/set?lab=1
curl -c /tmp/cj -b /tmp/cj -v https://httpbin.org/cookies
```

In the browser:

1. Open developer tools → Network.
2. Load a site that sets cookies.
3. Examine the `Set-Cookie` response header and the stored cookie attributes.
4. Confirm which requests include the `Cookie` header.

---

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Session ID in the URL | Leaks via Referer, logs, browser history |
| Missing `Secure` flag on authentication cookies | Cookie can be sent over HTTP |
| Missing `HttpOnly` on session cookies | XSS can steal the session |
| `SameSite=None` without necessity | Increases CSRF exposure |
| Long-lived sessions without re-authentication | Stolen cookies remain valid for extended periods |
| Storing sensitive data in non-HttpOnly storage | Trivial theft via XSS |

---

## Best Practices

- Always use HTTPS for sites that set authentication or session cookies.
- Set `Secure`, `HttpOnly`, and an appropriate `SameSite` value on session cookies.
- Regenerate session IDs after login and privilege elevation.
- Keep session lifetimes as short as operationally practical; use refresh tokens carefully if needed.
- Prefer server-side session stores for critical state when revocation is required.
- Document cookie purpose and attributes in application security notes.
- In labs, practise reading cookie attributes and deliberately testing the effect of missing flags on a controlled application.

---

## Hands-on Exercise

1. Using browser tools, list all cookies for a chosen lab or public test site and note their attributes.
2. With `curl`, set a cookie, store it in a cookie jar, and show that a subsequent request sends it.
3. Explain what happens to a session cookie when the browser is fully closed (test on your browser).
4. Identify which cookie attributes would be required for a session cookie on a banking-style application and justify each.
5. (Optional) On a deliberately vulnerable lab application, observe the difference when `HttpOnly` is present vs absent (authorized lab only).

---

## Review Questions

1. Why does HTTP need sessions or cookies for logged-in user experience?
2. What does the `HttpOnly` attribute prevent?
3. What is the difference between a session cookie and a persistent cookie?
4. How does `SameSite=Lax` help with CSRF defence?
5. Why should a new session identifier be issued after successful authentication?

---

## Summary

Sessions restore continuity on top of a stateless protocol. Cookies are the dominant transport for session identifiers in browsers. Correct use of cookie attributes (`Secure`, `HttpOnly`, `SameSite`, lifetime) and sound session management (random IDs, regeneration, short expiry) form a large part of practical web application defence.

---

## Sources

- RFC 6265 (HTTP State Management Mechanism) and updates
- MDN — HTTP cookies, Set-Cookie
- OWASP Session Management Cheat Sheet
- OWASP CSRF Prevention Cheat Sheet
