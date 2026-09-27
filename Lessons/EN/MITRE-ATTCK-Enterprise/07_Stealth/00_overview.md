# TA0005 – Stealth

**ID:** TA0005  
**Tactic:** Stealth (v19; previously part of Defense Evasion)  
**Shortname:** `stealth`

## Definition

The adversary is trying to hide and conceal their actions, appearing as normal behavior.

Stealth consists of techniques that reduce the likelihood of detection by blending in with legitimate activity or minimizing observable signals. These techniques are characterized by concealment behaviors, such as avoiding, obfuscating, or mimicking normal operations, without modifying security controls or compromising collection and monitoring feeds. The goal is to remain indistinguishable from benign activity while leaving defensive systems intact.

## Official Description

The adversary is trying to hide and conceal their actions, appearing as normal behavior.

Stealth focuses on techniques that help adversaries avoid detection by blending with legitimate activity, obfuscating artifacts, masquerading, removing indicators, or otherwise reducing the visibility of their actions while leaving defensive tools intact.

**Source:** https://attack.mitre.org/tactics/TA0005/

## Techniques in this Tactic (148 total)

| ID | Name | Type |
|----|------|------|
| [T1006](T1006_Direct_Volume_Access.md) | Direct Volume Access | Technique |
| [T1014](T1014_Rootkit.md) | Rootkit | Technique |
| [T1027](T1027_Obfuscated_Files_or_Information.md) | Obfuscated Files or Information | Technique |
| [T1027.001](T1027.001_Binary_Padding.md) | Binary Padding | Sub-technique |
| [T1027.002](T1027.002_Software_Packing.md) | Software Packing | Sub-technique |
| [T1027.003](T1027.003_Steganography.md) | Steganography | Sub-technique |
| [T1027.004](T1027.004_Compile_After_Delivery.md) | Compile After Delivery | Sub-technique |
| [T1027.005](T1027.005_Indicator_Removal_from_Tools.md) | Indicator Removal from Tools | Sub-technique |
| [T1027.006](T1027.006_HTML_Smuggling.md) | HTML Smuggling | Sub-technique |
| [T1027.007](T1027.007_Dynamic_API_Resolution.md) | Dynamic API Resolution | Sub-technique |
| [T1027.008](T1027.008_Stripped_Payloads.md) | Stripped Payloads | Sub-technique |
| [T1027.009](T1027.009_Embedded_Payloads.md) | Embedded Payloads | Sub-technique |
| [T1027.010](T1027.010_Command_Obfuscation.md) | Command Obfuscation | Sub-technique |
| [T1027.011](T1027.011_Fileless_Storage.md) | Fileless Storage | Sub-technique |
| [T1027.012](T1027.012_LNK_Icon_Smuggling.md) | LNK Icon Smuggling | Sub-technique |
| [T1027.013](T1027.013_Encrypted_Encoded_File.md) | Encrypted/Encoded File | Sub-technique |
| [T1027.014](T1027.014_Polymorphic_Code.md) | Polymorphic Code | Sub-technique |
| [T1027.015](T1027.015_Compression.md) | Compression | Sub-technique |
| [T1027.016](T1027.016_Junk_Code_Insertion.md) | Junk Code Insertion | Sub-technique |
| [T1027.017](T1027.017_SVG_Smuggling.md) | SVG Smuggling | Sub-technique |
| [T1027.018](T1027.018_Invisible_Unicode.md) | Invisible Unicode | Sub-technique |
| [T1036](T1036_Masquerading.md) | Masquerading | Technique |
| [T1036.001](T1036.001_Invalid_Code_Signature.md) | Invalid Code Signature | Sub-technique |
| [T1036.002](T1036.002_Right-to-Left_Override.md) | Right-to-Left Override | Sub-technique |
| [T1036.003](T1036.003_Rename_Legitimate_Utilities.md) | Rename Legitimate Utilities | Sub-technique |
| [T1036.004](T1036.004_Masquerade_Task_or_Service.md) | Masquerade Task or Service | Sub-technique |
| [T1036.005](T1036.005_Match_Legitimate_Resource_Name_or_Location.md) | Match Legitimate Resource Name or Location | Sub-technique |
| [T1036.006](T1036.006_Space_after_Filename.md) | Space after Filename | Sub-technique |
| [T1036.007](T1036.007_Double_File_Extension.md) | Double File Extension | Sub-technique |
| [T1036.008](T1036.008_Masquerade_File_Type.md) | Masquerade File Type | Sub-technique |
| [T1036.009](T1036.009_Break_Process_Trees.md) | Break Process Trees | Sub-technique |
| [T1036.010](T1036.010_Masquerade_Account_Name.md) | Masquerade Account Name | Sub-technique |
| [T1036.011](T1036.011_Overwrite_Process_Arguments.md) | Overwrite Process Arguments | Sub-technique |
| [T1036.012](T1036.012_Browser_Fingerprint.md) | Browser Fingerprint | Sub-technique |
| [T1055](T1055_Process_Injection.md) | Process Injection | Technique |
| [T1055.001](T1055.001_Dynamic-link_Library_Injection.md) | Dynamic-link Library Injection | Sub-technique |
| [T1055.002](T1055.002_Portable_Executable_Injection.md) | Portable Executable Injection | Sub-technique |
| [T1055.003](T1055.003_Thread_Execution_Hijacking.md) | Thread Execution Hijacking | Sub-technique |
| [T1055.004](T1055.004_Asynchronous_Procedure_Call.md) | Asynchronous Procedure Call | Sub-technique |
| [T1055.005](T1055.005_Thread_Local_Storage.md) | Thread Local Storage | Sub-technique |
| [T1055.008](T1055.008_Ptrace_System_Calls.md) | Ptrace System Calls | Sub-technique |
| [T1055.009](T1055.009_Proc_Memory.md) | Proc Memory | Sub-technique |
| [T1055.011](T1055.011_Extra_Window_Memory_Injection.md) | Extra Window Memory Injection | Sub-technique |
| [T1055.012](T1055.012_Process_Hollowing.md) | Process Hollowing | Sub-technique |
| [T1055.013](T1055.013_Process_Doppelgänging.md) | Process Doppelgänging | Sub-technique |
| [T1055.014](T1055.014_VDSO_Hijacking.md) | VDSO Hijacking | Sub-technique |
| [T1055.015](T1055.015_ListPlanting.md) | ListPlanting | Sub-technique |
| [T1070](T1070_Indicator_Removal.md) | Indicator Removal | Technique |
| [T1070.003](T1070.003_Clear_Command_History.md) | Clear Command History | Sub-technique |
| [T1070.004](T1070.004_File_Deletion.md) | File Deletion | Sub-technique |
| [T1070.005](T1070.005_Network_Share_Connection_Removal.md) | Network Share Connection Removal | Sub-technique |
| [T1070.006](T1070.006_Timestomp.md) | Timestomp | Sub-technique |
| [T1070.007](T1070.007_Clear_Network_Connection_History_and_Configurations.md) | Clear Network Connection History and Configurations | Sub-technique |
| [T1070.008](T1070.008_Clear_Mailbox_Data.md) | Clear Mailbox Data | Sub-technique |
| [T1070.009](T1070.009_Clear_Persistence.md) | Clear Persistence | Sub-technique |
| [T1070.010](T1070.010_Relocate_Malware.md) | Relocate Malware | Sub-technique |
| [T1078](T1078_Valid_Accounts.md) | Valid Accounts | Technique |
| [T1078.001](T1078.001_Default_Accounts.md) | Default Accounts | Sub-technique |
| [T1078.002](T1078.002_Domain_Accounts.md) | Domain Accounts | Sub-technique |
| [T1078.003](T1078.003_Local_Accounts.md) | Local Accounts | Sub-technique |
| [T1078.004](T1078.004_Cloud_Accounts.md) | Cloud Accounts | Sub-technique |
| [T1127](T1127_Trusted_Developer_Utilities_Proxy_Execution.md) | Trusted Developer Utilities Proxy Execution | Technique |
| [T1127.001](T1127.001_MSBuild.md) | MSBuild | Sub-technique |
| [T1127.002](T1127.002_ClickOnce.md) | ClickOnce | Sub-technique |
| [T1127.003](T1127.003_JamPlus.md) | JamPlus | Sub-technique |
| [T1134](T1134_Access_Token_Manipulation.md) | Access Token Manipulation | Technique |
| [T1134.001](T1134.001_Token_Impersonation_Theft.md) | Token Impersonation/Theft | Sub-technique |
| [T1134.002](T1134.002_Create_Process_with_Token.md) | Create Process with Token | Sub-technique |
| [T1134.003](T1134.003_Make_and_Impersonate_Token.md) | Make and Impersonate Token | Sub-technique |
| [T1134.004](T1134.004_Parent_PID_Spoofing.md) | Parent PID Spoofing | Sub-technique |
| [T1134.005](T1134.005_SID-History_Injection.md) | SID-History Injection | Sub-technique |
| [T1140](T1140_Deobfuscate_Decode_Files_or_Information.md) | Deobfuscate/Decode Files or Information | Technique |
| [T1197](T1197_BITS_Jobs.md) | BITS Jobs | Technique |
| [T1202](T1202_Indirect_Command_Execution.md) | Indirect Command Execution | Technique |
| [T1205](T1205_Traffic_Signaling.md) | Traffic Signaling | Technique |
| [T1205.001](T1205.001_Port_Knocking.md) | Port Knocking | Sub-technique |
| [T1205.002](T1205.002_Socket_Filters.md) | Socket Filters | Sub-technique |
| [T1211](T1211_Exploitation_for_Stealth.md) | Exploitation for Stealth | Technique |
| [T1216](T1216_System_Script_Proxy_Execution.md) | System Script Proxy Execution | Technique |
| [T1216.001](T1216.001_PubPrn.md) | PubPrn | Sub-technique |
| [T1216.002](T1216.002_SyncAppvPublishingServer.md) | SyncAppvPublishingServer | Sub-technique |
| [T1218](T1218_System_Binary_Proxy_Execution.md) | System Binary Proxy Execution | Technique |
| [T1218.001](T1218.001_Compiled_HTML_File.md) | Compiled HTML File | Sub-technique |
| [T1218.002](T1218.002_Control_Panel.md) | Control Panel | Sub-technique |
| [T1218.003](T1218.003_CMSTP.md) | CMSTP | Sub-technique |
| [T1218.004](T1218.004_InstallUtil.md) | InstallUtil | Sub-technique |
| [T1218.005](T1218.005_Mshta.md) | Mshta | Sub-technique |
| [T1218.007](T1218.007_Msiexec.md) | Msiexec | Sub-technique |
| [T1218.008](T1218.008_Odbcconf.md) | Odbcconf | Sub-technique |
| [T1218.009](T1218.009_Regsvcs_Regasm.md) | Regsvcs/Regasm | Sub-technique |
| [T1218.010](T1218.010_Regsvr32.md) | Regsvr32 | Sub-technique |
| [T1218.011](T1218.011_Rundll32.md) | Rundll32 | Sub-technique |
| [T1218.012](T1218.012_Verclsid.md) | Verclsid | Sub-technique |
| [T1218.013](T1218.013_Mavinject.md) | Mavinject | Sub-technique |
| [T1218.014](T1218.014_MMC.md) | MMC | Sub-technique |
| [T1218.015](T1218.015_Electron_Applications.md) | Electron Applications | Sub-technique |
| [T1220](T1220_XSL_Script_Processing.md) | XSL Script Processing | Technique |
| [T1221](T1221_Template_Injection.md) | Template Injection | Technique |
| [T1480](T1480_Execution_Guardrails.md) | Execution Guardrails | Technique |
| [T1480.001](T1480.001_Environmental_Keying.md) | Environmental Keying | Sub-technique |
| [T1480.002](T1480.002_Mutual_Exclusion.md) | Mutual Exclusion | Sub-technique |
| [T1497](T1497_Virtualization_Sandbox_Evasion.md) | Virtualization/Sandbox Evasion | Technique |
| [T1497.001](T1497.001_System_Checks.md) | System Checks | Sub-technique |
| [T1497.002](T1497.002_User_Activity_Based_Checks.md) | User Activity Based Checks | Sub-technique |
| [T1497.003](T1497.003_Time_Based_Checks.md) | Time Based Checks | Sub-technique |
| [T1535](T1535_Unused_Unsupported_Cloud_Regions.md) | Unused/Unsupported Cloud Regions | Technique |
| [T1542](T1542_Pre-OS_Boot.md) | Pre-OS Boot | Technique |
| [T1542.001](T1542.001_System_Firmware.md) | System Firmware | Sub-technique |
| [T1542.002](T1542.002_Component_Firmware.md) | Component Firmware | Sub-technique |
| [T1542.003](T1542.003_Bootkit.md) | Bootkit | Sub-technique |
| [T1542.004](T1542.004_ROMMONkit.md) | ROMMONkit | Sub-technique |
| [T1542.005](T1542.005_TFTP_Boot.md) | TFTP Boot | Sub-technique |
| [T1564](T1564_Hide_Artifacts.md) | Hide Artifacts | Technique |
| [T1564.001](T1564.001_Hidden_Files_and_Directories.md) | Hidden Files and Directories | Sub-technique |
| [T1564.002](T1564.002_Hidden_Users.md) | Hidden Users | Sub-technique |
| [T1564.003](T1564.003_Hidden_Window.md) | Hidden Window | Sub-technique |
| [T1564.004](T1564.004_NTFS_File_Attributes.md) | NTFS File Attributes | Sub-technique |
| [T1564.005](T1564.005_Hidden_File_System.md) | Hidden File System | Sub-technique |
| [T1564.006](T1564.006_Run_Virtual_Instance.md) | Run Virtual Instance | Sub-technique |
| [T1564.007](T1564.007_VBA_Stomping.md) | VBA Stomping | Sub-technique |
| [T1564.008](T1564.008_Email_Hiding_Rules.md) | Email Hiding Rules | Sub-technique |
| [T1564.009](T1564.009_Resource_Forking.md) | Resource Forking | Sub-technique |
| [T1564.010](T1564.010_Process_Argument_Spoofing.md) | Process Argument Spoofing | Sub-technique |
| [T1564.011](T1564.011_Ignore_Process_Interrupts.md) | Ignore Process Interrupts | Sub-technique |
| [T1564.012](T1564.012_File_Path_Exclusions.md) | File/Path Exclusions | Sub-technique |
| [T1564.013](T1564.013_Bind_Mounts.md) | Bind Mounts | Sub-technique |
| [T1564.014](T1564.014_Extended_Attributes.md) | Extended Attributes | Sub-technique |
| [T1574](T1574_Hijack_Execution_Flow.md) | Hijack Execution Flow | Technique |
| [T1574.001](T1574.001_DLL.md) | DLL | Sub-technique |
| [T1574.004](T1574.004_Dylib_Hijacking.md) | Dylib Hijacking | Sub-technique |
| [T1574.005](T1574.005_Executable_Installer_File_Permissions_Weakness.md) | Executable Installer File Permissions Weakness | Sub-technique |
| [T1574.006](T1574.006_Dynamic_Linker_Hijacking.md) | Dynamic Linker Hijacking | Sub-technique |
| [T1574.007](T1574.007_Path_Interception_by_PATH_Environment_Variable.md) | Path Interception by PATH Environment Variable | Sub-technique |
| [T1574.008](T1574.008_Path_Interception_by_Search_Order_Hijacking.md) | Path Interception by Search Order Hijacking | Sub-technique |
| [T1574.009](T1574.009_Path_Interception_by_Unquoted_Path.md) | Path Interception by Unquoted Path | Sub-technique |
| [T1574.010](T1574.010_Services_File_Permissions_Weakness.md) | Services File Permissions Weakness | Sub-technique |
| [T1574.011](T1574.011_Services_Registry_Permissions_Weakness.md) | Services Registry Permissions Weakness | Sub-technique |
| [T1574.012](T1574.012_COR_PROFILER.md) | COR_PROFILER | Sub-technique |
| [T1574.013](T1574.013_KernelCallbackTable.md) | KernelCallbackTable | Sub-technique |
| [T1574.014](T1574.014_AppDomainManager.md) | AppDomainManager | Sub-technique |
| [T1612](T1612_Build_Image_on_Host.md) | Build Image on Host | Technique |
| [T1620](T1620_Reflective_Code_Loading.md) | Reflective Code Loading | Technique |
| [T1622](T1622_Debugger_Evasion.md) | Debugger Evasion | Technique |
| [T1678](T1678_Delay_Execution.md) | Delay Execution | Technique |
| [T1679](T1679_Selective_Exclusion.md) | Selective Exclusion | Technique |
| [T1684](T1684_Social_Engineering.md) | Social Engineering | Technique |
| [T1684.001](T1684.001_Impersonation.md) | Impersonation | Sub-technique |
| [T1684.002](T1684.002_Email_Spoofing.md) | Email Spoofing | Sub-technique |

## Context of the v19 Split

In ATT&CK v19 the former Defense Evasion tactic was divided:

- **Stealth (TA0005)** – hide / blend / avoid notice
- **Defense Impairment (TA0112)** – actively break or degrade defender tooling

Most technique IDs remained stable; only the associated tactic changed for many entries.

## Educational Focus

Distinguish “hiding” behaviors (timestomping, obfuscation, process injection for stealth, indicator removal) from “breaking defenses.” Map detections to the correct tactic for clearer reporting and prioritization.

## Sources

*Source: [MITRE ATT&CK Tactic TA0005](https://attack.mitre.org/tactics/TA0005/)*
- MITRE blog posts on the Defense Evasion split
