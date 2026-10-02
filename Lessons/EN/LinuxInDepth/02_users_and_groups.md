# 02 — Users and Groups

## Introduction

Every process on a Linux system runs with a set of credentials: a user ID (UID), a group ID (GID), and a list of supplementary groups. These credentials determine what the process is allowed to do. Understanding how accounts are defined, where the data lives, and how the kernel uses UIDs and GIDs is essential for both system administration and security work.

This module covers user and group databases, the difference between names and numeric IDs, the special role of root, home directories, and the commands used to inspect and manage identity.

---

## Learning Objectives

By the end of this module you will be able to:

- Explain the difference between a username and a UID, and between a group name and a GID
- Read and interpret `/etc/passwd`, `/etc/group`, and `/etc/shadow`
- Describe what happens at login and how the process credentials are set
- List a user’s groups and determine the effective identity of the current process
- Understand the special status of UID 0 (root) and service/system accounts
- Use common account-inspection commands safely in a lab

---

## Prerequisites

- Module 01 (Files and System Architecture) or equivalent understanding of the filesystem
- Ability to run simple commands and read text files

---

## Core Concepts

### 1. Identity Is Numeric

The kernel cares about **numbers**, not names:

- **UID** — user identifier (unsigned integer)
- **GID** — group identifier

Names (`alice`, `sudo`, `root`) exist for humans. They are resolved through databases (usually local files, sometimes networked services such as LDAP/SSSD).

Common conventions:

| UID / GID range | Typical use |
|-----------------|-------------|
| 0 | root |
| 1–99 or 1–999 | System / service accounts (distribution-dependent) |
| 1000+ | Ordinary human users (common default on many distros) |

Exact ranges are configured in `/etc/login.defs` and may differ.

### 2. Primary Group and Supplementary Groups

- Every user has exactly one **primary group** (the GID stored in the user database).
- A user may belong to additional **supplementary groups**.
- When a process creates a new file, the file’s group is usually the process’s primary GID (unless the parent directory has the setgid bit).

### 3. The Three Classic Database Files

#### `/etc/passwd` — user account information (world-readable)

Format (colon-separated fields):

```
username:password_placeholder:UID:GID:GECOS:home_directory:shell
```

| Field | Meaning |
|-------|---------|
| username | Login name |
| password_placeholder | Almost always `x` (real password data is in `/etc/shadow`) |
| UID | Numeric user ID |
| GID | Numeric primary group ID |
| GECOS | Optional comment (full name, contact, etc.) |
| home_directory | Absolute path to the user’s home |
| shell | Absolute path to the login shell (or `/sbin/nologin`, `/bin/false` for non-login accounts) |

Example line:

```
alice:x:1001:1001:Alice Example,,,:/home/alice:/bin/bash
```

#### `/etc/shadow` — sensitive authentication data (readable only by root)

```
username:hashed_password:lastchange:min:max:warn:inactive:expire:reserved
```

The hashed password field may contain:

- A real hash (e.g. `$6$...` for SHA-512)
- `!` or `*` — account locked / no password login
- Empty — (rare, insecure)

Never copy `/etc/shadow` out of a controlled lab. It contains material that can be used for offline password attacks.

#### `/etc/group` — group definitions

```
groupname:password_placeholder:GID:member1,member2,...
```

The member list contains usernames that have this group as a **supplementary** group. The primary group relationship is stored in `/etc/passwd`, not necessarily repeated here.

### 4. Root — UID 0

The account with UID 0 is traditionally called `root`. The kernel grants it almost unrestricted privilege. Many security controls (file permissions, capability checks, etc.) treat UID 0 as a special case.

Best practice: do daily work as a normal user; elevate only when necessary (via `sudo` or a controlled root shell).

### 5. System and Service Accounts

Daemons and services usually run under dedicated low-privilege accounts (e.g. `www-data`, `nginx`, `postgres`, `nobody`). These accounts:

- Often have a non-login shell (`/usr/sbin/nologin` or `/bin/false`)
- Have home directories that may not be normal interactive homes
- Exist so that a compromised service does not automatically give full root access

### 6. Home Directories and the Skeleton

- Ordinary users normally receive a directory under `/home`.
- The root user’s home is `/root` (not under `/home`).
- When a user is created with the usual tools, files from `/etc/skel` are copied into the new home directory (default `.bashrc`, `.profile`, etc.).

---

## Detailed Explanation

### How Credentials Are Established

1. A user authenticates (password, key, etc.).
2. The login process (or display manager, or `sshd`) looks up the account.
3. A new process is created with:
   - Real UID / effective UID = the user’s UID
   - Real GID / effective GID = the user’s primary GID
   - Supplementary groups = the groups listed for that user
4. The process changes to the user’s home directory and starts the login shell (or the requested command).

Later, a process can change its credentials only under strict rules (setuid binaries, capabilities, or root privilege).

### Inspecting Identity

```bash
# Who am I?
whoami
id
id alice

# Numeric view
id -u
id -g
id -G

# Groups for a user
groups
groups alice

# Current login sessions
who
w
```

The `id` command is the most useful single tool: it shows UID, GID, and all groups in both name and numeric form.

### Account Management Commands (Lab Use)

These commands modify system state. Use them only on machines you own or are authorized to administer.

```bash
# Create a user (Debian/Ubuntu style)
sudo adduser alice

# Create a user with more control (lower-level)
sudo useradd -m -s /bin/bash bob

# Create a group
sudo groupadd developers

# Add a user to a supplementary group
sudo usermod -aG developers alice

# Lock / unlock
sudo passwd -l alice
sudo passwd -u alice

# Change shell
sudo chsh -s /bin/bash alice
```

Always prefer the distribution’s recommended high-level tool (`adduser` / `useradd`, `usermod`, etc.) and read the man page for the exact options on your system.

---

## Practical Examples

### Reading the databases (as a normal user)

```bash
# Public information
getent passwd alice
getent passwd 1001
getent group sudo
getent group 27

# Count local users
getent passwd | wc -l
```

`getent` is preferred over directly `cat`ing the files because it also works when accounts come from network sources (LDAP, etc.).

### Examining the current process credentials

```bash
id
cat /proc/$$/status | grep -E 'Uid|Gid|Groups'
```

### Looking at a service account

```bash
getent passwd www-data
getent passwd nobody
ls -ld /var/www 2>/dev/null || true
```

---

## Common Mistakes

| Mistake | Why it is a problem | Better practice |
|---------|---------------------|-----------------|
| Editing `/etc/passwd` or `/etc/shadow` by hand without locking | Risk of corruption or concurrent change | Use `vipw`, `vipw -s`, or the proper account tools |
| Assuming the primary group is listed in `/etc/group` member field | Primary group is defined in `/etc/passwd` | Always check both sources or use `id` |
| Giving a service account a login shell | Increases attack surface if the account is compromised | Use `/usr/sbin/nologin` or equivalent |
| Running daily work as root | Any mistake or malicious command has full power | Use a normal account + `sudo` |
| Forgetting that UIDs must be unique | Two names with the same UID are the same identity to the kernel | Let the account tools allocate UIDs |

---

## Best Practices

- Use `id` and `getent` for inspection; they are safer and more portable than parsing files by hand.
- Keep root and sudo use intentional and logged.
- Prefer dedicated service accounts over running daemons as root.
- Treat `/etc/shadow` as highly sensitive material.
- Document any local account or group you create in a lab so you can clean up later.
- On systems joined to a domain, remember that local files are not the only source of identity.

---

## Hands-on Exercise

On a lab system:

1. Run `id` and `whoami`. Note your UID, primary GID, and supplementary groups.
2. Use `getent passwd $USER` and map each field to its meaning.
3. List all groups you belong to with `id -Gn` and `groups`.
4. Inspect a system account (for example `nobody` or `www-data` if present). What is its shell? Its home?
5. (Optional, if you have sudo) Create a temporary user and a temporary group, add the user to the group, verify with `id`, then remove them cleanly.

---

## Review Questions

1. What is the difference between a username and a UID from the kernel’s point of view?
2. Which file stores the hashed password on a typical local account setup?
3. What does the seventh field of `/etc/passwd` represent?
4. Why do many service accounts use `/usr/sbin/nologin` as their shell?
5. How can you see the full set of groups for the current process?
6. What is special about UID 0?
7. Why is `getent passwd` often better than `cat /etc/passwd`?

---

## Summary

- The kernel authorizes actions based on numeric UIDs and GIDs.
- `/etc/passwd`, `/etc/shadow`, and `/etc/group` (or their network equivalents) define accounts and groups.
- Root (UID 0) is all-powerful; ordinary work should be done under unprivileged accounts.
- Service accounts isolate daemons from each other and from interactive users.
- Commands such as `id`, `getent`, `groups`, and `whoami` are the primary tools for inspecting identity.

---

## Sources

- man pages: `passwd(5)`, `shadow(5)`, `group(5)`, `id(1)`, `getent(1)`, `useradd(8)`, `usermod(8)`
- `login.defs(5)` for UID/GID range defaults
- Distribution documentation on user management (Debian, RHEL, Ubuntu, etc.)
