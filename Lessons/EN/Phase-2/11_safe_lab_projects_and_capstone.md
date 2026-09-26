# Stage 11: Safe Lab Projects and Capstone

## Why This Stage Matters

The previous stages built individual skills: lab safety, host inspection, network analysis, reconnaissance, vulnerability concepts, web observation, cryptography inspection, detection thinking, and incident response fundamentals.

This final stage asks you to combine those skills into guided end-to-end projects. The goal is integration, documentation discipline, and confidence — still entirely inside your authorized laboratory.

---

## Learning Objectives

By the end of this stage you will be able to:

- Execute multi-step laboratory projects that combine skills from Stages 1–10
- Produce clear, structured documentation of scope, actions, findings, and recommendations
- Demonstrate both offensive-leaning (discovery) and defensive-leaning (detection/response) perspectives on the same lab activity
- Create portfolio-style artifacts you can keep and later expand
- Reflect on gaps and define personal next steps beyond Phase-2

---

## Safety Checkpoint

Every project in this stage inherits all previous safety rules:

- Only laboratory systems you own or explicitly control
- No scanning, exploitation, or traffic generation against external or unauthorized systems
- Snapshots before major changes
- Evidence and notes treated carefully

If a project step feels unclear or risky, stop and revisit the relevant earlier stage.

---

## Project Design Principles

Each project should include:

1. **Clear scope** — which VMs, which network, what is in and out of bounds
2. **Preparation** — snapshots, baseline notes, tools ready
3. **Execution** — concrete steps with recorded commands and observations
4. **Analysis** — what the findings mean
5. **Defensive view** — how the same activity would appear in logs or detections
6. **Documentation** — a short report or structured notebook entry
7. **Cleanup / restore** — return the lab to a known state

---

## Suggested Capstone Projects

Complete at least two of the following (or equivalent projects of similar depth). Adapt IP addresses and service names to your actual lab.

### Project A — Lab Inventory and Baseline

**Goal:** Produce a living inventory of your laboratory.

Steps (outline):
1. List all lab VMs, their roles, IP addresses, and OS.
2. From the attacker VM, perform host discovery and a controlled port scan of each target.
3. On each target, identify the processes behind the main open ports (Stages 2–3 skills).
4. Capture a short packet sample of normal lab traffic (Stage 4).
5. Document everything in a structured inventory (table or markdown).
6. Note which services would be highest priority for monitoring.

**Deliverable:** Inventory document + short reflection on what surprised you.

### Project B — Controlled Reconnaissance to Detection

**Goal:** Perform authorized discovery and then find the evidence from the defender’s side.

Steps (outline):
1. Snapshot relevant VMs.
2. From the attacker VM, run a documented Nmap scan against one target.
3. Immediately examine authentication, process, and firewall logs (if any) on the target and any monitoring host.
4. Capture the scan traffic and identify characteristic packets.
5. Write a mini timeline: actions taken → evidence left behind.
6. Propose one simple detection idea that would have highlighted this activity.

**Deliverable:** Timeline + detection proposal + PCAP or log excerpts (redacted if needed).

### Project C — Web Application Observation Report

**Goal:** Map and observe an intentionally vulnerable web application.

Steps (outline):
1. Start DVWA, Juice Shop, or similar in the lab.
2. Browse the application normally; capture traffic with browser tools or a proxy.
3. Document visible surfaces (forms, parameters, cookies, interesting endpoints).
4. Identify at least two potential weakness categories (OWASP-style) based on observation only.
5. Note any cryptographic or transport observations (HTTPS, cookies flags, etc.).
6. Write a short non-exploitative report suitable for a technical reader.

**Deliverable:** Observation report with request/response samples and category mapping.

### Project D — Mini Incident Response Tabletop + Lab Validation

**Goal:** Walk through an IR lifecycle and validate key steps on lab systems.

Steps (outline):
1. Define a simple scenario (e.g. successful logon after failures + unusual process).
2. Write the phase-by-phase response plan (Stage 10).
3. On lab VMs, generate the scenario artifacts (failed/successful logons, process start).
4. Locate the evidence using skills from Stages 2, 3, and 9.
5. Practice a containment action that is safe in the lab (e.g. isolate network adapter, stop a service, restore snapshot).
6. Record lessons learned and one improvement.

**Deliverable:** Scenario write-up, evidence notes, and lessons-learned paragraph.

### Project E — Cryptographic Configuration Review (Lab Service)

**Goal:** Inspect TLS and certificate configuration of a lab service.

Steps (outline):
1. Identify an HTTPS service in your lab (or stand one up briefly).
2. Use `openssl` and/or Wireshark to inspect the certificate and handshake.
3. Record Subject, Issuer, validity, and any obvious weaknesses (expired, self-signed, name mismatch, old protocol).
4. Relate findings to prioritization concepts from Stage 6.
5. Suggest a hardened configuration (conceptual).

**Deliverable:** Certificate inspection notes + short prioritization and recommendation section.

---

## Documentation Template (Suggested)

## Practical code (Codes/)

Reuse any helper under `Codes/Python/` and `Codes/Bash/` inside your capstone projects. Common combinations:

| Project | Suggested scripts |
|---------|-------------------|
| A — Inventory | `check_lab_ports.py`, `host_inspect.sh`, `safe_lab_nmap.sh` |
| B — Recon → Detection | `safe_lab_nmap.sh`, `simple_detection_demo.py`, `tshark_quick_summary.sh` |
| C — Web observation | `lab_http_observe.py` |
| D — Mini IR | `collect_basic_evidence.sh`, `timeline_template.py` |
| E — Crypto review | `hash_and_cert_check.sh`, `hash_file.py` |

See `README.md (project root)` for the full map.


```markdown
# Project Title

## Scope
- Systems:
- Network:
- Allowed actions:
- Explicitly out of scope:

## Preparation
- Snapshots taken:
- Baseline notes:

## Execution Log
| Time | Action | Result / Observation |
|------|--------|----------------------|

## Findings
- ...

## Defensive Perspective
- Log evidence:
- Detection ideas:

## Recommendations / Lessons
- ...

## Cleanup
- Restored from snapshot: yes/no
```

---

## Portfolio Tips

- Keep projects in a dedicated folder with dated reports.
- Prefer clear language over tool output dumps; include output as evidence, not as the whole story.
- Note limitations honestly (“version detection may be inaccurate,” “only lab traffic was examined”).
- These artifacts can later support learning records, interview discussions, or more advanced training applications.

---

## Reflection and Next Steps

After completing your chosen projects, write a short personal reflection:

1. Which skills feel solid?
2. Which skills need more practice?
3. What would you add to your lab next?
4. What Phase-3 direction interests you most (deeper web testing, SOC/detection engineering, cloud fundamentals, etc.)?

Phase-2 ends when you can move through a multi-step lab exercise with discipline, document it clearly, and see both the discovery and the defensive sides of the same activity.

---

## Review Questions

1. Why does a capstone project require explicit scope and cleanup steps?
2. Name two ways the defensive perspective should appear in a discovery-oriented project.
3. What makes a laboratory report useful later as a portfolio artifact?
4. How do snapshots support both safety and recovery in these projects?
5. What is one sign that you are ready to move beyond Phase-2?

---

## Summary

- Capstone projects integrate the full set of Phase-2 skills under realistic laboratory constraints.
- Strong documentation, dual offensive/defensive viewpoints, and clean recovery are part of professional habit.
- Suggested projects cover inventory, recon-to-detection, web observation, incident response practice, and cryptographic review.
- Honest reflection prepares you for specialized next steps.
- All work remains inside the authorized lab boundary established at the beginning of Phase-2.

**You have completed Phase-2 · Intermediate Practical Foundations.**

Return to the curriculum overview for the big-picture map, or begin designing your own additional lab projects using the same safety and documentation standards.
