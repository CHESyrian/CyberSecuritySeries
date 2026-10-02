# TA0042 – Resource Development

**ID:** TA0042  
**Tactic:** Resource Development  
**Shortname:** `resource-development`

## Definition

The adversary is trying to establish resources they can use to support operations.

Resource Development consists of techniques that involve adversaries creating, purchasing, or compromising/stealing resources that can be used to support targeting. Such resources include infrastructure, accounts, or capabilities. These resources can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using purchased domains to support Command and Control, email accounts for phishing as a part of Initial Access, or stealing code signing certificates to help with Defense Evasion.

## Official Description

The adversary is trying to establish resources they can use to support operations.

Adversaries may buy, lease, or compromise resources that can be used during targeting. Resources include infrastructure, accounts, capabilities (malware, exploits, certificates), and staged tools or content. These resources enable later phases of the intrusion.

**Source:** https://attack.mitre.org/tactics/TA0042/


## Techniques in this Tactic (50 total)

| ID | Name | Type |
|-----|-------|-------|
| [T1583](T1583_Acquire_Infrastructure.md) | Acquire Infrastructure | Technique |
| [T1583.001](T1583.001_Domains.md) | Domains | Sub-technique |
| [T1583.002](T1583.002_DNS_Server.md) | DNS Server | Sub-technique |
| [T1583.003](T1583.003_Virtual_Private_Server.md) | Virtual Private Server | Sub-technique |
| [T1583.004](T1583.004_Server.md) | Server | Sub-technique |
| [T1583.005](T1583.005_Botnet.md) | Botnet | Sub-technique |
| [T1583.006](T1583.006_Web_Services.md) | Web Services | Sub-technique |
| [T1583.007](T1583.007_Serverless.md) | Serverless | Sub-technique |
| [T1583.008](T1583.008_Malvertising.md) | Malvertising | Sub-technique |
| [T1584](T1584_Compromise_Infrastructure.md) | Compromise Infrastructure | Technique |
| [T1584.001](T1584.001_Domains.md) | Domains | Sub-technique |
| [T1584.002](T1584.002_DNS_Server.md) | DNS Server | Sub-technique |
| [T1584.003](T1584.003_Virtual_Private_Server.md) | Virtual Private Server | Sub-technique |
| [T1584.004](T1584.004_Server.md) | Server | Sub-technique |
| [T1584.005](T1584.005_Botnet.md) | Botnet | Sub-technique |
| [T1584.006](T1584.006_Web_Services.md) | Web Services | Sub-technique |
| [T1584.007](T1584.007_Serverless.md) | Serverless | Sub-technique |
| [T1584.008](T1584.008_Network_Devices.md) | Network Devices | Sub-technique |
| [T1585](T1585_Establish_Accounts.md) | Establish Accounts | Technique |
| [T1585.001](T1585.001_Social_Media_Accounts.md) | Social Media Accounts | Sub-technique |
| [T1585.002](T1585.002_Email_Accounts.md) | Email Accounts | Sub-technique |
| [T1585.003](T1585.003_Cloud_Accounts.md) | Cloud Accounts | Sub-technique |
| [T1586](T1586_Compromise_Accounts.md) | Compromise Accounts | Technique |
| [T1586.001](T1586.001_Social_Media_Accounts.md) | Social Media Accounts | Sub-technique |
| [T1586.002](T1586.002_Email_Accounts.md) | Email Accounts | Sub-technique |
| [T1586.003](T1586.003_Cloud_Accounts.md) | Cloud Accounts | Sub-technique |
| [T1587](T1587_Develop_Capabilities.md) | Develop Capabilities | Technique |
| [T1587.001](T1587.001_Malware.md) | Malware | Sub-technique |
| [T1587.002](T1587.002_Code_Signing_Certificates.md) | Code Signing Certificates | Sub-technique |
| [T1587.003](T1587.003_Digital_Certificates.md) | Digital Certificates | Sub-technique |
| [T1587.004](T1587.004_Exploits.md) | Exploits | Sub-technique |
| [T1588](T1588_Obtain_Capabilities.md) | Obtain Capabilities | Technique |
| [T1588.001](T1588.001_Malware.md) | Malware | Sub-technique |
| [T1588.002](T1588.002_Tool.md) | Tool | Sub-technique |
| [T1588.003](T1588.003_Code_Signing_Certificates.md) | Code Signing Certificates | Sub-technique |
| [T1588.004](T1588.004_Digital_Certificates.md) | Digital Certificates | Sub-technique |
| [T1588.005](T1588.005_Exploits.md) | Exploits | Sub-technique |
| [T1588.006](T1588.006_Vulnerabilities.md) | Vulnerabilities | Sub-technique |
| [T1588.007](T1588.007_Artificial_Intelligence.md) | Artificial Intelligence | Sub-technique |
| [T1608](T1608_Stage_Capabilities.md) | Stage Capabilities | Technique |
| [T1608.001](T1608.001_Upload_Malware.md) | Upload Malware | Sub-technique |
| [T1608.002](T1608.002_Upload_Tool.md) | Upload Tool | Sub-technique |
| [T1608.003](T1608.003_Install_Digital_Certificate.md) | Install Digital Certificate | Sub-technique |
| [T1608.004](T1608.004_Drive-by_Target.md) | Drive-by Target | Sub-technique |
| [T1608.005](T1608.005_Link_Target.md) | Link Target | Sub-technique |
| [T1608.006](T1608.006_SEO_Poisoning.md) | SEO Poisoning | Sub-technique |
| [T1650](T1650_Acquire_Access.md) | Acquire Access | Technique |
| [T1683](T1683_Generate_Content.md) | Generate Content | Technique |
| [T1683.001](T1683.001_Written_Content.md) | Written Content | Sub-technique |
| [T1683.002](T1683.002_Audio-Visual_Content.md) | Audio-Visual Content | Sub-technique |


## Educational Focus

Understand how adversaries prepare infrastructure and tooling before Initial Access. In labs, practice mapping observed domain registration, certificate issuance, or malware staging to these techniques (authorized environments only).

## Safety

Never acquire or stage real malicious infrastructure or malware outside controlled, isolated laboratory environments with proper authorization and containment.

## Sources

*Source: [MITRE ATT&CK Tactic TA0042](https://attack.mitre.org/tactics/TA0042/)*

