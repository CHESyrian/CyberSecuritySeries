# T1573: Encrypted Channel

**Type:** Technique  
**Platforms:** ESXi, Linux, macOS, Network Devices, Windows  
**Tactics:** command-and-control

## Description / Explanation

Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded and/or generated within malware samples/configuration files.

---
*Source: [MITRE ATT&CK Technique T1573](https://attack.mitre.org/techniques/T1573/)*
