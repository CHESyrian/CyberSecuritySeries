# Track 1 · Web Application Security  
## From Web Awareness to Lab-Based Application Assessment

**Who this track is for**  
Learners who finished Phase-2 and want depth in how web applications are built, broken (in controlled labs), observed, and hardened. Suitable if you lean toward AppSec, web-focused testing, or defending web-facing systems.

**What you will be able to do by the end**
- Explain the request/response cycle, sessions, cookies, and common auth patterns in security terms
- Map a lab web application with browser tools and an intercepting proxy
- Recognize and safely demonstrate major issue classes on *intentionally vulnerable* apps (injection, XSS, access control, misconfig, etc.)
- Test and observe simple API behaviors in a lab
- Recommend practical hardening (headers, TLS, session flags, least privilege)
- Produce a structured assessment report suitable as a portfolio artifact

---

## Prerequisites

- Phase-2 complete (especially Stages 1, 4, 7, 8)
- Lab with at least one intentionally vulnerable web app (DVWA, OWASP Juice Shop, WebGoat, or similar)
- Attacker VM able to reach the app on a host-only/internal network
- Optional but recommended: OWASP ZAP or Burp Suite Community for proxy labs

---

## Track organization

| Stage | File | Focus |
|-------|------|-------|
| 0 | This file | Track map, outcomes, safety, lab targets |
| 1.1 | `01_http_sessions_and_auth.md` | HTTP methods, headers, cookies, sessions, auth flows |
| 1.2 | `02_mapping_and_proxy_workflow.md` | Spider/map, intercept, repeater-style workflow (lab) |
| 1.3 | `03_injection_in_the_lab.md` | SQLi, OS command, and related patterns on intentional targets |
| 1.4 | `04_xss_and_client_side.md` | Reflected/stored/DOM concepts; safe lab demos |
| 1.5 | `05_access_control_and_idor.md` | Broken access control, IDOR, privilege checks |
| 1.6 | `06_apis_and_modern_apps.md` | REST basics, tokens, common API lab issues |
| 1.7 | `07_hardening_and_defense.md` | Secure headers, TLS, session security, WAF *concepts* |
| 1.8 | `08_track_capstone_report.md` | Full assessment of one lab app + report template |

---

## Lab targets (authorized only)

Use applications **designed for training**, hosted in your isolated lab:

| Target | Typical use in this track |
|--------|---------------------------|
| **OWASP Juice Shop** | Modern app, rich finding surface, good for mapping + report |
| **DVWA** | Classic deliberate vulnerabilities, good for injection/XSS drills |
| **WebGoat** / similar | Guided lessons aligned to issue classes |
| Custom vulnerable app you wrote or imported | Optional advanced practice |

**Do not** use production sites, employer apps, or third-party systems without a written Rules of Engagement.

---

## Safety checkpoints (Track 1)

Before every active stage:

1. Confirm the target IP/URL is a lab VM or container you control.  
2. Confirm the proxy (if any) is pointed only at lab traffic.  
3. Prefer non-destructive proofs (observation, safe payloads on training apps).  
4. No credential stuffing against real user databases; use lab accounts only.  
5. Snapshot the target before aggressive experiments.

Injection and XSS stages teach **recognition and controlled demonstration on intentional labs**, not weaponization for the open Internet.

---

## Stage summaries

### 1.1 — HTTP, sessions, and authentication
Rebuild Phase-2 web knowledge with depth: methods, status codes, sensitive headers, cookie attributes (`Secure`, `HttpOnly`, `SameSite`), session lifecycle, basic auth vs form vs token patterns.  
**Practice:** Capture normal login and browse traffic to the lab app; document cookies and redirects.

### 1.2 — Mapping and proxy workflow
Systematic mapping: content discovery mindset, sitemap, parameters, authenticated vs anonymous surface. Intercepting proxy setup for lab only; intercept, log, repeat requests safely.  
**Practice:** Map Juice Shop or DVWA; export a simple site map and parameter list.

### 1.3 — Injection in the lab
How untrusted input becomes queries or commands when poorly handled. SQL injection and command injection *on intentional lab pages only*. Emphasize impact categories (read data, bypass auth) without turning the lesson into a generic attack manual for arbitrary sites.  
**Practice:** Complete designated DVWA/Juice Shop injection challenges; record request, payload class, and result.

### 1.4 — XSS and client-side issues
Reflected, stored, and DOM-based XSS as concepts; safe demonstration in lab apps; why output encoding and CSP matter.  
**Practice:** Trigger intentional XSS labs; note sink/source in your write-up; propose a fix in plain language.

### 1.5 — Access control and IDOR
Vertical/horizontal privilege issues; insecure direct object references; forced browsing.  
**Practice:** Change lab object IDs or roles only inside the training app; document authorization gaps.

### 1.6 — APIs and modern apps
REST verbs, JSON, status codes, API keys/JWT *concepts*, mass assignment and broken object auth in lab APIs if available.  
**Practice:** Observe API calls from the lab app (DevTools or proxy); one small Python `requests` script against the *lab* API only.

### 1.7 — Hardening and defense
Security headers (CSP, HSTS, X-Content-Type-Options, etc.), TLS configuration reminders, session fixation/timeout ideas, least privilege for app DB accounts, logging of auth failures. WAF as a layer—not a silver bullet.  
**Practice:** Checklist against your lab app; enable or recommend two concrete hardening improvements.

### 1.8 — Track capstone report
End-to-end assessment of **one** lab application: scope, methodology, findings (with evidence), risk rating rationale, remediation, retest notes.  
**Deliverable:** Portfolio-ready markdown or PDF-style report (structure provided in the stage file).

---

## Companion code (planned / existing)

| Area | Location |
|------|----------|
| HTTP observe (Phase-2) | `Codes/Python/07_web/lab_http_observe.py` |
| Track 1 extensions | `Codes/Python/` stage folders as 1.1–1.8 are written (e.g. header checker, simple lab API client) |
| Tool notes | `Tools/EN/04_crypto_and_web_tools.md` and future Track 1 tool pages |

---

## Deliverables checklist

- [ ] Lab notebook entries for 1.1–1.7  
- [ ] Site map / parameter inventory for the chosen lab app  
- [ ] At least three documented findings with request/response evidence (lab only)  
- [ ] Hardening checklist completed for that app  
- [ ] Capstone report (1.8) saved in your portfolio folder  

---

## How Track 1 relates to other tracks

- **Track 2 (SOC):** Web attack patterns you study here become detection use cases (failed logins, SQLi-like log noise, odd URLs).  
- **Track 5 (Adversary simulation):** Web initial access in lab is one scenario class; purple-team with Track 2.  
- **Track 3 / Track 4:** Hardening and exposure ideas overlap with infrastructure and cloud edges.

---

## Learning tips

- Always name the **lab target** and **date** in notes.  
- Separate *observation*, *controlled lab proof*, and *remediation advice* in write-ups.  
- Prefer understanding *why* a fix works over collecting payload lists.  
- Re-read Phase-2 Stage 7 and Stage 8 before 1.1 if the web/crypto material feels thin.

---

## Important boundary

This track does **not** authorize testing of real-world websites, bug bounty targets without program rules, or any system outside your lab agreement.  
Skills transfer to professional work only under contract, scope, and law.

---

**Next step:** When stage files are published, begin with `01_http_sessions_and_auth.md`.  
Until then, use this overview to set up Juice Shop or DVWA in the lab and practice Phase-2 Stage 7 observation with a proxy pointed only at that app.
