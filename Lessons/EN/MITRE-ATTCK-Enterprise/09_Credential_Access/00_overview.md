# TA0006 – Credential Access

**ID:** TA0006  
**Tactic:** Credential Access  
**Shortname:** `credential-access`

## Definition

The adversary is trying to steal account names and passwords.

Credential Access consists of techniques for stealing credentials like account names and passwords. Techniques used to get credentials include keylogging or credential dumping. Using legitimate credentials can give adversaries access to systems, make them harder to detect, and provide the opportunity to create more accounts to help achieve their goals.

## Techniques in this Tactic (67 total)

| ID | Name | Type |
|-----|-------|-------|
| [T1003](T1003_OS_Credential_Dumping.md) | OS Credential Dumping | Technique |
| [T1003.001](T1003.001_LSASS_Memory.md) | LSASS Memory | Sub-technique |
| [T1003.002](T1003.002_Security_Account_Manager.md) | Security Account Manager | Sub-technique |
| [T1003.003](T1003.003_NTDS.md) | NTDS | Sub-technique |
| [T1003.004](T1003.004_LSA_Secrets.md) | LSA Secrets | Sub-technique |
| [T1003.005](T1003.005_Cached_Domain_Credentials.md) | Cached Domain Credentials | Sub-technique |
| [T1003.006](T1003.006_DCSync.md) | DCSync | Sub-technique |
| [T1003.007](T1003.007_Proc_Filesystem.md) | Proc Filesystem | Sub-technique |
| [T1003.008](T1003.008_etc_passwd_and__etc_shadow.md) | /etc/passwd and /etc/shadow | Sub-technique |
| [T1040](T1040_Network_Sniffing.md) | Network Sniffing | Technique |
| [T1056](T1056_Input_Capture.md) | Input Capture | Technique |
| [T1056.001](T1056.001_Keylogging.md) | Keylogging | Sub-technique |
| [T1056.002](T1056.002_GUI_Input_Capture.md) | GUI Input Capture | Sub-technique |
| [T1056.003](T1056.003_Web_Portal_Capture.md) | Web Portal Capture | Sub-technique |
| [T1056.004](T1056.004_Credential_API_Hooking.md) | Credential API Hooking | Sub-technique |
| [T1110](T1110_Brute_Force.md) | Brute Force | Technique |
| [T1110.001](T1110.001_Password_Guessing.md) | Password Guessing | Sub-technique |
| [T1110.002](T1110.002_Password_Cracking.md) | Password Cracking | Sub-technique |
| [T1110.003](T1110.003_Password_Spraying.md) | Password Spraying | Sub-technique |
| [T1110.004](T1110.004_Credential_Stuffing.md) | Credential Stuffing | Sub-technique |
| [T1111](T1111_Multi-Factor_Authentication_Interception.md) | Multi-Factor Authentication Interception | Technique |
| [T1187](T1187_Forced_Authentication.md) | Forced Authentication | Technique |
| [T1212](T1212_Exploitation_for_Credential_Access.md) | Exploitation for Credential Access | Technique |
| [T1528](T1528_Steal_Application_Access_Token.md) | Steal Application Access Token | Technique |
| [T1539](T1539_Steal_Web_Session_Cookie.md) | Steal Web Session Cookie | Technique |
| [T1552](T1552_Unsecured_Credentials.md) | Unsecured Credentials | Technique |
| [T1552.001](T1552.001_Credentials_In_Files.md) | Credentials In Files | Sub-technique |
| [T1552.002](T1552.002_Credentials_in_Registry.md) | Credentials in Registry | Sub-technique |
| [T1552.003](T1552.003_Shell_History.md) | Shell History | Sub-technique |
| [T1552.004](T1552.004_Private_Keys.md) | Private Keys | Sub-technique |
| [T1552.005](T1552.005_Cloud_Instance_Metadata_API.md) | Cloud Instance Metadata API | Sub-technique |
| [T1552.006](T1552.006_Group_Policy_Preferences.md) | Group Policy Preferences | Sub-technique |
| [T1552.007](T1552.007_Container_API.md) | Container API | Sub-technique |
| [T1552.008](T1552.008_Chat_Messages.md) | Chat Messages | Sub-technique |
| [T1555](T1555_Credentials_from_Password_Stores.md) | Credentials from Password Stores | Technique |
| [T1555.001](T1555.001_Keychain.md) | Keychain | Sub-technique |
| [T1555.002](T1555.002_Securityd_Memory.md) | Securityd Memory | Sub-technique |
| [T1555.003](T1555.003_Credentials_from_Web_Browsers.md) | Credentials from Web Browsers | Sub-technique |
| [T1555.004](T1555.004_Windows_Credential_Manager.md) | Windows Credential Manager | Sub-technique |
| [T1555.005](T1555.005_Password_Managers.md) | Password Managers | Sub-technique |
| [T1555.006](T1555.006_Cloud_Secrets_Management_Stores.md) | Cloud Secrets Management Stores | Sub-technique |
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
| [T1557](T1557_Adversary-in-the-Middle.md) | Adversary-in-the-Middle | Technique |
| [T1557.001](T1557.001_Name_Resolution_Poisoning_and_SMB_Relay.md) | Name Resolution Poisoning and SMB Relay | Sub-technique |
| [T1557.002](T1557.002_ARP_Cache_Poisoning.md) | ARP Cache Poisoning | Sub-technique |
| [T1557.003](T1557.003_DHCP_Spoofing.md) | DHCP Spoofing | Sub-technique |
| [T1557.004](T1557.004_Evil_Twin.md) | Evil Twin | Sub-technique |
| [T1558](T1558_Steal_or_Forge_Kerberos_Tickets.md) | Steal or Forge Kerberos Tickets | Technique |
| [T1558.001](T1558.001_Golden_Ticket.md) | Golden Ticket | Sub-technique |
| [T1558.002](T1558.002_Silver_Ticket.md) | Silver Ticket | Sub-technique |
| [T1558.003](T1558.003_Kerberoasting.md) | Kerberoasting | Sub-technique |
| [T1558.004](T1558.004_AS-REP_Roasting.md) | AS-REP Roasting | Sub-technique |
| [T1558.005](T1558.005_Ccache_Files.md) | Ccache Files | Sub-technique |
| [T1606](T1606_Forge_Web_Credentials.md) | Forge Web Credentials | Technique |
| [T1606.001](T1606.001_Web_Cookies.md) | Web Cookies | Sub-technique |
| [T1606.002](T1606.002_SAML_Tokens.md) | SAML Tokens | Sub-technique |
| [T1621](T1621_Multi-Factor_Authentication_Request_Generation.md) | Multi-Factor Authentication Request Generation | Technique |
| [T1649](T1649_Steal_or_Forge_Authentication_Certificates.md) | Steal or Forge Authentication Certificates | Technique |

## Official Description

The adversary is trying to steal account names and passwords.

Credential Access consists of techniques for stealing credentials (passwords, hashes, tokens, keys, certificates) that can later be used for access or lateral movement.

**Source:** https://attack.mitre.org/tactics/TA0006/

## Key Technique Categories

Adversary-in-the-Middle, Brute Force, Credentials from Password Stores, Exploitation for Credential Access, Forced Authentication, Forge Web Credentials, Input Capture (keylogging, etc.), Modify Authentication Process, Network Sniffing, OS Credential Dumping, Steal or Forge Kerberos Tickets / Authentication Certificates, Unsecured Credentials, and others.

Full list: https://attack.mitre.org/tactics/TA0006/

## Educational Focus

Understand credential-dumping methods, password-spraying, and token theft at a conceptual level; emphasize detection (LSASS access, unusual authentication, etc.) and strong credential hygiene / MFA.

## Safety

Credential-access exercises only in isolated labs; never against production or third-party systems.

## Sources

*Source: [MITRE ATT&CK Tactic TA0006](https://attack.mitre.org/tactics/TA0006/)*
