# 04 — Ports and Channels

## Introduction

Ports allow multiple network applications on the same host to share a single IP address. Together with the IP address they form a **socket** endpoint. Understanding port ranges, well-known services, ephemeral ports, and the notion of channels is essential for firewall policy, service identification, and traffic analysis.

---

## Learning Objectives

- Explain the role of port numbers in TCP and UDP
- Distinguish well-known, registered, and ephemeral port ranges
- Define a socket and a connection (5-tuple)
- Recognise common service ports and their security implications
- Describe multiplexing and how many conversations share one interface
- Apply port knowledge to firewall rules and listening-service audits

---

## Core Concepts

### 1. What a Port Is

A port is a 16-bit number (0–65535) that identifies a specific endpoint for TCP or UDP on a host.

- **Source port** — usually chosen by the client (often ephemeral)
- **Destination port** — usually the well-known or registered port of the service

The combination:

```
(IP address, protocol, port)
```

identifies a socket. A TCP connection is uniquely identified by the **5-tuple**:

```
(source IP, source port, destination IP, destination port, protocol)
```

### 2. Port Number Ranges

| Range | Name | Typical use |
|-------|------|-------------|
| 0–1023 | Well-known / system | Privileged services (HTTP 80, HTTPS 443, SSH 22, DNS 53, …). Binding often requires elevated privileges. |
| 1024–49151 | Registered | Registered with IANA for specific applications |
| 49152–65535 | Dynamic / ephemeral | Temporary client ports allocated by the OS |

Exact ephemeral range can be tuned on some systems (`/proc/sys/net/ipv4/ip_local_port_range` on Linux).

### 3. Common Ports (Security-Relevant Subset)

| Port | Protocol | Service | Notes |
|------|----------|---------|-------|
| 20/21 | TCP | FTP data/control | Cleartext; prefer SFTP |
| 22 | TCP | SSH | Encrypted remote access |
| 23 | TCP | Telnet | Cleartext; disable |
| 25 | TCP | SMTP | Mail transfer |
| 53 | TCP/UDP | DNS | Critical infrastructure |
| 67/68 | UDP | DHCP | Local configuration |
| 80 | TCP | HTTP | Cleartext web |
| 110 | TCP | POP3 | Mail retrieval |
| 123 | UDP | NTP | Time |
| 143 | TCP | IMAP | Mail access |
| 161/162 | UDP | SNMP | Monitoring |
| 389 | TCP | LDAP | Directory |
| 443 | TCP | HTTPS | TLS-protected HTTP |
| 445 | TCP | SMB | Windows file sharing |
| 636 | TCP | LDAPS | LDAP over TLS |
| 993 | TCP | IMAPS | IMAP over TLS |
| 995 | TCP | POP3S | POP3 over TLS |
| 3389 | TCP | RDP | Windows remote desktop |
| 3306 | TCP | MySQL | Database |
| 5432 | TCP | PostgreSQL | Database |
| 5900+ | TCP | VNC | Remote display |
| 8080 / 8443 | TCP | Alternate HTTP/HTTPS | Often application servers or proxies |

Always verify what is actually listening; port numbers are conventions, not guarantees.

### 4. Channels and Multiplexing

- A single network interface can support thousands of concurrent TCP connections and UDP conversations because each is distinguished by the 5-tuple (or the UDP 4-tuple plus application context).
- **Multiplexing** — many application streams share the same lower-layer path.
- **Demultiplexing** — the OS delivers incoming segments/datagrams to the correct socket based on port (and address) information.

“Channel” is sometimes used informally for:

- A TCP connection
- A TLS session on top of TCP
- An SSH session or SSH tunnel
- A logical path through a firewall or VPN

### 5. Listening vs Established

```bash
# Listening sockets
ss -tuln
ss -tulpn          # with process info (may need root)

# Established connections
ss -tan
ss -tp
```

States you will see for TCP include LISTEN, SYN-SENT, SYN-RECV, ESTABLISHED, FIN-WAIT, TIME-WAIT, CLOSE-WAIT, etc.

### 6. Firewalls and Port Policy

- **Default-deny** inbound: only explicitly allowed destination ports are open.
- Egress filtering is increasingly important (limit outbound ports and destinations).
- Stateful firewalls track the 5-tuple so that return traffic for permitted outbound connections is allowed automatically.
- Port knocking, single-packet authorisation, and application-layer gateways are advanced patterns; basic host and network firewalls remain the foundation.

---

## Practical Examples

```bash
# What is listening on this host?
ss -tulpn

# Which process owns a given port? (Linux)
sudo ss -tulpn | grep ':22'
sudo lsof -i :22

# Ephemeral port range
cat /proc/sys/net/ipv4/ip_local_port_range

# Simple connectivity check
nc -zv example.com 443
curl -I https://example.com
```

---

## Common Mistakes

| Mistake | Risk |
|---------|------|
| Assuming a closed port means the service is absent | Service may listen on another interface or port; or be filtered |
| Opening wide port ranges “temporarily” | Forgotten rules become permanent attack surface |
| Relying only on port numbers for identification | Attackers can run services on unexpected ports; always correlate with process and certificate data |
| Ignoring outbound ports | Malware and exfiltration often use common outbound ports (80/443) or high ports |

---

## Best Practices

- Inventory listening ports regularly on critical hosts.
- Apply host-based and network-based filters with a default-deny posture.
- Prefer non-default ports only when combined with strong authentication and monitoring — security through obscurity alone is insufficient.
- Document required services and their ports per network segment.
- In labs, practise mapping ports → processes → configuration files.

---

## Hands-on Exercise

1. List all listening TCP and UDP sockets on a lab machine and identify the owning process where possible.
2. Determine the ephemeral port range on your system.
3. From a client, open an HTTPS connection and observe the source (ephemeral) port and destination port 443 with `ss` or a capture.
4. Write a minimal firewall rule set (conceptually or with `nftables`/`iptables` in a lab) that allows SSH and HTTPS inbound and DNS outbound.

---

## Review Questions

1. What is the numerical range of well-known ports?
2. What five pieces of information uniquely identify a TCP connection?
3. Why do client connections usually use high-numbered source ports?
4. What does a socket in the LISTEN state represent?
5. Why is filtering only on destination port numbers incomplete for modern threats?

---

## Summary

Ports enable multiplexing of many services and conversations on shared IP addresses. Knowing the standard ranges, common service ports, and the 5-tuple model is fundamental for service discovery, firewall design, and traffic analysis. Always verify actual listeners and processes rather than trusting port numbers alone.

---

## Sources

- IANA Service Name and Transport Protocol Port Number Registry
- Linux man pages: `ss(8)`, `lsof(8)`, `ip(8)`
- Firewall documentation (nftables, iptables, cloud security groups)
