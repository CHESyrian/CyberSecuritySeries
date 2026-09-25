# Phase-0 · Windows System

Windows is the dominant desktop operating system and is also widely used on servers. Its architecture and security model differ from Linux in important ways.

---

## 1. Windows Architecture (High-Level)

Windows is built in layers:

- **User mode** — ordinary applications and most services run here. They have limited privileges.
- **Kernel mode** — the core of the operating system, device drivers, and the most trusted components run here. Code running in kernel mode has full power over the machine.

Key components you will hear about:
- **Windows Executive** and **Kernel** — manage processes, memory, security, I/O.
- **Hardware Abstraction Layer (HAL)** — hides differences between hardware.
- **Win32 / Windows API** — the interface that applications use to request services from the OS.

Understanding the user-mode / kernel-mode boundary helps later when discussing drivers, privilege levels, and certain classes of vulnerabilities.

---

## 2. NTFS Permissions

NTFS is the standard filesystem on modern Windows.

Permissions can be set on files and folders for:
- Specific users
- Groups
- Built-in identities (Everyone, Authenticated Users, SYSTEM, etc.)

Common permission types include:
- Read
- Write
- Modify
- Full Control
- List folder contents
- Special advanced permissions

Permissions can be **inherited** from parent folders. Explicit permissions can override inheritance.  
The principle of least privilege still applies: grant only what is required.

---

## 3. Services

Windows services are background programs that typically start automatically and run without a user logged in.

They run under specific accounts:
- Local System (very powerful)
- Network Service / Local Service (more limited)
- Custom domain or local accounts

Services are managed through the Services console or command-line tools. Because many services run with high privileges, they are carefully controlled in secure environments.

---

## 4. Processes

Similar to Linux, a process is a running program. Windows tracks:

- Process ID
- Parent process
- User context (security token)
- Loaded modules (DLLs)
- Handles to files, registry keys, network connections, etc.

The **Security Identifier (SID)** and the access token attached to a process determine what the process is allowed to do. This token-based model is central to Windows security.

---

## 5. Registry

The **Windows Registry** is a hierarchical database that stores configuration for the operating system and installed applications.

It is divided into hives (major sections), for example:
- Configuration that applies to the whole machine
- Configuration that applies to the currently logged-on user
- Hardware and software information

Many security-relevant settings live in the Registry. Changes to certain keys can affect authentication, logging, startup programs, and more. Unauthorized modification of the Registry is a common goal of malware and a concern for defenders.

---

## 6. Event Viewer

Windows records a wide variety of events in logs that can be viewed with Event Viewer (or queried programmatically).

Important log categories:
- **Security** — logon attempts, privilege use, account changes, etc.
- **System** — hardware and driver issues, service starts/stops
- **Application** — messages from software
- Additional operational and analytic logs on modern versions

These logs are a primary source of visibility for Blue Team activities (detection, incident response, hunting).

---

## 7. PowerShell

PowerShell is the modern command-line shell and scripting language for Windows. It is object-oriented and deeply integrated with the operating system.

Why it matters:
- Preferred tool for administration and automation
- Can query almost every part of the system (processes, services, registry, event logs, Active Directory, etc.)
- Heavily used by both administrators and security professionals
- Also frequently abused by attackers, which is why modern Windows includes extensive PowerShell logging and constrained language modes

At this stage you only need to know that PowerShell is the powerful native automation and inspection interface for Windows.

---

## 8. Active Directory (Conceptual)

**Active Directory (AD)** is Microsoft’s directory service used in almost every medium-to-large Windows environment.

Core ideas:
- Central place to store users, groups, computers, and policies
- **Domain** — administrative boundary
- **Domain Controller** — server that holds a copy of the directory and authenticates users
- Group Policy — mechanism to push configuration and security settings to many machines
- Authentication protocols (commonly Kerberos in modern environments)

Active Directory is the identity and policy backbone of most corporate Windows networks. Compromising it (or defending it) is therefore one of the highest-stakes areas in enterprise security.

---

**Key takeaway**  
Windows separates user mode from kernel mode, uses NTFS permissions and access tokens for authorization, stores critical configuration in the Registry, records activity in Event Logs, and is administered largely through PowerShell. In organizations, Active Directory provides centralized identity and policy. These building blocks appear constantly in both offensive and defensive Windows security work.