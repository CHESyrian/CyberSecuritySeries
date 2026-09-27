# Cloud Shared Responsibility (Conceptual)

Supports Phase-3 Track 4.

```mermaid
flowchart TB
    subgraph Customer["Customer Responsibility"]
        C1[Data · Classification · Encryption keys you manage]
        C2[Identity & Access · IAM policies · MFA]
        C3[Application configuration · OS hardening in IaaS]
        C4[Network controls you configure · Security groups]
    end

    subgraph Shared["Often Shared / Configured Together"]
        S1[Patch management · depending on service model]
        S2[Logging configuration · retention choices]
    end

    subgraph Provider["Cloud Provider Responsibility"]
        P1[Physical facilities · Hardware]
        P2[Hypervisor · Managed service runtime]
        P3[Global infrastructure · Availability zones]
    end

    Customer --> Shared
    Shared --> Provider
```

**Explanation:** Exact boundaries depend on IaaS vs PaaS vs SaaS. The diagram is a teaching model: the customer is always responsible for data, identity, and the configuration choices they make. Use provider documentation for precise service-level splits.
