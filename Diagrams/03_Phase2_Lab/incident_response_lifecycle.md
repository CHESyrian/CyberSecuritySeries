# Incident Response Lifecycle

Based on common industry models (NIST-style) used in Phase-2 Stage 10.

```mermaid
flowchart TB
    subgraph Prep["1 · Preparation"]
        P1[Policies · Playbooks]
        P2[Tools · Logging]
        P3[Training · Lab practice]
    end

    subgraph Detect["2 · Detection & Analysis"]
        D1[Alerts · Indicators]
        D2[Triage · Scope]
        D3[Classify severity]
    end

    subgraph Contain["3 · Containment"]
        C1[Short-term isolation]
        C2[Long-term measures]
    end

    subgraph Erad["4 · Eradication"]
        E1[Remove threat]
        E2[Close root cause]
    end

    subgraph Rec["5 · Recovery"]
        R1[Restore systems]
        R2[Validate · Monitor]
    end

    subgraph Post["6 · Post-Incident"]
        L1[Lessons learned]
        L2[Update detections]
        L3[Report]
    end

    Prep --> Detect --> Contain --> Erad --> Rec --> Post
    Post -.->|improve| Prep
```

**Explanation:** Preparation is continuous. After every incident (or tabletop), feed lessons back into detection rules, playbooks, and training. In the curriculum, all practical IR steps are performed only against lab systems.
