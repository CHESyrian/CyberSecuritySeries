# Stage 5: Reconnaissance and Enumeration (Authorized)

## Why This Stage Matters

Before you can assess or defend a system, you need to know what exists. Reconnaissance and enumeration are the disciplined processes of discovering live hosts, open services, and basic information about them — always within authorization.

In Phase-1 you learned the conceptual place of reconnaissance inside a penetration test.  
In this stage you practice the *authorized* version of those activities inside your laboratory.

---

## Learning Objectives

By the end of this stage you will be able to:

- Distinguish passive reconnaissance from active reconnaissance
- Perform safe host discovery and port scanning against laboratory targets only
- Interpret common Nmap output and understand what different scan types reveal
- Enumerate basic service information (banners, versions) without crossing into exploitation
- Document findings in a clear, repeatable way
- Apply strict scope and safety rules so that no activity leaves the lab boundary

---

## Safety Checkpoint

**All scanning and enumeration in this stage must target only systems inside your isolated laboratory.**

- Never scan your home router, ISP equipment, or any public IP address as part of these exercises.
- Never scan systems belonging to other people or organizations.
- Confirm the IP addresses of your lab virtual machines before every scan.
- If a tool asks for a target and you are unsure, stop.

Unauthorized port scanning can be illegal. Treat scope as sacred.

---

## 1. Passive vs Active Reconnaissance

| Type | Description | Examples in a lab context |
|------|-------------|---------------------------|
| **Passive** | Collecting information without sending packets to the target | Reviewing lab documentation, examining your own VM configuration files, looking at previously captured PCAPs |
| **Active** | Sending packets to the target to elicit responses | Ping sweeps, port scans, service version probes against lab VMs |

In professional engagements both are used, but they are always constrained by the Rules of Engagement. In your lab the “Rules of Engagement” are simple: only the virtual machines you own.

---

## 2. Host Discovery (Finding Live Systems)

The first practical question is: which addresses in my lab network are actually responding?

Common approaches (lab only):

```bash
# Simple ping of a single lab host
ping -c 3 192.168.56.10

# Using Nmap for host discovery on a lab subnet (example range)
nmap -sn 192.168.56.0/24
```

`-sn` (ping scan) asks Nmap to discover hosts without performing a full port scan. Always replace the example range with the actual address range of *your* host-only or internal lab network.

Record every live IP and, if possible, the hostname.

---

## 3. Port Scanning Fundamentals

Once you know a host is alive, the next question is: which ports are open and what services might be listening?

Nmap is the industry-standard tool. Essential concepts:

| Scan type (conceptual) | What it does | Typical use in learning |
|------------------------|--------------|-------------------------|
| TCP SYN scan (`-sS`) | Sends SYN packets; interprets responses | Fast, common default for privileged users |
| TCP Connect scan (`-sT`) | Completes the full TCP handshake | Works without special privileges |
| UDP scan (`-sU`) | Probes UDP ports | Slower; useful for DNS, SNMP, etc. |
| Version detection (`-sV`) | Tries to determine service and version | Enumeration step after finding open ports |
| Script scanning (`-sC`) | Runs default safe scripts | Additional information gathering |

Example (lab target only):

```bash
# Replace with your actual lab target IP
nmap -sS -sV -O 192.168.56.10
```

**Reading the results:**
- Open ports are the primary findings.
- Service and version information helps you understand what is running.
- OS detection is an educated guess, not absolute truth.

---

## 4. Safe Enumeration Practices

Enumeration goes beyond “port is open” to “what can I learn about the service without exploiting it?”

Examples of appropriate lab enumeration:

- Reading service banners
- Querying DNS for lab hostnames
- Asking a web server for its Server header
- Listing anonymous FTP contents (if the lab target allows it)
- Checking for common, non-destructive information disclosures

Stay on the discovery side of the line. Do not attempt to log in with guessed credentials, submit attack payloads, or use exploit modules in this stage. Those topics belong to later specialized training and only under explicit authorization.

---

## 5. Documenting Findings

Good notes turn raw scan data into useful knowledge. For each lab target record at least:

- IP address and hostname (if known)
- Date and time of the scan
- Command(s) used
- Open ports and detected services/versions
- Any interesting banners or extra information
- Screenshots or saved Nmap output files

A simple markdown or text template is enough at this stage. Later you will turn these notes into professional report sections.

---

## 6. Linking Back to Previous Stages

- Stage 2 & 3 (Linux/Windows): After a port appears open, log into the lab VM (if you have credentials) and confirm which process owns that port with `ss` or PowerShell.
- Stage 4 (Network analysis): Capture the scan traffic itself. You will see the SYN packets, SYN-ACK replies, and any version-detection probes. This reinforces protocol understanding.

---

## Common Mistakes

| Mistake | Risk | Better practice |
|---------|------|-----------------|
| Scanning the wrong IP range | Hitting systems outside the lab | Double-check interface and IP addresses before every scan |
| Running aggressive scans on fragile lab VMs | Crashing a target | Start with milder options; snapshot first |
| Treating version detection as 100% accurate | Wrong conclusions | Treat banners and version guesses as hints, not proof |
| Skipping documentation | Lost context later | Save command lines and output immediately |
| Confusing enumeration with exploitation | Scope creep / ethics violation | Stop at information gathering in this stage |

---

## Best Practices

- Always begin with the narrowest scope possible (single host, then small range).
- Snapshot targets before intensive scanning.
- Prefer saving Nmap output in multiple formats (`-oA basename`) for later review.
- Re-run the same scan after configuration changes to see the difference.
- Keep a living inventory of your lab hosts and their open services.
- Never let curiosity override the lab boundary.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/Bash/05_reconnaissance/safe_lab_nmap.sh` | Nmap wrapper that writes dated output under `./nmap_lab_output` |
| `Codes/Python/05_reconnaissance/lab_port_scan.py` | Minimal educational TCP port check |
| `Codes/Python/05_reconnaissance/lab_banner_grab.py` | Short TCP banner grab (no exploitation) |
| `Codes/Python/04_network_analysis/scan_socket_*.py` | Additional socket scan demos |

```bash
chmod +x Codes/Bash/05_reconnaissance/safe_lab_nmap.sh
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10

python3 Codes/Python/05_reconnaissance/lab_port_scan.py 192.168.56.10
python3 Codes/Python/05_reconnaissance/lab_banner_grab.py 192.168.56.10 22
```

**SAFETY:** Every target IP must be inside your isolated laboratory.


1. Confirm the IP addresses of your attacker VM and at least one target VM.
2. Perform a host-discovery scan limited to your lab network range.
3. Choose one live target and run a TCP port scan with version detection.
4. Save the results (command line + output) in your lab notebook.
5. On the target VM itself (using skills from Stages 2 or 3), identify which process is listening on one of the open ports you found.
6. (Optional) Capture the scan traffic with Wireshark/tshark and identify the SYN packets.

**Success criteria:** You have a documented list of open ports on a lab target, you know which process owns at least one of them, and every packet stayed inside the lab.

---

## Review Questions

1. What is the key difference between passive and active reconnaissance?
2. Why is host discovery usually performed before a full port scan?
3. What does Nmap version detection (`-sV`) attempt to determine?
4. Name two pieces of information you should always record when documenting a scan.
5. How can host-based tools from Stages 2 and 3 improve the value of a port scan?
6. What should you do if you are unsure whether an IP address is inside your lab scope?

---

## Summary

- Reconnaissance and enumeration answer “what is there?” inside an authorized boundary.
- Passive methods collect information without touching the target; active methods send probes.
- Nmap is the standard tool for host discovery and port scanning; version detection adds useful context.
- Documentation turns scan results into lasting knowledge.
- Correlation with host process information and packet captures deepens understanding.
- Scope discipline is non-negotiable: only laboratory systems you own.

**Next stage:** Vulnerability Assessment Concepts — understanding how scanners work, how to read CVE and CVSS information, and how to prioritize findings.
