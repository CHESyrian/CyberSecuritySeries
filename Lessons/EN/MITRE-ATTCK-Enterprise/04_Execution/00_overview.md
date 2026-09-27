# TA0002 – Execution

**ID:** TA0002  
**Tactic:** Execution  
# TA0002: Execution

**Shortname:** `execution`

## Definition

The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from all other tactics to achieve broader goals, like exploring a network or stealing data. For example, an adversary might use a remote access tool to run a PowerShell script that does Remote System Discovery.

## Official Description

The adversary is trying to run malicious code.

Execution consists of techniques that result in adversary-controlled code running on a local or remote system. Techniques that run malicious code are often paired with techniques from other tactics (Initial Access, Lateral Movement, etc.).

**Source:** https://attack.mitre.org/tactics/TA0002/

## Techniques in this Tactic (64 total)

| ID | Name | Type |
|----|------|------|
| [T1047](T1047_Windows_Management_Instrumentation.md) | Windows Management Instrumentation | Technique |
| [T1053](T1053_Scheduled_Task_Job.md) | Scheduled Task/Job | Technique |
| [T1053.002](T1053.002_At.md) | At | Sub-technique |
| [T1053.003](T1053.003_Cron.md) | Cron | Sub-technique |
| [T1053.005](T1053.005_Scheduled_Task.md) | Scheduled Task | Sub-technique |
| [T1053.006](T1053.006_Systemd_Timers.md) | Systemd Timers | Sub-technique |
| [T1053.007](T1053.007_Container_Orchestration_Job.md) | Container Orchestration Job | Sub-technique |
| [T1059](T1059_Command_and_Scripting_Interpreter.md) | Command and Scripting Interpreter | Technique |
| [T1059.001](T1059.001_PowerShell.md) | PowerShell | Sub-technique |
| [T1059.002](T1059.002_AppleScript.md) | AppleScript | Sub-technique |
| [T1059.003](T1059.003_Windows_Command_Shell.md) | Windows Command Shell | Sub-technique |
| [T1059.004](T1059.004_Unix_Shell.md) | Unix Shell | Sub-technique |
| [T1059.005](T1059.005_Visual_Basic.md) | Visual Basic | Sub-technique |
| [T1059.006](T1059.006_Python.md) | Python | Sub-technique |
| [T1059.007](T1059.007_JavaScript.md) | JavaScript | Sub-technique |
| [T1059.008](T1059.008_Network_Device_CLI.md) | Network Device CLI | Sub-technique |
| [T1059.009](T1059.009_Cloud_API.md) | Cloud API | Sub-technique |
| [T1059.010](T1059.010_AutoHotKey___AutoIT.md) | AutoHotKey & AutoIT | Sub-technique |
| [T1059.011](T1059.011_Lua.md) | Lua | Sub-technique |
| [T1059.012](T1059.012_Hypervisor_CLI.md) | Hypervisor CLI | Sub-technique |
| [T1059.013](T1059.013_Container_CLI_API.md) | Container CLI/API | Sub-technique |
| [T1072](T1072_Software_Deployment_Tools.md) | Software Deployment Tools | Technique |
| [T1106](T1106_Native_API.md) | Native API | Technique |
| [T1127](T1127_Trusted_Developer_Utilities_Proxy_Execution.md) | Trusted Developer Utilities Proxy Execution | Technique |
| [T1127.001](T1127.001_MSBuild.md) | MSBuild | Sub-technique |
| [T1127.002](T1127.002_ClickOnce.md) | ClickOnce | Sub-technique |
| [T1127.003](T1127.003_JamPlus.md) | JamPlus | Sub-technique |
| [T1129](T1129_Shared_Modules.md) | Shared Modules | Technique |
| [T1197](T1197_BITS_Jobs.md) | BITS Jobs | Technique |
| [T1203](T1203_Exploitation_for_Client_Execution.md) | Exploitation for Client Execution | Technique |
| [T1204](T1204_User_Execution.md) | User Execution | Technique |
| [T1204.001](T1204.001_Malicious_Link.md) | Malicious Link | Sub-technique |
| [T1204.002](T1204.002_Malicious_File.md) | Malicious File | Sub-technique |
| [T1204.003](T1204.003_Malicious_Image.md) | Malicious Image | Sub-technique |
| [T1204.004](T1204.004_Malicious_Copy_and_Paste.md) | Malicious Copy and Paste | Sub-technique |
| [T1204.005](T1204.005_Malicious_Library.md) | Malicious Library | Sub-technique |
| [T1559](T1559_Inter-Process_Communication.md) | Inter-Process Communication | Technique |
| [T1559.001](T1559.001_Component_Object_Model.md) | Component Object Model | Sub-technique |
| [T1559.002](T1559.002_Dynamic_Data_Exchange.md) | Dynamic Data Exchange | Sub-technique |
| [T1559.003](T1559.003_XPC_Services.md) | XPC Services | Sub-technique |
| [T1569](T1569_System_Services.md) | System Services | Technique |
| [T1569.001](T1569.001_Launchctl.md) | Launchctl | Sub-technique |
| [T1569.002](T1569.002_Service_Execution.md) | Service Execution | Sub-technique |
| [T1569.003](T1569.003_Systemctl.md) | Systemctl | Sub-technique |
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
| [T1609](T1609_Container_Administration_Command.md) | Container Administration Command | Technique |
| [T1610](T1610_Deploy_Container.md) | Deploy Container | Technique |
| [T1648](T1648_Serverless_Execution.md) | Serverless Execution | Technique |
| [T1651](T1651_Cloud_Administration_Command.md) | Cloud Administration Command | Technique |
| [T1674](T1674_Input_Injection.md) | Input Injection | Technique |
| [T1675](T1675_ESXi_Administration_Command.md) | ESXi Administration Command | Technique |
| [T1677](T1677_Poisoned_Pipeline_Execution.md) | Poisoned Pipeline Execution | Technique |

## Key Techniques (representative)

- T1197 BITS Jobs
- T1651 Cloud Administration Command
- T1059 Command and Scripting Interpreter (PowerShell, Python, JavaScript, AppleScript, etc.)
- T1609 Container Administration Command
- T1610 Deploy Container
- T1675 ESXi Administration Command
- T1203 Exploitation for Client Execution
- T1574 Hijack Execution Flow
- T1674 Input Injection
- T1559 Inter-Process Communication
- T1106 Native API
- T1677 Poisoned Pipeline Execution
- T1053 Scheduled Task/Job
- T1648 Serverless Execution
- T1129 Shared Modules
- T1072 Software Deployment Tools
- T1569 System Services
- T1127 Trusted Developer Utilities Proxy Execution
- T1204 User Execution
- T1047 Windows Management Instrumentation

Full details on the official site.

## Educational Focus

Understand how code is executed after Initial Access and how defenders can monitor process creation, script interpreters, and scheduled tasks.

## Safety

Code-execution examples only in isolated labs.

## Sources

*Source: [MITRE ATT&CK Tactic TA0002](https://attack.mitre.org/tactics/TA0002/)*
