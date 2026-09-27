# Example Isolated Lab Topology

Recommended minimal layout for Phase-2 practical work.

```mermaid
flowchart TB
    subgraph Host["Host Machine"]
        HYP[Hypervisor<br/>VirtualBox / VMware]
    end

    subgraph LAB["Isolated Lab Network · e.g. 192.168.56.0/24"]
        ATT[Attacker VM<br/>Kali / similar<br/>192.168.56.10]
        TGT1[Target VM 1<br/>Intentionally vulnerable<br/>e.g. Metasploitable]
        TGT2[Target VM 2<br/>DVWA / Juice Shop]
        LOG[Optional Log / SIEM VM]
    end

    HYP --> ATT
    HYP --> TGT1
    HYP --> TGT2
    HYP --> LOG

    ATT -.->|authorized only| TGT1
    ATT -.->|authorized only| TGT2
    TGT1 -.-> LOG
    TGT2 -.-> LOG
```

**Explanation:** All offensive and defensive exercises stay inside the isolated lab network. No routing to the public internet for attack traffic. Snapshots before major changes are strongly recommended. This topology supports Phase-2 stages and Phase-3 tracks that require hands-on work.
