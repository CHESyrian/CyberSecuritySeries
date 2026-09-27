# Curriculum Progression

High-level path from absolute beginner to specialized tracks.

```mermaid
flowchart TB
    subgraph P0["Phase 0 · Foundations"]
        A1[Computer Basics]
        A2[Linux / Windows]
        A3[Networking Intro]
        A4[Cyber Basics]
        A5[Red / Blue Concepts]
    end

    subgraph P1["Phase 1 · Conceptual"]
        B1[CIA Triad]
        B2[Threats · Vulns · Risk]
        B3[Networking Depth]
        B4[Access Control]
        B5[Cryptography]
        B6[Attack Surfaces]
        B7[Ethics & Law]
        B8[Pentest Methodology]
    end

    subgraph P2["Phase 2 · Practical Lab"]
        C1[Lab Setup & Safety]
        C2[Linux / Windows for Security]
        C3[Packet Analysis]
        C4[Authorized Recon]
        C5[Vuln Concepts]
        C6[Web Fundamentals]
        C7[Crypto Practice]
        C8[Logging & Detection]
        C9[Incident Response]
        C10[Capstone]
    end

    subgraph P3["Phase 3 · Specialized Tracks"]
        D1[Track 1 · Web AppSec]
        D2[Track 2 · SOC / Detection]
        D3[Track 3 · Network Infra]
        D4[Track 4 · Cloud]
        D5[Track 5 · Adversary Sim]
    end

    P0 --> P1 --> P2 --> P3
```

**Explanation:** Learners progress linearly through Phases 0–2. Phase 3 offers parallel specialized tracks; most learners pick one primary track (or a related pair such as Track 2 + Track 5 for purple-team focus).
