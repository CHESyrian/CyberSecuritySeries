# TA0010 – Exfiltration

**ID:** TA0010  
**Tactic:** Exfiltration  
**Shortname:** `exfiltration`

## Definition

The adversary is trying to steal data.

Exfiltration consists of techniques that adversaries may use to steal data from your network. Once they’ve collected data, adversaries often package it to avoid detection while removing it. This can include compression and encryption. Techniques for getting data out of a target network typically include transferring it over their command and control channel or an alternate channel and may also include putting size limits on the transmission.

## Techniques in this Tactic (19 total)

| ID | Name | Type |
|----|------|------|
| [T1011](T1011_Exfiltration_Over_Other_Network_Medium.md) | Exfiltration Over Other Network Medium | Technique |
| [T1011.001](T1011.001_Exfiltration_Over_Bluetooth.md) | Exfiltration Over Bluetooth | Sub-technique |
| [T1020](T1020_Automated_Exfiltration.md) | Automated Exfiltration | Technique |
| [T1020.001](T1020.001_Traffic_Duplication.md) | Traffic Duplication | Sub-technique |
| [T1029](T1029_Scheduled_Transfer.md) | Scheduled Transfer | Technique |
| [T1030](T1030_Data_Transfer_Size_Limits.md) | Data Transfer Size Limits | Technique |
| [T1041](T1041_Exfiltration_Over_C2_Channel.md) | Exfiltration Over C2 Channel | Technique |
| [T1048](T1048_Exfiltration_Over_Alternative_Protocol.md) | Exfiltration Over Alternative Protocol | Technique |
| [T1048.001](T1048.001_Exfiltration_Over_Symmetric_Encrypted_Non-C2_Protocol.md) | Exfiltration Over Symmetric Encrypted Non-C2 Protocol | Sub-technique |
| [T1048.002](T1048.002_Exfiltration_Over_Asymmetric_Encrypted_Non-C2_Protocol.md) | Exfiltration Over Asymmetric Encrypted Non-C2 Protocol | Sub-technique |
| [T1048.003](T1048.003_Exfiltration_Over_Unencrypted_Non-C2_Protocol.md) | Exfiltration Over Unencrypted Non-C2 Protocol | Sub-technique |
| [T1052](T1052_Exfiltration_Over_Physical_Medium.md) | Exfiltration Over Physical Medium | Technique |
| [T1052.001](T1052.001_Exfiltration_over_USB.md) | Exfiltration over USB | Sub-technique |
| [T1537](T1537_Transfer_Data_to_Cloud_Account.md) | Transfer Data to Cloud Account | Technique |
| [T1567](T1567_Exfiltration_Over_Web_Service.md) | Exfiltration Over Web Service | Technique |
| [T1567.001](T1567.001_Exfiltration_to_Code_Repository.md) | Exfiltration to Code Repository | Sub-technique |
| [T1567.002](T1567.002_Exfiltration_to_Cloud_Storage.md) | Exfiltration to Cloud Storage | Sub-technique |
| [T1567.003](T1567.003_Exfiltration_to_Text_Storage_Sites.md) | Exfiltration to Text Storage Sites | Sub-technique |
| [T1567.004](T1567.004_Exfiltration_Over_Webhook.md) | Exfiltration Over Webhook | Sub-technique |

## Official Description

The adversary is trying to steal data.

Exfiltration consists of techniques that adversaries use to steal data from the victim environment. Data may be transferred over the command-and-control channel, alternate protocols, physical media, or web services / cloud accounts.

**Source:** https://attack.mitre.org/tactics/TA0010/

## Key Techniques (representative)

- T1020 Automated Exfiltration
- T1030 Data Transfer Size Limits
- T1048 Exfiltration Over Alternative Protocol
- T1041 Exfiltration Over C2 Channel
- T1011 Exfiltration Over Other Network Medium
- T1052 Exfiltration Over Physical Medium
- T1567 Exfiltration Over Web Service
- T1029 Scheduled Transfer
- T1537 Transfer Data to Cloud Account

Full list: https://attack.mitre.org/tactics/TA0010/

## Educational Focus

Detect large or unusual outbound data transfers, use of cloud storage for staging, and exfiltration over non-standard channels.

## Sources

*Source: [MITRE ATT&CK Tactic TA0010](https://attack.mitre.org/tactics/TA0010/)*
