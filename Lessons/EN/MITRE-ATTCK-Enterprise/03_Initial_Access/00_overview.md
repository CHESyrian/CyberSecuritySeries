# TA0001 – Initial Access

**ID:** TA0001  
**Tactic:** Initial Access  

**Shortname:** `initial-access`

## Definition

The adversary is trying to get into your network.

Initial Access consists of techniques that use various entry vectors to gain their initial foothold within a network. Techniques used to gain a foothold include targeted spearphishing and exploiting weaknesses on public-facing web servers. Footholds gained through initial access may allow for continued access, like valid accounts and use of external remote services, or may be limited-use due to changing passwords.

## Official Description

The adversary is trying to get into your network.

Initial Access consists of techniques that use various entry vectors to gain an initial foothold within a network. These techniques include targeted spearphishing and exploiting weaknesses on public-facing web servers. Techniques that result in access through the use of stolen credentials or remote services are also covered here.

**Source:** https://attack.mitre.org/tactics/TA0001/

## Techniques in this Tactic (22 total)

| ID | Name | Type |
|----|------|------|
| [T1078](T1078_Valid_Accounts.md) | Valid Accounts | Technique |
| [T1078.001](T1078.001_Default_Accounts.md) | Default Accounts | Sub-technique |
| [T1078.002](T1078.002_Domain_Accounts.md) | Domain Accounts | Sub-technique |
| [T1078.003](T1078.003_Local_Accounts.md) | Local Accounts | Sub-technique |
| [T1078.004](T1078.004_Cloud_Accounts.md) | Cloud Accounts | Sub-technique |
| [T1091](T1091_Replication_Through_Removable_Media.md) | Replication Through Removable Media | Technique |
| [T1133](T1133_External_Remote_Services.md) | External Remote Services | Technique |
| [T1189](T1189_Drive-by_Compromise.md) | Drive-by Compromise | Technique |
| [T1190](T1190_Exploit_Public-Facing_Application.md) | Exploit Public-Facing Application | Technique |
| [T1195](T1195_Supply_Chain_Compromise.md) | Supply Chain Compromise | Technique |
| [T1195.001](T1195.001_Compromise_Software_Dependencies_and_Development_Tools.md) | Compromise Software Dependencies and Development Tools | Sub-technique |
| [T1195.002](T1195.002_Compromise_Software_Supply_Chain.md) | Compromise Software Supply Chain | Sub-technique |
| [T1195.003](T1195.003_Compromise_Hardware_Supply_Chain.md) | Compromise Hardware Supply Chain | Sub-technique |
| [T1199](T1199_Trusted_Relationship.md) | Trusted Relationship | Technique |
| [T1200](T1200_Hardware_Additions.md) | Hardware Additions | Technique |
| [T1566](T1566_Phishing.md) | Phishing | Technique |
| [T1566.001](T1566.001_Spearphishing_Attachment.md) | Spearphishing Attachment | Sub-technique |
| [T1566.002](T1566.002_Spearphishing_Link.md) | Spearphishing Link | Sub-technique |
| [T1566.003](T1566.003_Spearphishing_via_Service.md) | Spearphishing via Service | Sub-technique |
| [T1566.004](T1566.004_Spearphishing_Voice.md) | Spearphishing Voice | Sub-technique |
| [T1659](T1659_Content_Injection.md) | Content Injection | Technique |
| [T1669](T1669_Wi-Fi_Networks.md) | Wi-Fi Networks | Technique |

## Key Techniques (representative)

- T1659 Content Injection
- T1189 Drive-by Compromise
- T1190 Exploit Public-Facing Application
- T1133 External Remote Services
- T1200 Hardware Additions
- T1566 Phishing (and spearphishing sub-techniques)
- T1091 Replication Through Removable Media
- T1195 Supply Chain Compromise
- T1199 Trusted Relationship
- T1078 Valid Accounts
- T1669 Wi-Fi Networks

Full list and details: https://attack.mitre.org/tactics/TA0001/

## Educational Focus

Map common entry vectors (phishing, exposed services, valid accounts) to technique IDs. Emphasize detection of initial footholds and rapid isolation.

## Safety

All examples and exercises restricted to authorized laboratory targets only.

## Sources

*Source: [MITRE ATT&CK Tactic TA0001](https://attack.mitre.org/tactics/TA0001/)*
