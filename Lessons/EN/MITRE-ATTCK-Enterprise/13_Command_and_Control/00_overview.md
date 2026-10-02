# TA0011 – Command and Control

**ID:** TA0011  
**Tactic:** Command and Control  
**Shortname:** `command-and-control`

## Definition

The adversary is trying to communicate with compromised systems to control them.

Command and Control consists of techniques that adversaries may use to communicate with systems under their control within a victim network. Adversaries commonly attempt to mimic normal, expected traffic to avoid detection. There are many ways an adversary can establish command and control with various levels of stealth depending on the victim’s network structure and defenses.

## Techniques in this Tactic (45 total)

| ID | Name | Type |
|-----|-------|-------|
| [T1001](T1001_Data_Obfuscation.md) | Data Obfuscation | Technique |
| [T1001.001](T1001.001_Junk_Data.md) | Junk Data | Sub-technique |
| [T1001.002](T1001.002_Steganography.md) | Steganography | Sub-technique |
| [T1001.003](T1001.003_Protocol_or_Service_Impersonation.md) | Protocol or Service Impersonation | Sub-technique |
| [T1008](T1008_Fallback_Channels.md) | Fallback Channels | Technique |
| [T1071](T1071_Application_Layer_Protocol.md) | Application Layer Protocol | Technique |
| [T1071.001](T1071.001_Web_Protocols.md) | Web Protocols | Sub-technique |
| [T1071.002](T1071.002_File_Transfer_Protocols.md) | File Transfer Protocols | Sub-technique |
| [T1071.003](T1071.003_Mail_Protocols.md) | Mail Protocols | Sub-technique |
| [T1071.004](T1071.004_DNS.md) | DNS | Sub-technique |
| [T1071.005](T1071.005_Publish_Subscribe_Protocols.md) | Publish/Subscribe Protocols | Sub-technique |
| [T1090](T1090_Proxy.md) | Proxy | Technique |
| [T1090.001](T1090.001_Internal_Proxy.md) | Internal Proxy | Sub-technique |
| [T1090.002](T1090.002_External_Proxy.md) | External Proxy | Sub-technique |
| [T1090.003](T1090.003_Multi-hop_Proxy.md) | Multi-hop Proxy | Sub-technique |
| [T1090.004](T1090.004_Domain_Fronting.md) | Domain Fronting | Sub-technique |
| [T1092](T1092_Communication_Through_Removable_Media.md) | Communication Through Removable Media | Technique |
| [T1095](T1095_Non-Application_Layer_Protocol.md) | Non-Application Layer Protocol | Technique |
| [T1102](T1102_Web_Service.md) | Web Service | Technique |
| [T1102.001](T1102.001_Dead_Drop_Resolver.md) | Dead Drop Resolver | Sub-technique |
| [T1102.002](T1102.002_Bidirectional_Communication.md) | Bidirectional Communication | Sub-technique |
| [T1102.003](T1102.003_One-Way_Communication.md) | One-Way Communication | Sub-technique |
| [T1104](T1104_Multi-Stage_Channels.md) | Multi-Stage Channels | Technique |
| [T1105](T1105_Ingress_Tool_Transfer.md) | Ingress Tool Transfer | Technique |
| [T1132](T1132_Data_Encoding.md) | Data Encoding | Technique |
| [T1132.001](T1132.001_Standard_Encoding.md) | Standard Encoding | Sub-technique |
| [T1132.002](T1132.002_Non-Standard_Encoding.md) | Non-Standard Encoding | Sub-technique |
| [T1205](T1205_Traffic_Signaling.md) | Traffic Signaling | Technique |
| [T1205.001](T1205.001_Port_Knocking.md) | Port Knocking | Sub-technique |
| [T1205.002](T1205.002_Socket_Filters.md) | Socket Filters | Sub-technique |
| [T1219](T1219_Remote_Access_Tools.md) | Remote Access Tools | Technique |
| [T1219.001](T1219.001_IDE_Tunneling.md) | IDE Tunneling | Sub-technique |
| [T1219.002](T1219.002_Remote_Desktop_Software.md) | Remote Desktop Software | Sub-technique |
| [T1219.003](T1219.003_Remote_Access_Hardware.md) | Remote Access Hardware | Sub-technique |
| [T1568](T1568_Dynamic_Resolution.md) | Dynamic Resolution | Technique |
| [T1568.001](T1568.001_Fast_Flux_DNS.md) | Fast Flux DNS | Sub-technique |
| [T1568.002](T1568.002_Domain_Generation_Algorithms.md) | Domain Generation Algorithms | Sub-technique |
| [T1568.003](T1568.003_DNS_Calculation.md) | DNS Calculation | Sub-technique |
| [T1571](T1571_Non-Standard_Port.md) | Non-Standard Port | Technique |
| [T1572](T1572_Protocol_Tunneling.md) | Protocol Tunneling | Technique |
| [T1573](T1573_Encrypted_Channel.md) | Encrypted Channel | Technique |
| [T1573.001](T1573.001_Symmetric_Cryptography.md) | Symmetric Cryptography | Sub-technique |
| [T1573.002](T1573.002_Asymmetric_Cryptography.md) | Asymmetric Cryptography | Sub-technique |
| [T1659](T1659_Content_Injection.md) | Content Injection | Technique |
| [T1665](T1665_Hide_Infrastructure.md) | Hide Infrastructure | Technique |

## Official Description

The adversary is trying to communicate with compromised systems to control them.

Command and Control consists of techniques that adversaries use to communicate with systems under their control. They may use standard protocols, non-standard ports, encryption, proxies, multi-stage channels, or web services to blend with normal traffic.

**Source:** https://attack.mitre.org/tactics/TA0011/

## Key Techniques (representative)

- T1071 Application Layer Protocol (DNS, Web, Mail, File Transfer, Publish/Subscribe)
- T1092 Communication Through Removable Media
- T1659 Content Injection
- T1132 Data Encoding
- T1001 Data Obfuscation
- T1568 Dynamic Resolution
- T1573 Encrypted Channel
- T1008 Fallback Channels
- T1665 Hide Infrastructure
- T1105 Ingress Tool Transfer
- T1104 Multi-Stage Channels
- T1095 Non-Application Layer Protocol
- T1571 Non-Standard Port
- T1572 Protocol Tunneling
- T1090 Proxy
- T1219 Remote Access Tools
- T1205 Traffic Signaling
- T1102 Web Service

Full list: https://attack.mitre.org/tactics/TA0011/

## Educational Focus

Understand C2 channels and how they can be detected (beaconing, unusual protocols/ports, encrypted traffic to rare destinations).

## Safety

C2 simulation only in isolated labs with proper containment.

## Sources

*Source: [MITRE ATT&CK Tactic TA0011](https://attack.mitre.org/tactics/TA0011/)*
