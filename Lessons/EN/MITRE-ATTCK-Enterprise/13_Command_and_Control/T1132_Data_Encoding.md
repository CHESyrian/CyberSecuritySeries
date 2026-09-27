# T1132: Data Encoding

**Type:** Technique  
**Platforms:** ESXi, Linux, macOS, Windows  
**Tactics:** command-and-control

## Description / Explanation

Adversaries may encode data to make the content of command and control traffic more difficult to detect. Command and control (C2) information can be encoded using a standard data encoding system. Use of data encoding may adhere to existing protocol specifications and includes use of ASCII, Unicode, Base64, MIME, or other binary-to-text and character encoding systems.(Citation: Wikipedia Binary-to-text Encoding) (Citation: Wikipedia Character Encoding) Some data encoding systems may also result in data compression, such as gzip.

---
*Source: [MITRE ATT&CK Technique T1132](https://attack.mitre.org/techniques/T1132/)*
