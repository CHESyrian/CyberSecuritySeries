# Track 2 · SOC / Detection Engineering  
## From Log Awareness to Lab Detections and Triage

**Who this track is for**  
Learners who finished Phase-2 and want depth on the blue-team side: collecting signal, writing detections, triaging alerts, and reducing noise—still inside an authorized laboratory.

**What you will be able to do by the end**
- Describe log sources and a simple pipeline from host → collector → search
- Search and correlate events in a lab SIEM or centralized log stack
- Design basic detection ideas (threshold, sequence, rarity)
- Triage alerts with a clear false-positive vs true-positive mindset
- Map lab activity to high-level ATT&CK *tactics* (as a vocabulary, not a cookbook)
- Deliver a small detection pack plus triage notes for a scripted lab scenario

---

## Prerequisites

- Phase-2 complete (especially Stages 2, 3, 9, 10)
- Lab with Linux and/or Windows targets generating auth and process logs
- Optional: lightweight SIEM or stack (e.g. Wazuh, Security Onion lite, ELK-style lab)
- Ability to generate controlled “noisy” activity from Track 1–style or Phase-2 recon only against lab VMs

---

## Track organization

| Stage | File | Focus |
|-------|------|-------|
| 0 | This file | Track map, outcomes, safety |
| 2.1 | `01_log_sources_and_pipelines.md` | What to collect, retention, normalization concepts |
| 2.2 | `02_siem_search_and_correlation.md` | Search, simple joins/correlation in lab |
| 2.3 | `03_detection_design.md` | Threshold, chain, baseline/rarity ideas |
| 2.4 | `04_alert_triage_and_fp.md` | Triage workflow, false positives, enrichment |
| 2.5 | `05_attack_mapping_lab.md` | ATT&CK tactics as labels for lab events |
| 2.6 | `06_detecting_web_and_recon.md` | Detections for lab web/recon patterns |
| 2.7 | `07_tuning_and_metrics.md` | Tune rules, measure noise vs value |
| 2.8 | `08_track_capstone_detections.md` | Detection pack + triage notes for one scenario |

---

## Lab setup notes

| Component | Role |
|-----------|------|
| Target VMs | Produce auth failures, process starts, web logs |
| Optional SIEM | Search and alert in one place |
| Attacker VM | Generate *lab-only* activity to detect |
| Notebook | Timeline of generation → alert → triage |

**Safety:** Generate attack-like traffic only inside the isolated lab. Do not probe external networks to “create detections.”

---

## Safety checkpoints (Track 2)

1. All telemetry comes from systems you control.  
2. Do not disable logging on production or third-party systems.  
3. Detection content in this track is for lab learning and portfolio demos.  
4. When replaying PCAPs or logs, use files you captured in lab or public *training* datasets with clear license.

---

## Stage summaries

### 2.1 — Log sources and pipelines  
Linux auth/syslog/journal, Windows Security/PowerShell, web server logs; why time sync matters; conceptual ship → parse → store.

### 2.2 — SIEM search and correlation  
Build questions (“failed logons then success from same source”); practice searches; simple multi-event correlation in lab tools.

### 2.3 — Detection design  
Write detections in plain language first, then as rule logic; threshold vs sequence; avoid alert-on-everything.

### 2.4 — Alert triage and false positives  
Severity vs confidence; enrich with host/user context; document FP reasons and suppress carefully.

### 2.5 — Attack mapping in the lab  
Label lab scenarios with ATT&CK *tactics* (e.g. Credential Access, Discovery) for communication—not as step-by-step attacker instructions.

### 2.6 — Detecting web and recon  
Failed logins, suspicious URL patterns on lab apps, port-scan noise on lab networks; link to Phase-2 Stages 5 and 7 activity.

### 2.7 — Tuning and metrics  
Before/after noise counts; maintenance ownership; when to disable a rule.

### 2.8 — Capstone  
Script or manually run a lab scenario; ship 3+ detections; triage table; one-page improvement plan.

---

## Companion code

| Area | Location |
|------|----------|
| Auth failure helpers | `Codes/Bash/09_logging_detection/`, `Codes/Python/09_logging_detection/` |
| IR evidence helper | `Codes/Bash/10_incident_response/` |
| Track 2 extensions | Added under `Codes/` as stages are written |

---

## Deliverables checklist

- [ ] Inventory of log sources in your lab  
- [ ] At least five written detection ideas (plain language + logic)  
- [ ] Triage notes for a generated lab scenario  
- [ ] Capstone detection pack with tuning comments  

---

## How Track 2 relates to other tracks

- **Track 1 (Web):** Application attacks become detection use cases.  
- **Track 3 (Infra):** Network/host hardening reduces alert noise and closes gaps.  
- **Track 5 (Adversary sim):** Purple-team pairs: they run a lab scenario; you detect it.  
- **Track 4 (Cloud):** Same detection mindset applied to cloud audit logs later.

---

## Important boundary

This track builds defensive skill. It does not authorize monitoring or attacking systems outside your lab agreement.

**Next step:** Begin with `01_log_sources_and_pipelines.md` when published; until then, strengthen Phase-2 Stage 9 exercises and centralize lab logs if possible.
