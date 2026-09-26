# Packet Analysis Tools

Used mainly in **Phase-2 Stage 4** and Phase-3 Tracks 3 and 5.

---

## Wireshark

| | |
|--|--|
| **What it is** | Graphical packet capture and protocol analyzer |
| **Used for** | Seeing traffic on a lab interface; applying display filters; following TCP streams; inspecting DNS/HTTP/TLS handshakes in a lab |

**Explanation:** Wireshark captures frames from a network interface (or opens a PCAP file) and decodes protocols layer by layer. Display filters limit what you *see*; capture filters limit what is *recorded*.

**Examples (lab only):**

1. Select your **lab** interface (e.g. host-only `vboxnet0` / `eth1`), start capture.  
2. Browse a lab web app; stop capture.  
3. Display filter examples:
   - `dns`
   - `http`
   - `tcp.port == 80`
   - `ip.addr == 192.168.56.10`
4. Right-click a TCP packet → **Follow → TCP Stream**.

**Safety:** Capture only on interfaces/networks you are authorized to monitor.

---

## tshark

| | |
|--|--|
| **What it is** | Command-line engine of Wireshark |
| **Used for** | Headless capture; scripting; quick PCAP summaries on lab VMs without a GUI |

**Explanation:** Same dissection engine as Wireshark; ideal for servers and automation.

**Examples:**

```bash
# List interfaces
tshark -D

# Capture 30 seconds on lab interface to a file
tshark -i eth0 -a duration:30 -w lab.pcap

# Read first 20 packets from a file
tshark -r lab.pcap -c 20

# Display filter while reading
tshark -r lab.pcap -Y "dns or http"
```

**Project helper:**

```bash
./Codes/Bash/04_network_analysis/tshark_quick_summary.sh lab.pcap
```

---

## Scapy (Python)

| | |
|--|--|
| **What it is** | Python library to sniff, dissect, craft, and send packets |
| **Used for** | Learning packet structure; controlled lab experiments; reading PCAPs programmatically |

**Explanation:** You write short Python programs instead of only using a GUI. Sending packets is powerful — **lab destinations only**.

**Examples:**

```bash
# Educational scripts in the project (edit iface / IP first)
python3 Codes/Python/04_network_analysis/read_pcap_scapy.py
python3 Codes/Python/04_network_analysis/sniff_packet_scapy.py
python3 Codes/Python/04_network_analysis/send_dns_scapy.py   # lab DNS target only
```

**Safety:** Never inject crafted packets onto production or public networks.

---

## tcpdump

| | |
|--|--|
| **What it is** | Classic CLI packet capture on many Linux systems |
| **Used for** | Quick captures when Wireshark/tshark are not installed |

**Example:**

```bash
sudo tcpdump -i eth0 -n -c 50 -w lab_snap.pcap
```

---

## ping

| | |
|--|--|
| **What it is** | ICMP echo request/reply utility |
| **Used for** | Basic reachability check to a **lab** host before deeper work |

**Example:**

```bash
ping -c 3 192.168.56.10
```

Also wrapped in `Codes/Bash/01_lab_setup/check_lab_connectivity.sh`.


---

## Worked lab workflow (end-to-end)

1. Confirm lab interface IP (`ip -brief addr`).
2. Start tshark or Wireshark on that interface only.
3. From the attacker VM, `ping -c 3 <lab-target>` and open the lab web app once.
4. Stop capture; save `lab_session.pcap`.
5. Filter: `icmp or http or dns`.
6. Summarize with:
   ```bash
   ./Codes/Bash/04_network_analysis/tshark_quick_summary.sh lab_session.pcap
   ```
7. Optional: read the same PCAP with Scapy educational scripts under `Codes/Python/04_network_analysis/`.

**Common mistakes**
- Capturing on the wrong interface (home Wi‑Fi instead of host-only).
- Leaving Scapy send scripts pointed at a non-lab IP.
- Interpreting encrypted TLS payloads as “empty” without checking the handshake.
