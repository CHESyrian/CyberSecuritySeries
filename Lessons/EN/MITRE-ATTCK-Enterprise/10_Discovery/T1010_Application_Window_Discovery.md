# T1010: Application Window Discovery

**Type:** Technique  
**Platforms:** Linux, macOS, Windows  
**Tactics:** discovery

## Description / Explanation

Adversaries may attempt to get a listing of open application windows. Window listings could convey information about how the system is used.(Citation: Prevailion DarkWatchman 2021) For example, information about application windows could be used identify potential data to collect as well as identifying security tooling ([Security Software Discovery](https://attack.mitre.org/techniques/T1518/001)) to evade.(Citation: ESET Grandoreiro April 2020)

Adversaries typically abuse system features for this type of enumeration. For example, they may gather information through native system features such as [Command and Scripting Interpreter](https://attack.mitre.org/techniques/T1059) commands and [Native API](https://attack.mitre.org/techniques/T1106) functions.

---
*Source: [MITRE ATT&CK Technique T1010](https://attack.mitre.org/techniques/T1010/)*
