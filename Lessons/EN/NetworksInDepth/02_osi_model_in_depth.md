# 02 — OSI Model in Depth

## Introduction

The Open Systems Interconnection (OSI) model is a conceptual framework that divides network communication into seven layers. It is not a protocol suite itself; it is a teaching and design tool that helps locate where functions, headers, and problems belong.

This module explains each layer’s responsibility, the protocol data units (PDUs), encapsulation/decapsulation, and how the model relates to the practical TCP/IP stack used on the Internet.

---

## Learning Objectives

- Name and order the seven OSI layers
- State the primary responsibility of each layer
- Describe encapsulation and the PDUs at each layer
- Map common protocols onto OSI layers
- Compare OSI with the TCP/IP (Internet) model
- Use the model to reason about troubleshooting and security controls

---

## Core Concepts

### 1. The Seven Layers

| Layer | Name | PDU name (common) | Primary concern |
|-------|------|-------------------|-----------------|
| 7 | Application | Data | Application services and semantics |
| 6 | Presentation | Data | Syntax, encoding, encryption (conceptual) |
| 5 | Session | Data | Dialog control, sessions (conceptual) |
| 4 | Transport | Segment (TCP) / Datagram (UDP) | End-to-end delivery, ports, reliability options |
| 3 | Network | Packet | Logical addressing and routing |
| 2 | Data Link | Frame | Node-to-node delivery, MAC, error detection on link |
| 1 | Physical | Bit / Symbol | Signalling, media, connectors, encoding |

Memory aid (bottom to top): **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way  
(Physical, Data Link, Network, Transport, Session, Presentation, Application)

### 2. Encapsulation and Decapsulation

When an application sends data:

1. Application data is passed down the stack.
2. Each layer may add a **header** (and sometimes a trailer).
3. The unit becomes a frame on the wire.
4. At the receiving host the process is reversed: each layer removes its header and passes the payload upward.

```
Application data
  → [HTTP headers + data]
    → [TCP header + HTTP]
      → [IP header + TCP]
        → [Ethernet header + IP + FCS]
```

Intermediate devices typically process only the layers they need:

- Switch → Layer 2 (and sometimes limited Layer 3/4 features)
- Router → Layer 3 (and often ACLs that inspect higher layers)
- Firewall / IDS → may inspect up to Layer 7

### 3. Layer-by-Layer Detail

#### Layer 1 — Physical

- Electrical, optical, or radio signalling
- Connectors, pinouts, voltage levels, modulation
- No concept of addresses or frames — only bits/symbols
- Examples: copper signalling, fibre optics, Wi-Fi radio

#### Layer 2 — Data Link

- Framing, physical addressing (MAC), media access control
- Error detection (CRC/FCS)
- Local delivery between devices on the same link or broadcast domain
- Examples: Ethernet (IEEE 802.3), Wi-Fi (802.11), PPP
- Sublayers often discussed: LLC and MAC

#### Layer 3 — Network

- Logical addressing (IP addresses)
- Routing between networks
- Fragmentation and reassembly (IPv4)
- Examples: IPv4, IPv6, ICMP, IPSec (network mode)

#### Layer 4 — Transport

- End-to-end communication between processes (ports)
- Optional reliability, ordering, flow control (TCP)
- Lightweight, connectionless alternative (UDP)
- Examples: TCP, UDP, SCTP

#### Layer 5 — Session

- Establishing, managing, and terminating dialogs
- In practice many session functions are absorbed by the application or transport layer
- Examples of concepts: RPC session semantics, NetBIOS sessions (historical)

#### Layer 6 — Presentation

- Data representation, encryption, compression (conceptual placement)
- In real stacks, TLS is often described as sitting between transport and application
- Character encoding, serialisation formats

#### Layer 7 — Application

- Application protocols and user-facing services
- Examples: HTTP, HTTPS, DNS, SMTP, FTP, SSH, DHCP

### 4. TCP/IP Model Comparison

The practical Internet model is usually described with four (sometimes five) layers:

| TCP/IP layer | Rough OSI mapping | Examples |
|--------------|-------------------|----------|
| Application | 5–7 | HTTP, DNS, SSH, SMTP |
| Transport | 4 | TCP, UDP |
| Internet | 3 | IP, ICMP |
| Link | 1–2 | Ethernet, Wi-Fi, PPP |

Security controls and troubleshooting are often discussed with a hybrid vocabulary (“Layer 3 ACL”, “Layer 7 firewall”, “TLS at Layer 4/5/6/7”).

### 5. Using the Model for Security and Troubleshooting

| Symptom / control | Typical layer focus |
|-------------------|---------------------|
| Link lights, cable, speed/duplex | 1 |
| MAC table, VLAN, ARP | 2 |
| Routing, traceroute, ICMP unreachable | 3 |
| Port reachability, TCP handshake | 4 |
| Certificate errors, HTTP status, application auth | 7 (and TLS) |
| Packet filter / stateful firewall | 3–4 (sometimes 7) |
| Application-layer gateway / WAF | 7 |

---

## Practical Examples

```bash
# Observe layers indirectly
ip link show          # Layer 1/2 interface state
ip addr show          # Layer 3 addresses
ss -tuln              # Layer 4 listening sockets
curl -v https://example.com/   # Application + TLS
```

When capturing packets (authorized lab only), you will see the nested headers that correspond to encapsulation:

- Ethernet header (L2)
- IP header (L3)
- TCP/UDP header (L4)
- Application payload (L7)

---

## Common Mistakes

| Mistake | Clarification |
|---------|---------------|
| Treating OSI as a strict implementation | Real stacks are TCP/IP-oriented; OSI is a reference model |
| Placing TLS rigidly at one layer | TLS is best understood as providing security services between transport and application |
| Assuming Layer 2 isolation equals security | VLANs and switches reduce exposure but do not replace authentication or encryption |
| Ignoring lower layers when debugging “application” problems | Many application failures originate in DNS, routing, or TCP |

---

## Best Practices

- When troubleshooting, start from the bottom (link) and move up unless evidence points higher.
- When designing controls, decide which layer the control can reliably see and enforce.
- Use consistent terminology in documentation (state whether you mean OSI or TCP/IP numbering).
- In labs, practise mapping every header you see in a capture back to a layer and a purpose.

---

## Hands-on Exercise

1. Draw the seven OSI layers and list two protocols or technologies for each of layers 1–4 and 7.
2. Capture a short HTTP or DNS exchange in a lab (authorized environment) and identify the Ethernet, IP, and TCP/UDP headers.
3. Explain why a switch does not need to understand IP addresses to forward most frames.
4. Map the following to a primary layer: ARP, TCP SYN, HTTP GET, ICMP Echo Request, 802.11 association.

---

## Review Questions

1. What is the PDU called at Layer 3? At Layer 4 for TCP?
2. Which layer is responsible for MAC addressing?
3. Why do intermediate routers normally not examine TCP port numbers for basic forwarding?
4. How does the TCP/IP model differ from the OSI model in structure?
5. Give one example of a security control that operates primarily at Layer 3–4 and one at Layer 7.

---

## Summary

The OSI model organises network functions into seven layers and clarifies encapsulation. Real networks implement the TCP/IP suite, but OSI vocabulary remains standard for teaching, design, and security discussions. Mapping protocols, devices, and controls onto layers improves both troubleshooting and defensive architecture.

---

## Sources

- ISO/IEC 7498 (OSI reference model concepts)
- RFC 1122 / RFC 1123 (Internet host requirements — practical layering)
- Standard networking textbooks and vendor architecture documents
