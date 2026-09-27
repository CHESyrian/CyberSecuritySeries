# T1037: Boot or Logon Initialization Scripts

**Type:** Technique  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Tactics:** persistence, privilege-escalation

## Description / Explanation

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other programs or send information to an internal logging server. These scripts can vary based on operating system and whether applied locally or remotely.  

Adversaries may use these scripts to maintain persistence on a single system. Depending on the access configuration of the logon scripts, either local credentials or an administrator account may be necessary. 

An adversary may also be able to escalate their privileges since some boot or logon initialization scripts run with higher privileges.

---
*Source: [MITRE ATT&CK Technique T1037](https://attack.mitre.org/techniques/T1037/)*
