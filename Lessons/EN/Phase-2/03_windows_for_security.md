# Stage 3: Windows for Security Practitioners

## Why This Stage Matters

Many organizations run a mix of Windows and Linux systems. End-user workstations, Active Directory domains, file servers, and many business applications are Windows-based. A security practitioner who can only work on Linux is only half-equipped.

Phase-0 introduced Windows concepts (architecture, NTFS permissions, services, processes, Registry, Event Viewer, PowerShell, Active Directory).  
This stage turns those ideas into practical investigation habits you can use inside a laboratory or, later, in authorized professional engagements.

---

## Learning Objectives

By the end of this stage you will be able to:

- Use PowerShell as the primary investigation interface
- List processes, services, and network connections on a Windows system
- Read and filter Windows Event Logs for security-relevant events
- Inspect basic Registry locations that affect security posture
- Understand local users, groups, and privilege concepts
- Apply the same least-privilege mindset you practiced on Linux
- Document findings clearly for later reporting

---

## Safety Checkpoint

All commands and techniques in this stage are intended for **Windows virtual machines that you own and control** inside your isolated laboratory.  
Do not run investigative commands against production systems or any machine outside your lab without explicit authorization.

---

## 1. PowerShell as the Investigation Console

PowerShell is the modern command-line and scripting environment for Windows. Most security-relevant inspection can be done from it.

Useful habits:

- Run PowerShell as a normal user by default; elevate only when necessary.
- Use `Get-Help <cmdlet> -Examples` to see usage patterns.
- Prefer full cmdlet names while learning (`Get-Process` instead of `gps`).
- Pipe output to `Format-List`, `Format-Table`, or `Select-Object` for readability.

Basic orientation commands:

```powershell
$PSVersionTable          # PowerShell version
whoami                   # current user
whoami /groups           # group memberships
hostname                 # computer name
Get-Location             # current directory
```

---

## 2. Processes and Services

### Processes

```powershell
Get-Process
Get-Process | Sort-Object CPU -Descending | Select-Object -First 10
Get-Process -Name explorer | Format-List *
```

Key properties to notice: process name, ID (Id), CPU and memory usage, and the user context when available.

### Services

```powershell
Get-Service
Get-Service | Where-Object {$_.Status -eq "Running"}
Get-Service -Name "Spooler" | Format-List *
```

Services that start automatically and listen on the network form part of the system’s attack surface. In a lab you can safely explore which services are running and which accounts they use.

---

## 3. Network Connections and Listening Ports

Modern Windows provides useful networking cmdlets:

```powershell
Get-NetTCPConnection
Get-NetTCPConnection -State Listen
Get-NetTCPConnection -State Listen | Select-Object LocalAddress, LocalPort, OwningProcess
Get-NetUDPEndpoint
```

To map a listening port back to a process:

```powershell
Get-Process -Id <OwningProcess>
```

Alternatively, the classic tool `netstat` is still available:

```powershell
netstat -ano
netstat -ano | findstr LISTENING
```

**Reading the output:**  
Pay attention to whether a service is listening on `0.0.0.0` (all interfaces) or `127.0.0.1` (localhost only). This distinction matters for exposure assessment, just as it did on Linux.

---

## 4. Windows Event Logs

Windows records a large volume of events. The most security-relevant logs are usually:

- Security
- System
- Application
- PowerShell operational logs (when enabled)

Viewing logs with PowerShell:

```powershell
Get-EventLog -LogName Security -Newest 20
Get-WinEvent -LogName Security -MaxEvents 20
Get-WinEvent -FilterHashtable @{LogName='Security'; ID=4624} -MaxEvents 10
```

Common security event IDs worth recognizing (conceptual awareness):

| Event ID | Typical meaning |
|----------|-----------------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4672 | Special privileges assigned to new logon |
| 4688 | New process created (when process tracking is enabled) |
| 4720 | User account created |

In a laboratory you can generate some of these events yourself (successful and failed logons) and then locate them in the logs. This builds intuition for later blue-team and incident-response work.

---

## 5. Local Users, Groups, and Privileges

```powershell
Get-LocalUser
Get-LocalGroup
Get-LocalGroupMember -Group "Administrators"
whoami /priv
```

Important concepts:

- Local Administrator membership grants very high power on that machine.
- Many privileges (SeDebugPrivilege, SeTakeOwnershipPrivilege, etc.) are powerful and normally restricted.
- Service accounts and scheduled tasks often run with elevated rights; understanding *which* account runs a service is part of attack-surface review.

In domain environments (Active Directory) the picture becomes larger — users, groups, and policies are managed centrally. Phase-0 introduced the idea; deeper Active Directory security is a later specialized topic.

---

## 6. Registry Basics for Security Awareness

The Windows Registry is a hierarchical database of configuration settings. Certain locations influence security posture:

- Auto-start locations (persistence)
- Policy settings
- Service configuration
- Software installation information

Exploration commands (read-only is safest while learning):

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
Get-ChildItem -Path "HKLM:\SYSTEM\CurrentControlSet\Services" | Select-Object -First 10
```

**Safety habit:** Prefer reading over writing while you are learning. Changing Registry values can break a system; always have a snapshot before experiments.

---

## 7. File System and Permissions Awareness

Windows uses Access Control Lists (ACLs) rather than the simple owner/group/other model of Linux.

```powershell
Get-Acl C:\Windows
Get-Acl C:\Users | Format-List
icacls C:\Windows
```

You do not need to master every ACE flag yet. The practical takeaway is:

- Who has Full Control or Modify rights on sensitive directories?
- Are there overly permissive shares or folders?
- Least privilege still applies: grant only what is required.

---

## 8. Simple PowerShell for Investigation Scripts

PowerShell scripts use the `.ps1` extension. A minimal safe pattern:

```powershell
# Simple lab inventory snippet
Write-Output "Host: $(hostname)"
Write-Output "User: $(whoami)"
Write-Output "Listening TCP ports:"
Get-NetTCPConnection -State Listen |
    Select-Object LocalAddress, LocalPort, OwningProcess |
    Format-Table -AutoSize
```

Good habits:

- Start with clear comments.
- Prefer read-only operations while learning.
- Test scripts on a snapshot of a lab VM.
- Avoid hard-coding credentials.
- Use `Set-ExecutionPolicy` understanding carefully (RemoteSigned is common on lab machines you control).

---

## Common Mistakes

| Mistake | Risk | Better practice |
|---------|------|-----------------|
| Always running PowerShell as Administrator | Unnecessary privilege; harder to see normal-user behavior | Elevate only when required |
| Ignoring OwningProcess when looking at ports | Cannot tell which program is listening | Always map port → process |
| Treating Event Logs as noise | Misses valuable signal | Learn a few high-value Event IDs first |
| Editing the Registry without a snapshot | Can render a VM unbootable | Snapshot first; prefer read-only exploration |
| Forgetting that Windows and Linux logging models differ | Confusion when switching environments | Keep a short comparison note in your notebook |

---

## Best Practices

- Use snapshots liberally before any configuration change or new tool installation.
- Keep a personal list of the PowerShell cmdlets you use most.
- When examining a lab target, record: hostname, OS version, listening ports, running services, and recent interesting log events.
- Practice the same investigative questions on both Linux and Windows so the mental model becomes consistent.
- Remember that many corporate environments restrict PowerShell logging or script execution — lab freedom is a privilege, not a universal reality.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/PowerShell/03_windows_security/Host-Inspect.ps1` | Identity, listening ports, top processes, Administrators group |
| `Codes/PowerShell/03_windows_security/Get-ListeningPorts.ps1` | Map listening TCP ports to process name and path |
| `Codes/PowerShell/03_windows_security/Get-SecurityEvents.ps1` | Newest Security log events (optional `-LogonOnly`) |
| `Codes/PowerShell/03_windows_security/Get-StartupAndServices.ps1` | Run-key startups, running services, local users |

```powershell
# From an elevated or normal PowerShell on your Windows lab VM:
Set-Location <path-to-repo>\Codes\PowerShell\03_windows_security
.\Host-Inspect.ps1
.\Get-ListeningPorts.ps1
.\Get-SecurityEvents.ps1 -MaxEvents 15 -LogonOnly
.\Get-StartupAndServices.ps1
```

If script execution is restricted in the lab VM:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` (only on machines you control).

**SAFETY:** Run only on Windows laboratory VMs you own.


On a Windows virtual machine you control:

1. List all listening TCP ports and identify the owning process for each.
2. Retrieve the newest 15 Security log events and note any logon-related entries.
3. List the members of the local Administrators group.
4. Display the programs configured to run at startup from the common Run key.
5. Write a short PowerShell snippet that prints hostname, current user, and listening TCP ports. Save the output in your lab notebook.

**Success criteria:** You can map ports to processes, locate recent logon events, and have a reusable inspection snippet.

---

## Review Questions

1. Why is PowerShell the preferred investigation interface on modern Windows systems?
2. How do you determine which process owns a listening TCP port?
3. Name two Windows Security event IDs that relate to logon activity.
4. What is the practical risk of making Registry changes without a snapshot?
5. How does the Windows permission model differ conceptually from the Linux owner/group/other model?
6. Why should you avoid running everyday investigation commands as Administrator?

---

## Summary

- Windows is a major part of most real environments; practical familiarity is required.
- PowerShell provides process, service, network, log, and configuration visibility.
- Event Logs, especially the Security log, are a primary investigative source.
- Mapping listening ports to processes and understanding account privileges are core habits.
- Least privilege, snapshots, and careful documentation remain essential even in a laboratory.
- With both Linux and Windows inspection skills in place, you are ready to move into network traffic analysis — the next major practical pillar.

**Next stage:** Network Analysis and Packet Crafting — seeing and interpreting the traffic that flows between systems.
