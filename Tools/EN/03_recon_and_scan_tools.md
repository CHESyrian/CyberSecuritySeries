# Reconnaissance and Scan Tools (Laboratory Only)

Named in Phase-1 as **concepts**; practiced in **Phase-2 Stage 5** and Phase-3 Tracks 1 and 5 — **only against lab targets**.

Unauthorized scanning of systems you do not own can be illegal.

---

## Nmap

| | |
|--|--|
| **What it is** | Network discovery and port/service scanner |
| **Used for** | Host discovery and service/version enumeration on **your lab network** |

**Explanation:** Nmap sends probes and interprets responses to list live hosts and open ports. Timing and probe types affect noise and accuracy. In this curriculum, every target IP must be inside your documented lab range.

**Examples (replace with your lab IP):**

```bash
# Host discovery on a lab range you own
nmap -sn 192.168.56.0/24

# SYN scan + version detection, moderate timing, one lab host
nmap -sS -sV -T3 --top-ports 100 192.168.56.10
```

**Project wrapper (writes dated output under `./nmap_lab_output`):**

```bash
./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
```

---

## ping

| | |
|--|--|
| **What it is** | ICMP reachability tool |
| **Used for** | Confirming a lab VM answers before scanning or capturing |

**Example:**

```bash
ping -c 3 192.168.56.10
```

---

## Python socket helpers (educational)

| | |
|--|--|
| **What they are** | Small scripts using Python’s `socket` module |
| **Used for** | Teaching connect checks and short banner reads — **not** a replacement for Nmap |

**Examples:**

```bash
python3 Codes/Python/05_reconnaissance/lab_port_scan.py 192.168.56.10
python3 Codes/Python/05_reconnaissance/lab_banner_grab.py 192.168.56.10 22
python3 Codes/Python/01_lab_setup/check_lab_ports.py 192.168.56.10
```

Also under `Codes/Python/04_network_analysis/`: `scan_socket_1.py`, `scan_socket_2.py`, `scan_port_scapy.py`.

**Safety:** Pass **lab IPs only**. Do not point these at the public Internet.


---

## Worked lab workflow

1. Write the lab range on paper (e.g. `192.168.56.0/24`).
2. Ping the known target.
3. Run the safe wrapper:
   ```bash
   ./Codes/Bash/05_reconnaissance/safe_lab_nmap.sh 192.168.56.10
   ```
4. Compare with educational socket scan:
   ```bash
   python3 Codes/Python/05_reconnaissance/lab_port_scan.py 192.168.56.10
   ```
5. Banner-grab only a service you expect (e.g. SSH on lab):
   ```bash
   python3 Codes/Python/05_reconnaissance/lab_banner_grab.py 192.168.56.10 22
   ```

**Common mistakes**
- Using `192.168.1.0/24` (home LAN) by habit.
- Aggressive timing (`-T5`) on fragile lab VMs without need.
- Treating educational socket scripts as production scanners.
