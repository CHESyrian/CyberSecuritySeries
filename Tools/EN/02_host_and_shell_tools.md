# Host and Shell Tools

Used in **Phase-2 Stages 2–3** and Phase-3 Tracks 2, 3, and 5.

---

## Bash

| | |
|--|--|
| **What it is** | Default shell on most Linux lab VMs |
| **Used for** | Running commands, pipelines, small inspection scripts |

**Explanation:** Security work on Linux is largely “read state → filter → record.” Bash glues tools together.

**Examples:**

```bash
whoami; id
ss -tulnp
ps aux --sort=-%cpu | head
grep -i fail /var/log/auth.log | tail
```

**Project scripts:**

```bash
./Codes/Bash/02_linux_security/host_inspect.sh
./Codes/Bash/02_linux_security/failed_logons_summary.sh
```

---

## ss / netstat

| | |
|--|--|
| **What they are** | Socket statistics (ss is modern; netstat is legacy) |
| **Used for** | Listing listening ports and connections on a lab host |

**Examples:**

```bash
ss -tulnp          # listening TCP/UDP with process
ss -tan            # all TCP, numeric
```

---

## ps, top / htop

| | |
|--|--|
| **What they are** | Process listing and live process monitors |
| **Used for** | Seeing what runs on a lab host; spotting unexpected processes in exercises |

**Example:**

```bash
ps aux --sort=-%mem | head -n 15
```

---

## ip / ifconfig

| | |
|--|--|
| **What they are** | Interface and address configuration viewers |
| **Used for** | Confirming lab IP addresses and interfaces before scans/captures |

**Example:**

```bash
ip -brief addr
ip route
```

---

## journalctl / auth.log

| | |
|--|--|
| **What they are** | systemd journal viewer; classic auth log files |
| **Used for** | Investigating logons and service messages on lab Linux VMs |

**Examples:**

```bash
journalctl -u ssh -n 30 --no-pager
grep -iE 'failed|invalid' /var/log/auth.log | tail -n 20
```

**Project:** `Codes/Python/02_linux_security/parse_auth_failures.py`

---

## grep, awk, tail, find

| | |
|--|--|
| **What they are** | Search and text-processing utilities |
| **Used for** | Filtering logs and command output during lab investigations |

**Example:**

```bash
grep -i fail /var/log/auth.log | awk '{print $(NF-3)}' | sort | uniq -c | sort -nr | head
```

---

## PowerShell

| | |
|--|--|
| **What it is** | Primary shell and automation environment on modern Windows |
| **Used for** | Host inspection, event queries, service/process inventory on **lab** Windows VMs |

**Explanation:** Cmdlets return objects you can filter and format — better for investigation than raw text alone.

**Examples:**

```powershell
Get-NetTCPConnection -State Listen | Format-Table -AutoSize
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-WinEvent -LogName Security -MaxEvents 15
Get-LocalUser
```

**Project scripts:**

```powershell
.\Codes\PowerShell\03_windows_security\Host-Inspect.ps1
.\Codes\PowerShell\03_windows_security\Get-ListeningPorts.ps1
.\Codes\PowerShell\03_windows_security\Get-SecurityEvents.ps1 -LogonOnly
.\Codes\PowerShell\03_windows_security\Get-StartupAndServices.ps1
```

If scripts are blocked on a lab VM you control:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

---

## Get-NetTCPConnection / netstat (Windows)

| | |
|--|--|
| **Used for** | Mapping listening ports to PIDs on lab Windows hosts |

**Example:** See `Get-ListeningPorts.ps1` above.

---

## Get-WinEvent / Get-EventLog

| | |
|--|--|
| **Used for** | Reading Security and other logs on lab Windows VMs |

**Common IDs (lab study):** 4624 logon success, 4625 logon failure, 4688 process creation (if audited).


---

## Worked lab workflow (Linux then Windows)

**Linux lab VM**
```bash
./Codes/Bash/02_linux_security/host_inspect.sh
./Codes/Bash/02_linux_security/failed_logons_summary.sh
python3 Codes/Python/02_linux_security/parse_auth_failures.py /var/log/auth.log
```

**Windows lab VM**
```powershell
Set-Location ...\Codes\PowerShell\03_windows_security
.\Host-Inspect.ps1
.\Get-ListeningPorts.ps1
.\Get-SecurityEvents.ps1 -LogonOnly -MaxEvents 25
```

**What to record in the notebook**
- Hostname, date, account used
- Unexpected listening ports
- Recent failed logons (count + source if visible)

**Common mistakes**
- Running inventory as an excuse to scan outside the lab.
- Ignoring 127.0.0.1 listeners (local-only is different from 0.0.0.0).
