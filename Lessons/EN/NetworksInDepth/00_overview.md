# Networks In Depth — Overview

This series provides a detailed, progressive treatment of computer networking for security practitioners and system administrators. It goes beyond the conceptual networking material in Foundations and the practical analysis stages in Phase-2/Phase-3.

---

## Scope

| Module | Title | Focus |
|--------|-------|-------|
| 01 | Network Hardware | Physical and data-link devices, media, topologies, cabling, NICs, switches, routers, firewalls, wireless |
| 02 | OSI Model in Depth | Seven layers, encapsulation, PDUs, responsibilities, comparison with TCP/IP model |
| 03 | Protocols | Major protocols across layers — Ethernet, ARP, IP, ICMP, TCP, UDP, DNS, HTTP/HTTPS, TLS, DHCP, and others |
| 04 | Ports and Channels | Port numbers, well-known / registered / ephemeral ranges, sockets, multiplexing, common services |
| 05 | SSH and Telnet | Remote access protocols, differences, security properties, keys, practical usage |
| 06 | Requests and Responses | Client–server exchange patterns, HTTP message structure, status codes, headers, methods |
| 07 | Sessions and Cookies | Session state, cookies attributes, session identifiers, fixation/hijacking concepts (defensive view) |
| 08 | Authentication and Authorization | Identity vs permissions, common mechanisms, tokens, AAA, practical patterns |
| 09 | Traffic Analysis and Packets | Packet structure, capture tools, Wireshark/tcpdump concepts, flow analysis, safe lab practice |

All practical work is restricted to **authorized laboratory environments** only. Do not capture, inject, or analyse traffic on networks you do not own or have explicit written permission to test.

---

## Learning Path

1. Start with **01 — Network Hardware** and **02 — OSI Model**. These provide the physical and conceptual foundation.
2. Proceed to **03 — Protocols** and **04 — Ports and Channels**.
3. Study **05 — SSH and Telnet** as concrete remote-access examples.
4. Continue with application-layer topics: **06 Requests/Responses**, **07 Sessions/Cookies**, **08 Authentication/Authorization**.
5. Finish with **09 — Traffic Analysis and Packets**, which integrates earlier knowledge into practical inspection skills.

---

## Prerequisites

- Comfortable with basic Linux command-line usage (see LinuxInDepth or Phase-2 Linux stage).
- Conceptual familiarity with Foundations networking material.
- A lab environment where you can run packet captures and network tools safely (isolated VMs, containers, or dedicated lab network).

---

## Conventions

- Commands with `$` are for a normal user; elevated commands are marked with `sudo` or `#`.
- Packet and protocol examples are illustrative; field values on your system will differ.
- Safety and ethics notes appear throughout. Treat them as mandatory.

---

## Ethical Framing

Deep networking knowledge is used by network engineers, SOC analysts, incident responders, and penetration testers working under authorization. The same knowledge can be misused. This curriculum covers only techniques appropriate inside controlled laboratories and under explicit permission. Unauthorized interception, scanning, or modification of network traffic is illegal and unethical.
