# Track 5 · Adversary Simulation Basics (Authorized Only)  
## Purple-Team Thinking Inside the Laboratory

**Who this track is for**  
Learners who finished Phase-2 and want to understand attacker *paths* in order to improve defense. This is **not** a course in attacking the Internet. Every technique is framed for intentional lab targets and paired with detection or control discussion.

**What you will be able to do by the end**
- Use ATT&CK *tactics* as a shared language for lab scenarios
- Plan and run a simple multi-step scenario only against lab VMs you own
- Document actions, evidence, and impact without unnecessary harm to the lab
- Hand off the same scenario to a defensive view (Track 2 skills)
- Write a purple-team style report: activity → evidence → detections → fixes

---

## Prerequisites

- Phase-2 complete (recon, web fundamentals, logging, IR)
- Strong commitment to scope discipline
- Lab snapshots before every scenario
- Recommended: Track 2 in parallel or after for detection half of purple team

---

## Track organization

| Stage | File | Focus |
|-------|------|-------|
| 0 | This file | Track map, ethics, safety |
| 5.1 | `01_attack_mapping_and_scope.md` | ATT&CK tactics as labels; RoE for lab scenarios |
| 5.2 | `02_lab_initial_access_patterns.md` | Intentional weak services/apps as entry (lab only) |
| 5.3 | `03_discovery_and_situational_awareness.md` | What an operator learns post-access *on lab hosts* |
| 5.4 | `04_persistence_categories.md` | Categories of persistence (conceptual + safe lab demos) |
| 5.5 | `05_purple_team_loop.md` | Run → detect → tune → retest |
| 5.6 | `06_track_capstone_purple_report.md` | Full scenario report |

---

## Lab setup notes

| Component | Role |
|-----------|------|
| Intentional targets | Metasploitable, DVWA, Juice Shop, weak lab AD (optional) |
| Clean snapshots | Return to known state after each scenario |
| Logging on | So Track 2-style detections have signal |
| Written scenario card | Scope, steps, stop conditions |

---

## Safety checkpoints (Track 5) — critical

1. **Only lab systems you own** — no third-party, no production, no “practice” on random Internet hosts.  
2. No distribution of real malware samples as course material; prefer intentional vulnerable apps and benign lab markers.  
3. Stop conditions written before you start (time box, no data destruction beyond disposable lab data).  
4. Prefer evidence of access (files, lab flags, screenshots) over destructive proof.  
5. If a step is unclear or feels out of scope — stop.

Unauthorized access to computer systems is illegal. This track teaches structured *authorized* simulation for learning and defense improvement.

---

## Stage summaries

### 5.1 — Attack mapping and scope  
Tactics vs techniques at a high level; write a one-page Rules of Engagement for a lab scenario; success criteria that do not require harming the lab permanently.

### 5.2 — Lab initial access patterns  
Using *known weak lab services* or web challenges as entry; document the path; no zero-day research requirement.

### 5.3 — Discovery on lab hosts  
What files, users, and network neighbors an operator might enumerate **on a machine they already control in lab**; tie to Phase-2 host inspection skills.

### 5.4 — Persistence categories  
Service installs, scheduled tasks, startup entries, account changes—*categories* and how defenders spot them; safe demos only on disposable lab VMs.

### 5.5 — Purple-team loop  
Hand the scenario to detection work: which logs fire, which rules to add, retest after tuning.

### 5.6 — Capstone  
One end-to-end lab scenario report: timeline, evidence, mapped tactics, detections, recommended fixes, cleanup confirmation (snapshot restore).

---

## Companion code

| Area | Location |
|------|----------|
| Recon / web / logs | Phase-2 `Codes/` scripts for generating and detecting lab activity |
| Evidence collection | `Codes/Bash/10_incident_response/collect_basic_evidence.sh` |
| Track 5 | Scenario templates under track folder as stages are written |

---

## Deliverables checklist

- [ ] Written lab RoE for at least one scenario  
- [ ] Timeline of actions with evidence references  
- [ ] Tactic labels for major steps  
- [ ] At least two detection or control recommendations tested in lab  
- [ ] Capstone purple-team report + confirmed cleanup  

---

## How Track 5 relates to other tracks

- **Track 2:** Primary partner—detections for your scenarios.  
- **Track 1:** Web entry paths in intentional apps.  
- **Track 3:** Controls that should block or log your lab behaviors.  
- **Track 4:** Cloud misconfig narratives studied defensively, not as attack recipes against others.

---

## Important boundary

Completing Track 5 does **not** authorize real-world offensive operations. Professional red teaming requires contracts, scope, insurance, and law. Here, the only valid battlefield is the lab you built.

**Next step:** When published, start `01_attack_mapping_and_scope.md`; until then, practice writing scope statements and restoring snapshots cleanly after Phase-2 exercises.
