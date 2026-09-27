# T1567: Exfiltration Over Web Service

**Type:** Technique  
**Platforms:** ESXi, Linux, macOS, Office Suite, SaaS, Windows  
**Tactics:** exfiltration

## Description / Explanation

Adversaries may use an existing, legitimate external Web service to exfiltrate data rather than their primary command and control channel. Popular Web services acting as an exfiltration mechanism may give a significant amount of cover due to the likelihood that hosts within a network are already communicating with them prior to compromise. Firewall rules may also already exist to permit traffic to these services.

Web service providers also commonly use SSL/TLS encryption, giving adversaries an added level of protection.

---
*Source: [MITRE ATT&CK Technique T1567](https://attack.mitre.org/techniques/T1567/)*
