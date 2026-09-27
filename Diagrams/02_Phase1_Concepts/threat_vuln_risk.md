# Threat · Vulnerability · Risk Relationship

```mermaid
flowchart LR
    T[Threat<br/>Potential cause of harm<br/>e.g. adversary, malware, error]
    V[Vulnerability<br/>Weakness that can be exploited<br/>e.g. unpatched software, weak config]
    A[Asset<br/>Something of value<br/>e.g. data, system, reputation]
    R[Risk<br/>Likelihood × Impact<br/>of threat exploiting vulnerability]

    T -->|exploits| V
    V -->|affects| A
    T --> R
    V --> R
    A --> R
```

**Explanation:** Risk exists when a threat can exploit a vulnerability that affects an asset. Removing the vulnerability, reducing the threat, or lowering the value/impact of the asset all reduce risk. This model underpins prioritization in Phase-1 and vulnerability assessment in Phase-2.
