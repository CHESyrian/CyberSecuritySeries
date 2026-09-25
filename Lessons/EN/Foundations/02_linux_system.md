# Phase-0 · Linux System

Linux is the most common operating system on servers, cloud instances, containers, and many security tools. Understanding its core ideas is essential.

---

## 1. Filesystem

Linux organizes everything in a single hierarchical tree that starts at the root directory `/`.

Important standard directories (conceptual map):

| Path | Typical purpose |
|------|-----------------|
| `/` | Root of the entire filesystem |
| `/home` | User personal directories |
| `/etc` | System configuration files |
| `/var` | Variable data (logs, caches, etc.) |
| `/var/log` | Log files |
| `/tmp` | Temporary files |
| `/bin`, `/usr/bin` | Essential and common commands |
| `/sbin`, `/usr/sbin` | System administration commands |
| `/opt` | Optional third-party software |
| `/proc`, `/sys` | Virtual filesystems that expose kernel and process information |

Everything is a file: devices, processes, configuration, even network sockets appear as files in certain locations.

---

## 2. Permissions

Linux uses a simple and powerful permission model for every file and directory:

- **Owner** (user who owns the file)
- **Group** (group associated with the file)
- **Others** (everyone else)

Each of the three can have:
- **r** — read
- **w** — write
- **x** — execute (or enter a directory)

Permissions are often shown as a string such as `rwxr-xr--` or as an octal number (e.g. 755).

Special bits (setuid, setgid, sticky bit) exist for more advanced control; the core idea remains “who can read / write / execute”.

**Principle of least privilege** is applied by giving each user and process only the permissions they actually need.

---

## 3. Users and Groups

- Every process runs as a specific user.
- Users are identified by a numeric **UID** and a name.
- Groups are identified by a **GID**.
- A user can belong to multiple groups.

Key files (for conceptual awareness):
- User accounts and basic information
- Group memberships
- Password hashes (stored securely, not in plain text)

The special user **root** (UID 0) has unrestricted power. Good practice is to use root only when necessary and prefer limited accounts for daily work.

---

## 4. Processes

A process is a running program. Linux tracks:

- Process ID (**PID**)
- Parent Process ID (**PPID**)
- The user it runs as
- CPU and memory usage
- Open files and network connections

Processes can create child processes. When you close a terminal, the shell often sends a signal that ends the processes started from that session (unless they were deliberately detached).

Understanding processes is the foundation for later topics such as privilege escalation awareness and monitoring.

---

## 5. Services

Services (also called daemons) are long-running background processes that start at boot or on demand.

Modern Linux distributions commonly use **systemd** to manage services. Conceptual operations include:

- Starting / stopping / restarting a service
- Enabling a service to start automatically at boot
- Checking status and recent logs

Services often listen on network ports and are a major part of a system’s attack surface.

---

## 6. Logs

Linux records important events in log files, traditionally under `/var/log`.

Common categories:
- System messages
- Authentication attempts
- Service-specific logs (web server, mail, etc.)
- Kernel messages

Logs are one of the primary sources of truth for both defenders (Blue Team) and for understanding what happened during an assessment. Good logging practices are a core security control.

---

## 7. SSH (Secure Shell)

SSH is the standard way to administer Linux systems remotely over an encrypted channel.

Conceptual points:
- Provides encrypted command-line access.
- Supports key-based authentication (strongly preferred over passwords).
- Can also forward ports and transfer files securely.
- The server listens on a port (commonly 22, though it can be changed).

SSH is both a critical administrative tool and a high-value target. Protecting SSH access is one of the highest-priority hardening steps on any Internet-facing Linux system.

---

## 8. Bash Scripting (Conceptual)

Bash is the most common command-line shell on Linux. A **script** is simply a text file containing a sequence of commands that the shell executes.

Why it matters for security work:
- Automation of repetitive tasks
- System administration and configuration
- Log analysis and simple monitoring
- Many security tools are invoked or glued together with shell scripts

You do not need to become a programming expert. Understanding that scripts exist, that they run with the privileges of the user who launches them, and that poorly written scripts can create security problems is the essential takeaway at this stage.

---

**Key takeaway**  
Linux is a permission-based, multi-user system built around a single filesystem tree, processes that run as users, services that expose functionality, and extensive logging. SSH is the primary remote access method, and Bash is the everyday automation language. Mastering these ideas makes every later Linux-related security topic far easier.