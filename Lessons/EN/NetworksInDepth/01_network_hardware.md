# 01 — Network Hardware

## Introduction

Networks are built from physical media, interface cards, and intermediate devices that forward, filter, or transform frames and packets. Understanding the hardware layer helps you reason about performance, failure modes, attack surfaces, and where monitoring or control points can be placed.

This module covers transmission media, network interface cards, hubs, switches, routers, firewalls, wireless access points, and common topologies.

---

## Learning Objectives

- Identify common transmission media and their characteristics
- Explain the role of a NIC and MAC addresses
- Distinguish hubs, switches, and routers by layer and behaviour
- Describe basic switch and router functions relevant to security
- Recognise wireless hardware components and associated risks
- Map simple physical and logical topologies

---

## Core Concepts

### 1. Transmission Media

| Medium | Type | Typical use | Notes |
|--------|------|-------------|-------|
| Twisted-pair copper (Cat5e/Cat6/Cat6a) | Guided | LANs, short–medium runs | RJ-45 connectors; susceptible to EMI if unshielded |
| Coaxial | Guided | Legacy, some broadband | Less common in modern data centres |
| Fibre optic (single-mode / multi-mode) | Guided | Backbones, long distance, high bandwidth | Immune to EMI; different connectors (LC, SC, etc.) |
| Radio (Wi-Fi, cellular, Bluetooth) | Unguided | Mobile, wireless LANs | Shared medium; subject to interference and interception |
| Free-space optical / microwave | Unguided | Point-to-point links | Line-of-sight constraints |

Key properties: bandwidth, latency, distance limits, noise immunity, and whether the medium is shared or dedicated.

### 2. Network Interface Card (NIC)

A NIC (or network adapter) connects a host to a network medium.

- Has a permanent **MAC address** (48-bit hardware address, often burned in; can be spoofed in software).
- Operates primarily at Layer 1 (physical signalling) and Layer 2 (framing, MAC).
- Modern NICs support checksum offload, segmentation offload, multiple queues, and SR-IOV in virtualised environments.
- Drivers and firmware are part of the trusted computing base for network I/O.

```bash
# Linux inspection examples
ip link show
ip addr show
ethtool eth0          # if installed
lshw -class network   # if available
```

### 3. Hubs vs Switches vs Routers

| Device | Primary layer | Behaviour | Security relevance |
|--------|---------------|-----------|--------------------|
| Hub | Layer 1 | Repeats bits to all ports (shared collision domain) | Rare today; traffic visible to all attached hosts |
| Switch | Layer 2 | Forwards frames based on MAC address table | Segments collision domains; CAM table overflow / MAC spoofing are classic concerns |
| Router | Layer 3 | Forwards packets based on IP addresses / routes | Isolates broadcast domains; ACL and routing policy control |

**Switch internals (simplified):**

- Learns source MAC → port mappings by observing frames.
- Forwards known unicast frames only to the destination port.
- Floods unknown unicast, broadcast, and (usually) multicast.
- Maintains a MAC address table (CAM table) with aging.

**Router internals (simplified):**

- Maintains a routing table (directly connected, static, or dynamic).
- Decrements TTL, recalculates checksums, and may perform NAT.
- Applies access-control lists or firewall rules on ingress/egress.

### 4. Firewalls and Security Appliances

- **Host-based firewall** — software on the endpoint (iptables/nftables, Windows Firewall).
- **Network firewall** — dedicated appliance or virtual instance placed at network boundaries.
- **Next-generation / UTM** — may add application awareness, IPS, URL filtering, malware inspection.
- Placement determines what traffic can be inspected and controlled (edge, internal segmentation, host).

### 5. Wireless Hardware

- Access points (APs) bridge wireless clients to a wired network.
- Controllers may manage multiple APs centrally.
- Clients and APs use radio channels in defined bands (2.4 GHz, 5 GHz, 6 GHz).
- Security depends on authentication/encryption (WPA3 preferred; WEP is obsolete and broken).

### 6. Topologies

| Topology | Description | Characteristics |
|----------|-------------|-----------------|
| Bus | Shared backbone | Legacy; single point of failure |
| Star | Devices connect to a central switch/hub | Dominant in modern LANs |
| Mesh | Multiple paths between nodes | Redundancy; used in some wireless and backbone designs |
| Hybrid | Combination | Common in enterprise networks |

Logical topology (how data flows) can differ from physical cabling layout.

### 7. Virtualisation and Cloud Hardware Abstractions

- Virtual switches (vSwitch), virtual NICs, and software-defined networking (SDN) abstract physical hardware.
- Cloud providers expose virtual networks, security groups, and load balancers that map onto underlying physical gear.
- Understanding the physical model still helps reason about bandwidth, latency, and isolation guarantees.

---

## Practical Examples

```bash
# List interfaces and MAC addresses
ip -br link
ip link show

# Show addresses and routes
ip addr
ip route

# Basic link statistics (if ethtool available)
ethtool -S eth0 2>/dev/null | head
```

On a lab switch or router (vendor CLI varies), useful conceptual checks include:

- MAC address table contents
- Interface status and VLAN assignment
- Routing table and ACL counters

---

## Common Mistakes

| Mistake | Why it matters |
|---------|----------------|
| Assuming a switch provides confidentiality | Switches isolate collision domains but do not encrypt; traffic can still be mirrored or intercepted on the path |
| Ignoring physical access | An attacker with physical access to a switch port or cable can often bypass higher-layer controls |
| Treating wireless as “just another cable” | Shared medium, easier interception, different authentication models |
| Overlooking management interfaces | Out-of-band or poorly secured management ports are frequent entry points |

---

## Best Practices

- Prefer switches over hubs; prefer managed switches when visibility and control matter.
- Segment networks with VLANs and Layer-3 boundaries according to trust levels.
- Protect management interfaces (SSH only, ACLs, separate management network).
- Document physical and logical topology; keep diagrams current.
- In labs, practise identifying devices and their roles before applying policy.

---

## Hands-on Exercise

1. On a Linux lab host, list all network interfaces, their MAC addresses, and operational state.
2. Identify which interface is used for your default route.
3. Sketch the path a packet takes from your host to an external IP (host → switch → router/firewall → ISP …).
4. If you have a managed switch in the lab, examine its MAC address table and interface status (authorized access only).

---

## Review Questions

1. What is the primary difference between a hub and a switch?
2. At which OSI layer does a classic router make forwarding decisions?
3. Why does a switch flood frames for unknown unicast destinations?
4. What information does a NIC’s MAC address provide?
5. Name two risks specific to wireless networks compared with wired Ethernet.

---

## Summary

Network hardware defines the physical and data-link foundation of communication. NICs, switches, routers, and firewalls each operate at characteristic layers and introduce distinct security and operational considerations. Solid hardware knowledge makes later protocol and traffic-analysis topics concrete.

---

## Sources

- IEEE 802 standards overview (Ethernet, wireless)
- Vendor documentation for switches and routers (Cisco, Juniper, etc.)
- Linux man pages: `ip(8)`, `ethtool(8)`
