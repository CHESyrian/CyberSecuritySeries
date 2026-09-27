# TA0003 – Persistence

**ID:** TA0003  
**Tactic:** Persistence  
**Shortname:** `persistence`

## Definition

The adversary is trying to maintain their foothold.

Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that could cut off their access. Techniques used for persistence include any access, action, or configuration changes that let them maintain their foothold on systems, such as replacing or hijacking legitimate code or adding startup code.

## Official Description

The adversary is trying to maintain their foothold.

Persistence consists of techniques that adversaries use to keep access to systems across restarts, changed credentials, and other interruptions that would otherwise cut off their access.

**Source:** https://attack.mitre.org/tactics/TA0003/

## Techniques in this Tactic (113 total)

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
| [T1112](T1112_Modify_Registry.md) | Modify Registry | Technique |
| [T1133](T1133_External_Remote_Services.md) | External Remote Services | Technique |
| [T1136](T1136_Create_Account.md) | Create Account | Technique |
| [T1136.001](T1136.001_Local_Account.md) | Local Account | Sub-technique |
| [T1136.002](T1136.002_Domain_Account.md) | Domain Account | Sub-technique |
| [T1136.003](T1136.003_Cloud_Account.md) | Cloud Account | Sub-technique |
| [T1137](T1137_Office_Application_Startup.md) | Office Application Startup | Technique |
| [T1137.001](T1137.001_Office_Template_Macros.md) | Office Template Macros | Sub-technique |
| [T1137.002](T1137.002_Office_Test.md) | Office Test | Sub-technique |
| [T1137.003](T1137.003_Outlook_Forms.md) | Outlook Forms | Sub-technique |
| [T1137.004](T1137.004_Outlook_Home_Page.md) | Outlook Home Page | Sub-technique |
| [T1137.005](T1137.005_Outlook_Rules.md) | Outlook Rules | Sub-technique |
| [T1137.006](T1137.006_Add-ins.md) | Add-ins | Sub-technique |
| [T1176](T1176_Software_Extensions.md) | Software Extensions | Technique |
| [T1176.001](T1176.001_Browser_Extensions.md) | Browser Extensions | Sub-technique |
| [T1176.002](T1176.002_IDE_Extensions.md) | IDE Extensions | Sub-technique |
| [T1197](T1197_BITS_Jobs.md) | BITS Jobs | Technique |
| [T1205](T1205_Traffic_Signaling.md) | Traffic Signaling | Technique |
| [T1205.001](T1205.001_Port_Knocking.md) | Port Knocking | Sub-technique |
| [T1205.002](T1205.002_Socket_Filters.md) | Socket Filters | Sub-technique |
| [T1505](T1505_Server_Software_Component.md) | Server Software Component | Technique |
| [T1505.001](T1505.001_SQL_Stored_Procedures.md) | SQL Stored Procedures | Sub-technique |
| [T1505.002](T1505.002_Transport_Agent.md) | Transport Agent | Sub-technique |
| [T1505.003](T1505.003_Web_Shell.md) | Web Shell | Sub-technique |
| [T1505.004](T1505.004_IIS_Components.md) | IIS Components | Sub-technique |
| [T1505.005](T1505.005_Terminal_Services_DLL.md) | Terminal Services DLL | Sub-technique |
| [T1505.006](T1505.006_vSphere_Installation_Bundles.md) | vSphere Installation Bundles | Sub-technique |
| [T1525](T1525_Implant_Internal_Image.md) | Implant Internal Image | Technique |
| [T1542](T1542_Pre-OS_Boot.md) | Pre-OS Boot | Technique |
| [T1542.001](T1542.001_System_Firmware.md) | System Firmware | Sub-technique |
| [T1542.002](T1542.002_Component_Firmware.md) | Component Firmware | Sub-technique |
| [T1542.003](T1542.003_Bootkit.md) | Bootkit | Sub-technique |
| [T1542.004](T1542.004_ROMMONkit.md) | ROMMONkit | Sub-technique |
| [T1542.005](T1542.005_TFTP_Boot.md) | TFTP Boot | Sub-technique |
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
| [T1554](T1554_Compromise_Host_Software_Binary.md) | Compromise Host Software Binary | Technique |
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
| [T1653](T1653_Power_Settings.md) | Power Settings | Technique |
| [T1668](T1668_Exclusive_Control.md) | Exclusive Control | Technique |
| [T1671](T1671_Cloud_Application_Integration.md) | Cloud Application Integration | Technique |

## Key Technique Categories

Account Manipulation, Boot or Logon Autostart Execution, Create Account, Create or Modify System Process, Event Triggered Execution, External Remote Services, Hijack Execution Flow, Implant Internal Image, Modify Authentication Process, Office Application Startup, Pre-OS Boot, Scheduled Task/Job, Server Software Component, Traffic Signaling, Valid Accounts, and others.

See https://attack.mitre.org/tactics/TA0003/ for the complete current list and sub-techniques.

## Educational Focus

Learn common persistence mechanisms on Windows, Linux, macOS, and cloud, and how to hunt for them (autostart locations, new accounts, scheduled tasks, etc.).

## Safety

Persistence mechanisms in labs must be fully documented and cleaned up after exercises.

## Sources

*Source: [MITRE ATT&CK Tactic TA0003](https://attack.mitre.org/tactics/TA0003/)*
