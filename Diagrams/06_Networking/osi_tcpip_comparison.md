# OSI Model vs TCP/IP Model

Used in Foundations and Phase-1 networking lessons.

```mermaid
flowchart TB
    subgraph OSI["OSI 7-Layer Model"]
        O7[7 · Application]
        O6[6 · Presentation]
        O5[5 · Session]
        O4[4 · Transport]
        O3[3 · Network]
        O2[2 · Data Link]
        O1[1 · Physical]
        O7 --> O6 --> O5 --> O4 --> O3 --> O2 --> O1
    end

    subgraph TCP["TCP/IP Model"]
        T4[Application<br/>HTTP · DNS · TLS · SSH]
        T3[Transport<br/>TCP · UDP]
        T2[Internet<br/>IP · ICMP · Routing]
        T1[Network Access<br/>Ethernet · Wi-Fi · MAC]
        T4 --> T3 --> T2 --> T1
    end

    O7 -.-> T4
    O6 -.-> T4
    O5 -.-> T4
    O4 -.-> T3
    O3 -.-> T2
    O2 -.-> T1
    O1 -.-> T1
```

**Explanation:** The OSI model is a teaching and reference model; TCP/IP is the model actually used on the internet. Mapping between them helps place security controls (e.g., firewalls at Network/Internet, TLS at Application/Presentation, segmentation at Data Link/Network).
