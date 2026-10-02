# 03 — Privileges and Permissions

## Introduction

Linux access control is built on a few simple ideas that combine into a powerful model: every file has an owner and a group, every process runs with credentials (UID/GID/groups), and permission bits decide what those credentials are allowed to do. Special bits, ACLs, capabilities, and sudo extend the model for real-world needs.

This module explains the classic permission bits, ownership, the setuid/setgid/sticky bits, Access Control Lists, Linux capabilities, and controlled privilege escalation with sudo — all from a security-aware perspective.

---

## Learning Objectives

By the end of this module you will be able to:

- Read and interpret the permission string shown by `ls -l` and the octal mode used by `chmod`
- Change ownership and permissions deliberately and safely
- Explain the effect of the setuid, setgid, and sticky bits
- Describe when traditional Unix permissions are insufficient and how ACLs help
- Understand the idea of Linux capabilities as a finer-grained alternative to “all or nothing” root
- Use `sudo` correctly and inspect sudo policy at a basic level
- Apply the principle of least privilege in daily lab work

---

## Prerequisites

- Modules 01 and 02 (filesystem model and users/groups)
- Comfort with `ls -l`, `id`, and basic navigation

---

## Core Concepts

### 1. The Classic Permission Model

Every file and directory has:

- An **owner** (UID)
- A **group** (GID)
- **Permission bits** for three classes of subjects:
  - **User** (owner)
  - **Group**
  - **Others** (everyone else)

For each class there are three primary permissions:

| Symbol | Name | Effect on a regular file | Effect on a directory |
|--------|------|---------------------------|------------------------|
| `r` | read | Open and read contents | List directory entries (`ls`) |
| `w` | write | Modify contents / truncate | Create, delete, rename entries **inside** the directory |
| `x` | execute | Run the file as a program/script | Traverse (enter) the directory (`cd`) |

Important nuance for directories:

- Write permission on a directory controls whether you can add or remove names in that directory, not whether you can modify the files themselves.
- To delete a file you need write permission on the **containing directory**, not necessarily on the file.

### 2. Viewing Permissions

```bash
ls -l filename
ls -ld directory
stat filename
```

Example listing:

```
-rwxr-xr-- 1 alice developers 4096 Sep 30 10:00 script.sh
```

Breakdown of the mode string:

| Position | Meaning |
|----------|---------|
| 1 | File type (`-` regular, `d` directory, `l` symlink, `c` char device, `b` block, `p` FIFO, `s` socket) |
| 2–4 | Owner permissions (rwx) |
| 5–7 | Group permissions (r-x) |
| 8–10 | Others permissions (r--) |

### 3. Octal Notation

Each rwx triplet is a 3-bit value:

| Permission | Value |
|------------|-------|
| r | 4 |
| w | 2 |
| x | 1 |

Common modes:

| Octal | Meaning |
|-------|---------|
| 755 | Owner rwx, group and others rx (typical for executables and directories) |
| 644 | Owner rw, group and others r (typical for data files) |
| 600 | Owner rw only (private files) |
| 700 | Owner rwx only (private directories or scripts) |
| 777 | Everyone everything (almost never appropriate) |

```bash
chmod 644 notes.txt
chmod 755 backup.sh
chmod u=rw,g=r,o= file.txt     # symbolic form
chmod u+x script.sh
chmod go-w file.txt
```

### 4. Changing Ownership

```bash
# Change owner and group
sudo chown alice:developers file.txt
sudo chown alice file.txt          # owner only
sudo chown :developers file.txt    # group only

# Recursive (use with care)
sudo chown -R alice:alice /home/alice/project
```

Only root (or a process with the appropriate capability) can change ownership arbitrarily.

### 5. Special Permission Bits

Three extra bits appear in the high positions of the mode:

#### Setuid (set user ID)

- On an executable: the process runs with the **effective UID** of the file’s owner, not the caller.
- Classic example: `/usr/bin/passwd` is setuid root so ordinary users can update their own password hash.
- Shown as `s` in the owner’s execute position (`rws` instead of `rwx`).

#### Setgid (set group ID)

- On an executable: the process runs with the **effective GID** of the file’s group.
- On a directory: new files created inside inherit the directory’s group (instead of the creator’s primary group). Very useful for shared project directories.

#### Sticky bit

- On a directory: only the file’s owner (or root) can delete or rename the files inside, even if the directory is world-writable.
- Classic example: `/tmp` has the sticky bit so users cannot delete each other’s temporary files.
- Shown as `t` in the others’ execute position.

```bash
# Examples of inspection
ls -l /usr/bin/passwd
ls -ld /tmp
ls -ld /var/mail   # often setgid
```

### 6. Access Control Lists (ACLs)

Traditional owner/group/others is limited when you need more than one group or specific users to have different access. POSIX ACLs add finer entries.

```bash
# View ACLs
getfacl file.txt

# Grant a specific user read access
setfacl -m u:bob:r file.txt

# Grant a group write access
setfacl -m g:auditors:w file.txt

# Remove an ACL entry
setfacl -x u:bob file.txt

# Default ACLs on a directory (inherited by new files)
setfacl -d -m g:developers:rw project_dir
```

When ACLs are present, `ls -l` shows a `+` at the end of the mode string.

### 7. Linux Capabilities

Instead of giving a process full root (UID 0), the kernel can grant a subset of root-like powers as **capabilities**. Examples:

- `CAP_NET_BIND_SERVICE` — bind to ports below 1024
- `CAP_NET_RAW` — use raw sockets (needed by some network tools)
- `CAP_SYS_ADMIN` — broad administrative operations (still very powerful)
- `CAP_DAC_OVERRIDE` — bypass file permission checks

Tools such as `ping` or `tcpdump` are often installed with specific capabilities rather than full setuid root on modern systems.

```bash
# Inspect capabilities of a binary (if libcap is installed)
getcap /usr/bin/ping
getcap -r /usr/bin 2>/dev/null | head
```

### 8. sudo — Controlled Elevation

`sudo` lets a permitted user run individual commands as root (or another user) according to a policy file, usually `/etc/sudoers` and files under `/etc/sudoers.d/`.

```bash
# Run a single command as root
sudo whoami
sudo apt update          # example on Debian/Ubuntu

# Open a root shell (use sparingly)
sudo -i
sudo -s

# List allowed commands (depends on policy)
sudo -l
```

Best practices:

- Prefer specific command rules over full root shells when possible.
- Use `sudo -l` to understand what you are allowed to do.
- Never put world-writable scripts or binaries in a sudo rule.
- Prefer editing files in `/etc/sudoers.d/` with `visudo -f` rather than editing the main file directly.

---

## Detailed Explanation — Decision Order (Simplified)

When a process tries to open a file, the kernel roughly checks:

1. If the process has the `DAC_OVERRIDE` capability (or is root with traditional full privileges), access is often granted.
2. Otherwise, if the process UID matches the file owner → use the owner permission bits.
3. Else if one of the process’s GIDs matches the file group (or an ACL group entry matches) → use group / ACL permissions.
4. Else → use the “others” permission bits (or corresponding ACL “other” entry).
5. ACL mask and named user/group entries refine the result when ACLs are present.

(The real algorithm is more precise and includes capability checks, LSM modules such as SELinux/AppArmor, etc., but the above is the classic DAC core.)

---

## Practical Examples

### Inspect and change basic permissions

```bash
touch /tmp/demo.txt
ls -l /tmp/demo.txt
chmod 600 /tmp/demo.txt
ls -l /tmp/demo.txt
chmod u+x /tmp/demo.txt
stat /tmp/demo.txt
```

### Shared directory with setgid

```bash
# (as a user with sudo)
sudo mkdir /tmp/project
sudo chgrp developers /tmp/project
sudo chmod 2775 /tmp/project    # setgid + rwxrwxr-x
ls -ld /tmp/project
# New files created inside should inherit group "developers"
```

### Sticky bit demonstration (conceptual)

```bash
ls -ld /tmp
# You should see a 't' at the end of the mode, e.g. drwxrwxrwt
```

### Capabilities

```bash
getcap /usr/bin/ping 2>/dev/null || echo "getcap not available or no capabilities set"
```

### sudo

```bash
sudo -l
sudo id
sudo cat /etc/shadow | head -3     # only if your policy allows it
```

---

## Common Mistakes

| Mistake | Risk | Safer approach |
|---------|------|----------------|
| `chmod 777` on files or directories | Any user can modify or replace content | Use the tightest mode that still works (often 644 / 755 / 600 / 700) |
| Running a web server or service as root | Full system compromise if the service is breached | Dedicated service account + minimal capabilities or permissions |
| Setuid binaries that you wrote yourself without careful design | Privilege escalation vulnerability | Avoid custom setuid programs; prefer capabilities or sudo |
| Recursive `chmod` / `chown` on the wrong path | Breaking system files or locking yourself out | Double-check the path; prefer non-recursive when possible |
| World-writable scripts referenced by sudo or cron | Anyone can inject commands | Keep scripts non-writable by others; verify ownership |

---

## Best Practices

- Default to the principle of least privilege: grant only the permissions required.
- Prefer group collaboration (setgid directories + shared group) over world-writable locations.
- Use ACLs when the classic model is too coarse, but keep the ACL set small and documented.
- Prefer file capabilities over full setuid root when a binary needs only one or two privileges.
- Treat sudo rules as code: review them, keep them minimal, and use `visudo`.
- In labs, practice both “how to grant” and “how to audit” permissions (`find /path -perm ...`, `getfacl`, `getcap`).

---

## Hands-on Exercise

1. Create a file and experiment with `chmod` using both octal and symbolic modes. Verify with `ls -l` and `stat`.
2. Inspect `/tmp` and at least one setuid binary (e.g. `passwd`). Note the special bits.
3. Create a directory, apply setgid, and observe the group of a new file created inside it (requires a second group you belong to, or sudo).
4. Run `sudo -l` and interpret the output for your account.
5. (Optional) Use `find` to locate setuid binaries on the system:  
   `find /usr -perm -4000 -type f 2>/dev/null`

---

## Review Questions

1. What does write permission on a directory allow that write permission on a file does not?
2. How is the mode `rwxr-xr--` expressed in octal?
3. What is the purpose of the sticky bit on `/tmp`?
4. When a setuid-root program runs, which UID is used for permission checks — the caller’s or root’s?
5. Why might an administrator prefer Linux capabilities over a full setuid-root binary?
6. What does the `+` character mean at the end of an `ls -l` mode string?
7. Why is `chmod 777` almost always a bad idea on a multi-user system?

---

## Summary

- Classic Unix permissions (owner/group/others × rwx) remain the foundation of Linux access control.
- Special bits (setuid, setgid, sticky) modify behaviour for executables and directories.
- ACLs and capabilities provide finer control when the basic model is insufficient.
- sudo supplies audited, policy-driven privilege escalation.
- The consistent application of least privilege is one of the highest-value habits a security practitioner can develop.

---

## Sources

- man pages: `chmod(1)`, `chown(1)`, `umask(2)`, `credentials(7)`, `capabilities(7)`, `acl(5)`, `sudo(8)`, `sudoers(5)`
- POSIX ACL documentation
- Kernel documentation on credentials and capabilities
