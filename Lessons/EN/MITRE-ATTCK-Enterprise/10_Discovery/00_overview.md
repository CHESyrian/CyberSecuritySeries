# TA0007 – Discovery

**ID:** TA0007  
**Tactic:** Discovery  
**Shortname:** `discovery`

## Definition

The adversary is trying to figure out your environment.

Discovery consists of techniques an adversary may use to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and orient themselves before deciding how to act. They also allow adversaries to explore what they can control and what’s around their entry point in order to discover how it could benefit their current objective. Native operating system tools are often used toward this post-compromise information-gathering objective.

## Techniques in this Tactic (49 total)

| ID | Name | Type |
|----|------|------|
| [T1007](T1007_System_Service_Discovery.md) | System Service Discovery | Technique |
| [T1010](T1010_Application_Window_Discovery.md) | Application Window Discovery | Technique |
| [T1012](T1012_Query_Registry.md) | Query Registry | Technique |
| [T1016](T1016_System_Network_Configuration_Discovery.md) | System Network Configuration Discovery | Technique |
| [T1016.001](T1016.001_Internet_Connection_Discovery.md) | Internet Connection Discovery | Sub-technique |
| [T1016.002](T1016.002_Wi-Fi_Discovery.md) | Wi-Fi Discovery | Sub-technique |
| [T1018](T1018_Remote_System_Discovery.md) | Remote System Discovery | Technique |
| [T1033](T1033_System_Owner_User_Discovery.md) | System Owner/User Discovery | Technique |
| [T1040](T1040_Network_Sniffing.md) | Network Sniffing | Technique |
| [T1046](T1046_Network_Service_Discovery.md) | Network Service Discovery | Technique |
| [T1049](T1049_System_Network_Connections_Discovery.md) | System Network Connections Discovery | Technique |
| [T1057](T1057_Process_Discovery.md) | Process Discovery | Technique |
| [T1069](T1069_Permission_Groups_Discovery.md) | Permission Groups Discovery | Technique |
| [T1069.001](T1069.001_Local_Groups.md) | Local Groups | Sub-technique |
| [T1069.002](T1069.002_Domain_Groups.md) | Domain Groups | Sub-technique |
| [T1069.003](T1069.003_Cloud_Groups.md) | Cloud Groups | Sub-technique |
| [T1082](T1082_System_Information_Discovery.md) | System Information Discovery | Technique |
| [T1083](T1083_File_and_Directory_Discovery.md) | File and Directory Discovery | Technique |
| [T1087](T1087_Account_Discovery.md) | Account Discovery | Technique |
| [T1087.001](T1087.001_Local_Account.md) | Local Account | Sub-technique |
| [T1087.002](T1087.002_Domain_Account.md) | Domain Account | Sub-technique |
| [T1087.003](T1087.003_Email_Account.md) | Email Account | Sub-technique |
| [T1087.004](T1087.004_Cloud_Account.md) | Cloud Account | Sub-technique |
| [T1120](T1120_Peripheral_Device_Discovery.md) | Peripheral Device Discovery | Technique |
| [T1124](T1124_System_Time_Discovery.md) | System Time Discovery | Technique |
| [T1135](T1135_Network_Share_Discovery.md) | Network Share Discovery | Technique |
| [T1201](T1201_Password_Policy_Discovery.md) | Password Policy Discovery | Technique |
| [T1217](T1217_Browser_Information_Discovery.md) | Browser Information Discovery | Technique |
| [T1482](T1482_Domain_Trust_Discovery.md) | Domain Trust Discovery | Technique |
| [T1497](T1497_Virtualization_Sandbox_Evasion.md) | Virtualization/Sandbox Evasion | Technique |
| [T1497.001](T1497.001_System_Checks.md) | System Checks | Sub-technique |
| [T1497.002](T1497.002_User_Activity_Based_Checks.md) | User Activity Based Checks | Sub-technique |
| [T1497.003](T1497.003_Time_Based_Checks.md) | Time Based Checks | Sub-technique |
| [T1518](T1518_Software_Discovery.md) | Software Discovery | Technique |
| [T1518.001](T1518.001_Security_Software_Discovery.md) | Security Software Discovery | Sub-technique |
| [T1518.002](T1518.002_Backup_Software_Discovery.md) | Backup Software Discovery | Sub-technique |
| [T1526](T1526_Cloud_Service_Discovery.md) | Cloud Service Discovery | Technique |
| [T1538](T1538_Cloud_Service_Dashboard.md) | Cloud Service Dashboard | Technique |
| [T1580](T1580_Cloud_Infrastructure_Discovery.md) | Cloud Infrastructure Discovery | Technique |
| [T1613](T1613_Container_and_Resource_Discovery.md) | Container and Resource Discovery | Technique |
| [T1614](T1614_System_Location_Discovery.md) | System Location Discovery | Technique |
| [T1614.001](T1614.001_System_Language_Discovery.md) | System Language Discovery | Sub-technique |
| [T1615](T1615_Group_Policy_Discovery.md) | Group Policy Discovery | Technique |
| [T1619](T1619_Cloud_Storage_Object_Discovery.md) | Cloud Storage Object Discovery | Technique |
| [T1622](T1622_Debugger_Evasion.md) | Debugger Evasion | Technique |
| [T1652](T1652_Device_Driver_Discovery.md) | Device Driver Discovery | Technique |
| [T1654](T1654_Log_Enumeration.md) | Log Enumeration | Technique |
| [T1673](T1673_Virtual_Machine_Discovery.md) | Virtual Machine Discovery | Technique |
| [T1680](T1680_Local_Storage_Discovery.md) | Local Storage Discovery | Technique |

## Official Description

The adversary is trying to figure out your environment.

Discovery consists of techniques that enable an adversary to gain knowledge about the system and internal network. These techniques help adversaries observe the environment and decide how to act.

**Source:** https://attack.mitre.org/tactics/TA0007/

## Key Technique Categories

Account Discovery, Domain Discovery, System Information Discovery, Network Service Discovery, Process Discovery, File and Directory Discovery, Software Discovery, Cloud Discovery, Container Discovery, Permission Groups Discovery, Remote System Discovery, System Network Configuration Discovery, and many others.

Full list: https://attack.mitre.org/tactics/TA0007/

## Educational Focus

Map common “whoami / net / systeminfo / ipconfig” style activity and cloud inventory commands to Discovery techniques. Use discovery logs for early post-compromise detection.

## Sources

*Source: [MITRE ATT&CK Tactic TA0007](https://attack.mitre.org/tactics/TA0007/)*
