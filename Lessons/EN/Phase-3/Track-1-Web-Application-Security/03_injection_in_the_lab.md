# Track 1 · Stage 1.3 — Injection in the Lab

## Why this stage matters
Injection flaws occur when untrusted input is interpreted as code or queries. Training apps exist so you can see impact **without** attacking real systems.

## Learning objectives
- Explain SQL and OS command injection at a conceptual and lab-demo level
- Demonstrate a designated challenge on DVWA/Juice Shop only
- Describe impact categories and primary mitigations (parameterization, allow-lists)

## Safety checkpoint
Only intentional vulnerable pages. No scanning random Internet forms. Prefer built-in low/medium difficulty labs.

## Core concepts
- Trust boundary between user data and interpreter
- Parameterized queries vs string concatenation
- Least privilege for database and OS accounts

## Practice
Complete one SQL and (if available) one command-injection challenge in your lab app. Document: request, what you changed, result, suggested fix in plain language.

## Review
- Why does input validation alone often fail as the only control?
- What is the defensive role of least privilege on the DB account?
