# T1568: Dynamic Resolution

**Type:** Technique  
**Platforms:** ESXi, Linux, macOS, Windows  
**Tactics:** command-and-control

## Description / Explanation

Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculations can be used to dynamically adjust parameters such as the domain name, IP address, or port number the malware uses for command and control.

Adversaries may use dynamic resolution for the purpose of [Fallback Channels](https://attack.mitre.org/techniques/T1008). When contact is lost with the primary command and control server malware may employ dynamic resolution as a means to reestablishing command and control.(Citation: Talos CCleanup 2017)(Citation: FireEye POSHSPY April 2017)(Citation: ESET Sednit 2017 Activity)

---
*Source: [MITRE ATT&CK Technique T1568](https://attack.mitre.org/techniques/T1568/)*
