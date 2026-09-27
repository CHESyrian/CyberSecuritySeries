# Track 1 · Stage 1.1 — HTTP, Sessions, and Authentication

## Why this stage matters

Web security starts with understanding how browsers and servers exchange requests, maintain state, and prove identity. Almost every subsequent control—access control, injection defenses, API security, and logging—depends on correct handling of the request/response cycle, cookies, and sessions.

HTTP itself is stateless. The server does not inherently “remember” previous requests from the same browser. Applications therefore invent state-management mechanisms (cookies, session identifiers, tokens). When those mechanisms are weak, an attacker who obtains a session identifier can impersonate a legitimate user. When authentication is poorly designed, the attacker may never need to steal a session at all.

This stage rebuilds and deepens the web foundations from Phase-2 Stage 7. You will move from high-level awareness to precise observation of headers, cookie attributes, and login flows against intentionally vulnerable laboratory applications only.

---

## Learning objectives

By the end of this stage you will be able to:

- Describe the structure of an HTTP request and response, including methods, status codes, and security-relevant headers
- Explain how cookies work and the security purpose of the `Secure`, `HttpOnly`, and `SameSite` attributes
- Compare basic authentication, form/session-based authentication, and token-style patterns at a conceptual level
- Capture and document a normal login and logout flow against a laboratory application
- Identify common session-related risks (fixation, theft, missing timeout, insecure transmission) and the primary mitigations for each

---

## Prerequisites

- Phase-2 complete, especially Stages 1 (lab safety), 4 (network analysis), and 7 (web fundamentals)
- An isolated lab containing at least one intentionally vulnerable web application (OWASP Juice Shop, DVWA, WebGoat, or equivalent)
- Browser with developer tools
- Optional: intercepting proxy (OWASP ZAP or Burp Suite Community) already restricted to lab traffic

---

## Safety checkpoint

**Non-negotiable rules for this stage:**

1. The target URL or IP must belong to an intentional training application that you control inside your isolated lab.
2. Do not authenticate to production systems, employer applications, or any third-party site as part of these exercises.
3. Use only the laboratory accounts supplied by the training application (or accounts you created yourself on that lab instance).
4. If you use a proxy, bind it to a local or lab-only interface and disable intercept when browsing any other site.
5. Snapshot the target VM or container before experimenting with logout or session-invalidation behavior.

All practice below assumes these constraints. If the target is outside your lab, stop.

---

## Core concepts

### 1. The HTTP request/response model

A client (usually a browser) sends a request; the server returns a response. The fundamental elements are:

| Element | Request | Response |
|---------|---------|----------|
| Start line | Method + path + HTTP version | Status code + reason + HTTP version |
| Headers | Host, User-Agent, Cookie, Authorization, Content-Type, … | Set-Cookie, Content-Type, Location, Cache-Control, security headers, … |
| Body | Optional (POST/PUT form data or JSON) | Optional (HTML, JSON, binary) |

Common methods and their typical security implications:

- **GET** — retrieve a resource; parameters appear in the URL (and therefore in logs, history, and referrers). Should not change server state.
- **POST** — submit data; body is not part of the URL. Preferred for login and state-changing actions.
- **PUT / PATCH / DELETE** — more common in APIs; still subject to the same authentication and authorization rules.
- **OPTIONS** — often used in CORS pre-flight; misconfigured CORS can widen attack surface.

Important status-code families:

- 2xx — success
- 3xx — redirection (watch for open-redirect issues later)
- 4xx — client error (401 Unauthorized, 403 Forbidden, 404 Not Found)
- 5xx — server error (can leak stack traces if verbose)

Security-relevant request headers you will examine:

- `Cookie` — carries session identifiers and other state
- `Authorization` — Basic, Bearer, etc.
- `Origin` / `Referer` — used by CSRF defenses and CORS
- `Content-Type` — must match what the server expects

Security-relevant response headers:

- `Set-Cookie` — issues new cookies with optional attributes
- `Location` — redirection target
- `Strict-Transport-Security` (HSTS)
- `Content-Security-Policy` (CSP)
- `X-Content-Type-Options`, `X-Frame-Options`, etc.

### 2. Why HTTP needs sessions

Because HTTP is stateless, the server cannot distinguish “this is still Alice” from “this is a completely new visitor” unless the client sends some proof of prior authentication. The classic solution is a **session identifier**:

1. User authenticates (username/password, or other credential).
2. Server creates a session record (in memory, database, or signed token).
3. Server sends a session ID to the client, usually inside a `Set-Cookie` header.
4. On subsequent requests the client automatically includes that cookie.
5. Server looks up the session ID and restores the user’s context (identity, role, shopping cart, etc.).

If an attacker obtains a valid session ID, the server treats the attacker as the legitimate user. This is why session handling is foundational.

### 3. Cookies and security attributes

A cookie is a small piece of data the server asks the browser to store and re-send. The most important security attributes are:

| Attribute | Purpose | Risk if missing |
|-----------|---------|-----------------|
| `Secure` | Cookie is sent only over HTTPS | Session ID can travel in cleartext |
| `HttpOnly` | Cookie is inaccessible to JavaScript | XSS can steal the session ID |
| `SameSite` | Restricts when the cookie is sent on cross-site requests (`Strict`, `Lax`, or `None`) | CSRF becomes easier |
| `Path` / `Domain` | Scope the cookie | Overly broad scope increases exposure |
| `Expires` / `Max-Age` | Lifetime | Long-lived sessions increase window for theft |
| `Priority` (Chrome) | Eviction order under storage pressure | Rarely security-critical |

Modern applications should set `Secure; HttpOnly; SameSite=Lax` (or `Strict`) on session cookies unless a deliberate cross-site need exists.

### 4. Authentication patterns (high level)

| Pattern | How it works | Typical risks |
|---------|--------------|---------------|
| **HTTP Basic** | Credentials base64-encoded in every request | Credentials always in transit; no logout without browser close; rarely used alone today |
| **Form + server session** | POST credentials → server issues session cookie | Session fixation, weak session IDs, missing logout invalidation |
| **Token-based (Bearer / JWT-style)** | After login the client receives a token and sends it in `Authorization` or a cookie | Token theft, missing expiration, insufficient signature verification, storage in localStorage (XSS risk) |
| **Multi-factor / passwordless** | Additional factor or WebAuthn | Implementation flaws in enrollment or recovery flows |

You do not need to implement these patterns yet; you need to recognize them when you observe traffic.

### 5. Common session risks and mitigations

- **Session fixation** — attacker forces a known session ID onto the victim before login. Mitigation: regenerate session ID after successful authentication.
- **Session theft** — via network sniffing, XSS, or malware. Mitigation: HTTPS only + HttpOnly + short lifetime + secure storage.
- **Missing timeout / logout** — session remains valid indefinitely. Mitigation: absolute and idle timeouts; server-side invalidation on logout.
- **Predictable session IDs** — sequential or low-entropy values. Mitigation: cryptographically strong random identifiers.
- **Cookie without Secure flag** — transmitted over HTTP. Mitigation: always set Secure (and prefer HSTS).

---

## Illustrative map: login flow (lab application)

```mermaid
sequenceDiagram
    participant B as Browser
    participant S as Lab Web App

    B->>S: GET /login
    S-->>B: 200 HTML form + Set-Cookie (pre-auth session optional)
    B->>S: POST /login (username, password)
    Note over S: Validate credentials<br/>Create/regenerate session
    S-->>B: 302 Redirect + Set-Cookie (session ID, Secure; HttpOnly; SameSite)
    B->>S: GET /dashboard (Cookie: session=…)
    S-->>B: 200 Authenticated page
    B->>S: POST /logout
    Note over S: Invalidate session server-side
    S-->>B: 302 + Set-Cookie (expire session)
```

In a well-designed application the session identifier changes after login and is destroyed on logout. In many training applications you will observe weaker behavior—exactly the point of the exercise.

---

## Detailed explanation of observation technique

1. Open the browser developer tools (F12) → Network tab. Enable “Preserve log”.
2. Navigate to the lab application’s login page. Clear existing cookies for that host if you want a clean start.
3. Submit valid laboratory credentials.
4. Inspect the POST request: method, path, body (form fields or JSON), and any `Authorization` header.
5. Inspect the response: status code (often 302), `Set-Cookie` headers, and the `Location` header.
6. Follow the redirect and examine subsequent requests; confirm the session cookie is present.
7. Note every cookie attribute (Secure, HttpOnly, SameSite, Path, Expires).
8. Perform a logout (if the application provides one) and verify whether the server invalidates the session or merely deletes the cookie client-side.
9. Optionally repeat the same flow through an intercepting proxy so you can see the raw bytes and easily copy requests later.

Document everything with timestamps, the exact lab URL, and the laboratory account name. Screenshots of the Network panel or proxy history are excellent evidence for your notebook.

---

## Practical example (DVWA / Juice Shop style)

Assume a lab instance of DVWA reachable at `http://192.168.56.101/dvwa`.

1. Browse to the login page with Network open.
2. Log in with the default laboratory credentials (commonly `admin` / `password` on a fresh DVWA—confirm on your own instance).
3. Observe a `Set-Cookie` containing `PHPSESSID=…` (or equivalent). On a default DVWA install the flags are often incomplete—note what is missing.
4. Navigate to a few internal pages; confirm the cookie is re-sent.
5. Click Logout and re-check whether the same session ID is still accepted on a protected page.

Repeat the same steps on Juice Shop (usually `http://localhost:3000` or a lab IP). Juice Shop uses more modern patterns and may set additional cookies or tokens; compare the two applications.

---

## Companion code

`Codes/Python/07_web/lab_http_observe.py` (or the Track-1 equivalent once published) can be pointed at a laboratory URL to print status code, selected headers, and redirect chain. Use it only against targets inside your lab.

Example conceptual usage:

```bash
python lab_http_observe.py --url http://192.168.56.101/dvwa/login.php
```

Never point such a script at production or third-party hosts.

---

## Common mistakes

- Forgetting to clear old cookies and therefore mixing sessions from previous tests.
- Assuming a cookie is “secure” because the page loaded over HTTPS while the `Secure` flag is still absent.
- Treating client-side logout (deleting the cookie in JavaScript) as equivalent to server-side invalidation.
- Capturing credentials or session IDs from real systems “just to practice.”
- Leaving an intercepting proxy enabled while browsing non-lab sites, which can leak traffic or break certificate validation.

---

## Best practices (defensive summary)

- Always issue session cookies with `Secure; HttpOnly; SameSite=Lax` (or stricter).
- Regenerate the session identifier after authentication.
- Implement both idle and absolute session timeouts.
- Invalidate the session server-side on logout.
- Prefer short-lived tokens plus refresh tokens over long-lived bearer tokens stored in localStorage.
- Log authentication successes and failures with sufficient context for later detection work (Track 2).

---

## Hands-on exercise

**Objective:** Produce a short laboratory notebook entry for one training application.

1. Choose DVWA, Juice Shop, or another intentional target in your lab.
2. Capture the full login flow (request + response headers, cookies, redirects).
3. Record every cookie name, value length (not the full secret), and attributes.
4. Attempt logout and test whether the old session ID still grants access.
5. Write two sentences: (a) what is correctly implemented, (b) what is missing or weak.
6. Optional: repeat the observation through ZAP or Burp with scope limited to the lab host.

Save the notebook entry with date, target IP/URL, and laboratory account used.

---

## Review questions

1. What does the `HttpOnly` attribute protect against, and what does it *not* protect against?
2. Why is transmitting a session identifier over plain HTTP dangerous even if the login form itself used HTTPS?
3. Explain the difference between regenerating a session ID after login and simply issuing a new cookie without invalidating the old one.
4. In a sequence diagram of a login flow, where should the server perform the credential check relative to issuing the authenticated session cookie?
5. A laboratory application sets `SameSite=None` without the `Secure` flag. What is the practical consequence?

---

## Summary

- HTTP is stateless; sessions and cookies restore context.
- Cookie attributes (`Secure`, `HttpOnly`, `SameSite`) are the first line of defense against theft and misuse.
- Authentication patterns differ, but all ultimately produce some form of proof that subsequent requests belong to an authenticated principal.
- Observation of real login traffic on intentional laboratory applications is the fastest way to internalize these concepts.
- Weak session handling undermines almost every later control; strong session handling is therefore non-negotiable.

---

## Sources and further reading

- RFC 6265 (HTTP State Management Mechanism) — cookie semantics
- OWASP Session Management Cheat Sheet
- OWASP Authentication Cheat Sheet
- MDN documentation on `Set-Cookie` attributes
- Phase-2 Stage 7 (Web Application Security Fundamentals) for prior context

All practical work remains restricted to authorized laboratory environments.
