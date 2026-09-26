# Stage 4: Network Analysis and Packet Crafting

## Why This Stage Matters

Almost every security activity eventually touches the network. Reconnaissance, exploitation, command-and-control, data movement, and defensive detection all leave traces in packets. The ability to capture, read, and interpret network traffic is therefore one of the highest-leverage practical skills you can develop.

Phase-0 and Phase-1 gave you the conceptual models (OSI, TCP/IP, common protocols).  
This stage gives you the practical ability to *see* that traffic and to craft simple packets inside a laboratory for learning purposes.

---

## Learning Objectives

By the end of this stage you will be able to:

- Capture live traffic and save it to PCAP files using Wireshark and tshark
- Open and navigate PCAPs confidently
- Apply display and capture filters for common protocols
- Identify the main fields of Ethernet, IP, TCP, UDP, and DNS packets
- Use Scapy for basic packet inspection and controlled crafting inside the lab
- Relate observed traffic back to the processes and services you examined in earlier stages
- Follow strict safety rules so that packet crafting never leaves the laboratory

---

## Safety Checkpoint

**Packet capture** is generally safe when performed on interfaces you control.  
**Packet crafting and injection** must be limited to laboratory networks you own.  

Never inject crafted packets onto a production network or the public internet.  
Never capture traffic on networks for which you do not have authorization.

All examples below assume you are working inside the isolated lab created in Stage 1.

---

## 1. The Role of Network Analysis

Network analysis answers questions such as:

- What is talking to what?
- Which protocols and ports are in use?
- Are there unexpected connections or cleartext credentials?
- Does the traffic match what the application or service should be doing?
- Can I reconstruct a conversation (for example an HTTP request/response)?

Defenders use the same skills for detection and incident response. Attackers (in authorized tests) use them to understand the environment. Learning both perspectives makes you stronger on either side.

---

## 2. Wireshark and tshark

**Wireshark** is the graphical standard for packet analysis.  
**tshark** is its command-line counterpart — ideal for scripting and remote or headless environments.

### Basic capture workflow (conceptual)

1. Choose the correct network interface (the lab interface that can see the traffic of interest).
2. Start a capture.
3. Generate the traffic you want to study (browse a lab web application, perform a lab scan, etc.).
4. Stop the capture and save it as a PCAP/PCAPNG file.
5. Apply display filters to focus on the interesting packets.

### Useful tshark examples (lab only)

```bash
# List interfaces
tshark -D

# Capture on a specific interface for 30 seconds
tshark -i eth0 -a duration:30 -w lab_capture.pcap

# Read an existing PCAP and show a short summary
tshark -r lab_capture.pcap -c 20

# Display filter example: only DNS
tshark -r lab_capture.pcap -Y "dns"
```

---

## 3. Display Filters You Will Use Constantly

Wireshark/tshark display filters let you hide noise and keep signal.

| Filter | Meaning |
|--------|---------|
| `dns` | DNS traffic |
| `http` | HTTP traffic |
| `tcp.port == 80` | TCP port 80 |
| `ip.addr == 192.168.56.10` | Traffic to or from a specific host |
| `tcp.flags.syn == 1 && tcp.flags.ack == 0` | SYN packets (start of TCP handshake) |
| `http.request` | HTTP requests only |
| `frame contains "password"` | Frames containing the string (use carefully) |

Learn a few filters well rather than trying to memorize dozens. The Wireshark expression builder and official documentation are excellent references.

---

## 4. Reading Common Protocol Headers

When you open a packet, practice identifying:

**Ethernet**
- Source and destination MAC addresses

**IP**
- Source and destination IP addresses
- Protocol number (6 = TCP, 17 = UDP, 1 = ICMP)

**TCP**
- Source and destination ports
- Sequence and acknowledgment numbers
- Flags (SYN, ACK, FIN, RST, PSH, URG)
- Window size

**UDP**
- Source and destination ports
- Length

**DNS**
- Query name
- Query type (A, AAAA, MX, etc.)
- Response codes and answers

You do not need to memorize every field. The goal is to be able to answer “who is talking, on what ports, and what is the high-level purpose of this conversation?”

---

## 5. Scapy for Inspection and Controlled Crafting

Scapy is a powerful Python library for packet manipulation. The project already contains several educational Scapy scripts under `Codes/Python/04_network_analysis/`. This stage teaches you the mindset for using them safely.

### Reading packets

```python
from scapy.all import rdpcap, sniff

packets = rdpcap("lab_capture.pcap")
packets[0].show()          # detailed view of first packet
packets[0].summary()       # one-line summary
```

### Simple sniffing (lab interface only)

```python
from scapy.all import sniff

pkts = sniff(iface="eth0", filter="udp port 53", count=5)
pkts.summary()
```

### Controlled crafting (lab targets only)

Crafting is useful for understanding how protocols work and for testing how a lab service reacts. Always restrict destination addresses to systems inside your laboratory.

Conceptual example (DNS query to a lab resolver or public resolver from the attacker VM only for learning):

```python
from scapy.all import IP, UDP, DNS, DNSQR, sr1

packet = IP(dst="8.8.8.8")/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname="example.com"))
response = sr1(packet, timeout=2)
if response:
    response.show()
```

**Safety rule:** If a Scapy script contains a destination IP, verify that IP belongs to a machine you own or have explicit permission to test before running it.

---

## 6. Relating Packets to Hosts and Processes

Network analysis becomes far more powerful when combined with the host skills from Stages 2 and 3:

- On the host: `ss -tulnp` or `Get-NetTCPConnection` shows which process owns a port.
- In the PCAP: you see the actual packets that process is sending and receiving.
- Together you can answer “this process opened that connection and transferred this data.”

This correlation is a core technique for both incident response and authorized testing.

---

## 7. Common Analysis Workflows in the Lab

**Workflow A — Understand a web request**
1. Start a capture on the attacker or target interface.
2. Browse a lab web application (DVWA, Juice Shop, etc.).
3. Stop the capture.
4. Filter on `http` or the relevant TCP port.
5. Follow the TCP stream to see the reconstructed request and response.

**Workflow B — Observe name resolution**
1. Capture traffic.
2. Generate DNS activity (visit a site, use `dig` or `nslookup` against a lab or public resolver).
3. Filter on `dns` and examine queries and answers.

**Workflow C — Map conversations**
1. Open a PCAP.
2. Use Statistics → Conversations (in Wireshark) or tshark conversation options.
3. Identify the heaviest talkers and the ports they use.

---

## Common Mistakes

| Mistake | Consequence | Better practice |
|---------|-------------|-----------------|
| Capturing on the wrong interface | Empty or irrelevant PCAP | Confirm interface with `ip addr` / `tshark -D` first |
| Capturing without a filter on a busy network | Huge files, hard to analyze | Start with a capture filter when possible |
| Injecting crafted packets outside the lab | Legal and operational risk | Restrict destinations to lab IPs only |
| Looking only at packet list without following streams | Miss application-level content | Use “Follow TCP Stream” regularly |
| Assuming cleartext protocols are rare | Miss credentials or sensitive data | Always check HTTP, FTP, Telnet, etc. in lab traffic |

---

## Best Practices

- Save PCAPs with descriptive names and dates (`lab_http_juice_2026-09-25.pcap`).
- Keep a short personal list of your most-used display filters.
- When learning, capture first, filter later. As you gain experience, use capture filters to reduce volume.
- Correlate host process information with packet data whenever possible.
- Treat every crafted packet as something that must stay inside the lab boundary.
- Snapshot VMs before installing new capture or crafting tools.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/Python/04_network_analysis/` | Full Scapy / socket suite (sniff, PCAP read, send, scan demos) |
| `Codes/Bash/04_network_analysis/tshark_quick_summary.sh` | Quick protocol hierarchy + packet summary for a PCAP |

```bash
# Existing educational Scapy examples
python3 Codes/Python/04_network_analysis/read_pcap_scapy.py
python3 Codes/Python/04_network_analysis/sniff_packet_scapy.py   # edit iface first

# tshark helper
chmod +x Codes/Bash/04_network_analysis/tshark_quick_summary.sh
./Codes/Bash/04_network_analysis/tshark_quick_summary.sh lab_capture.pcap
```

See `Codes/Python/04_network_analysis/` for the full script list. Always set interface names and destination IPs to lab values only.


Inside your laboratory:

1. Start a packet capture on the appropriate lab interface.
2. From the attacker VM, generate some traffic toward a target (HTTP request to a lab web app, DNS query, or simple ping).
3. Stop the capture and open it in Wireshark or inspect it with tshark.
4. Apply a display filter to isolate the traffic you generated.
5. Identify source/destination IPs, ports, and the protocol.
6. (Optional) Use one of the existing Scapy scripts in `Codes/Python/04_network_analysis/` or write a minimal script to send a single ICMP or DNS packet to a lab target and observe the response.
7. Record the PCAP name, filters used, and key observations in your lab notebook.

**Success criteria:** You have a PCAP that contains the traffic you generated, you can filter it, and you can explain the main header fields of at least one packet.

---

## Review Questions

1. What is the difference between a capture filter and a display filter?
2. Why must packet injection be restricted to laboratory networks?
3. Name three fields you would examine in a TCP packet to understand a connection.
4. How can host-level tools (`ss`, PowerShell networking cmdlets) improve the value of a PCAP analysis?
5. What does “Follow TCP Stream” help you see that the packet list alone may not?
6. Give one practical reason to prefer tshark over Wireshark in certain situations.

---

## Summary

- Network analysis turns abstract protocol knowledge into visible, interpretable evidence.
- Wireshark and tshark are the standard tools for capture and inspection; Scapy adds programmable inspection and controlled crafting.
- Display filters, stream following, and header literacy are the core daily skills.
- Always correlate packets with the processes and services that produce them.
- Safety boundaries are non-negotiable: capture only where authorized, craft only inside the lab.
- With host inspection (Stages 2–3) and network visibility (this stage) in place, you are ready to perform controlled reconnaissance and enumeration against laboratory targets.

**Next stage:** Reconnaissance and Enumeration (Authorized) — discovering live systems and services inside the lab boundary.
