# T1098: Account Manipulation

**Type:** Technique  
**Platforms:** Containers, ESXi, IaaS, Identity Provider, Linux, macOS, Network Devices, Office Suite, SaaS, Windows  
**Tactics:** persistence, privilege-escalation

## Description / Explanation

Adversaries may manipulate accounts to maintain and/or elevate access to victim systems. Account manipulation may consist of any action that preserves or modifies adversary access to a compromised account, such as modifying credentials or permission groups.(Citation: FireEye SMOKEDHAM June 2021) These actions could also include account activity designed to subvert security policies, such as performing iterative password updates to bypass password duration policies and preserve the life of compromised credentials. 

In order to create or manipulate accounts, the adversary must already have sufficient permissions on systems or the domain. However, account manipulation may also lead to privilege escalation where modifications grant access to additional roles, permissions, or higher-privileged [Valid Accounts](https://attack.mitre.org/techniques/T1078).

---
*Source: [MITRE ATT&CK Technique T1098](https://attack.mitre.org/techniques/T1098/)*
