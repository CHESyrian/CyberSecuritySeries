# TA0112 – Defense Impairment

**ID:** TA0112  
**Tactic:** Defense Impairment (new in v19)  
**Shortname:** `defense-impairment`

## Definition

The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening.

Defense Impairment consists of techniques that degrade, disable, or undermine the effectiveness and trustworthiness of security controls and monitoring mechanisms. These techniques are characterized by direct interference with defensive systems. The goal is to reduce defenders’ ability to detect, interpret, or respond to adversary activity.

## Official Description

The adversary is trying to break security mechanisms, pipelines, and tooling so defenders can’t see or trust what’s happening.

Defense Impairment covers techniques that actively disable, modify, or degrade security products, logging, monitoring agents, firewalls, and related controls.

**Source:** https://attack.mitre.org/tactics/TA0112/

## Techniques in this Tactic (56 total)

| ID | Name | Type |
|-----|-------|-------|
| [T1112](T1112_Modify_Registry.md) | Modify Registry | Technique |
| [T1207](T1207_Rogue_Domain_Controller.md) | Rogue Domain Controller | Technique |
| [T1222](T1222_File_and_Directory_Permissions_Modification.md) | File and Directory Permissions Modification | Technique |
| [T1222.001](T1222.001_Windows_Permissions.md) | Windows Permissions | Sub-technique |
| [T1222.002](T1222.002_Linux_and_Mac_Permissions.md) | Linux and Mac Permissions | Sub-technique |
| [T1484](T1484_Domain_or_Tenant_Policy_Modification.md) | Domain or Tenant Policy Modification | Technique |
| [T1484.001](T1484.001_Group_Policy_Modification.md) | Group Policy Modification | Sub-technique |
| [T1484.002](T1484.002_Trust_Modification.md) | Trust Modification | Sub-technique |
| [T1553](T1553_Subvert_Trust_Controls.md) | Subvert Trust Controls | Technique |
| [T1553.001](T1553.001_Gatekeeper_Bypass.md) | Gatekeeper Bypass | Sub-technique |
| [T1553.002](T1553.002_Code_Signing.md) | Code Signing | Sub-technique |
| [T1553.003](T1553.003_SIP_and_Trust_Provider_Hijacking.md) | SIP and Trust Provider Hijacking | Sub-technique |
| [T1553.004](T1553.004_Install_Root_Certificate.md) | Install Root Certificate | Sub-technique |
| [T1553.005](T1553.005_Mark-of-the-Web_Bypass.md) | Mark-of-the-Web Bypass | Sub-technique |
| [T1553.006](T1553.006_Code_Signing_Policy_Modification.md) | Code Signing Policy Modification | Sub-technique |
| [T1556](T1556_Modify_Authentication_Process.md) | Modify Authentication Process | Technique |
| [T1556.001](T1556.001_Domain_Controller_Authentication.md) | Domain Controller Authentication | Sub-technique |
| [T1556.002](T1556.002_Password_Filter_DLL.md) | Password Filter DLL | Sub-technique |
| [T1556.003](T1556.003_Pluggable_Authentication_Modules.md) | Pluggable Authentication Modules | Sub-technique |
| [T1556.004](T1556.004_Network_Device_Authentication.md) | Network Device Authentication | Sub-technique |
| [T1556.005](T1556.005_Reversible_Encryption.md) | Reversible Encryption | Sub-technique |
| [T1556.006](T1556.006_Multi-Factor_Authentication.md) | Multi-Factor Authentication | Sub-technique |
| [T1556.007](T1556.007_Hybrid_Identity.md) | Hybrid Identity | Sub-technique |
| [T1556.008](T1556.008_Network_Provider_DLL.md) | Network Provider DLL | Sub-technique |
| [T1556.009](T1556.009_Conditional_Access_Policies.md) | Conditional Access Policies | Sub-technique |
| [T1578](T1578_Modify_Cloud_Compute_Infrastructure.md) | Modify Cloud Compute Infrastructure | Technique |
| [T1578.001](T1578.001_Create_Snapshot.md) | Create Snapshot | Sub-technique |
| [T1578.002](T1578.002_Create_Cloud_Instance.md) | Create Cloud Instance | Sub-technique |
| [T1578.003](T1578.003_Delete_Cloud_Instance.md) | Delete Cloud Instance | Sub-technique |
| [T1578.004](T1578.004_Revert_Cloud_Instance.md) | Revert Cloud Instance | Sub-technique |
| [T1578.005](T1578.005_Modify_Cloud_Compute_Configurations.md) | Modify Cloud Compute Configurations | Sub-technique |
| [T1599](T1599_Network_Boundary_Bridging.md) | Network Boundary Bridging | Technique |
| [T1599.001](T1599.001_Network_Address_Translation_Traversal.md) | Network Address Translation Traversal | Sub-technique |
| [T1600](T1600_Weaken_Encryption.md) | Weaken Encryption | Technique |
| [T1600.001](T1600.001_Reduce_Key_Space.md) | Reduce Key Space | Sub-technique |
| [T1600.002](T1600.002_Disable_Crypto_Hardware.md) | Disable Crypto Hardware | Sub-technique |
| [T1601](T1601_Modify_System_Image.md) | Modify System Image | Technique |
| [T1601.001](T1601.001_Patch_System_Image.md) | Patch System Image | Sub-technique |
| [T1601.002](T1601.002_Downgrade_System_Image.md) | Downgrade System Image | Sub-technique |
| [T1647](T1647_Plist_File_Modification.md) | Plist File Modification | Technique |
| [T1666](T1666_Modify_Cloud_Resource_Hierarchy.md) | Modify Cloud Resource Hierarchy | Technique |
| [T1685](T1685_Disable_or_Modify_Tools.md) | Disable or Modify Tools | Technique |
| [T1685.001](T1685.001_Disable_or_Modify_Windows_Event_Log.md) | Disable or Modify Windows Event Log | Sub-technique |
| [T1685.002](T1685.002_Disable_or_Modify_Cloud_Log.md) | Disable or Modify Cloud Log | Sub-technique |
| [T1685.003](T1685.003_Modify_or_Spoof_Tool_UI.md) | Modify or Spoof Tool UI | Sub-technique |
| [T1685.004](T1685.004_Disable_or_Modify_Linux_Audit_System_Log.md) | Disable or Modify Linux Audit System Log | Sub-technique |
| [T1685.005](T1685.005_Clear_Windows_Event_Logs.md) | Clear Windows Event Logs | Sub-technique |
| [T1685.006](T1685.006_Clear_Linux_or_Mac_System_Logs.md) | Clear Linux or Mac System Logs | Sub-technique |
| [T1686](T1686_Disable_or_Modify_System_Firewall.md) | Disable or Modify System Firewall | Technique |
| [T1686.001](T1686.001_Cloud_Firewall.md) | Cloud Firewall | Sub-technique |
| [T1686.002](T1686.002_Network_Device_Firewall.md) | Network Device Firewall | Sub-technique |
| [T1686.003](T1686.003_Windows_Host_Firewall.md) | Windows Host Firewall | Sub-technique |
| [T1687](T1687_Exploitation_for_Defense_Impairment.md) | Exploitation for Defense Impairment | Technique |
| [T1688](T1688_Safe_Mode_Boot.md) | Safe Mode Boot | Technique |
| [T1689](T1689_Downgrade_Attack.md) | Downgrade Attack | Technique |
| [T1690](T1690_Prevent_Command_History_Logging.md) | Prevent Command History Logging | Technique |

## Context of the v19 Split

See the Stealth (TA0005) overview for the rationale behind splitting the old Defense Evasion tactic. Techniques that previously lived under Defense Evasion and involved impairing defenses (e.g., disabling security tools, clearing logs, modifying firewalls) largely moved here or were restructured (e.g., related to T1562 / new Disable or Modify Tools techniques).

## Educational Focus

Recognize the forensic footprint of defense impairment (service stops, log clears, configuration changes to security tools) versus pure stealth. Prioritize restoration of visibility in incident response.

## Sources

*Source: [MITRE ATT&CK Tactic TA0112](https://attack.mitre.org/tactics/TA0112/)*
- ATT&CK v19 release notes and related blog posts
