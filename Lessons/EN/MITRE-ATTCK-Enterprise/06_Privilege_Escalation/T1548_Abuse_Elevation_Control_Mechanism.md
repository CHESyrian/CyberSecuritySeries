# T1548: Abuse Elevation Control Mechanism

**Type:** Technique  
**Platforms:** Linux, macOS, Windows, IaaS, Office Suite, Identity Provider  
**Tactics:** privilege-escalation

## Description / Explanation

Adversaries may circumvent mechanisms designed to control privilege elevation to gain higher-level permissions. Most modern systems contain native elevation control mechanisms that are intended to limit privileges that a user can perform on a machine. Authorization has to be granted to specific users in order to perform tasks that can be considered of higher risk.(Citation: TechNet How UAC Works)(Citation: sudo man page 2018) An adversary can perform several methods to take advantage of built-in control mechanisms in order to escalate privileges on a system.(Citation: OSX Keydnap malware)(Citation: Fortinet Fareit)

---
*Source: [MITRE ATT&CK Technique T1548](https://attack.mitre.org/techniques/T1548/)*
