# Tools Overview (Curriculum-Wide)

This folder documents **tools by name**: what each is for, a short explanation, and **lab-safe usage examples**.  
Executable helpers live under top-level `Codes/`. Active use is limited to systems you own or control in an isolated laboratory.

| Phase | How tools appear |
|-------|------------------|
| Phase-0 / Phase-1 | Named and explained; no attack recipes against real systems |
| Phase-2 / Phase-3 | Hands-on in the lab + companion scripts |

---

## Index of tool guides

| File | Tools covered |
|------|----------------|
| `01_packet_analysis_tools.md` | Wireshark, tshark, Scapy, tcpdump, ping |
| `02_host_and_shell_tools.md` | Bash, ss, ps, ip, journalctl, grep; PowerShell, Get-NetTCPConnection, Get-Process, Get-WinEvent |
| `03_recon_and_scan_tools.md` | Nmap, ping, Python socket helpers |
| `04_crypto_and_web_tools.md` | openssl, sha256sum, hashlib, Browser DevTools, OWASP ZAP, Burp Community |
| `05_soc_and_detection_tools.md` | Auth logs, journalctl, Get-WinEvent, lab SIEM concepts, detection helper scripts |
| `06_infra_and_cloud_tools.md` | Firewall/segmentation concepts, baseline inspection, cloud CLI (lab/free-tier only) |

Arabic versions: `Tools/AR/`.

---

## Safety (applies to every guide)

1. Prefer intentionally vulnerable lab targets (DVWA, Juice Shop, Metasploitable, etc.).  
2. Replace example IPs with addresses on **your** lab network.  
3. Do not scan or probe the public Internet as part of this curriculum.  
4. When unsure whether a target is in scope — stop.

Each topic file ends with a **Worked lab workflow** and **common mistakes** section where applicable.
