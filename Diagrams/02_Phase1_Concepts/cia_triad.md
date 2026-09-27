# CIA Triad

Core security goals taught in Phase-1.

```mermaid
flowchart TB
    CIA((CIA Triad))

    C[Confidentiality<br/>Only authorized parties<br/>can read the data]
    I[Integrity<br/>Data is accurate and<br/>has not been altered]
    A[Availability<br/>Systems and data are<br/>usable when needed]

    CIA --> C
    CIA --> I
    CIA --> A

    C ---|supports| Auth[Authentication<br/>& Authorization]
    I ---|supports| Hash[Hashing · Signatures<br/>· Checksums]
    A ---|supports| Redund[Redundancy<br/>· Backups · Failover]
```

**Explanation:** Every security control ultimately supports one or more of these three goals. When evaluating a control or an incident impact, ask which CIA properties are affected.
