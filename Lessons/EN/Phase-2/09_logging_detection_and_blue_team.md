# Stage 9: Logging, Detection, and Blue Team Basics

## Why This Stage Matters

So far Phase-2 has emphasized discovery, analysis, and understanding of weaknesses.  
Real security also requires the ability to *notice* activity, decide whether it is suspicious, and respond. That is the blue-team side of the work.

This stage introduces the core ideas of logging, detection, and a defensive mindset. You will practice reading logs you already met in Stages 2 and 3 and begin thinking about how defenders turn raw events into useful signal.

---

## Learning Objectives

By the end of this stage you will be able to:

- Explain why logging is a foundational security control
- Identify common log sources on Linux and Windows systems
- Describe the high-level purpose of a SIEM
- Apply simple detection thinking to lab log data
- Distinguish between normal activity, suspicious activity, and confirmed incidents at a basic level
- Maintain the same strict lab-only boundary when generating or examining log events

---

## Safety Checkpoint

Generating authentication failures, process activity, or network connections for learning is fine **inside your laboratory**.  
Do not generate attack-like traffic against any system outside the lab.  
Do not attempt to disable or evade logging on systems you do not own.

---

## 1. Why Logging Matters

Logs are chronological records of events. Without them:

- You cannot investigate what happened after an incident
- You cannot prove that controls are working
- You cannot detect many classes of malicious or abusive activity
- Compliance and audit requirements often cannot be met

Logging does not stop attacks by itself. It enables detection, investigation, and accountability.

---

## 2. Common Log Sources

### Linux (recap and expansion)

| Source | Typical content |
|--------|-----------------|
| `/var/log/auth.log` or `/var/log/secure` | Authentication and privilege events |
| `/var/log/syslog` / `/var/log/messages` | General system messages |
| `journalctl` | systemd journal (many modern distributions) |
| Application logs | Web servers, databases, custom services |
| Audit frameworks (e.g. auditd) | Fine-grained security-relevant events when configured |

### Windows (recap and expansion)

| Source | Typical content |
|--------|-----------------|
| Security log | Logons, account changes, privilege use, process creation (when enabled) |
| System log | Service starts/stops, driver and hardware events |
| Application log | Application-specific events |
| PowerShell logs | Script block and module logging when enabled |
| Sysmon (if installed) | Rich process, network, and file activity (popular in defensive labs) |

---

## 3. SIEM — Conceptual Role

A **SIEM** (Security Information and Event Management) system collects logs from many sources, normalizes them, stores them, and supports searching, correlation, alerting, and reporting.

High-level value:

- One place to search across many systems
- Correlation of related events (e.g. failed logons followed by a successful logon from the same source)
- Alerting when patterns match known-bad or policy-violating behavior
- Retention for investigations and compliance

You do not need to deploy a full SIEM in this stage. Understanding *why* organizations invest in them prepares you for later defensive work and for reading SIEM-related findings.

---

## 4. Detection Thinking — Simple Patterns

Detection starts with questions such as:

- Is this activity expected for this user, host, or time of day?
- Does it match a known-bad pattern (e.g. repeated failed logons)?
- Does it combine with other events into a suspicious sequence?
- Would a defender want to know about this quickly?

Basic patterns worth practicing in the lab:

| Pattern | Example lab observation |
|---------|-------------------------|
| Brute-force style logons | Many failed authentications from one source in a short time |
| New or unusual process | A process name or path you have never seen on that host |
| Unexpected network connection | A lab host connecting to an address that is not part of normal lab activity |
| Privilege-related events | Sudden use of administrator or root privileges |
| Log clearing or service stop | Attempts to remove evidence or disable logging |

Generate some of these safely inside the lab (failed SSH or RDP logons, starting unusual processes, etc.) and then find them in the logs. This builds the feedback loop between action and visibility.

---

## 5. From Events to Incidents (Conceptual)

Not every suspicious event is an incident. A simple mental model:

1. **Raw event** — something was recorded
2. **Alert / detection** — a rule or human judgment marked it as interesting
3. **Investigation** — additional context is gathered
4. **Incident** — confirmed harmful or policy-violating activity that requires response
5. **Response** — containment, eradication, recovery, and lessons learned (covered more in Stage 10)

False positives exist on the defensive side just as they do with vulnerability scanners. Tuning and context are part of the craft.

---

## 6. Linking Blue-Team Skills to Earlier Stages

- Stages 2 & 3: You already know how to *read* the logs; this stage focuses on *why* and *what to look for*.
- Stage 4: Packet captures can corroborate or enrich log evidence.
- Stage 5 & 6: Scanning and vulnerability activity also generate logs — defenders can detect reconnaissance.
- Stage 7: Web application logs and web-server logs are rich detection sources.

Thinking from both sides (how an activity looks when performed, and how it looks when logged) is a professional advantage.

---

## Common Mistakes

| Mistake | Consequence | Better practice |
|---------|-------------|-----------------|
| Collecting logs but never reviewing them | Detection capability exists only on paper | Practice regular review even in the lab |
| Alerting on everything | Alert fatigue; real issues are missed | Start with high-signal patterns |
| Ignoring time synchronization | Correlating events across hosts becomes unreliable | Keep lab VMs reasonably in sync |
| Assuming absence of logs means absence of activity | Blind spots | Know which actions are logged and which are not |
| Disabling logging to “clean up” a lab | Destroys learning opportunities | Prefer filtering and focused searches |

---

## Best Practices

- Enable and retain authentication and process-creation logging in lab VMs where practical.
- Practice writing one or two simple detection ideas in plain language (“alert if more than N failed logons from one IP in M minutes”).
- When you perform an action in the lab, immediately try to find its log evidence.
- Keep a short personal list of high-value Event IDs (Windows) and log locations (Linux).
- Remember that good detection is iterative: deploy, observe noise, tune, repeat.

---

## Hands-on Exercise

## Practical code (Codes/)

| Script | Purpose |
|--------|---------|
| `Codes/Bash/09_logging_detection/auth_failure_watch.sh` | Follow auth log and highlight failure/accepted lines |
| `Codes/Bash/02_linux_security/failed_logons_summary.sh` | Count failure sources from a static log |
| `Codes/Python/09_logging_detection/simple_detection_demo.py` | Flag IPs that exceed a failure threshold |
| `Codes/Python/02_linux_security/parse_auth_failures.py` | Parse and rank failure sources |

```bash
chmod +x Codes/Bash/09_logging_detection/auth_failure_watch.sh
# Generate a few failed logons in the lab, then:
./Codes/Bash/09_logging_detection/auth_failure_watch.sh
python3 Codes/Python/09_logging_detection/simple_detection_demo.py /var/log/auth.log -t 5
```


1. On a Linux lab VM, generate a few failed SSH logon attempts (from the attacker VM) and then locate them in the authentication log or journal.
2. On a Windows lab VM, generate a failed logon and a successful logon; find the corresponding Security log events.
3. List three detection ideas that would be relevant inside your lab (e.g. repeated failures, unexpected new process, unusual outbound connection).
4. (Optional) If you have a simple centralized logging setup, send a test event and confirm it arrives.
5. Record the commands used, the log lines found, and your detection ideas in the lab notebook.

**Success criteria:** You can generate and then locate authentication-related events on both Linux and Windows lab systems, and you have written at least three concrete detection ideas.

---

## Review Questions

1. Why is logging considered a foundational security control?
2. Name two important log sources on Linux and two on Windows.
3. What problem does a SIEM help solve?
4. Give one example of a simple detection pattern you could apply to log data.
5. How does blue-team thinking change the way you interpret activity performed in earlier stages?
6. Why should you still respect lab boundaries when generating “attack-like” events for learning?

---

## Summary

- Logging provides the raw material for detection, investigation, and accountability.
- Both Linux and Windows offer rich security-relevant event sources.
- A SIEM centralizes and correlates those sources at scale.
- Detection begins with clear questions and simple, high-signal patterns.
- Practicing the loop “perform action → find evidence in logs” builds durable skill.
- The defensive perspective complements everything learned in the discovery-oriented stages.

**Next stage:** Incident Response Fundamentals — what happens after a detection is confirmed.
