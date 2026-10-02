# TA0009 – Collection

**ID:** TA0009  
**Tactic:** Collection  
**Shortname:** `collection`

## Definition

The adversary is trying to gather data of interest to their goal.

Collection consists of techniques adversaries may use to gather information and the sources information is collected from that are relevant to following through on the adversary's objectives. Frequently, the next goal after collecting data is to either steal (exfiltrate) the data or to use the data to gain more information about the target environment. Common target sources include various drive types, browsers, audio, video, and email. Common collection methods include capturing screenshots and keyboard input.

## Techniques in this Tactic (41 total)

| ID | Name | Type |
|-----|-------|-------|
| [T1005](T1005_Data_from_Local_System.md) | Data from Local System | Technique |
| [T1025](T1025_Data_from_Removable_Media.md) | Data from Removable Media | Technique |
| [T1039](T1039_Data_from_Network_Shared_Drive.md) | Data from Network Shared Drive | Technique |
| [T1056](T1056_Input_Capture.md) | Input Capture | Technique |
| [T1056.001](T1056.001_Keylogging.md) | Keylogging | Sub-technique |
| [T1056.002](T1056.002_GUI_Input_Capture.md) | GUI Input Capture | Sub-technique |
| [T1056.003](T1056.003_Web_Portal_Capture.md) | Web Portal Capture | Sub-technique |
| [T1056.004](T1056.004_Credential_API_Hooking.md) | Credential API Hooking | Sub-technique |
| [T1074](T1074_Data_Staged.md) | Data Staged | Technique |
| [T1074.001](T1074.001_Local_Data_Staging.md) | Local Data Staging | Sub-technique |
| [T1074.002](T1074.002_Remote_Data_Staging.md) | Remote Data Staging | Sub-technique |
| [T1113](T1113_Screen_Capture.md) | Screen Capture | Technique |
| [T1114](T1114_Email_Collection.md) | Email Collection | Technique |
| [T1114.001](T1114.001_Local_Email_Collection.md) | Local Email Collection | Sub-technique |
| [T1114.002](T1114.002_Remote_Email_Collection.md) | Remote Email Collection | Sub-technique |
| [T1114.003](T1114.003_Email_Forwarding_Rule.md) | Email Forwarding Rule | Sub-technique |
| [T1115](T1115_Clipboard_Data.md) | Clipboard Data | Technique |
| [T1119](T1119_Automated_Collection.md) | Automated Collection | Technique |
| [T1123](T1123_Audio_Capture.md) | Audio Capture | Technique |
| [T1125](T1125_Video_Capture.md) | Video Capture | Technique |
| [T1185](T1185_Browser_Session_Hijacking.md) | Browser Session Hijacking | Technique |
| [T1213](T1213_Data_from_Information_Repositories.md) | Data from Information Repositories | Technique |
| [T1213.001](T1213.001_Confluence.md) | Confluence | Sub-technique |
| [T1213.002](T1213.002_Sharepoint.md) | Sharepoint | Sub-technique |
| [T1213.003](T1213.003_Code_Repositories.md) | Code Repositories | Sub-technique |
| [T1213.004](T1213.004_Customer_Relationship_Management_Software.md) | Customer Relationship Management Software | Sub-technique |
| [T1213.005](T1213.005_Messaging_Applications.md) | Messaging Applications | Sub-technique |
| [T1213.006](T1213.006_Databases.md) | Databases | Sub-technique |
| [T1530](T1530_Data_from_Cloud_Storage.md) | Data from Cloud Storage | Technique |
| [T1557](T1557_Adversary-in-the-Middle.md) | Adversary-in-the-Middle | Technique |
| [T1557.001](T1557.001_Name_Resolution_Poisoning_and_SMB_Relay.md) | Name Resolution Poisoning and SMB Relay | Sub-technique |
| [T1557.002](T1557.002_ARP_Cache_Poisoning.md) | ARP Cache Poisoning | Sub-technique |
| [T1557.003](T1557.003_DHCP_Spoofing.md) | DHCP Spoofing | Sub-technique |
| [T1557.004](T1557.004_Evil_Twin.md) | Evil Twin | Sub-technique |
| [T1560](T1560_Archive_Collected_Data.md) | Archive Collected Data | Technique |
| [T1560.001](T1560.001_Archive_via_Utility.md) | Archive via Utility | Sub-technique |
| [T1560.002](T1560.002_Archive_via_Library.md) | Archive via Library | Sub-technique |
| [T1560.003](T1560.003_Archive_via_Custom_Method.md) | Archive via Custom Method | Sub-technique |
| [T1602](T1602_Data_from_Configuration_Repository.md) | Data from Configuration Repository | Technique |
| [T1602.001](T1602.001_SNMP__MIB_Dump.md) | SNMP (MIB Dump) | Sub-technique |
| [T1602.002](T1602.002_Network_Device_Configuration_Dump.md) | Network Device Configuration Dump | Sub-technique |

## Official Description

The adversary is trying to gather data of interest to their goal.

Collection consists of techniques used to identify and gather information (files, emails, clipboard, audio/video, screen, browser data, cloud storage, configuration repositories, etc.) before exfiltration.

**Source:** https://attack.mitre.org/tactics/TA0009/

## Key Techniques (representative)

- T1557 Adversary-in-the-Middle
- T1560 Archive Collected Data
- T1123 Audio Capture
- T1119 Automated Collection
- T1185 Browser Session Hijacking
- T1115 Clipboard Data
- T1530 Data from Cloud Storage
- T1602 Data from Configuration Repository
- T1213 Data from Information Repositories
- T1005 Data from Local System
- T1039 Data from Network Shared Drive
- T1025 Data from Removable Media
- T1074 Data Staged
- T1114 Email Collection
- T1056 Input Capture
- T1113 Screen Capture
- T1125 Video Capture

Full list: https://attack.mitre.org/tactics/TA0009/

## Educational Focus

Understand data-collection patterns and staging; map to detection of unusual file access, archive creation, and input capture.

## Sources

*Source: [MITRE ATT&CK Tactic TA0009](https://attack.mitre.org/tactics/TA0009/)*
