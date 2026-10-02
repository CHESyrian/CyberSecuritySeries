# 01 — Files and System Architecture

## Introduction

Linux presents almost every resource — regular files, directories, devices, pipes, sockets, and even kernel data — through a unified filesystem interface. Understanding this model is the foundation for nearly every later skill: permissions, process inspection, logging, packaging, and security tooling.

This module explains the hierarchical filesystem, the Virtual File System (VFS), inodes, the Filesystem Hierarchy Standard (FHS), special filesystems (`/proc`, `/sys`), and how devices appear as files.

---

## Learning Objectives

By the end of this module you will be able to:

- Describe the single-tree hierarchical filesystem and the role of the root directory `/`
- Explain what an inode is and how it relates to filenames and directory entries
- Distinguish regular files, directories, symbolic links, device files, sockets, and named pipes
- Navigate and interpret the major top-level directories defined by the FHS
- Use `/proc` and `/sys` to inspect kernel and process information
- Identify mount points and understand the difference between a filesystem and a directory tree

---

## Prerequisites

- Ability to open a terminal and run `ls`, `cd`, `pwd`, `cat`, `less`
- Conceptual familiarity with “everything is a file”

---

## Core Concepts

### 1. The Single Hierarchical Tree

Unlike systems that assign drive letters (C:, D:), Linux organizes all storage into one tree that begins at `/` (the root directory).

- Every file and directory has a path starting from `/`.
- Additional disks, partitions, network shares, and virtual filesystems are **mounted** onto directories inside this tree.
- The directory that receives a mount is called a **mount point**.

```
/
├── bin
├── boot
├── dev
├── etc
├── home
│   └── alice
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── sys
├── tmp
├── usr
└── var
```

### 2. Everything Is a File (Almost)

In the Linux model:

| Type | Description | Example |
|------|-------------|---------|
| Regular file | Bytes on disk | `/etc/passwd`, a script, a log |
| Directory | Special file that contains directory entries (name → inode mappings) | `/home`, `/var/log` |
| Symbolic link | Pointer to another path | `/usr/bin/python` → `python3.11` |
| Hard link | Another name for the same inode | (same file, different name) |
| Character device | Byte-stream device | `/dev/tty`, `/dev/null` |
| Block device | Block-oriented storage | `/dev/sda`, `/dev/nvme0n1` |
| Named pipe (FIFO) | Inter-process communication | created with `mkfifo` |
| Unix domain socket | Local IPC | `/run/systemd/private`, many daemon sockets |

You can list the type with `ls -l` (first character of the mode string) or with the `file` and `stat` commands.

### 3. Inodes — The Real Identity of a File

A **filename** is only a label stored inside a directory. The actual metadata and data location live in an **inode**.

An inode typically stores:

- File type and permissions
- Owner UID and group GID
- Size
- Timestamps (access, modification, change)
- Link count (how many directory entries point to this inode)
- Pointers to the data blocks on disk

Key consequences:

- Multiple hard links can point to the same inode (same data, same permissions).
- Deleting a name decreases the link count; the data is freed only when the link count reaches zero **and** no process still has the file open.
- Renaming a file within the same filesystem is cheap — it only changes a directory entry.

```bash
# Inspect inode number and metadata
ls -i filename
stat filename
```

### 4. Virtual File System (VFS)

The kernel presents a uniform interface (open, read, write, close, etc.) to user space regardless of the underlying filesystem type (ext4, xfs, btrfs, nfs, tmpfs, procfs, …). This layer is the **Virtual File System**.

User programs talk to VFS; VFS talks to the specific filesystem driver.

### 5. Filesystem Hierarchy Standard (FHS)

The FHS defines the expected purpose of major directories so that software and administrators can rely on a common layout.

| Path | Purpose |
|------|---------|
| `/` | Root of the hierarchy |
| `/bin` | Essential user command binaries (may be merged with `/usr/bin`) |
| `/boot` | Boot loader files, kernel, initramfs |
| `/dev` | Device files |
| `/etc` | Host-specific system configuration |
| `/home` | User home directories |
| `/lib`, `/lib64` | Essential shared libraries and kernel modules |
| `/media` | Mount points for removable media |
| `/mnt` | Temporary mount point for administrator use |
| `/opt` | Optional / third-party application packages |
| `/proc` | Virtual filesystem for process and kernel information |
| `/root` | Home directory of the root user |
| `/run` | Runtime variable data (since last boot) |
| `/sbin` | Essential system binaries (may be merged with `/usr/sbin`) |
| `/srv` | Data for services provided by this system |
| `/sys` | Virtual filesystem for devices, drivers, and kernel objects |
| `/tmp` | Temporary files (often cleared on reboot) |
| `/usr` | Secondary hierarchy — shareable, read-only data |
| `/usr/bin` | Most user commands |
| `/usr/lib` | Libraries for `/usr/bin` and `/usr/sbin` |
| `/usr/local` | Locally installed software (site-specific) |
| `/usr/share` | Architecture-independent data |
| `/var` | Variable data — logs, spools, caches, databases |
| `/var/log` | Log files |
| `/var/tmp` | Temporary files preserved between reboots |

Modern distributions often use a **merged /usr** layout where `/bin` → `/usr/bin` and `/sbin` → `/usr/sbin`.

### 6. Special Filesystems: `/proc` and `/sys`

These are not real disk storage. They are generated by the kernel on demand.

#### `/proc`

- One directory per process: `/proc/<PID>/`
- Useful files inside a process directory:
  - `cmdline` — command line
  - `status` — state, UIDs, memory summary
  - `fd/` — open file descriptors
  - `exe` — symlink to the executable
  - `cwd` — symlink to current working directory
  - `environ` — environment variables
- System-wide information:
  - `/proc/cpuinfo`
  - `/proc/meminfo`
  - `/proc/version`
  - `/proc/mounts`
  - `/proc/net/` (network-related)

```bash
# Example: examine the current shell process
echo $$
ls -l /proc/$$
cat /proc/$$/cmdline | tr '\0' ' '; echo
cat /proc/$$/status | head
```

#### `/sys` (sysfs)

Exposes kernel objects: devices, drivers, buses, power management, modules, etc. It is the modern interface for device discovery and some configuration.

```bash
ls /sys/class/net          # network interfaces
ls /sys/block              # block devices
```

### 7. Mounts and Mount Points

A filesystem (partition, network share, tmpfs, etc.) becomes visible when it is mounted on a directory.

```bash
# View current mounts
mount
findmnt
cat /proc/mounts
df -h
```

Important concepts:

- The directory used as the mount point must already exist.
- After mounting, the previous contents of that directory are hidden until the filesystem is unmounted.
- Bind mounts can attach one part of the tree to another location.
- Namespaces (used by containers) can give different mount views to different processes.

---

## Detailed Explanation — Putting It Together

When you run `cat /etc/passwd`:

1. The shell resolves the path component by component starting from the current root.
2. VFS looks up each directory entry, finds the inode for `passwd`.
3. The permission bits on the inode are checked against the process credentials.
4. The filesystem driver reads the data blocks associated with that inode.
5. The bytes are returned to the `cat` process.

When you run `ls /proc/1`:

1. VFS recognizes that `/proc` is a special filesystem.
2. The procfs driver synthesizes directory entries and file contents from kernel data structures for PID 1 (usually systemd or init).
3. No disk I/O for the content itself occurs; it is generated live.

This unified interface is why the same tools (`cat`, `ls`, `grep`, `less`) work on configuration files, logs, device information, and process state.

---

## Practical Examples

### Inspecting a file’s identity

```bash
touch /tmp/demo.txt
ls -li /tmp/demo.txt
stat /tmp/demo.txt

# Create a hard link
ln /tmp/demo.txt /tmp/demo-hard.txt
ls -li /tmp/demo.txt /tmp/demo-hard.txt
# Same inode number, link count = 2

# Create a symbolic link
ln -s /tmp/demo.txt /tmp/demo-sym.txt
ls -li /tmp/demo-sym.txt
# Different inode; the symlink has its own small inode that stores the target path
```

### Exploring the hierarchy

```bash
ls -l /
ls /bin /usr/bin | head
ls /etc | head
ls /var/log
ls /dev | head
ls /proc | head
ls /sys/class
```

### Process information via /proc

```bash
# Your current process
PID=$$
echo "PID: $PID"
cat /proc/$PID/status | grep -E 'Name|State|Uid|Gid|VmSize'
ls -l /proc/$PID/fd
readlink /proc/$PID/exe
```

### Mount information

```bash
findmnt -D
df -hT
```

---

## Common Mistakes

| Mistake | Why it matters | Better approach |
|---------|----------------|-----------------|
| Treating a symlink as the real file when editing | You may edit the wrong target or create a broken link | Use `readlink -f` or `realpath` to resolve; `ls -l` to see the target |
| Assuming `/tmp` is private | Other users can often read world-readable files there | Use `mktemp` and set restrictive permissions, or use a private directory |
| Deleting a file that a process still has open | The disk space is not freed until the process closes the file | Check with `lsof` or `fuser` before assuming space is reclaimed |
| Writing large data into `/` or filling `/var` | Can make the system unbootable or break services | Monitor with `df -h`; separate partitions or logical volumes help |
| Confusing hard links and symbolic links | Hard links cannot cross filesystems; symlinks can dangle | Know which one you need; prefer symlinks for most cross-directory references |

---

## Best Practices

- Prefer absolute paths in scripts and documentation when clarity matters.
- Use `stat` and `ls -li` when you need to reason about identity versus name.
- Treat `/proc` and `/sys` as read-mostly interfaces; changing values under `/sys` can alter hardware or kernel behaviour.
- Keep an eye on disk usage of `/var/log` and `/tmp`.
- When exploring an unfamiliar system, start with `findmnt`, `df -h`, `ls /`, and `ls /etc` to orient yourself.

---

## Hands-on Exercise

Perform these steps on a lab machine you control.

1. Create a regular file, a hard link, and a symbolic link. Record the inode numbers with `ls -li`.
2. List the contents of `/proc/self` and identify at least five useful files. Explain what each one tells you.
3. Run `findmnt` and identify the filesystem that contains your home directory and the one that contains `/`.
4. Use `df -h` and note which mount points are closest to full.
5. Locate the device file that corresponds to your root filesystem (hint: start from `findmnt` or `/proc/mounts`).

---

## Review Questions

1. What is the difference between a hard link and a symbolic link?
2. Why can two different filenames refer to exactly the same data and metadata?
3. What does the first character of an `ls -l` listing indicate?
4. Name three pieces of information you can obtain about a process by looking under `/proc/<PID>/`.
5. Why is `/proc` called a virtual filesystem?
6. What is a mount point?
7. According to the FHS, where should host-specific configuration files live? Where should variable log data live?

---

## Summary

- Linux presents a single hierarchical namespace rooted at `/`.
- Filenames are directory entries; the real object is the inode.
- Regular files, directories, devices, sockets, and pipes are all accessed through the same VFS interface.
- The FHS defines conventional locations for binaries, configuration, logs, and runtime data.
- `/proc` and `/sys` expose live kernel and process state as files.
- Understanding mounts, inodes, and the “everything is a file” model is required before privileges, processes, and security tools make complete sense.

---

## Sources

- Filesystem Hierarchy Standard (FHS) — official specification
- Linux man pages: `inode(7)`, `proc(5)`, `sysfs(5)`, `hier(7)`, `path_resolution(7)`
- Kernel documentation on VFS and procfs (kernel.org)
