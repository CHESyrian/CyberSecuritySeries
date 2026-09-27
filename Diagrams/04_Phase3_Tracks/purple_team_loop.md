# Purple Team Loop

Supports Phase-3 Track 5 (Adversary Simulation) paired with Track 2 (SOC).

```mermaid
flowchart TB
    SCOPE[1 · Define Scope & RoE<br/>Lab systems only]
    PLAN[2 · Plan ATT&CK-mapped<br/>test cases]
    EXEC[3 · Execute in lab<br/>Red perspective]
    OBS[4 · Observe detections<br/>Blue perspective]
    ANALYZE[5 · Analyze gaps<br/>Missed / delayed / noisy]
    IMPROVE[6 · Improve detections<br/>& controls]
    REPORT[7 · Document & report]

    SCOPE --> PLAN --> EXEC --> OBS --> ANALYZE --> IMPROVE --> REPORT
    IMPROVE -.->|re-test| EXEC
```

**Explanation:** Purple teaming is collaborative improvement, not pure competition. Every cycle stays inside the authorized lab boundary defined in the Rules of Engagement. Map each test case to ATT&CK technique IDs so results are comparable over time.
