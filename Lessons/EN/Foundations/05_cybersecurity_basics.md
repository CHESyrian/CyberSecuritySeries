# Phase-0 · Cyber Security Basics

This module introduces the core vocabulary and concepts that appear in almost every security conversation. It stays at a conceptual level.

---

## Foundational Principles

### CIA Triad
- **Confidentiality** — only authorized parties can read the data.
- **Integrity** — data has not been altered in an unauthorized way.
- **Availability** — systems and data are usable when needed.

Almost every security control exists to support one or more of these three goals.

### Authentication, Authorization, Accounting (AAA)
- **Authentication** — proving identity (“Who are you?”).
- **Authorization** — deciding what that identity is allowed to do.
- **Accounting** (or Auditing) — recording what was done for later review.

### Least Privilege
Give every user and process only the minimum permissions required to perform their legitimate tasks.

### Defense in Depth
Use multiple independent layers of protection so that the failure of one layer does not lead to complete compromise.

### Attack Surface
The sum of all points where an unauthorized party could try to enter or extract data. Reducing unnecessary attack surface is a primary defensive strategy.

### Threat Modeling
A structured way of thinking about what can go wrong, who might attack, what they might want, and where the system is weak. It helps prioritize protective effort.

### Vulnerability, Exploit, Risk
- **Vulnerability** — a weakness that could be abused.
- **Exploit** — a method or technique that takes advantage of a vulnerability (we discuss the concept only).
- **Risk** — the combination of likelihood and impact. Risk is what organizations actually manage.

### Security Controls
Safeguards put in place to reduce risk. They can be technical (firewalls, encryption), administrative (policies, training), or physical (locks, cameras).

### Logging and Monitoring
- **Logging** — recording security-relevant events.
- **Monitoring** — actively watching those logs and other signals for signs of problems.
Without visibility, detection and response are almost impossible.

---

## Web Application Concepts

Modern applications are largely built on the web. Understanding a few core ideas is essential.

### HTTP Requests and Responses
The client (usually a browser) sends a **request**; the server returns a **response**.  
Requests contain a method (GET, POST, etc.), headers, and sometimes a body. Responses contain a status code, headers, and a body.

### Cookies
Small pieces of data the server asks the browser to store and send back with later requests. Commonly used to keep users logged in or to track sessions.

### Sessions
A way for the server to remember that a series of requests belong to the same user. Session identifiers are often stored in cookies.

### JWT (JSON Web Token)
A compact, self-contained way of transmitting information between parties as a JSON object, commonly used for authentication and authorization in modern APIs. The token is signed so its integrity can be verified.

### CORS (Cross-Origin Resource Sharing)
A browser security mechanism that controls how a web page from one origin can request resources from another origin. Misconfigurations can create security problems.

### CSRF (Cross-Site Request Forgery)
An attack concept in which a malicious site causes a victim’s browser to perform unwanted actions on a site where the victim is already authenticated. Defenses include anti-CSRF tokens and SameSite cookie attributes.

### Same-Origin Policy
A fundamental browser security rule: a web page can only freely interact with resources from the same origin (scheme + host + port). Many web security mechanisms build on this policy.

---

## Common Vulnerability Classes (Conceptual Only)

These are categories of weaknesses frequently discussed in application security. Descriptions stay high-level; no exploitation steps are provided.

| Class | Core idea |
|-------|-----------|
| **SQL Injection** | Untrusted input is interpreted as part of a database query. |
| **XSS (Cross-Site Scripting)** | Untrusted input is rendered as active content in a victim’s browser. |
| **CSRF** | Victim’s browser is tricked into making an unwanted authenticated request. |
| **IDOR (Insecure Direct Object Reference)** | Access control checks are missing or insufficient for direct references to objects. |
| **SSRF (Server-Side Request Forgery)** | The server is tricked into making requests to unintended locations. |
| **File Upload vulnerabilities** | Uploaded files are handled in an unsafe way (type, location, execution). |
| **Path Traversal** | Input is used to access files outside the intended directory. |
| **Command Injection** | Untrusted input is passed to a system shell or command interpreter. |
| **Session attacks** | Session identifiers are guessed, stolen, or fixed so an attacker can impersonate a user. |
| **API Security issues** | Broken authentication, excessive data exposure, lack of rate limiting, etc. in APIs. |

Understanding the *existence* and *impact* of these classes is more important at this stage than knowing how to trigger them.

---

**Key takeaway**  
Security is built on a small set of enduring principles (CIA, AAA, least privilege, defense in depth) and a clear understanding of risk. Web applications introduce additional concepts (sessions, cookies, same-origin policy, common vulnerability classes) that every practitioner must recognize. Logging and continuous monitoring turn those principles into operational reality.