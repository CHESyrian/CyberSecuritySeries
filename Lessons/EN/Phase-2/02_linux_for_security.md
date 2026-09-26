# Stage 2: Linux for Security Practitioners

## Why This Stage Matters

Most security tools run on Linux. Most servers you will encounter in professional work run Linux. The ability to move confidently on a Linux system — inspect processes, examine network connections, read logs, and write small helper scripts — is a core practical skill.

Phase-0 introduced the *concepts* (filesystem, permissions, processes, services, logs, SSH, Bash).  
This stage turns those concepts into *working habits* you will use repeatedly in later stages and in real laboratory exercises.

---

## Learning Objectives

By the end of this stage you will be able to:

- Navigate the filesystem and inspect permissions with confidence
- List and interpret running processes and their network connections
- Examine listening ports and active sockets
- Read and filter common log files
- Use basic text-processing tools (`grep`, `awk`, `cut`, `sort`, `uniq`) for security-relevant tasks
- Write small, safe Bash scripts for repetitive investigation steps
- Apply the principle of least privilege in daily lab work

---

## Safety Checkpoint

All commands in this stage are intended to be run **inside your isolated laboratory** (the attacker VM or a target VM you own).  
Do not run investigative or scanning commands against systems outside your lab.

---

## 1. Working Comfortably on the Command Line

You will spend most of your time in a terminal. Useful habits:

- Use tab completion.
- Use the up-arrow to recall previous commands.
- Learn `man <command>` or `<command> --help` when you need details.
- Prefer relative paths when you are already inside a directory; use absolute paths when clarity matters.

Essential navigation and inspection commands:

| Command | Purpose |
|---------|---------|
| `pwd` | Print current directory |
| `ls -la` | List files with details and hidden files |
| `cd <dir>` | Change directory |
| `file <name>` | Identify file type |
| `stat <name>` | Detailed metadata (permissions, owner, timestamps) |
| `which <cmd>` | Locate an executable |
| `find /path -name "*.log"` | Search for files by name (use carefully) |

---

## 2. Permissions in Practice

Recall the model: owner / group / others × read / write / execute.

Useful commands:

```bash
ls -l filename          # view permissions
stat filename           # more detailed view
id                      # see your current UID, GID, and groups
whoami                  # current username
```

When you create files or scripts in the lab, set permissions deliberately:

```bash
chmod 644 notes.txt     # owner read/write, others read
chmod 755 script.sh     # owner full, others read+execute
chmod 600 secret.txt    # owner only
```

**Security habit:** Avoid giving world-writable permissions (`chmod 777`) unless you have a very specific reason and understand the risk.

---

## 3. Processes and What They Are Doing

A process is a running program. For security work you frequently need to answer:

- What is running?
- Who is it running as?
- What files or network connections does it have open?

Core commands:

```bash
ps aux                  # snapshot of all processes
ps aux | grep <name>    # filter by name
top                     # live view (press q to quit)
htop                    # improved live view (if installed)
```

To see network connections and listening ports belonging to processes:

```bash
ss -tulnp               # listening TCP/UDP sockets with process info
ss -tp                  # established TCP connections with process info
lsof -i                 # list open Internet sockets (if lsof is installed)
lsof -p <PID>           # files and sockets opened by a specific process
```

**Reading the output of `ss -tulnp`:**

- `State` = LISTEN means the process is waiting for connections (a service).
- Local address `0.0.0.0` or `*` means it is listening on all interfaces.
- Local address `127.0.0.1` means it is listening only on the loopback interface (local only).

These distinctions become important when you later assess attack surface.

---

## 4. Network Inspection from the Host

Beyond process-centric tools, you often want a quick picture of the system’s network posture:

```bash
ip addr                 # IP addresses and interfaces
ip route                # routing table
ss -s                   # summary of socket statistics
ping -c 3 <target>      # basic reachability (lab targets only)
```

**Safety note:** Restrict active probes (`ping`, any port checks, etc.) to addresses that belong to your laboratory virtual machines.

---

## 5. Reading Logs

Logs are one of the primary sources of truth for both defenders and investigators.

Common locations on many distributions:

| Path | Typical content |
|------|-----------------|
| `/var/log/syslog` or `/var/log/messages` | General system messages |
| `/var/log/auth.log` or `/var/log/secure` | Authentication attempts |
| `/var/log/kern.log` | Kernel messages |
| `journalctl` | systemd journal (modern distributions) |

Useful reading patterns:

```bash
# Last 50 lines of a log
tail -n 50 /var/log/auth.log

# Follow a log in real time
tail -f /var/log/syslog

# Search for a term
grep -i "failed" /var/log/auth.log

# systemd journal examples
journalctl -u ssh -n 50
journalctl --since "1 hour ago"
```

When you are investigating a lab target, logs often reveal what services are running, whether authentication is being attempted, and whether errors are occurring.

---

## 6. Text Processing for Security Tasks

Security work frequently involves filtering and summarizing text (logs, command output, configuration files).

Essential tools:

| Tool | Typical use |
|------|-------------|
| `grep` | Find lines matching a pattern |
| `cut` | Extract columns by delimiter |
| `awk` | More flexible column and pattern processing |
| `sort` | Sort lines |
| `uniq` | Remove or count duplicates |
| `wc` | Count lines, words, bytes |
| `head` / `tail` | First or last lines |

Example pattern (conceptual):

```bash
# Count unique IP addresses that appeared in a log field
grep "Failed password" /var/log/auth.log | awk '{print $NF}' | sort | uniq -c | sort -nr
```

You do not need to memorize complex one-liners yet. The goal is to become comfortable combining simple tools with pipes (`|`).

---

## 7. Small, Safe Bash Scripts

A Bash script is a text file that starts with a shebang and contains commands.

Minimal safe template:

```bash
#!/usr/bin/env bash
set -euo pipefail

# Simple example: list listening TCP ports
echo "Listening TCP sockets:"
ss -tlnp
```

Good habits for educational and lab scripts:

- Start with `#!/usr/bin/env bash`
- Use `set -euo pipefail` so the script stops on errors and undefined variables
- Add comments that explain *why*, not only *what*
- Make the script executable: `chmod 755 script.sh`
- Prefer explicit paths and clear variable names
- Never hard-code real credentials or production secrets

Scripts are excellent for automating repetitive lab checks (for example, “show me all listening ports and the last 20 authentication failures”).

---

## 8. Privilege Awareness

- Prefer working as a normal user.
- Use `sudo` only when a command genuinely requires elevated privileges.
- Understand that any process you start inherits your privileges (or the privileges of the account you escalate to).
- In the lab it is tempting to stay logged in as root. Resist that habit; it hides problems that appear only under normal user accounts.

```bash
id                  # confirm who you are
sudo -l             # see what you are allowed to run with sudo (if configured)
```

---

## Common Mistakes

| Mistake | Consequence | Better practice |
|---------|-------------|-----------------|
| Running everything as root | Hides permission issues; increases blast radius of mistakes | Use a normal user + sudo only when needed |
| Searching the entire filesystem with `find /` without limits | Can be slow and generate huge output | Narrow the starting path and add filters |
| Ignoring the difference between LISTEN on `0.0.0.0` vs `127.0.0.1` | Misunderstands exposure | Always note the bind address |
| Copy-pasting complex commands without understanding them | Unexpected side effects | Break commands into pieces and test |
| Leaving world-writable scripts or files | Creates unnecessary risk even in a lab | Set deliberate permissions |

---

## Best Practices

- Keep a short personal cheat-sheet of the commands you use most.
- After any major change to a lab VM, re-check listening ports and running processes.
- When reading logs, start broad (`tail`, `journalctl -n`) then narrow with `grep` or time filters.
- Treat every script you write as something that might later be run by someone else — clarity matters.
- Snapshot your attacker VM before experimenting with new packages or configuration changes.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/Bash/02_linux_security/host_inspect.sh` | Identity, listening sockets, top processes, recent auth lines |
| `Codes/Bash/02_linux_security/failed_logons_summary.sh` | Summarize failed auth attempts by source IP |
| `Codes/Python/02_linux_security/parse_auth_failures.py` | Parse a local auth log and rank failure sources |

```bash
chmod +x Codes/Bash/02_linux_security/*.sh
./Codes/Bash/02_linux_security/host_inspect.sh
./Codes/Bash/02_linux_security/failed_logons_summary.sh
python3 Codes/Python/02_linux_security/parse_auth_failures.py /var/log/auth.log
```


Inside your attacker virtual machine (or a Linux target you control):

1. List all listening TCP and UDP sockets and note which processes own them.
2. Identify your own shell’s process ID and list the files it has open.
3. Read the last 30 authentication-related log lines and count how many “Failed” or “Accepted” entries appear.
4. Write a small Bash script that prints:
   - Current date and time
   - Your username and UID
   - A summary of listening TCP ports
5. Make the script executable and run it. Record the output in your lab notebook.

**Success criteria:** You can explain what each major listening process is, you have a working script, and your notebook contains the commands and observations.

---

## Review Questions

1. What information does `ss -tulnp` provide that is especially useful for security work?
2. Why is binding a service to `127.0.0.1` different from binding it to `0.0.0.0`?
3. Name three common log locations or tools on a modern Linux system.
4. What does `set -euo pipefail` achieve at the start of a Bash script?
5. Why should you prefer a normal user account over remaining logged in as root during lab work?
6. Give one example of combining `grep`, `sort`, and `uniq` for a security-relevant task.

---

## Summary

- Linux command-line fluency is a foundational practical skill for security work.
- Process and socket inspection (`ps`, `ss`, `lsof`) reveals what is running and what is exposed.
- Logs are a primary source of investigative signal.
- Simple text-processing tools and small Bash scripts amplify your effectiveness.
- Privilege discipline and deliberate permissions remain important even inside a laboratory.
- With these habits in place you are ready to examine Windows systems from a security perspective and then move into network analysis.

**Next stage:** Windows for Security Practitioners — the other major operating system you will encounter in real environments.
