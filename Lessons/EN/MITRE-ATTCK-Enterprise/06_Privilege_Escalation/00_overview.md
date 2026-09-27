# TA0004 – Privilege Escalation

**ID:** TA0004  
**Tactic:** Privilege Escalation  
**Shortname:** `privilege-escalation`

## Definition

The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that adversaries use to gain higher-level permissions on a system or network. Adversaries can often enter and explore a network with unprivileged access but require elevated permissions to follow through on their objectives. Common approaches are to take advantage of system weaknesses, misconfigurations, and vulnerabilities. Examples of elevated access include: 

* SYSTEM/root level
* local administrator
* user account with admin-like access 
* user accounts with access to specific system or perform specific function

These techniques often overlap with Persistence techniques, as OS features that let an adversary persist can execute in an elevated context.

## Official Description

The adversary is trying to gain higher-level permissions.

Privilege Escalation consists of techniques that enable an adversary to obtain higher-level permissions on a system or network. Certain tools or actions require higher privileges; adversaries often escalate to achieve their goals.

**Source:** https://attack.mitre.org/tactics/TA0004/

## Techniques in this Tactic (96 total)

| ID | Name | Type |
|----|------|------|
| [T1037](T1037_Boot_or_Logon_Initialization_Scripts.md) | Boot or Logon Initialization Scripts | Technique |
| [T1037.001](T1037.001_Logon_Script__Windows.md) | Logon Script (Windows) | Sub-technique |
| [T1037.002](T1037.002_Login_Hook.md) | Login Hook | Sub-technique |
| [T1037.003](T1037.003_Network_Logon_Script.md) | Network Logon Script | Sub-technique |
| [T1037.004](T1037.004_RC_Scripts.md) | RC Scripts | Sub-technique |
| [T1037.005](T1037.005_Startup_Items.md) | Startup Items | Sub-technique |
| [T1053](T1053_Scheduled_Task_Job.md) | Scheduled Task/Job | Technique |
| [T1053.002](T1053.002_At.md) | At | Sub-technique |
| [T1053.003](T1053.003_Cron.md) | Cron | Sub-technique |
| [T1053.005](T1053.005_Scheduled_Task.md) | Scheduled Task | Sub-technique |
| [T1053.006](T1053.006_Systemd_Timers.md) | Systemd Timers | Sub-technique |
| [T1053.007](T1053.007_Container_Orchestration_Job.md) | Container Orchestration Job | Sub-technique |
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
| [T1068](T1068_Exploitation_for_Privilege_Escalation.md) | Exploitation for Privilege Escalation | Technique |
| [T1078](T1078_Valid_Accounts.md) | Valid Accounts | Technique |
| [T1078.001](T1078.001_Default_Accounts.md) | Default Accounts | Sub-technique |
| [T1078.002](T1078.002_Domain_Accounts.md) | Domain Accounts | Sub-technique |
| [T1078.003](T1078.003_Local_Accounts.md) | Local Accounts | Sub-technique |
| [T1078.004](T1078.004_Cloud_Accounts.md) | Cloud Accounts | Sub-technique |
| [T1098](T1098_Account_Manipulation.md) | Account Manipulation | Technique |
| [T1098.001](T1098.001_Additional_Cloud_Credentials.md) | Additional Cloud Credentials | Sub-technique |
| [T1098.002](T1098.002_Additional_Email_Delegate_Permissions.md) | Additional Email Delegate Permissions | Sub-technique |
| [T1098.003](T1098.003_Additional_Cloud_Roles.md) | Additional Cloud Roles | Sub-technique |
| [T1098.004](T1098.004_SSH_Authorized_Keys.md) | SSH Authorized Keys | Sub-technique |
| [T1098.005](T1098.005_Device_Registration.md) | Device Registration | Sub-technique |
| [T1098.006](T1098.006_Additional_Container_Cluster_Roles.md) | Additional Container Cluster Roles | Sub-technique |
| [T1098.007](T1098.007_Additional_Local_or_Domain_Groups.md) | Additional Local or Domain Groups | Sub-technique |
| [T1134](T1134_Access_Token_Manipulation.md) | Access Token Manipulation | Technique |
| [T1134.001](T1134.001_Token_Impersonation_Theft.md) | Token Impersonation/Theft | Sub-technique |
| [T1134.002](T1134.002_Create_Process_with_Token.md) | Create Process with Token | Sub-technique |
| [T1134.003](T1134.003_Make_and_Impersonate_Token.md) | Make and Impersonate Token | Sub-technique |
| [T1134.004](T1134.004_Parent_PID_Spoofing.md) | Parent PID Spoofing | Sub-technique |
| [T1134.005](T1134.005_SID-History_Injection.md) | SID-History Injection | Sub-technique |
| [T1484](T1484_Domain_or_Tenant_Policy_Modification.md) | Domain or Tenant Policy Modification | Technique |
| [T1484.001](T1484.001_Group_Policy_Modification.md) | Group Policy Modification | Sub-technique |
| [T1484.002](T1484.002_Trust_Modification.md) | Trust Modification | Sub-technique |
| [T1543](T1543_Create_or_Modify_System_Process.md) | Create or Modify System Process | Technique |
| [T1543.001](T1543.001_Launch_Agent.md) | Launch Agent | Sub-technique |
| [T1543.002](T1543.002_Systemd_Service.md) | Systemd Service | Sub-technique |
| [T1543.003](T1543.003_Windows_Service.md) | Windows Service | Sub-technique |
| [T1543.004](T1543.004_Launch_Daemon.md) | Launch Daemon | Sub-technique |
| [T1543.005](T1543.005_Container_Service.md) | Container Service | Sub-technique |
| [T1546](T1546_Event_Triggered_Execution.md) | Event Triggered Execution | Technique |
| [T1546.001](T1546.001_Change_Default_File_Association.md) | Change Default File Association | Sub-technique |
| [T1546.002](T1546.002_Screensaver.md) | Screensaver | Sub-technique |
| [T1546.003](T1546.003_Windows_Management_Instrumentation_Event_Subscription.md) | Windows Management Instrumentation Event Subscription | Sub-technique |
| [T1546.004](T1546.004_Unix_Shell_Configuration_Modification.md) | Unix Shell Configuration Modification | Sub-technique |
| [T1546.005](T1546.005_Trap.md) | Trap | Sub-technique |
| [T1546.006](T1546.006_LC_LOAD_DYLIB_Addition.md) | LC_LOAD_DYLIB Addition | Sub-technique |
| [T1546.007](T1546.007_Netsh_Helper_DLL.md) | Netsh Helper DLL | Sub-technique |
| [T1546.008](T1546.008_Accessibility_Features.md) | Accessibility Features | Sub-technique |
| [T1546.009](T1546.009_AppCert_DLLs.md) | AppCert DLLs | Sub-technique |
| [T1546.010](T1546.010_AppInit_DLLs.md) | AppInit DLLs | Sub-technique |
| [T1546.011](T1546.011_Application_Shimming.md) | Application Shimming | Sub-technique |
| [T1546.012](T1546.012_Image_File_Execution_Options_Injection.md) | Image File Execution Options Injection | Sub-technique |
| [T1546.013](T1546.013_PowerShell_Profile.md) | PowerShell Profile | Sub-technique |
| [T1546.014](T1546.014_Emond.md) | Emond | Sub-technique |
| [T1546.015](T1546.015_Component_Object_Model_Hijacking.md) | Component Object Model Hijacking | Sub-technique |
| [T1546.016](T1546.016_Installer_Packages.md) | Installer Packages | Sub-technique |
| [T1546.017](T1546.017_Udev_Rules.md) | Udev Rules | Sub-technique |
| [T1546.018](T1546.018_Python_Startup_Hooks.md) | Python Startup Hooks | Sub-technique |
| [T1547](T1547_Boot_or_Logon_Autostart_Execution.md) | Boot or Logon Autostart Execution | Technique |
| [T1547.001](T1547.001_Registry_Run_Keys___Startup_Folder.md) | Registry Run Keys / Startup Folder | Sub-technique |
| [T1547.002](T1547.002_Authentication_Package.md) | Authentication Package | Sub-technique |
| [T1547.003](T1547.003_Time_Providers.md) | Time Providers | Sub-technique |
| [T1547.004](T1547.004_Winlogon_Helper_DLL.md) | Winlogon Helper DLL | Sub-technique |
| [T1547.005](T1547.005_Security_Support_Provider.md) | Security Support Provider | Sub-technique |
| [T1547.006](T1547.006_Kernel_Modules_and_Extensions.md) | Kernel Modules and Extensions | Sub-technique |
| [T1547.007](T1547.007_Re-opened_Applications.md) | Re-opened Applications | Sub-technique |
| [T1547.008](T1547.008_LSASS_Driver.md) | LSASS Driver | Sub-technique |
| [T1547.009](T1547.009_Shortcut_Modification.md) | Shortcut Modification | Sub-technique |
| [T1547.010](T1547.010_Port_Monitors.md) | Port Monitors | Sub-technique |
| [T1547.012](T1547.012_Print_Processors.md) | Print Processors | Sub-technique |
| [T1547.013](T1547.013_XDG_Autostart_Entries.md) | XDG Autostart Entries | Sub-technique |
| [T1547.014](T1547.014_Active_Setup.md) | Active Setup | Sub-technique |
| [T1547.015](T1547.015_Login_Items.md) | Login Items | Sub-technique |
| [T1548](T1548_Abuse_Elevation_Control_Mechanism.md) | Abuse Elevation Control Mechanism | Technique |
| [T1548.001](T1548.001_Setuid_and_Setgid.md) | Setuid and Setgid | Sub-technique |
| [T1548.002](T1548.002_Bypass_User_Account_Control.md) | Bypass User Account Control | Sub-technique |
| [T1548.003](T1548.003_Sudo_and_Sudo_Caching.md) | Sudo and Sudo Caching | Sub-technique |
| [T1548.004](T1548.004_Elevated_Execution_with_Prompt.md) | Elevated Execution with Prompt | Sub-technique |
| [T1548.005](T1548.005_Temporary_Elevated_Cloud_Access.md) | Temporary Elevated Cloud Access | Sub-technique |
| [T1548.006](T1548.006_TCC_Manipulation.md) | TCC Manipulation | Sub-technique |
| [T1611](T1611_Escape_to_Host.md) | Escape to Host | Technique |

## Key Technique Categories

Abuse Elevation Control Mechanism, Access Token Manipulation, Boot or Logon Autostart Execution, Domain or Tenant Policy Modification, Escape to Host, Exploitation for Privilege Escalation, Hijack Execution Flow, Process Injection, Scheduled Task/Job, Valid Accounts, and others.

Full list: https://attack.mitre.org/tactics/TA0004/

## Educational Focus

Understand common privilege-escalation paths (token manipulation, misconfigured services, kernel exploits in lab only, etc.) and corresponding detection and hardening controls.

## Safety

Privilege-escalation exercises only against systems you own/control and that are isolated.

## Sources

*Source: [MITRE ATT&CK Tactic TA0004](https://attack.mitre.org/tactics/TA0004/)*
