# TA0008 – Lateral Movement

**ID:** TA0008  
**Tactic:** Lateral Movement  
**Shortname:** `lateral-movement`

## Definition

The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Following through on their primary objective often requires exploring the network to find their target, then pivoting through multiple systems and accounts to gain access to it. Adversaries might install their own remote access tools to accomplish Lateral Movement or use legitimate credentials with native network and operating system tools, which may be stealthier.

## Techniques in this Tactic (23 total)

| ID | Name | Type |
|----|------|------|
| [T1021](T1021_Remote_Services.md) | Remote Services | Technique |
| [T1021.001](T1021.001_Remote_Desktop_Protocol.md) | Remote Desktop Protocol | Sub-technique |
| [T1021.002](T1021.002_SMB_Windows_Admin_Shares.md) | SMB/Windows Admin Shares | Sub-technique |
| [T1021.003](T1021.003_Distributed_Component_Object_Model.md) | Distributed Component Object Model | Sub-technique |
| [T1021.004](T1021.004_SSH.md) | SSH | Sub-technique |
| [T1021.005](T1021.005_VNC.md) | VNC | Sub-technique |
| [T1021.006](T1021.006_Windows_Remote_Management.md) | Windows Remote Management | Sub-technique |
| [T1021.007](T1021.007_Cloud_Services.md) | Cloud Services | Sub-technique |
| [T1021.008](T1021.008_Direct_Cloud_VM_Connections.md) | Direct Cloud VM Connections | Sub-technique |
| [T1072](T1072_Software_Deployment_Tools.md) | Software Deployment Tools | Technique |
| [T1080](T1080_Taint_Shared_Content.md) | Taint Shared Content | Technique |
| [T1091](T1091_Replication_Through_Removable_Media.md) | Replication Through Removable Media | Technique |
| [T1210](T1210_Exploitation_of_Remote_Services.md) | Exploitation of Remote Services | Technique |
| [T1534](T1534_Internal_Spearphishing.md) | Internal Spearphishing | Technique |
| [T1550](T1550_Use_Alternate_Authentication_Material.md) | Use Alternate Authentication Material | Technique |
| [T1550.001](T1550.001_Application_Access_Token.md) | Application Access Token | Sub-technique |
| [T1550.002](T1550.002_Pass_the_Hash.md) | Pass the Hash | Sub-technique |
| [T1550.003](T1550.003_Pass_the_Ticket.md) | Pass the Ticket | Sub-technique |
| [T1550.004](T1550.004_Web_Session_Cookie.md) | Web Session Cookie | Sub-technique |
| [T1563](T1563_Remote_Service_Session_Hijacking.md) | Remote Service Session Hijacking | Technique |
| [T1563.001](T1563.001_SSH_Hijacking.md) | SSH Hijacking | Sub-technique |
| [T1563.002](T1563.002_RDP_Hijacking.md) | RDP Hijacking | Sub-technique |
| [T1570](T1570_Lateral_Tool_Transfer.md) | Lateral Tool Transfer | Technique |

## Official Description

The adversary is trying to move through your environment.

Lateral Movement consists of techniques that adversaries use to enter and control remote systems on a network. Adversaries may install their own remote-access tools or use legitimate credentials with native network and operating-system tools.

**Source:** https://attack.mitre.org/tactics/TA0008/

## Key Techniques (representative)

- T1210 Exploitation of Remote Services
- T1534 Internal Spearphishing
- T1570 Lateral Tool Transfer
- T1021 Remote Services (RDP, SMB/Windows Admin Shares, SSH, WinRM, VNC, DCOM, Cloud Services, etc.)
- T1550 Use Alternate Authentication Material (Pass the Hash, Pass the Ticket, Application Access Token, Web Session Cookie)

Full list: https://attack.mitre.org/tactics/TA0008/

## Educational Focus

Understand how adversaries pivot using valid credentials or remote services; focus on detection of unusual remote logons and tool transfer.

## Safety

Lateral-movement exercises only inside fully isolated lab networks.

## Sources

*Source: [MITRE ATT&CK Tactic TA0008](https://attack.mitre.org/tactics/TA0008/)*
