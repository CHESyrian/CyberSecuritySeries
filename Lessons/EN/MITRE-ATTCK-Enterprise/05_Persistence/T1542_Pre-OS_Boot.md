# T1542: Pre-OS Boot

**Type:** Technique  
**Platforms:** Linux, macOS, Network Devices, Windows  
**Tactics:** stealth, persistence

## Description / Explanation

Adversaries may abuse Pre-OS Boot mechanisms as a way to establish persistence on a system. During the booting process of a computer, firmware and various startup services are loaded before the operating system. These programs control flow of execution before the operating system takes control.(Citation: Wikipedia Booting)

Adversaries may overwrite data in boot drivers or firmware such as BIOS (Basic Input/Output System) and The Unified Extensible Firmware Interface (UEFI) to persist on systems at a layer below the operating system. This can be particularly difficult to detect as malware at this level will not be detected by host software-based defenses.

---
*Source: [MITRE ATT&CK Technique T1542](https://attack.mitre.org/techniques/T1542/)*
