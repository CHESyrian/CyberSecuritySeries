# Infrastructure and Cloud Tools

Used mainly in **Phase-3 Track 3** (infra) and **Track 4** (cloud fundamentals).

---

## Host baseline inspection (Linux / Windows)

| | |
|--|--|
| **What it is** | Using existing shell tools and project scripts to record “normal” listening ports and services |
| **Used for** | Hardening lab VMs; noticing unnecessary exposure |

**Examples:**

```bash
./Codes/Bash/02_linux_security/host_inspect.sh
./Codes/Bash/Track-3-Infra/baseline_ports_note.sh
```

```powershell
.\Codes\PowerShell\03_windows_security\Host-Inspect.ps1
.\Codes\PowerShell\03_windows_security\Get-StartupAndServices.ps1
```

**Explanation:** A baseline is a dated record of what *should* be listening. After changes, compare and close what you do not need **on lab VMs**.

---

## Nmap (inventory role)

| | |
|--|--|
| **Used for** | Authorized inventory of lab hosts during a vulnerability-management mini-cycle |

**Example:**

```bash
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
```

See also `Tools/EN/03_recon_and_scan_tools.md`.

---

## Firewall / segmentation (lab concepts)

| | |
|--|--|
| **What it is** | Policy devices or OS firewalls separating trust zones |
| **Used for** | Practicing default-deny thinking between lab segments |

**Explanation:** Tools vary (nftables/iptables, Windows Firewall, virtual firewall appliances). This curriculum emphasizes **policy intent** and diagrams more than vendor syntax. Experiment only on lab gateways you own; snapshot first.

**Example practice:** Draw management vs workload zones; allow only needed ports between them on a lab firewall VM.

---

## IDS/IPS concepts (lab traffic)

| | |
|--|--|
| **What it is** | Network sensors that alert (IDS) or may block (IPS) on matching patterns |
| **Used for** | Understanding placement and false positives using **lab PCAPs or generated lab traffic** |

**Example practice:** Capture lab port-scan traffic with tshark/Wireshark; discuss what a signature might look like — without deploying sensors on production networks.

---

## Cloud provider CLIs (optional, lab/free-tier only)

| | |
|--|--|
| **Examples** | AWS CLI, Azure CLI, Google Cloud SDK |
| **Used for** | Inspecting **your** lab/free-tier resources (identity, network rules, storage exposure) |

**Explanation:** Track 4 is vendor-agnostic first (shared responsibility, least privilege, exposure checklists). CLIs are optional. Never use employer production accounts for curriculum experiments. Enable billing alarms if the account can incur cost.

**Example practice pattern (any cloud you own):**

1. List resources in the lab project.  
2. Confirm storage is not world-readable.  
3. Confirm admin endpoints are not open to `0.0.0.0/0` unless required and intentional.  
4. Locate audit/login logs for that project.

**Safety:** Do not scan or attack other tenants’ cloud resources. Delete temporary open resources after labs.


---

## Worked lab workflow (infra baseline)

1. Snapshot the lab VM.
2. Record ports:
   ```bash
   ./Codes/Bash/Track-3-Infra/baseline_ports_note.sh
   ./Codes/Bash/02_linux_security/host_inspect.sh
   ```
3. Inventory one lab host only:
   ```bash
   ./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
   ```
4. Document: port, process, need-to-have yes/no, action.

**Cloud lab habit (free-tier / emulator you own)**
1. List resources in *your* project only.
2. Check storage is not public-read.
3. Check admin ports are not open to the world unless intentional.
4. Turn off or delete temporary resources after the exercise.

**Common mistakes**
- Changing firewall rules on a home router “for practice.”
- Using employer cloud accounts for curriculum labs.
