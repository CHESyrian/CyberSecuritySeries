# TA0040 – Impact

**ID:** TA0040  
**Tactic:** Impact  
**Shortname:** `impact`

## Definition

The adversary is trying to manipulate, interrupt, or destroy your systems and data.
 
Impact consists of techniques that adversaries use to disrupt availability or compromise integrity by manipulating business and operational processes. Techniques used for impact can include destroying or tampering with data. In some cases, business processes can look fine, but may have been altered to benefit the adversaries’ goals. These techniques might be used by adversaries to follow through on their end goal or to provide cover for a confidentiality breach.

## Techniques in this Tactic (33 total)

| ID | Name | Type |
|-----|-------|-------|
| [T1485](T1485_Data_Destruction.md) | Data Destruction | Technique |
| [T1485.001](T1485.001_Lifecycle-Triggered_Deletion.md) | Lifecycle-Triggered Deletion | Sub-technique |
| [T1486](T1486_Data_Encrypted_for_Impact.md) | Data Encrypted for Impact | Technique |
| [T1489](T1489_Service_Stop.md) | Service Stop | Technique |
| [T1490](T1490_Inhibit_System_Recovery.md) | Inhibit System Recovery | Technique |
| [T1491](T1491_Defacement.md) | Defacement | Technique |
| [T1491.001](T1491.001_Internal_Defacement.md) | Internal Defacement | Sub-technique |
| [T1491.002](T1491.002_External_Defacement.md) | External Defacement | Sub-technique |
| [T1495](T1495_Firmware_Corruption.md) | Firmware Corruption | Technique |
| [T1496](T1496_Resource_Hijacking.md) | Resource Hijacking | Technique |
| [T1496.001](T1496.001_Compute_Hijacking.md) | Compute Hijacking | Sub-technique |
| [T1496.002](T1496.002_Bandwidth_Hijacking.md) | Bandwidth Hijacking | Sub-technique |
| [T1496.003](T1496.003_SMS_Pumping.md) | SMS Pumping | Sub-technique |
| [T1496.004](T1496.004_Cloud_Service_Hijacking.md) | Cloud Service Hijacking | Sub-technique |
| [T1498](T1498_Network_Denial_of_Service.md) | Network Denial of Service | Technique |
| [T1498.001](T1498.001_Direct_Network_Flood.md) | Direct Network Flood | Sub-technique |
| [T1498.002](T1498.002_Reflection_Amplification.md) | Reflection Amplification | Sub-technique |
| [T1499](T1499_Endpoint_Denial_of_Service.md) | Endpoint Denial of Service | Technique |
| [T1499.001](T1499.001_OS_Exhaustion_Flood.md) | OS Exhaustion Flood | Sub-technique |
| [T1499.002](T1499.002_Service_Exhaustion_Flood.md) | Service Exhaustion Flood | Sub-technique |
| [T1499.003](T1499.003_Application_Exhaustion_Flood.md) | Application Exhaustion Flood | Sub-technique |
| [T1499.004](T1499.004_Application_or_System_Exploitation.md) | Application or System Exploitation | Sub-technique |
| [T1529](T1529_System_Shutdown_Reboot.md) | System Shutdown/Reboot | Technique |
| [T1531](T1531_Account_Access_Removal.md) | Account Access Removal | Technique |
| [T1561](T1561_Disk_Wipe.md) | Disk Wipe | Technique |
| [T1561.001](T1561.001_Disk_Content_Wipe.md) | Disk Content Wipe | Sub-technique |
| [T1561.002](T1561.002_Disk_Structure_Wipe.md) | Disk Structure Wipe | Sub-technique |
| [T1565](T1565_Data_Manipulation.md) | Data Manipulation | Technique |
| [T1565.001](T1565.001_Stored_Data_Manipulation.md) | Stored Data Manipulation | Sub-technique |
| [T1565.002](T1565.002_Transmitted_Data_Manipulation.md) | Transmitted Data Manipulation | Sub-technique |
| [T1565.003](T1565.003_Runtime_Data_Manipulation.md) | Runtime Data Manipulation | Sub-technique |
| [T1657](T1657_Financial_Theft.md) | Financial Theft | Technique |
| [T1667](T1667_Email_Bombing.md) | Email Bombing | Technique |

## Official Description

The adversary is trying to manipulate, interrupt, or destroy your systems and data.

Impact consists of techniques that adversaries use to disrupt availability or integrity of systems and data (destruction, encryption for ransomware, defacement, denial-of-service, resource hijacking, service stop, account removal, etc.).

**Source:** https://attack.mitre.org/tactics/TA0040/

## Key Techniques (representative)

- T1531 Account Access Removal
- T1485 Data Destruction
- T1486 Data Encrypted for Impact
- T1565 Data Manipulation
- T1491 Defacement
- T1561 Disk Wipe
- T1667 Email Bombing
- T1499 Endpoint Denial of Service
- T1657 Financial Theft
- T1495 Firmware Corruption
- T1490 Inhibit System Recovery
- T1498 Network Denial of Service
- T1496 Resource Hijacking
- T1489 Service Stop
- T1529 System Shutdown/Reboot

Full list: https://attack.mitre.org/tactics/TA0040/

## Educational Focus

Understand ransomware and destructive TTPs; emphasize backup/recovery, integrity monitoring, and rapid isolation of impact activities.

## Safety

Destructive techniques must never be practiced outside fully disposable, isolated lab environments.

## Sources

*Source: [MITRE ATT&CK Tactic TA0040](https://attack.mitre.org/tactics/TA0040/)*
