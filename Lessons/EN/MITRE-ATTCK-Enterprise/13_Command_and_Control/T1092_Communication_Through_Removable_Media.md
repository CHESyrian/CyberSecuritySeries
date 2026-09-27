# T1092: Communication Through Removable Media

**Type:** Technique  
**Platforms:** Linux, macOS, Windows  
**Tactics:** command-and-control

## Description / Explanation

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [Replication Through Removable Media](https://attack.mitre.org/techniques/T1091). Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

---
*Source: [MITRE ATT&CK Technique T1092](https://attack.mitre.org/techniques/T1092/)*
