# Linux In Depth — Overview

This series goes deeper than the Phase-0 conceptual introduction and the Phase-2 practical Linux-for-security stage.  
It is intended for learners who already know basic navigation (`pwd`, `ls`, `cd`, `cat`) and want a solid, accurate mental model of how Linux actually works.

---

## Scope

| Module | Title | Focus |
|--------|-------|-------|
| 01 | Files and System Architecture | Filesystem hierarchy, VFS, inodes, device files, `/proc` & `/sys`, FHS |
| 02 | Users and Groups | Accounts, UIDs/GIDs, `/etc/passwd`, `/etc/group`, `/etc/shadow`, home directories |
| 03 | Privileges and Permissions | Permission bits, ownership, special bits (setuid/setgid/sticky), ACLs, capabilities, sudo |
| 04 | Command Line in Depth | Shells, expansion, redirection, pipes, job control, environment, useful tools |

All material is written for **authorized laboratory use only**. Commands that inspect system state or change configuration must be run only on systems you own or have explicit permission to use.

---

## Learning Path

1. Read **01 — Files and System Architecture** first. Almost every later concept rests on understanding “everything is a file” and the inode model.
2. Then **02 — Users and Groups**. You need a clear picture of identity before you can reason about privileges.
3. **03 — Privileges and Permissions** builds directly on the previous two modules.
4. **04 — Command Line in Depth** is practical and can be studied in parallel, but is most useful once the model of files, users, and permissions is solid.

---

## Prerequisites

- Comfortable opening a terminal and running basic commands.
- Familiarity with the ideas in Foundations `02_linux_system.md` and Phase-2 `02_linux_for_security.md`.
- A Linux lab environment (VM, container, or physical machine you control).

---

## Conventions Used in This Series

- Commands shown with a `$` prompt are intended for a normal user.
- Commands shown with a `#` prompt (or preceded by `sudo`) require elevated privileges.
- Output examples are illustrative; exact numbers, paths, and timestamps will differ on your system.
- Safety notes appear in callouts. Treat them seriously.

---

## How to Use the Exercises

Each module ends with hands-on exercises.  
Do them on a disposable lab machine. Prefer creating a snapshot or clone so you can revert if you make a configuration mistake.

---

## Ethical Framing

Understanding Linux deeply is a professional skill used by system administrators, security engineers, incident responders, and developers.  
The same knowledge can be misused. This curriculum only covers techniques that are appropriate inside controlled laboratory environments and under explicit authorization. Do not apply investigative or configuration-changing commands to systems you do not own or have written permission to test.
