# Stage 7: Web Application Security Fundamentals

## Why This Stage Matters

Web applications are one of the most common and most frequently attacked surfaces in real environments. They accept user input, talk to databases, manage sessions, and often handle sensitive data. Understanding how they fail — at a conceptual and laboratory level — is essential for both defenders and authorized testers.

Phase-1 introduced attack surfaces at a high level.  
This stage focuses specifically on web applications, using intentionally vulnerable lab targets so you can observe issues safely.

---

## Learning Objectives

By the end of this stage you will be able to:

- Describe the core components of a typical web application request/response cycle
- Explain the OWASP Top 10 categories at a conceptual level
- Identify common symptoms of injection, broken access control, and security misconfiguration in a lab setting
- Use a browser and a simple intercepting proxy to observe and safely modify lab traffic
- Recognize the difference between observing a weakness and exploiting it
- Apply strict rules so that all testing stays inside authorized laboratory applications

---

## Safety Checkpoint

**Only test web applications that you own or that are explicitly provided as intentionally vulnerable training targets** (DVWA, OWASP Juice Shop, WebGoat, etc.).

- Never test public websites, your employer’s applications, or any third-party site without written authorization.
- Never attempt to extract real personal data or disrupt service outside the lab.
- If a lab application contains reset or “safe mode” features, prefer those.

Unauthorized web application testing is illegal in most jurisdictions.

---

## 1. The Web Request/Response Cycle (Security View)

A simplified view:

1. Browser sends an HTTP(S) request (method, path, headers, optional body).
2. Web server / application receives it, performs logic, often talks to a database or other backend.
3. Application returns an HTTP response (status code, headers, body).
4. Browser renders the result and may store cookies or other client-side state.

Security issues can appear at every step: untrusted input, insecure processing, weak session handling, overly verbose errors, missing transport encryption, and more.

---

## 2. OWASP Top 10 — Conceptual Map

The OWASP Top 10 is a widely recognized awareness document that lists the most critical web application security risks. Categories evolve over time; the exact list is less important than the underlying ideas.

Core themes you should understand:

| Theme | Plain-language idea |
|-------|---------------------|
| **Injection** | Untrusted data is interpreted as commands or queries (SQL, OS, LDAP, etc.) |
| **Broken Access Control** | Users can act outside their intended permissions |
| **Cryptographic Failures** | Sensitive data is not properly protected in transit or at rest |
| **Insecure Design** | Missing or weak security controls by design |
| **Security Misconfiguration** | Insecure default settings, unnecessary features, verbose errors |
| **Vulnerable Components** | Outdated or vulnerable libraries and frameworks |
| **Authentication Failures** | Weak login, session, or credential handling |
| **Software and Data Integrity Failures** | Untrusted updates, insecure deserialization, etc. |
| **Logging & Monitoring Failures** | Missing or insufficient detection and response capability |
| **Server-Side Request Forgery (SSRF)** | Application can be tricked into making requests to unintended locations |

You are not expected to memorize every subcategory. You are expected to recognize the *patterns*.

---

## 3. Observing Traffic with Browser Tools and a Proxy

Modern browsers include developer tools that show requests, responses, cookies, and storage. An intercepting proxy (such as OWASP ZAP or Burp Community in a lab setting) lets you pause traffic, inspect it, and safely modify requests destined for lab applications.

Typical learning workflow:

1. Configure the browser to send lab traffic through the proxy.
2. Visit the intentionally vulnerable lab application.
3. Observe the raw HTTP requests and responses.
4. Note cookies, tokens, parameters, and headers.
5. Make small, controlled modifications *only against the lab target* and observe the application’s reaction.

The goal at this stage is understanding and observation, not weaponization.

---

## 4. High-Level Look at Selected Issues

### Injection (conceptual)

If user input is concatenated into a database query or system command without proper handling, an attacker may change the meaning of that query or command. In the lab you can observe how applications that fail to separate data from code behave when unexpected input arrives.

### Broken Access Control (conceptual)

Applications must enforce who is allowed to do what. Failures include:
- Accessing another user’s data by changing an identifier
- Reaching administrative functions without proper authorization
- Directory traversal style issues that expose unintended files

### Security Misconfiguration (conceptual)

Examples visible in labs:
- Default credentials still active
- Directory listing enabled
- Verbose error messages that reveal stack traces or software versions
- Unnecessary HTTP methods or services enabled

### Session and Authentication Issues (conceptual)

- Predictable session tokens
- Session tokens transmitted without secure flags
- Missing or weak logout / invalidation
- Brute-force friendly login forms without rate limiting (observe only in lab)

---

## 5. Safe Lab Methodology

1. Start with an intentionally vulnerable application in your isolated lab.
2. Map the application’s visible surface (pages, forms, parameters).
3. Observe normal traffic with browser tools or a proxy.
4. Introduce small, controlled variations and watch the responses.
5. Record what you observe (request, response, interesting behavior).
6. Reset the lab application when needed.
7. Never move from observation to destructive or data-extracting actions unless a later specialized course and explicit authorization say otherwise.

---

## Common Mistakes

| Mistake | Risk | Better practice |
|---------|------|-----------------|
| Testing a real public website | Legal consequences | Lab applications only |
| Confusing “I saw a strange response” with “I have a confirmed exploit” | Overstated findings | Document observation vs verified impact separately |
| Ignoring HTTPS and certificate issues in the lab | Missed learning | Note transport security even in training environments |
| Failing to reset the lab app after tests | Polluted state for later exercises | Use snapshots or built-in reset features |
| Focusing only on injection while ignoring access control | Incomplete mental model | Practice recognizing multiple categories |

---

## Best Practices

- Keep a dedicated browser profile or container for lab proxy work.
- Save interesting requests/responses (or proxy history) with notes.
- Prefer applications that publish their intended vulnerabilities (DVWA, Juice Shop, etc.) so you can compare what you find with what was designed to be present.
- Practice describing issues in plain language suitable for a non-technical reader.
- Remember that real professional testing requires a contract and Rules of Engagement; the lab is where you build skill safely.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/Python/07_web/lab_http_observe.py` | Fetch a lab URL and print status, headers, and a short body preview |

```bash
# Point only at intentionally vulnerable lab apps (DVWA, Juice Shop, etc.)
python3 Codes/Python/07_web/lab_http_observe.py http://192.168.56.10/dvwa/
```

Observation only — no attack payloads. Use solely against applications you own or that are published as training targets.


1. Start an intentionally vulnerable web application inside your lab (DVWA, Juice Shop, or similar).
2. Configure browser developer tools or a lab proxy to observe traffic to that application.
3. Perform normal browsing and form submissions; capture at least three interesting requests.
4. For each request, note: method, path, parameters, cookies, and response status.
5. Identify at least two places where user input is reflected or processed.
6. (Optional) Make one small, non-destructive modification to a parameter and record how the application responds.
7. Write a short summary in your notebook: what the application appears to do and any potential weakness categories you observed.

**Success criteria:** You have observed real lab web traffic, documented requests/responses, and linked observations to at least one OWASP-style category — all inside the lab boundary.

---

## Review Questions

1. Why are web applications such a frequent target?
2. Name three themes from the OWASP Top 10 and explain each in one sentence.
3. What is the difference between observing a weakness and exploiting it?
4. Why must web testing in this curriculum be limited to intentionally vulnerable lab applications?
5. What information can browser developer tools or an intercepting proxy show you?
6. Give one example of a security misconfiguration that might be visible in a lab application.

---

## Summary

- Web applications combine user input, business logic, data stores, and sessions — creating a rich attack surface.
- The OWASP Top 10 provides a durable map of the most important risk categories.
- Browser tools and intercepting proxies let you observe and safely interact with lab applications.
- The emphasis at this stage is understanding patterns and safe observation, not exploitation.
- Strict authorization boundaries remain mandatory.
- With web fundamentals in place, you can next examine cryptography as it appears in real systems and protocols.

**Next stage:** Cryptography in Practice — certificates, TLS, hashing tools, and common real-world misconfigurations.
