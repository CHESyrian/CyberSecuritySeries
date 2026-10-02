# 05 — SSH and Telnet

## Introduction

Remote command-line access is a daily requirement for system administration and security work. Two historically important protocols serve this purpose: **Telnet** (cleartext, obsolete for untrusted networks) and **SSH** (Secure Shell — encrypted and authenticated). This module explains both, emphasises why Telnet is unsafe, and covers practical SSH usage, key-based authentication, and basic hardening.

---

## Learning Objectives

- Describe the Telnet protocol and its security deficiencies
- Explain the SSH protocol’s security goals and high-level architecture
- Use SSH for interactive login, command execution, and file transfer (SCP/SFTP)
- Configure and use public-key authentication
- Apply basic SSH server hardening practices in a lab
- Recognise common SSH-related risks (weak keys, agent forwarding misuse, etc.)

---

## Core Concepts

### 1. Telnet

- Protocol for bidirectional interactive text communication (RFC 854 and related).
- Default port **TCP 23**.
- **No encryption** — usernames, passwords, and session content travel in cleartext.
- **No integrity protection** — sessions can be modified by an on-path attacker.
- Still occasionally found on legacy equipment and must be treated as a high risk if exposed.

```bash
# Example (lab only, against a system you own)
telnet 192.0.2.10
```

**Recommendation:** Disable Telnet servers; use SSH instead. If a device only supports Telnet, isolate it on a management network and prefer a jump host with SSH.

### 2. SSH — Goals and Architecture

SSH provides:

- Confidentiality (encryption)
- Integrity (tamper detection)
- Authentication (server host key + user authentication)
- Optional forwarding (TCP, X11, agent)

Major versions: SSH-2 is the current standard (SSH-1 is obsolete and insecure).

Typical components:

| Component | Role |
|-----------|------|
| `sshd` | Server daemon |
| `ssh` | Client |
| `ssh-keygen` | Key generation |
| `ssh-agent` / `ssh-add` | Key holding in memory |
| `scp` / `sftp` | File transfer over SSH |
| `~/.ssh/config` | Client configuration |
| `/etc/ssh/sshd_config` | Server configuration |

Default port: **TCP 22** (can be changed; obscurity alone is not security).

### 3. Host Authentication

On first connection the client receives the server’s **host key**. The fingerprint should be verified out-of-band. Subsequent connections check the key against `~/.ssh/known_hosts` (or the system equivalent). A changed key produces a strong warning — investigate before accepting.

```bash
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
ssh-keygen -R hostname    # remove old entry if legitimate change
```

### 4. User Authentication Methods

Common methods (in rough order of preference for many environments):

1. **Public-key authentication** — private key on the client, public key in `~/.ssh/authorized_keys` on the server.
2. **Keyboard-interactive / password** — acceptable when keys are not yet deployed; protect with rate limiting and MFA where possible.
3. **Certificate-based** (OpenSSH CA) — scalable enterprise pattern.
4. **GSSAPI / Kerberos** — in domain-joined environments.

```bash
# Generate a key pair (ed25519 preferred for most modern use)
ssh-keygen -t ed25519 -C "lab-key" -f ~/.ssh/id_ed25519_lab

# Install public key on server (example)
ssh-copy-id -i ~/.ssh/id_ed25519_lab.pub user@server
```

Protect private keys with a passphrase and restrictive file permissions (`chmod 600`).

### 5. Practical Client Usage

```bash
# Interactive login
ssh user@server.example.com
ssh -p 2222 user@server          # non-standard port

# Single command
ssh user@server "uptime; df -h"

# Verbose mode for troubleshooting
ssh -v user@server

# Jump host (ProxyJump)
ssh -J jumpuser@jumphost targetuser@target

# Local / remote port forwarding (lab examples)
ssh -L 8080:localhost:80 user@server
ssh -R 9000:localhost:3000 user@server
```

File transfer:

```bash
scp file.txt user@server:/path/
sftp user@server
```

### 6. Basic Server Hardening (Lab Guidance)

Typical `/etc/ssh/sshd_config` directives to consider (test in lab before production):

```
PermitRootLogin no
PasswordAuthentication no          # after keys are deployed
PubkeyAuthentication yes
PermitEmptyPasswords no
X11Forwarding no                   # unless required
AllowUsers alice bob               # or AllowGroups
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
```

After changes:

```bash
sudo sshd -t                       # syntax check
sudo systemctl reload sshd         # or equivalent
```

---

## Practical Examples

```bash
# Check whether sshd is listening
ss -tlnp | grep ':22'

# Client configuration snippet (~/.ssh/config)
# Host lab
#     HostName 192.0.2.20
#     User alice
#     IdentityFile ~/.ssh/id_ed25519_lab
#     IdentitiesOnly yes
```

---

## Common Mistakes

| Mistake | Consequence |
|---------|-------------|
| Leaving Telnet enabled | Credential and session exposure |
| Using weak or default SSH host keys | Impersonation risk |
| Unprotected private keys (no passphrase, world-readable) | Key theft leads to account compromise |
| Blindly accepting changed host keys | Possible MITM |
| Overly permissive `authorized_keys` or root login with password | Broad attack surface |
| Unnecessary agent forwarding | Exposure of keys to compromised jump hosts |

---

## Best Practices

- Prefer key-based authentication; disable password authentication once keys are working.
- Use ed25519 or strong RSA (≥ 3072 bits) keys; prefer hardware tokens or smart cards where available.
- Keep `known_hosts` accurate; verify fingerprints on first use.
- Restrict `sshd` with AllowUsers/AllowGroups, network ACLs, and fail2ban or equivalent rate limiting.
- Treat SSH jump hosts as high-value assets.
- Log and monitor authentication success/failure.
- In labs, practise both successful key login and deliberate failure modes (wrong key, changed host key).

---

## Hands-on Exercise

1. Generate an ed25519 key pair and configure key-based login to a lab server.
2. Disable password authentication on the lab `sshd` (after confirming key login works) and verify that password attempts fail.
3. Use `scp` or `sftp` to transfer a file.
4. Inspect the server’s host key fingerprint and compare it with the client’s `known_hosts` entry.
5. (Optional) Configure a simple ProxyJump path through a jump host.

---

## Review Questions

1. Why is Telnet considered unsafe on untrusted networks?
2. What two authentication steps does SSH perform (host and user)?
3. What file on the server lists public keys allowed for a user?
4. What is the purpose of the `known_hosts` file?
5. Name three useful hardening settings for `sshd_config`.

---

## Summary

Telnet transmits sessions in cleartext and should not be used on untrusted networks. SSH provides encrypted, authenticated remote access and is the standard tool for secure administration. Mastery of key-based authentication, basic hardening, and safe forwarding practices is essential for both daily operations and defensive security work.

---

## Sources

- RFC 4251–4254 (SSH protocol architecture and components)
- OpenSSH manual pages: `ssh(1)`, `sshd(8)`, `sshd_config(5)`, `ssh-keygen(1)`
- Mozilla / CIS SSH hardening guidelines (conceptual reference)
