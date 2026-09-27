# T1137: Office Application Startup

**Type:** Technique  
**Platforms:** Windows, Office Suite  
**Tactics:** persistence

## Description / Explanation

Adversaries may leverage Microsoft Office-based applications for persistence between startups. Microsoft Office is a fairly common application suite on Windows-based operating systems within an enterprise network. There are multiple mechanisms that can be used with Office for persistence when an Office-based application is started; this can include the use of Office Template Macros and add-ins.

A variety of features have been discovered in Outlook that can be abused to obtain persistence, such as Outlook rules, forms, and Home Page.(Citation: SensePost Ruler GitHub) These persistence mechanisms can work within Outlook or be used through Office 365.(Citation: TechNet O365 Outlook Rules)

---
*Source: [MITRE ATT&CK Technique T1137](https://attack.mitre.org/techniques/T1137/)*
