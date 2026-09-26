# SOC and Detection Tools

Used in **Phase-2 Stages 9–10** and **Phase-3 Track 2** (and Track 5 purple-team loops).

---

## Linux authentication logs / journalctl

| | |
|--|--|
| **What they are** | Local records of logons and service messages |
| **Used for** | Detecting failed logons and tracing activity on lab Linux VMs |

**Examples:**

```bash
grep -iE 'failed|invalid|accepted' /var/log/auth.log | tail -n 30
journalctl -u ssh -n 50 --no-pager

# Follow failures live (lab)
./Codes/Bash/09_logging_detection/auth_failure_watch.sh
./Codes/Bash/Track-2-SOC/count_auth_failures.sh /var/log/auth.log
```

---

## Windows Security log (Get-WinEvent)

| | |
|--|--|
| **What it is** | Windows event channel for security-relevant events |
| **Used for** | Lab investigation of logon success/failure and related events |

**Examples:**

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4624,4625} -MaxEvents 20
.\Codes\PowerShell\03_windows_security\Get-SecurityEvents.ps1 -LogonOnly -MaxEvents 20
```

---

## Lab SIEM (Wazuh, Security Onion lite, ELK-style stacks)

| | |
|--|--|
| **What it is** | Searchable, centralized view of logs and simple alerts |
| **Used for** | Practicing search, correlation, and detection design in a **self-hosted lab** |

**Explanation:** A SIEM does not magically detect attacks; you define what “interesting” means. Phase-3 Track 2 focuses on questions, thresholds, and triage — not product certification.

**Example practice pattern:**

1. Ship lab auth logs into your stack (or use local files first).  
2. Search: failed logons from one source, then a success.  
3. Write a detection idea in plain language, then as a rule/query.  
4. Generate the activity only against lab VMs; triage TP vs FP.

---

## Project detection helpers

| Tool / script | Used for |
|---------------|----------|
| `Codes/Python/09_logging_detection/simple_detection_demo.py` | Threshold alerts from a log file |
| `Codes/Python/Track-2-SOC/detection_threshold_demo.py` | Offline teaching demo of threshold logic |
| `Codes/Python/02_linux_security/parse_auth_failures.py` | Rank failure sources in a log |
| `Codes/Bash/10_incident_response/collect_basic_evidence.sh` | Collect basic host artifacts after a lab incident exercise |

**Examples:**

```bash
python3 Codes/Python/09_logging_detection/simple_detection_demo.py /var/log/auth.log -t 5
python3 Codes/Python/Track-2-SOC/detection_threshold_demo.py
./Codes/Bash/10_incident_response/collect_basic_evidence.sh
```

**Safety:** Collect and alert only on systems you control. Do not disable logging on production systems as part of these exercises.


---

## Worked lab workflow (detection)

1. Generate a few failed logons against a **lab** SSH/RDP service only.
2. Count and rank:
   ```bash
   ./Codes/Bash/Track-2-SOC/count_auth_failures.sh /var/log/auth.log
   python3 Codes/Python/09_logging_detection/simple_detection_demo.py /var/log/auth.log -t 3
   ```
3. Teaching correlation demo:
   ```bash
   python3 Codes/Python/Track-2-SOC/correlate_failed_then_success.py
   ```
4. Fill triage notes:
   ```bash
   python3 Codes/Python/Track-2-SOC/triage_template.py
   ```
5. After a tabletop incident, collect basic evidence:
   ```bash
   ./Codes/Bash/10_incident_response/collect_basic_evidence.sh
   ```

**Common mistakes**
- Alerting on every log line (no threshold or context).
- Collecting evidence from production without authorization.
