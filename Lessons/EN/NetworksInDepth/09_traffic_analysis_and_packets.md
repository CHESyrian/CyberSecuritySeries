# 09 — Traffic Analysis and Packets

## Introduction

Packet-level visibility turns abstract protocol knowledge into concrete evidence. Traffic analysis is used for troubleshooting, performance monitoring, threat detection, and incident response. This module covers packet structure, capture tools, basic analysis workflows, and the strict requirement to work only in authorized environments.

---

## Learning Objectives

- Describe the nested structure of a typical Ethernet + IP + TCP/UDP packet
- Capture traffic safely with `tcpdump` and inspect it with Wireshark or `tshark`
- Apply display and capture filters effectively
- Extract high-value fields (addresses, ports, flags, payloads when appropriate)
- Recognise common patterns (handshakes, DNS queries, TLS ClientHello, cleartext credentials)
- Follow an ethical, minimal-impact capture methodology in lab settings

---

## Core Concepts

### 1. Packet Structure (Review of Encapsulation)

A common IPv4 TCP packet on Ethernet:

```
[ Ethernet header ]
    Dest MAC | Src MAC | EtherType (0x0800)
[ IPv4 header ]
    Version, IHL, TOS/DSCP, Total Length, ID, Flags, Fragment Offset,
    TTL, Protocol (6=TCP), Header Checksum, Src IP, Dst IP, Options
[ TCP header ]
    Src Port, Dst Port, Seq, Ack, Data Offset, Flags, Window,
    Checksum, Urg Ptr, Options
[ Payload ]
    Application data (HTTP, TLS records, …)
[ Ethernet FCS ]
```

UDP replaces the TCP header with a shorter UDP header (ports, length, checksum).

### 2. Capture Points and Visibility

| Capture location | What you typically see |
|------------------|------------------------|
| Host interface | Traffic to/from that host (and sometimes broadcast/multicast) |
| Switch SPAN/mirror port | Copy of traffic from selected ports or VLANs |
| Network TAP | Passive copy of a link |
| Firewall / IDS sensor | Traffic crossing that boundary |
| Cloud VPC flow logs | Metadata (not full packets) in many offerings |

Encryption (TLS, VPN, SSH) limits payload visibility; metadata (addresses, ports, sizes, timing, TLS handshake fields) often remains useful.

### 3. Tools

**tcpdump** — command-line capture and light analysis (libpcap).

```bash
# Capture on an interface, write to file
sudo tcpdump -i eth0 -w capture.pcap

# Capture only TCP port 80, print to screen
sudo tcpdump -i eth0 -nn tcp port 80

# Read a saved file
tcpdump -r capture.pcap -nn
```

**Wireshark / tshark** — full-featured analysis (GUI and CLI).

- Display filters (Wireshark) vs capture filters (pcap/BPF syntax — different languages).
- Follow TCP stream, Expert Info, protocol dissectors, export objects.

**Other useful tools**

- `ss`, `netstat` — socket state (not full packets)
- `tshark` — scriptable Wireshark engine
- Zeek / Suricata — network security monitoring (higher-level events)
- Cloud flow logs, NetFlow/IPFIX — metadata summaries

### 4. Capture Filters (BPF) vs Display Filters

**Capture filter** (limits what is stored — efficient):

```
host 192.0.2.10
net 192.0.2.0/24
port 53
tcp port 443
icmp
```

**Display filter** (Wireshark — after capture):

```
ip.addr == 192.0.2.10
tcp.port == 443
http.request.method == "GET"
dns.qry.name contains "example"
tls.handshake.type == 1
```

### 5. Analysis Workflow (Practical)

1. **Define the question** — connectivity failure? Slow transfer? Suspected cleartext secret? DNS behaviour?
2. **Choose capture point and filter** — minimise volume and privacy impact.
3. **Capture for a bounded time** or until the event of interest occurs.
4. **Inspect metadata first** — conversations, endpoints, ports, volumes, timing.
5. **Drill into selected streams** — TCP handshake, retransmissions, application headers.
6. **Document findings** and securely delete captures that contain sensitive data when no longer needed.

### 6. Patterns Worth Recognising

| Pattern | What to look for |
|---------|------------------|
| TCP three-way handshake | SYN, SYN-ACK, ACK with matching seq/ack |
| TCP termination | FIN/ACK sequence or RST |
| DNS query/response | UDP/53, query name, response codes and RRs |
| TLS ClientHello / ServerHello | SNI, cipher suites, certificate messages |
| HTTP request line | Method, path, Host header (cleartext only) |
| ARP request/reply | Who-has / is-at on local segment |
| Retransmissions / duplicate ACKs | Performance or loss issues |

### 7. Ethics, Law, and Lab Discipline

- Capture **only** on networks and systems you own or for which you have **explicit written authorisation**.
- Prefer isolated lab networks and synthetic traffic.
- Treat captures as sensitive: they may contain credentials, personal data, or session tokens.
- Minimise retention; encrypt storage if retention is required.
- Unauthorised interception of communications is illegal in most jurisdictions.

---

## Practical Examples

```bash
# Short HTTP capture (lab interface name may differ)
sudo tcpdump -i eth0 -nn -c 50 tcp port 80 -w http-lab.pcap

# DNS only
sudo tcpdump -i eth0 -nn port 53 -c 20

# Read with tshark if available
tshark -r http-lab.pcap -q -z endpoints
tshark -r http-lab.pcap -Y "http.request" -T fields -e http.host -e http.request.uri
```

Wireshark GUI workflow:

1. Open the pcap.
2. Use display filter `tcp.flags.syn == 1 and tcp.flags.ack == 0` to find connection starts.
3. Right-click a packet → Follow → TCP Stream.
4. Examine the Statistics menus (Conversations, Endpoints, Protocol Hierarchy).

---

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Capturing without a filter on a busy link | Huge files, missed events, privacy over-collection |
| Confusing capture filters with display filters | Empty captures or unexpected results |
| Analysing production traffic without authorisation | Legal and ethical violation |
| Leaving captures with credentials on shared storage | Secondary data breach |
| Looking only at payload and ignoring timing/volume | Missed C2 beacons or exfiltration patterns |

---

## Best Practices

- Always start with a written or clearly understood authorisation scope.
- Use the narrowest filter that still answers the question.
- Prefer metadata and handshake analysis when payloads are encrypted.
- Correlate packet data with host logs, firewall logs, and process information.
- Document the capture environment (interface, filter, time window, purpose).
- In training, use public pcaps or self-generated lab traffic rather than real user data.

---

## Hands-on Exercise

1. Generate a few DNS queries and an HTTP request on a lab network; capture them with `tcpdump` using appropriate filters.
2. Open the capture in Wireshark or `tshark` and identify Ethernet, IP, and transport headers for one packet.
3. Follow a TCP stream for a cleartext exchange and locate the request line or DNS query name.
4. Write a display filter that shows only DNS responses containing a specific name.
5. List the conversations (IP pairs) present in the capture and the ports involved.

---

## Review Questions

1. What information is contained in the 5-tuple of a TCP packet?
2. Why might you choose a capture filter instead of capturing everything and filtering later?
3. What is the difference between a capture filter and a Wireshark display filter?
4. Name three fields you can still observe when application data is protected by TLS.
5. What is the primary ethical rule for packet capture?

---

## Summary

Traffic analysis connects protocol theory to observable behaviour on the wire. Understanding packet structure, using capture and display filters correctly, and following a disciplined, authorised workflow enables effective troubleshooting and defensive investigation. Encryption limits payload visibility but leaves valuable metadata; host and network context complete the picture.

---

## Sources

- tcpdump / libpcap documentation
- Wireshark User’s Guide and display filter reference
- RFCs for IP, TCP, UDP (header formats)
- Legal and organisational policy on monitoring (local jurisdiction and employer rules)
