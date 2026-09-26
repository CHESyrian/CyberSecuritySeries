# Phase-2 · Intermediate Practical Foundations  
## From Conceptual Understanding to Safe Hands-On Skills

**Who this phase is for**  
Learners who have completed Phase-0 (Foundations) and Phase-1 (Conceptual Curriculum). You already understand the core ideas of cybersecurity, the CIA triad, risk, networking fundamentals, access control, cryptography, ethics, and the high-level structure of a penetration test. Phase-2 moves you from theory into controlled, practical work.

**What you will learn**  
By the end of Phase-2 you will be able to:
- Set up and operate a safe home laboratory environment
- Use intermediate Linux and Windows skills for security investigation
- Capture, analyze, and interpret network traffic with professional tools
- Perform authorized reconnaissance and enumeration against lab targets only
- Understand how vulnerability scanners work and how to prioritize findings
- Recognize the most common web application security issues (OWASP Top 10) in a safe lab
- Apply cryptography concepts with real tools and certificates
- Read logs, think like a defender, and follow basic incident-response steps
- Complete guided mini-projects that combine offensive and defensive skills

**How this phase is organized**

| Stage | File | Focus |
|-------|------|-------|
| 0 | This file | Curriculum map, prerequisites, lab philosophy, and learning tips |
| 1 | `01_lab_setup_and_safety.md` | Building a safe home lab, virtualization, legal & ethical rules |
| 2 | `02_linux_for_security.md` | Intermediate Bash, process/network inspection, security-oriented scripting |
| 3 | `03_windows_for_security.md` | PowerShell for investigation, Event Viewer, Registry, local security tools |
| 4 | `04_network_analysis_and_packet_crafting.md` | Wireshark, tshark, Scapy analysis & controlled crafting, PCAP work |
| 5 | `05_reconnaissance_and_enumeration.md` | Passive OSINT concepts + active discovery against authorized lab targets |
| 6 | `06_vulnerability_assessment_concepts.md` | How scanners work, reading CVE/CVSS reports, prioritization |
| 7 | `07_web_application_security_fundamentals.md` | OWASP Top 10 (lab-based), HTTP deep dive, safe use of proxy tools |
| 8 | `08_cryptography_in_practice.md` | Certificates, TLS inspection, hashing tools, common misconfigurations |
| 9 | `09_logging_detection_and_blue_team.md` | Log sources, SIEM concepts, simple detection rules, threat-hunting mindset |
| 10 | `10_incident_response_fundamentals.md` | IR lifecycle, containment concepts, evidence awareness, tabletop exercise |
| 11 | `11_safe_lab_projects_and_capstone.md` | Guided mini-projects that integrate previous stages |

**Prerequisites**
- Completion of Phase-0 (Foundations) and Phase-1 (Stages 1–9)
- Willingness to work only inside authorized lab environments
- Basic comfort with installing software and using a terminal

**Lab philosophy (critical)**  
All practical exercises in Phase-2 are designed for **controlled, isolated laboratory environments** that you own or have explicit permission to use.  
You will never be asked to scan, probe, or attack any system on the public internet or any system belonging to another person or organization.

Recommended minimal lab stack:
- Hypervisor: VirtualBox or VMware Workstation Player
- Attacking machine: Kali Linux (or equivalent)
- Target machines: intentionally vulnerable training VMs (e.g. Metasploitable, DVWA, Juice Shop)
- Optional: a simple logging / SIEM stack for blue-team exercises


**Practical code**  
Companion scripts live under `Codes/Python/` and `Codes/Bash/`, organized by stage.  
See `README.md (project root)` for the full map. All scripts are for **authorized laboratory use only**.

**Learning tips**
- Complete the stages in order. Each builds practical skills on the previous one.
- Always read the Safety Checkpoint sections before running any tool.
- Keep a lab notebook: record commands, expected vs actual output, and observations.
- When a Mermaid diagram appears, most modern Markdown viewers will render it visually.
- Balance red-team and blue-team thinking — the same technique looks different from each side.
- The final capstone stage is designed to produce portfolio-style artifacts you can keep.

**Important boundary**  
Phase-2 introduces real tools and commands, but only inside safe, authorized laboratory environments.  
It never provides instructions for attacking systems without permission.  
Unauthorized scanning or exploitation of systems you do not own is illegal and unethical.  
If you are ever unsure whether an activity is allowed — stop and ask.

**How Phase-2 relates to the rest of the curriculum**

```
Phase-0  →  Absolute beginner foundations (conceptual)
Phase-1  →  Core cybersecurity concepts + pentest methodology (conceptual)
Phase-2  →  Intermediate practical skills in a safe lab (this phase)
Future   →  Specialized tracks (web pentesting, SOC analyst path, cloud, etc.)
```

Ready? Begin with Stage 1: Lab Setup and Safety.

## Self-check / review checklist

Before Phase-3, confirm you can:
- [ ] Run an isolated lab with snapshots and lab-only targets
- [ ] Inspect a Linux and/or Windows host (processes, ports, basic logs)
- [ ] Capture and filter packets in the lab (Wireshark or tshark)
- [ ] Run **authorized** discovery only against lab IPs
- [ ] Observe a lab web app (headers/cookies) without attacking production
- [ ] Describe a simple detection idea and an IR lifecycle step
- [ ] Point to companion scripts under `Codes/` that you have actually run
