# Track 3 · Network & Infrastructure Defense  
## From Host Skills to Defending a Small Lab Network

**Who this track is for**  
Learners who finished Phase-2 and want to think like an infrastructure defender: segmentation, baselines, vulnerability management, and monitoring—applied to a laboratory network you control.

**What you will be able to do by the end**
- Explain segmentation and firewall policy intent with simple lab diagrams
- Apply high-level hardening baselines on Linux and Windows lab VMs
- Run a vulnerability-management mini-cycle (discover → prioritize → verify) in lab
- Relate IDS/IPS concepts to traffic you can capture in the lab
- Document defensive controls for a small multi-VM lab segment

---

## Prerequisites

- Phase-2 complete (Stages 1–6, 9 strongly recommended)
- Lab with at least two segments or VLANs/host-only networks if possible (even simple dual-NIC layouts help)
- Comfort with `ss`/firewall basics and Phase-2 vulnerability concepts

---

## Track organization

| Stage | File | Focus |
|-------|------|-------|
| 0 | This file | Track map, outcomes, safety |
| 3.1 | `01_segmentation_and_policy.md` | Zones, trust boundaries, allow-lists |
| 3.2 | `02_host_hardening_baselines.md` | Linux/Windows baseline controls (lab) |
| 3.3 | `03_vulnerability_management_cycle.md` | Inventory, scan (lab), prioritize, retest |
| 3.4 | `04_ids_ips_concepts.md` | Network detection/prevention ideas + lab traffic |
| 3.5 | `05_remote_access_and_vpn_concepts.md` | Admin access, VPN as control (defensive) |
| 3.6 | `06_monitoring_the_lab_network.md` | What to log at network/host edge |
| 3.7 | `07_track_capstone_defended_lab.md` | Control list + diagram + verification notes |

---

## Lab setup notes

| Component | Role |
|-----------|------|
| Gateway / firewall VM (optional) | Policy experiments |
| Hardened “server” VM | Baseline practice |
| Vulnerable target (isolated) | Contrast before/after controls |
| Packet capture | Validate what crosses segments |

**Safety:** Firewall and scan experiments stay inside lab networks. Do not change rules on production routers or ISP equipment.

---

## Safety checkpoints (Track 3)

1. Snapshot before firewall or baseline changes.  
2. Scans only against lab address ranges you documented in Stage 1 of Phase-2.  
3. Hardening guides are applied to **your** VMs, not customer systems without authorization.  
4. IDS rules in this track are educational; test them only on lab traffic.

---

## Stage summaries

### 3.1 — Segmentation and policy  
Trust zones; default-deny thinking; management plane vs user plane; simple lab topology diagrams.

### 3.2 — Host hardening baselines  
SSH/RDP exposure, local admin reduction, service minimization, patching discipline—practical checklist on lab VMs (CIS-style *ideas*, not dumping entire benchmarks).

### 3.3 — Vulnerability management cycle  
Asset list → authorized lab scan → CVSS/context prioritization → fix or accept → retest. Reuse Phase-2 Stage 6 judgment.

### 3.4 — IDS/IPS concepts  
Signature vs anomaly ideas; where sensors sit; false positives; use lab PCAPs or generated traffic to illustrate alerts.

### 3.5 — Remote access and VPN concepts  
Why admin interfaces should not face the open Internet; VPN as encrypted path and policy control (conceptual + lab if available).

### 3.6 — Monitoring the lab network  
Flow/log sources; tie-in to Track 2; minimum monitoring set for a small environment.

### 3.7 — Capstone  
Document a “defended lab”: diagram, control inventory, one verified hardening change, one monitoring gap closed.

---

## Companion code

| Area | Location |
|------|----------|
| Host inspect | `Codes/Bash/02_linux_security/`, `Codes/PowerShell/03_windows_security/` |
| Safe lab Nmap | `Codes/Bash/05_reconnaissance/safe_lab_nmap.sh` |
| Track 3 extensions | Baseline audit snippets under `Codes/` as stages are written |

---

## Deliverables checklist

- [ ] Lab network diagram with trust zones  
- [ ] Hardening checklist applied to at least one Linux and/or Windows lab VM  
- [ ] Mini VM cycle write-up (find → prioritize → verify)  
- [ ] Capstone control inventory  

---

## How Track 3 relates to other tracks

- **Track 2:** Defenses reduce noise and define what “suspicious” means on the wire/host.  
- **Track 1:** Web apps sit in zones; headers and TLS meet infrastructure TLS policy.  
- **Track 4:** Cloud security groups and network exposure echo segmentation ideas.  
- **Track 5:** Purple-team scenarios validate whether controls actually detect or block lab behaviors.

---

## Important boundary

Infrastructure defense skills are powerful on real networks only with authorization and change control. This curriculum practices on isolated labs.

**Next step:** When published, start `01_segmentation_and_policy.md`; meanwhile, redraw your Phase-2 lab with explicit trust boundaries.
