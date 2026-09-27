# Authentication · Authorization · Accounting (AAA)

```mermaid
sequenceDiagram
    participant U as User / Process
    participant AuthN as Authentication
    participant AuthZ as Authorization
    participant Acc as Accounting / Audit
    participant Res as Resource

    U->>AuthN: Present credentials / token
    AuthN-->>U: Identity confirmed (or rejected)
    U->>AuthZ: Request action on resource
    AuthZ-->>U: Allow / Deny (policy)
    AuthZ->>Res: Grant access if allowed
    Acc->>Acc: Log identity · action · result
```

**Explanation:**  
- **Authentication** answers “Who are you?”  
- **Authorization** answers “What are you allowed to do?”  
- **Accounting** records what happened for audit and detection.  

These three concepts appear throughout Phase-1 (access control), Phase-2 (logging), and Phase-3 (IAM, detection).
