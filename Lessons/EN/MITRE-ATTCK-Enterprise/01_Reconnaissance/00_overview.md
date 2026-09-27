# TA0043 - Reconnaissance

**ID:** TA0043  
**Tactic:** Reconnaissance  
**Shortname:** `reconnaissance`

## Definition

The adversary is trying to gather information they can use to plan future operations.

Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.

## Official Description

The adversary is trying to gather information they can use to plan future operations.

Reconnaissance consists of techniques that involve adversaries actively or passively gathering information that can be used to support targeting. Such information may include details of the victim organization, infrastructure, or staff/personnel. This information can be leveraged by the adversary to aid in other phases of the adversary lifecycle, such as using gathered information to plan and execute Initial Access, to scope and prioritize post-compromise objectives, or to drive and lead further Reconnaissance efforts.

**Source:** https://attack.mitre.org/tactics/TA0043/

## Learning Objectives

- Understand the difference between active and passive reconnaissance.
- Map common OSINT and scanning activities to ATT&CK technique IDs.
- Recognize how reconnaissance feeds later tactics (Initial Access, Resource Development).
- Apply defensive monitoring and hunting guidance for these techniques in authorized lab environments only.

## Techniques in this Tactic (46 total)

| ID | Name | Type |
|----|------|------|
| [T1589](T1589_Gather_Victim_Identity_Information.md) | Gather Victim Identity Information | Technique |
| [T1589.001](T1589.001_Credentials.md) | Credentials | Sub-technique |
| [T1589.002](T1589.002_Email_Addresses.md) | Email Addresses | Sub-technique |
| [T1589.003](T1589.003_Employee_Names.md) | Employee Names | Sub-technique |
| [T1590](T1590_Gather_Victim_Network_Information.md) | Gather Victim Network Information | Technique |
| [T1590.001](T1590.001_Domain_Properties.md) | Domain Properties | Sub-technique |
| [T1590.002](T1590.002_DNS.md) | DNS | Sub-technique |
| [T1590.003](T1590.003_Network_Trust_Dependencies.md) | Network Trust Dependencies | Sub-technique |
| [T1590.004](T1590.004_Network_Topology.md) | Network Topology | Sub-technique |
| [T1590.005](T1590.005_IP_Addresses.md) | IP Addresses | Sub-technique |
| [T1590.006](T1590.006_Network_Security_Appliances.md) | Network Security Appliances | Sub-technique |
| [T1591](T1591_Gather_Victim_Org_Information.md) | Gather Victim Org Information | Technique |
| [T1591.001](T1591.001_Determine_Physical_Locations.md) | Determine Physical Locations | Sub-technique |
| [T1591.002](T1591.002_Business_Relationships.md) | Business Relationships | Sub-technique |
| [T1591.003](T1591.003_Identify_Business_Tempo.md) | Identify Business Tempo | Sub-technique |
| [T1591.004](T1591.004_Identify_Roles.md) | Identify Roles | Sub-technique |
| [T1592](T1592_Gather_Victim_Host_Information.md) | Gather Victim Host Information | Technique |
| [T1592.001](T1592.001_Hardware.md) | Hardware | Sub-technique |
| [T1592.002](T1592.002_Software.md) | Software | Sub-technique |
| [T1592.003](T1592.003_Firmware.md) | Firmware | Sub-technique |
| [T1592.004](T1592.004_Client_Configurations.md) | Client Configurations | Sub-technique |
| [T1593](T1593_Search_Open_Websites_Domains.md) | Search Open Websites/Domains | Technique |
| [T1593.001](T1593.001_Social_Media.md) | Social Media | Sub-technique |
| [T1593.002](T1593.002_Search_Engines.md) | Search Engines | Sub-technique |
| [T1593.003](T1593.003_Code_Repositories.md) | Code Repositories | Sub-technique |
| [T1594](T1594_Search_Victim-Owned_Websites.md) | Search Victim-Owned Websites | Technique |
| [T1595](T1595_Active_Scanning.md) | Active Scanning | Technique |
| [T1595.001](T1595.001_Scanning_IP_Blocks.md) | Scanning IP Blocks | Sub-technique |
| [T1595.002](T1595.002_Vulnerability_Scanning.md) | Vulnerability Scanning | Sub-technique |
| [T1595.003](T1595.003_Wordlist_Scanning.md) | Wordlist Scanning | Sub-technique |
| [T1596](T1596_Search_Open_Technical_Databases.md) | Search Open Technical Databases | Technique |
| [T1596.001](T1596.001_DNS_Passive_DNS.md) | DNS/Passive DNS | Sub-technique |
| [T1596.002](T1596.002_WHOIS.md) | WHOIS | Sub-technique |
| [T1596.003](T1596.003_Digital_Certificates.md) | Digital Certificates | Sub-technique |
| [T1596.004](T1596.004_CDNs.md) | CDNs | Sub-technique |
| [T1596.005](T1596.005_Scan_Databases.md) | Scan Databases | Sub-technique |
| [T1597](T1597_Search_Closed_Sources.md) | Search Closed Sources | Technique |
| [T1597.001](T1597.001_Threat_Intel_Vendors.md) | Threat Intel Vendors | Sub-technique |
| [T1597.002](T1597.002_Purchase_Technical_Data.md) | Purchase Technical Data | Sub-technique |
| [T1598](T1598_Phishing_for_Information.md) | Phishing for Information | Technique |
| [T1598.001](T1598.001_Spearphishing_Service.md) | Spearphishing Service | Sub-technique |
| [T1598.002](T1598.002_Spearphishing_Attachment.md) | Spearphishing Attachment | Sub-technique |
| [T1598.003](T1598.003_Spearphishing_Link.md) | Spearphishing Link | Sub-technique |
| [T1598.004](T1598.004_Spearphishing_Voice.md) | Spearphishing Voice | Sub-technique |
| [T1681](T1681_Search_Threat_Vendor_Data.md) | Search Threat Vendor Data | Technique |
| [T1682](T1682_Query_Public_AI_Services.md) | Query Public AI Services | Technique |

## Safety & Ethics

All practical exercises using these concepts must be performed only against systems you own or have explicit written authorization to test. Reconnaissance against third-party infrastructure without permission is illegal in most jurisdictions.

## Related Curriculum

- Phase-2 Stage 5 (Reconnaissance)
- Phase-3 Track-5 (Adversary Simulation Basics) – authorized lab only
- Tools: Nmap, OSINT frameworks (lab use)

## Sources

- https://attack.mitre.org/tactics/TA0043/
- Individual technique pages linked from the matrix

---
*Source: [MITRE ATT&CK Tactic TA0043](https://attack.mitre.org/tactics/TA0043/)*