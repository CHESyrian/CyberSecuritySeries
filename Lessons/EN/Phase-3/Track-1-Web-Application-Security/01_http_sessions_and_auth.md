# Track 1 · Stage 1.1 — HTTP, Sessions, and Authentication

## Why this stage matters
Web security starts with understanding how browsers and servers exchange requests, maintain state, and prove identity. Weak session or cookie handling undermines almost every control that follows.

## Learning objectives
- Describe HTTP methods, status codes, and security-relevant headers
- Explain cookies and attributes: Secure, HttpOnly, SameSite
- Compare basic auth, form/session auth, and token-style patterns at a high level
- Capture and document a normal login flow against a **lab** application only

## Safety checkpoint
Target URL/IP must be an intentional training app in your lab (DVWA, Juice Shop, etc.). Do not authenticate to production or third-party sites as part of this exercise.

## Core concepts
- **Request/response:** method, path, headers, body, status
- **State:** HTTP is stateless; sessions/cookies restore context
- **Session risks:** fixation, theft of session ID, missing timeout
- **Cookie flags:** reduce exposure to XSS (HttpOnly) and cleartext (Secure)

## Practice (lab only)
1. Browse the lab app while DevTools → Network is open
2. Log in with a **lab** account; note Set-Cookie and redirects
3. Record which cookies appear and which flags are set
4. Log out and confirm session invalidation behavior (if any)

## Companion code
`Codes/Python/07_web/lab_http_observe.py` — observe status/headers for a lab URL.

## Review
- What does HttpOnly protect against?
- Why is transmitting session IDs over HTTP dangerous?
