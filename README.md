# Cybersecurity Education Curriculum

Bilingual (English + Arabic) progressive curriculum: absolute beginner → intermediate lab skills → specialized tracks.

**Authorized educational use only.** Practical exercises target isolated laboratory environments you own or control. Do not scan, probe, or attack systems without explicit authorization.

---

## Project layout

```
.
├── README.md                 ← this file
├── Lessons/
│   ├── EN/
│   │   ├── Foundations/      ← Phase-0
│   │   ├── Phase-1/          ← Conceptual core
│   │   ├── Phase-2/          ← Intermediate practical lab
│   │   └── Phase-3/          ← Specialized Tracks 1–5
│   └── AR/                   ← Full Arabic parallel
├── Codes/
│   ├── Python/               ← Phase-2 stages + Track-1/2/5 helpers + 04_network_analysis
│   ├── Bash/                 ← Phase-2 stages + Track helpers
│   └── PowerShell/           ← Stage 3 Windows helpers
└── Tools/
    ├── EN/                   ← Tool name, purpose, explanation, lab examples
    └── AR/                   ← Arabic parallel
```

---

## Curriculum phases

| Phase | Path | Level | Focus |
|-------|------|-------|--------|
| **0 · Foundations** | `Lessons/*/Foundations/` | Absolute beginner | Computer basics, Linux, Windows, networking, cyber basics, red/blue conceptual |
| **1 · Conceptual** | `Lessons/*/Phase-1/` | Beginner | CIA, risk, networking, access control, crypto, attack surfaces, ethics, pentest methodology — **theory only** |
| **2 · Practical** | `Lessons/*/Phase-2/` | Intermediate | Lab setup, host inspection, packets, authorized recon, vuln concepts, web, crypto practice, detection, IR, capstone |
| **3 · Specialized** | `Lessons/*/Phase-3/` | Intermediate→role | **Track 1** Web · **Track 2** SOC · **Track 3** Infra · **Track 4** Cloud · **Track 5** Adversary sim (lab) |

Each phase overview includes a **self-check / review checklist**.

### Phase-3 track folders

| Track | Folder |
|-------|--------|
| 1 Web Application Security | `Track-1-Web-Application-Security/` |
| 2 SOC / Detection Engineering | `Track-2-SOC-Detection-Engineering/` |
| 3 Network & Infrastructure Defense | `Track-3-Network-Infrastructure-Defense/` |
| 4 Cloud Security Fundamentals | `Track-4-Cloud-Security-Fundamentals/` |
| 5 Adversary Simulation Basics | `Track-5-Adversary-Simulation-Basics/` |

---

## Codes (lab only)

### Phase-2 (by stage)

| Stage | Topic | Example paths |
|-------|--------|----------------|
| 1 | Lab setup | `Codes/Bash/01_lab_setup/`, `Codes/Python/01_lab_setup/` |
| 2 | Linux | `Codes/Bash/02_linux_security/`, `Codes/Python/02_linux_security/` |
| 3 | Windows | `Codes/PowerShell/03_windows_security/` |
| 4 | Network analysis | `Codes/Python/04_network_analysis/`, `Codes/Bash/04_network_analysis/` |
| 5 | Recon | `Codes/Bash/05_reconnaissance/`, `Codes/Python/05_reconnaissance/` |
| 6–10 | Vuln, web, crypto, detection, IR | `Codes/Python/06_` … `10_`, matching Bash folders |

### Phase-3 (by track)

| Track | Paths |
|-------|--------|
| **1 Web** | `Codes/Python/Track-1-Web/` (headers, cookies, API GET, OWASP note categories), `Codes/Bash/Track-1-Web/` |
| **2 SOC** | `Codes/Python/Track-2-SOC/` (threshold, triage, correlation, burst score), `Codes/Bash/Track-2-SOC/` |
| **3 Infra** | `Codes/Bash/Track-3-Infra/baseline_ports_note.sh` |
| **5 Adversary** | `Codes/Python/Track-5-Adversary/`, `Codes/Bash/Track-5-Adversary/` |

```bash
# Examples
python3 Codes/Python/Track-1-Web/check_security_headers.py http://192.168.56.10/
python3 Codes/Python/Track-2-SOC/detection_threshold_demo.py
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
```

---

## Tools reference

| Path | Content |
|------|---------|
| `Tools/EN/00_tools_overview.md` | Index + safety |
| `Tools/EN/01_packet_analysis_tools.md` | Wireshark, tshark, Scapy, tcpdump, ping |
| `Tools/EN/02_host_and_shell_tools.md` | Bash, PowerShell, host inspection |
| `Tools/EN/03_recon_and_scan_tools.md` | Nmap, sockets (lab only) |
| `Tools/EN/04_crypto_and_web_tools.md` | openssl, hashing, DevTools, ZAP/Burp |
| `Tools/EN/05_soc_and_detection_tools.md` | Logs, SIEM concepts, detection helpers |
| `Tools/EN/06_infra_and_cloud_tools.md` | Baselines, segmentation, cloud lab habits |
| `Tools/AR/` | Arabic parallel of the above |

Each tool entry includes: **name**, **what it is for**, **explanation**, **usage examples**.

---

## Safety rules (non-negotiable)

1. Practical work only against systems you own or have written permission to test.  
2. Prefer intentionally vulnerable training platforms in an isolated lab.  
3. Never scan or attack the public Internet as part of this curriculum.  
4. Take VM snapshots before experiments; restore after.  
5. Phase-1 remains conceptual — no actionable attack instructions against real systems.  
6. When unsure of scope — stop.

---

## How to study

1. **Phase-0** if you are new to computers, OS, or networking.  
2. **Phase-1** in order for concepts and ethics.  
3. Build the lab (**Phase-2 Stage 1**), then complete Phase-2.  
4. Choose a **Phase-3** track; complete its stages and capstone.  
5. Use `Codes/` only inside the lab; read `Tools/EN` or `Tools/AR` for tool usage.  
6. Use the **self-check** lists in each phase overview before moving on.

---

## Languages

- **EN** — English lessons and tool guides  
- **AR** — Arabic parallel  

Prefer the language you learn in; the other remains available for reference.

## By Help : **GROK**
