# T1216: System Script Proxy Execution

**Type:** Technique  
**Platforms:** Windows  
**Tactics:** stealth

## Description / Explanation

Adversaries may use trusted scripts, often signed with certificates, to proxy the execution of malicious files. Several Microsoft signed scripts that have been downloaded from Microsoft or are default on Windows installations can be used to proxy execution of other files.(Citation: LOLBAS Project) This behavior may be abused by adversaries to execute malicious files that could bypass application control and signature validation on systems.(Citation: GitHub Ultimate AppLocker Bypass List)

---
*Source: [MITRE ATT&CK Technique T1216](https://attack.mitre.org/techniques/T1216/)*
