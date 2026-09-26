# Phase-3 · Specialized Tracks  
## From Intermediate Lab Skills to Role-Oriented Depth

**Who this phase is for**  
Learners who have completed Phase-0, Phase-1, and Phase-2. You can operate a safe lab, inspect hosts, analyze packets, perform authorized discovery, reason about vulnerabilities and web risks, practice detection and incident response, and document your work.

Phase-3 is **not** one linear path for everyone. It offers **numbered specialized tracks**. Choose one primary track (or two related tracks).

**What you will gain**  
Depending on the track(s) you complete, skills toward roles such as:
- Web application security / lab-based AppSec testing (**Track 1**)
- SOC analyst / detection engineering (**Track 2**)
- Network and infrastructure defense (**Track 3**)
- Cloud security fundamentals (**Track 4**)
- Authorized adversary simulation / purple-team thinking (**Track 5**)

Every track: **authorized laboratory systems only**.

---

## How Phase-3 is organized

| Component | Path |
|-----------|------|
| This overview | `00_curriculum_overview.md` |
| **Track 1 · Web Application Security** | `Track-1-Web-Application-Security/` |
| **Track 2 · SOC / Detection Engineering** | `Track-2-SOC-Detection-Engineering/` |
| **Track 3 · Network & Infrastructure Defense** | `Track-3-Network-Infrastructure-Defense/` |
| **Track 4 · Cloud Security Fundamentals** | `Track-4-Cloud-Security-Fundamentals/` |
| **Track 5 · Adversary Simulation Basics** | `Track-5-Adversary-Simulation-Basics/` |

Each folder contains a **fully detailed** `00_track_overview.md` (stages, safety, deliverables, relations to other tracks).

---

## Track directory map

| Track | Specification | Overview file |
|-------|---------------|---------------|
| **Track 1** | Web Application Security | `Track-1-Web-Application-Security/00_track_overview.md` |
| **Track 2** | SOC / Detection Engineering | `Track-2-SOC-Detection-Engineering/00_track_overview.md` |
| **Track 3** | Network & Infrastructure Defense | `Track-3-Network-Infrastructure-Defense/00_track_overview.md` |
| **Track 4** | Cloud Security Fundamentals | `Track-4-Cloud-Security-Fundamentals/00_track_overview.md` |
| **Track 5** | Adversary Simulation Basics (authorized) | `Track-5-Adversary-Simulation-Basics/00_track_overview.md` |

---

## Short track sketches

**Track 1 — Web Application Security**  
HTTP/sessions depth; mapping and proxy; injection/XSS/access control on intentional lab apps; APIs; hardening; full lab-app assessment report.

**Track 2 — SOC / Detection Engineering**  
Log pipelines; SIEM search; detection design; triage; ATT&CK as labels; detect lab web/recon; detection pack capstone.

**Track 3 — Network & Infrastructure Defense**  
Segmentation; host baselines; vulnerability-management cycle; IDS/IPS concepts; monitoring; defended-lab documentation.

**Track 4 — Cloud Security Fundamentals**  
Shared responsibility; IAM least privilege; exposure patterns; cloud logging; secure baseline checklist (lab/free-tier/emulator only).

**Track 5 — Adversary Simulation Basics**  
Lab RoE; intentional initial access; discovery/persistence *categories*; purple-team loop with Track 2; purple-team report. Hard boundary: lab only, no real-world unauthorized operations.

---

## Suggested combinations

| Goal | Tracks |
|------|--------|
| Web / AppSec | **Track 1** → sample of Track 2 |
| SOC analyst | **Track 2** → sample of Track 3 |
| Infrastructure defender | **Track 3** → sample of Track 2 |
| Cloud-oriented | **Track 4** → sample of Track 2 |
| Purple team | **Track 5** + **Track 2** |

---

## Prerequisites

- Phase-0, Phase-1, Phase-2 completed (or equivalent)
- Isolated lab still meeting Phase-2 safety rules
- Commitment to authorized scope only

---

## Safety philosophy (non-negotiable)

1. Active testing only against systems you own or have written permission to test.  
2. Prefer intentionally vulnerable training platforms.  
3. No scanning or exploitation of public Internet targets in this curriculum.  
4. Snapshots before major changes.  
5. When unsure of scope — stop.

---

## Codes and Tools

- Scripts: top-level `Codes/` (Python, Bash, PowerShell)  
- Tool explainers: `Tools/EN/` and `Tools/AR/`  
- Track-specific modules will extend these as stage files are written

---

## Curriculum position

```
Phase-0  →  Foundations
Phase-1  →  Conceptual core + ethics
Phase-2  →  Intermediate practical lab
Phase-3  →  Specialized tracks (this phase)
```

---

## Where to start

1. Pick a primary track from the table above.  
2. Open that folder’s `00_track_overview.md`.  
3. Confirm lab isolation.  
4. Work track stages in order; keep portfolio artifacts.

**Example:** Track 1 → `Track-1-Web-Application-Security/00_track_overview.md`

## Self-check / review checklist (per track)

After your chosen track:
- [ ] Track overview read; lab targets still in scope
- [ ] All stage exercises for that track completed in the lab
- [ ] Capstone deliverable saved (report, detections, checklist, or purple-team write-up)
- [ ] Related `Codes/` scripts for the track tried at least once
- [ ] Tool notes in `Tools/EN/` (or `Tools/AR/`) reviewed for tools you used

**Track 1 extra:** [ ] Header/cookie notes  [ ] Lab app findings table  
**Track 2 extra:** [ ] ≥3 detection ideas  [ ] Triage table  
**Track 3 extra:** [ ] Zone diagram  [ ] Baseline ports note  
**Track 4 extra:** [ ] Shared-responsibility page  [ ] Exposure checklist  
**Track 5 extra:** [ ] Written lab RoE  [ ] Snapshot restored after scenario
