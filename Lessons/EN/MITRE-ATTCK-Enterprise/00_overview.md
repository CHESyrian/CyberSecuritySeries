# MITRE ATT&CK® Enterprise Matrix Summary

**Version focus:** Enterprise ATT&CK (current live matrix reflects v19 structural changes).  
**Source:** Official MITRE ATT&CK website (https://attack.mitre.org).  
**Scope:** Tactics and techniques for enterprise environments (Windows, Linux, macOS, cloud/IaaS/SaaS, containers, ESXi, network devices, identity providers, Office Suite, PRE).

> **Educational use only.** This summary is for learning, mapping, detection engineering, and authorized purple-team / lab exercises. Never apply techniques against systems without explicit authorization.

## What is the Enterprise Matrix?

The MITRE ATT&CK Enterprise Matrix is a living knowledge base of adversary tactics and techniques observed in the real world. It organizes **why** an adversary acts (tactics) and **how** they achieve those goals (techniques and sub-techniques).

- **Tactics** = the adversary’s tactical objective (“why”).
- **Techniques** = the method used to achieve the objective (“how”).
- **Sub-techniques** = more specific variants of a technique.
- **Procedures** = concrete implementations observed in the wild (documented on individual technique pages).

Defenders use the matrix for threat modeling, detection coverage mapping, red/purple team planning, and incident response storytelling.

## Tactics

Tactics represent the adversary's tactical goals (the "why").

| ID | Tactic | Folder |
|-----|---------|---------|
| TA0043 | Reconnaissance | [01_Reconnaissance/](01_Reconnaissance/) |
| TA0042 | Resource Development | [02_Resource_Development/](02_Resource_Development/) |
| TA0001 | Initial Access | [03_Initial_Access/](03_Initial_Access/) |
| TA0002 | Execution | [04_Execution/](04_Execution/) |
| TA0003 | Persistence | [05_Persistence/](05_Persistence/) |
| TA0004 | Privilege Escalation | [06_Privilege_Escalation/](06_Privilege_Escalation/) |
| TA0005 | Stealth | [07_Stealth/](07_Stealth/) |
| TA0112 | Defense Impairment | [08_Defense_Impairment/](08_Defense_Impairment/) |
| TA0006 | Credential Access | [09_Credential_Access/](09_Credential_Access/) |
| TA0007 | Discovery | [10_Discovery/](10_Discovery/) |
| TA0008 | Lateral Movement | [11_Lateral_Movement/](11_Lateral_Movement/) |
| TA0009 | Collection | [12_Collection/](12_Collection/) |
| TA0011 | Command and Control | [13_Command_and_Control/](13_Command_and_Control/) |
| TA0010 | Exfiltration | [14_Exfiltration/](14_Exfiltration/) |
| TA0040 | Impact | [15_Impact/](15_Impact/) |

Each technique markdown file contains the official MITRE description/explanation.

Techniques that map to multiple tactics appear in each relevant tactic folder.

*All definitions and descriptions are official MITRE ATT&CK content.*

---

## Folder structure (this directory)

```
MITRE-ATTCK-Enterprise/
├── 00_overview.md                          ← this file
├── 01_Reconnaissance/                      ← TA0043 (full technique files)
│   ├── 00_overview.md
│   ├── T1595_Active_Scanning.md
│   ├── T1592_Gather_Victim_Host_Information.md
│   └── … (all techniques + sub-technique coverage)
├── 02_Resource_Development/                ← TA0042
│   └── 00_overview.md
├── 03_Initial_Access/                      ← TA0001
│   └── 00_overview.md
├── 04_Execution/                           ← TA0002
│   └── 00_overview.md
├── 05_Persistence/                         ← TA0003
│   └── 00_overview.md
├── 06_Privilege_Escalation/                ← TA0004
│   └── 00_overview.md
├── 07_Stealth/                             ← TA0005 (v19)
│   └── 00_overview.md
├── 08_Defense_Impairment/                  ← TA0112 (v19)
│   └── 00_overview.md
├── 09_Credential_Access/                   ← TA0006
│   └── 00_overview.md
├── 10_Discovery/                           ← TA0007
│   └── 00_overview.md
├── 11_Lateral_Movement/                    ← TA0008
│   └── 00_overview.md
├── 12_Collection/                          ← TA0009
│   └── 00_overview.md
├── 13_Command_and_Control/                 ← TA0011
│   └── 00_overview.md
├── 14_Exfiltration/                        ← TA0010
│   └── 00_overview.md
└── 15_Impact/                              ← TA0040
    └── 00_overview.md
```

Each tactic folder contains at minimum a `00_overview.md` with the official description, representative techniques, educational notes, and safety framing.  
The Reconnaissance folder is fully expanded with individual technique files; additional technique files for other tactics can be added following the same pattern (official description + educational notes + lab guidance + sources).

> **Note on v19 change:** The classic single “Defense Evasion” tactic (TA0005) was split into **Stealth** (TA0005 – hide/blend) and **Defense Impairment** (TA0112 – break defender tooling). Most technique IDs remained stable; only tactic associations changed for many entries. The attached SVG reflects a pre-split or Navigator-style view of the classic 14-tactic layout.

## Tactic summaries (official descriptions)

### TA0043 – Reconnaissance
The adversary is trying to gather information they can use to plan future operations.

Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged to aid in other phases of the adversary lifecycle (Initial Access, prioritization of post-compromise objectives, or further reconnaissance).

**Representative techniques (from matrix):**  
Active Scanning (T1595) and sub-techniques (Scanning IP Blocks, Vulnerability Scanning, Wordlist Scanning); Gather Victim Host / Identity / Network / Org Information (T1592, T1589, T1590, T1591); Phishing for Information (T1598); Search Open/Closed Sources, Technical Databases, Websites/Domains, Threat Vendor Data, Victim-Owned Websites; Query Public AI Services.

### TA0042 – Resource Development
The adversary is trying to establish resources they can use to support operations.

Adversaries may buy, lease, or compromise resources that can be used during targeting. Resources include infrastructure, accounts, capabilities (malware, exploits, certificates), and staged tools/content.

**Representative techniques:**  
Acquire Access, Acquire Infrastructure (domains, servers, VPS, serverless, botnet, web services, malvertising, DNS); Compromise Accounts / Infrastructure; Develop Capabilities (malware, exploits, certificates); Establish Accounts; Generate Content; Obtain Capabilities (malware, tools, exploits, AI, certificates, vulnerabilities); Stage Capabilities (upload malware/tool, drive-by, SEO poisoning, link target, install certificate).

### TA0001 – Initial Access
The adversary is trying to get into your network.

Initial Access consists of techniques that use various entry vectors to gain an initial foothold within a network. These techniques include targeted spearphishing, exploiting public-facing applications, and valid accounts, among others.

**Representative techniques:**  
Content Injection, Drive-by Compromise, Exploit Public-Facing Application, External Remote Services, Hardware Additions, Phishing (and spearphishing variants), Replication Through Removable Media, Supply Chain Compromise, Trusted Relationship, Valid Accounts, Wi-Fi Networks.

### TA0002 – Execution
The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system. This tactic is often used with Initial Access and Lateral Movement.

**Representative techniques:**  
BITS Jobs, Cloud Administration Command, Command and Scripting Interpreter (PowerShell, Python, JavaScript, AppleScript, etc.), Container / ESXi Administration Command, Deploy Container, Exploitation for Client Execution, Hijack Execution Flow, Input Injection, Inter-Process Communication, Native API, Poisoned Pipeline Execution, Scheduled Task/Job, Serverless Execution, Shared Modules, Software Deployment Tools, System Services, Trusted Developer Utilities Proxy Execution, User Execution, Windows Management Instrumentation.

### TA0003 – Persistence
The adversary is trying to maintain their foothold.

Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that would otherwise cut off access.

**Representative techniques (common categories):**  
Account Manipulation, Boot or Logon Autostart Execution / Initialization Scripts, Create Account, Create or Modify System Process, Event Triggered Execution, External Remote Services, Hijack Execution Flow, Implant Internal Image, Modify Authentication Process, Office Application Startup, Pre-OS Boot, Scheduled Task/Job, Server Software Component, Traffic Signaling, Valid Accounts, etc.

### TA0004 – Privilege Escalation
The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that enable an adversary to obtain a higher level of permissions on a system or network. Techniques that run with higher privileges or that abuse elevation-control mechanisms fall here.

**Representative techniques:**  
Abuse Elevation Control Mechanism, Access Token Manipulation, Boot or Logon Autostart Execution, Domain or Tenant Policy Modification, Escape to Host, Exploitation for Privilege Escalation, Hijack Execution Flow, Process Injection, Scheduled Task/Job, Valid Accounts, etc.

### TA0005 – Stealth (v19)
The adversary is trying to hide and conceal their actions, appearing as normal behavior.

(Previously part of Defense Evasion.) Focuses on blending in, obfuscation, masquerading, indicator removal, and other methods that reduce the chance of detection while leaving defensive tools intact.

### TA0112 – Defense Impairment (v19)
The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening.

(Previously part of Defense Evasion.) Focuses on disabling or degrading security products, logging, firewalls, monitoring agents, and related controls.

### TA0006 – Credential Access
The adversary is trying to steal account names and passwords.

Credential Access consists of techniques for stealing credentials (passwords, hashes, tokens, keys, certificates) that can later be used for access or lateral movement.

**Representative techniques:**  
Adversary-in-the-Middle, Brute Force, Credentials from Password Stores, Exploitation for Credential Access, Forced Authentication, Forge Web Credentials, Input Capture (keylogging, etc.), Modify Authentication Process, Network Sniffing, OS Credential Dumping, Steal or Forge Kerberos Tickets / Authentication Certificates, Unsecured Credentials, etc.

### TA0007 – Discovery
The adversary is trying to figure out your environment.

Discovery consists of techniques that enable an adversary to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and decide how to act.

**Representative techniques:**  
Account / Domain / System / Network / Process / File / Software / Cloud / Container / Permission Group Discovery, Network Service Discovery, Remote System Discovery, System Information / Location / Network Configuration / Owner / Time Discovery, etc.

### TA0008 – Lateral Movement
The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Adversaries may install their own remote-access tools or use legitimate credentials with native tools.

**Representative techniques:**  
Exploitation of Remote Services, Internal Spearphishing, Lateral Tool Transfer, Remote Service Session Hijacking, Remote Services (RDP, SMB, SSH, WinRM, VNC, DCOM, cloud services, etc.), Use Alternate Authentication Material (Pass-the-Hash, Pass-the-Ticket, etc.).

### TA0009 – Collection
The adversary is trying to gather data of interest to their goal.

Collection consists of techniques used to identify and gather information (files, emails, clipboard, audio/video, screen, browser data, cloud storage, configuration repositories, etc.) before exfiltration.

**Representative techniques:**  
Adversary-in-the-Middle, Archive Collected Data, Audio / Video / Screen Capture, Automated Collection, Browser Session Hijacking, Clipboard Data, Data from Cloud Storage / Configuration Repository / Information Repositories / Local System / Network Shared Drive / Removable Media, Data Staged, Email Collection, Input Capture.

### TA0011 – Command and Control
The adversary is trying to communicate with compromised systems to control them.

Command and Control consists of techniques that adversaries use to communicate with systems under their control. They may use standard protocols, non-standard ports, encryption, proxies, multi-stage channels, or web services to blend with normal traffic.

**Representative techniques:**  
Application Layer Protocol (DNS, web, mail, file-transfer, pub/sub), Communication Through Removable Media, Content Injection, Data Encoding / Obfuscation, Dynamic Resolution (DGA, fast-flux), Encrypted Channel, Fallback Channels, Hide Infrastructure, Ingress Tool Transfer, Multi-Stage Channels, Non-Application Layer Protocol, Non-Standard Port, Protocol Tunneling, Proxy, Remote Access Tools, Traffic Signaling, Web Service.

### TA0010 – Exfiltration
The adversary is trying to steal data.

Exfiltration consists of techniques that adversaries use to steal data from the victim environment. Data may be transferred over the command-and-control channel, alternate protocols, physical media, or web services / cloud accounts.

**Representative techniques:**  
Automated Exfiltration, Data Transfer Size Limits, Exfiltration Over Alternative Protocol / C2 Channel / Other Network Medium / Physical Medium / Web Service, Scheduled Transfer, Transfer Data to Cloud Account.

### TA0040 – Impact
The adversary is trying to manipulate, interrupt, or destroy your systems and data.

Impact consists of techniques that adversaries use to disrupt availability or integrity of systems and data (destruction, encryption for ransomware, defacement, denial-of-service, resource hijacking, service stop, account removal, etc.).

**Representative techniques:**  
Account Access Removal, Data Destruction / Encrypted for Impact / Manipulation, Defacement, Disk Wipe, Email Bombing, Endpoint / Network Denial of Service, Financial Theft, Firmware Corruption, Inhibit System Recovery, Resource Hijacking, Service Stop, System Shutdown/Reboot.

## How to use this summary in the curriculum

- Map lab findings and detection rules to specific technique IDs.
- Use the tactic sequence as a high-level intrusion narrative skeleton.
- Cross-reference with Phase-2 (recon, network analysis, detection) and Phase-3 Track-2 (SOC) / Track-5 (Adversary Simulation) materials.
- Always stay inside authorized laboratory environments.

## Official sources

- Enterprise tactics: https://attack.mitre.org/tactics/enterprise/
- Enterprise matrix: https://attack.mitre.org/matrices/enterprise/
- Techniques list: https://attack.mitre.org/techniques/enterprise/
- Design & philosophy paper (MITRE)
- ATT&CK Navigator for interactive exploration

**Last aligned:** September 2026 (reflecting v19 Stealth / Defense Impairment split).

For the most current technique lists, sub-techniques, mitigations, detections, and procedure examples, always consult the live ATT&CK website.
