# 03 — Protocols

## Introduction

A protocol is an agreed set of rules that define the format and meaning of messages exchanged between entities. This module surveys the major protocols you will encounter in enterprise and Internet environments, organised roughly by layer, with emphasis on purpose, key fields, and security relevance.

“All protocols” is unbounded; the focus here is on the protocols that dominate real traffic and security work.

---

## Learning Objectives

- Explain the purpose of major protocols at each layer
- Identify key header fields for Ethernet, IP, TCP, UDP, and common application protocols
- Distinguish connection-oriented vs connectionless behaviour
- Recognise which protocols provide confidentiality, integrity, or authentication
- Relate protocol behaviour to common security controls and attacks (conceptual, defensive view)

---

## Core Concepts by Layer

### Layer 2 — Ethernet and ARP

**Ethernet (IEEE 802.3)**

- Frame structure (simplified): Destination MAC | Source MAC | EtherType | Payload | FCS
- EtherType indicates the upper-layer protocol (e.g. 0x0800 = IPv4, 0x86DD = IPv6, 0x0806 = ARP)
- MTU typically 1500 bytes for standard frames

**ARP (Address Resolution Protocol)**

- Resolves IPv4 address → MAC address on the local link
- Request is broadcast; reply is normally unicast
- Cache can be poisoned (defensive note: static entries, dynamic ARP inspection, monitoring)

```bash
ip neigh show
arp -n
```

### Layer 3 — IP and ICMP

**IPv4**

- Header fields of particular interest: Version, IHL, Total Length, TTL, Protocol, Source Address, Destination Address, Options
- Connectionless, best-effort delivery
- Fragmentation possible (often avoided with PMTUD)

**IPv6**

- 128-bit addresses, simplified header, extension headers
- No broadcast; uses multicast and neighbour discovery (NDP) instead of ARP

**ICMP**

- Diagnostics and error reporting (Echo Request/Reply, Destination Unreachable, Time Exceeded, …)
- Used by `ping` and `traceroute`
- Can be abused for reconnaissance or tunnelling; often filtered selectively

```bash
ping -c 3 8.8.8.8
traceroute example.com
```

### Layer 4 — TCP and UDP

**TCP (Transmission Control Protocol)**

- Connection-oriented, reliable, ordered byte stream
- Ports identify endpoints
- Three-way handshake: SYN → SYN-ACK → ACK
- Sequence and acknowledgement numbers, window, flags (SYN, ACK, FIN, RST, PSH, URG)
- Flow control and congestion control
- Termination: FIN/ACK exchange or RST

**UDP (User Datagram Protocol)**

- Connectionless, minimal header (ports, length, checksum)
- No reliability, ordering, or congestion control in the protocol itself
- Preferred for DNS queries, real-time media, and many tunnelling/VPN designs where the application handles reliability

```bash
ss -tuln
ss -tan
```

### Application and Supporting Protocols

#### DNS (Domain Name System)

- Resolves names ↔ addresses (and other record types)
- UDP/53 for most queries; TCP/53 for zone transfers and large responses
- Recursive vs authoritative resolvers
- Security extensions: DNSSEC (authenticity/integrity of data); still largely cleartext without DoT/DoH

#### DHCP

- Dynamic host configuration (IP address, mask, gateway, DNS servers, …)
- UDP ports 67 (server) / 68 (client)
- Discovery → Offer → Request → Acknowledge sequence
- Rogue DHCP servers are a classic local-network risk

#### HTTP / HTTPS

- Application protocol for the Web (and many APIs)
- HTTP/1.1: text-oriented request/response, headers, methods (GET, POST, PUT, DELETE, …)
- HTTPS = HTTP over TLS (confidentiality, integrity, server authentication)
- HTTP/2 and HTTP/3 introduce framing, multiplexing, and (for HTTP/3) QUIC over UDP

Covered in more depth in module 06.

#### TLS (Transport Layer Security)

- Provides encryption, integrity, and authentication for a byte stream (typically under HTTP, SMTP, etc.)
- Handshake negotiates version, cipher suite, and certificates
- Current best practice: TLS 1.2+ with strong ciphers; TLS 1.0/1.1 deprecated

#### SSH (Secure Shell)

- Secure remote login and tunnelling
- Covered in detail in module 05

#### SMTP / IMAP / POP3

- Mail transfer and access
- Modern deployments expect STARTTLS or implicit TLS
- Authentication mechanisms vary; cleartext AUTH is obsolete

#### NTP

- Clock synchronisation (UDP/123)
- Important for log correlation and certificate validation
- Authenticated NTP variants exist; many deployments still rely on unauthenticated time

#### SNMP

- Network device monitoring and management
- Versions: v1/v2c (community strings — weak), v3 (user-based security)
- Should be restricted and preferably version 3 only

#### Other Notable Protocols

| Protocol | Port (common) | Role |
|----------|---------------|------|
| FTP | 21 (control) | File transfer (cleartext; prefer SFTP/FTPS) |
| SFTP | 22 (via SSH) | Secure file transfer |
| RDP | 3389 | Remote desktop (Windows) |
| SMB | 445 | File/printer sharing (Windows ecosystems) |
| LDAP | 389 / 636 | Directory access (636 = LDAPS) |
| Kerberos | 88 | Ticket-based authentication |
| Syslog | 514 (UDP traditional) | Log shipping |

---

## Protocol Security Properties (Summary View)

| Protocol | Confidentiality | Integrity | Authentication (typical) |
|----------|-----------------|-----------|---------------------------|
| HTTP | No | No | Application-level if any |
| HTTPS (TLS) | Yes | Yes | Server (client optional) |
| Telnet | No | No | Weak (passwords in clear) |
| SSH | Yes | Yes | Host + user (keys/passwords) |
| DNS | No (unless DoT/DoH/DNSSEC) | DNSSEC provides data integrity | Limited |
| ARP | No | No | None (link-local trust) |

---

## Practical Examples

```bash
# Observe protocol usage on a host
ss -tuln
ss -tan | head

# DNS resolution path
dig example.com
dig +trace example.com

# Quick TLS check (if openssl available)
openssl s_client -connect example.com:443 -servername example.com </dev/null 2>/dev/null | head -30
```

---

## Common Mistakes

| Mistake | Better approach |
|---------|-----------------|
| Assuming “encrypted port” means the application is secure | Encryption protects the channel; application logic and authentication still matter |
| Leaving legacy cleartext protocols enabled | Disable Telnet, FTP, SNMPv1/v2c, unauthenticated management |
| Ignoring DNS as a critical dependency | Monitor and protect resolvers; consider DNSSEC and encrypted DNS transport |
| Treating ICMP as pure noise | It is useful for diagnostics and can also carry covert channels |

---

## Best Practices

- Prefer protocols with modern cryptographic protection (SSH, TLS 1.2+, HTTPS).
- Disable or restrict obsolete cleartext services.
- Document which protocols are required on each network segment.
- In labs, practise identifying protocols from port numbers and from packet headers.
- Keep protocol knowledge current — new versions (HTTP/3, TLS 1.3, QUIC) change traffic patterns.

---

## Hands-on Exercise

1. List listening sockets on a lab host and map each to a protocol/service.
2. Perform a DNS lookup with `dig` and identify the query type and response records.
3. Capture a short ARP exchange and an ICMP Echo exchange in a lab; note the Ethernet and IP headers.
4. Compare a cleartext HTTP request with an HTTPS connection using a browser developer tool or `curl -v` (lab targets only).

---

## Review Questions

1. What problem does ARP solve, and at which layer does it operate?
2. What is the main behavioural difference between TCP and UDP?
3. Why is HTTPS preferred over HTTP for sensitive data?
4. Which protocol is primarily responsible for resolving names to addresses?
5. Name two management or monitoring protocols and a security concern for each.

---

## Summary

Protocols define the language of network communication. Mastery of the major Layer 2–4 protocols plus DNS, HTTP/HTTPS, TLS, and SSH covers the majority of traffic and security analysis work. Always map a protocol to its layer, its security properties, and the controls that can protect or monitor it.

---

## Sources

- RFCs for individual protocols (RFC 791 IP, RFC 793 TCP, RFC 768 UDP, RFC 826 ARP, RFC 1034/1035 DNS, RFC 8446 TLS 1.3, etc.)
- IEEE 802.3 / 802.11 standards overviews
- Vendor and operational documentation
