# Red Team vs Blue Team (Conceptual)

Introduced in Foundations; refined in later phases.

```mermaid
flowchart LR
    subgraph Red["Red Team · Offensive perspective"]
        R1[Think like an adversary]
        R2[Find weaknesses<br/>in authorized scope]
        R3[Demonstrate impact]
    end

    subgraph Blue["Blue Team · Defensive perspective"]
        B1[Prevent · Detect · Respond]
        B2[Monitor · Hunt · Contain]
        B3[Improve controls]
    end

    subgraph Purple["Purple · Collaborative"]
        P1[Shared goals]
        P2[Joint exercises]
        P3[Better detections]
    end

    Red <--> Purple
    Blue <--> Purple
```

**Explanation:** In this curriculum, “red” activities are always performed against systems you own or have explicit written permission to test. Blue focuses on visibility and response. Purple combines both to improve the overall security posture of the lab environment.
