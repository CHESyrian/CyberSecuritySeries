# T1115: Clipboard Data

**Type:** Technique  
**Platforms:** Linux, macOS, Windows  
**Tactics:** collection

## Description / Explanation

Adversaries may collect data stored in the clipboard from users copying information within or between applications. 

For example, on Windows adversaries can access clipboard data by using <code>clip.exe</code> or <code>Get-Clipboard</code>.(Citation: MSDN Clipboard)(Citation: clip_win_server)(Citation: CISA_AA21_200B) Additionally, adversaries may monitor then replace users’ clipboard with their data (e.g., [Transmitted Data Manipulation](https://attack.mitre.org/techniques/T1565/002)).(Citation: mining_ruby_reversinglabs)

macOS and Linux also have commands, such as <code>pbpaste</code>, to grab clipboard contents.(Citation: Operating with EmPyre)

---
*Source: [MITRE ATT&CK Technique T1115](https://attack.mitre.org/techniques/T1115/)*
