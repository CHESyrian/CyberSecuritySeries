# Stage 7: Common Attack Surfaces (High-Level View)

## What Is an Attack Surface?

The **attack surface** is the sum of all the points where an unauthorized person could try to enter or extract data from a system.

Reducing the attack surface is a fundamental defensive strategy: the fewer openings that exist, the harder it is for threats to succeed.

## Major Categories of Attack Surface

### 1. Network Exposure
Any service that accepts connections from other computers.
- Public-facing websites and APIs
- Remote access services
- Email servers
- Cloud resources with overly permissive network rules

### 2. Software and Applications
Code that processes input from users or other systems.
- Web applications
- Mobile apps
- Desktop software
- APIs that exchange data between systems

### 3. Human / Social
People can be influenced or make mistakes.
- Phishing and other social-engineering attempts
- Insider actions (malicious or accidental)
- Poor security habits (weak passwords, unsecured devices)

### 4. Physical
Access to buildings, devices, or media.
- Stolen or lost laptops and phones
- Unauthorized entry to server rooms
- Improper disposal of storage media

### 5. Supply Chain and Third Parties
Systems and services you depend on but do not fully control.
- Cloud providers
- Software libraries and open-source components
- Vendors with access to your environment
- Managed service providers

## Why Understanding Attack Surface Matters

Security work is largely about:

1. Knowing what the attack surface currently is
2. Reducing unnecessary exposure
3. Putting appropriate controls on the remaining exposure
4. Monitoring for signs that something is going wrong

You cannot protect what you do not know exists.

## High-Level Defensive Themes

Without describing any specific attack techniques, the common defensive patterns are:

- **Minimize** — turn off or remove anything not required
- **Segment** — separate systems so that a problem in one area does not automatically spread
- **Authenticate and authorize strongly** — make sure only the right identities get access
- **Encrypt sensitive data** — both in transit and at rest
- **Monitor and log** — so unusual activity can be noticed
- **Keep software updated** — reduce known weaknesses
- **Train people** — reduce human-related openings
- **Plan for failure** — backups, incident response, recovery

These themes appear repeatedly across professional security programs.

## Connection to Earlier Stages

- Attack surface analysis is really an application of **asset + vulnerability** thinking.
- Controls applied to the attack surface support the **CIA triad**.
- Risk prioritization decides which parts of the attack surface deserve the most attention and resources.

---

**Next stage:** The ethical and legal framework that governs professional security work.