# T1005: Data from Local System

**Type:** Technique  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Tactics:** collection

## Description / Explanation

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

Adversaries may do this using a [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059), such as [cmd](https://attack.mitre.org/software/S0106) as well as a [Network Device CLI](https://attack.mitre.org/techniques/T1059/008), which have functionality to interact with the file system to gather information.(Citation: show_run_config_cmd_cisco) Adversaries may also use [Automated Collection](https://attack.mitre.org/techniques/T1119) on the local system.

---
*Source: [MITRE ATT&CK Technique T1005](https://attack.mitre.org/techniques/T1005/)*
