# SOC Detection Pipeline (Simplified)

Supports Phase-2 logging/detection and Phase-3 Track 2.

```mermaid
flowchart LR
    S1[Log / Telemetry<br/>Sources] --> S2[Collection &<br/>Normalization]
    S2 --> S3[Parsing &<br/>Enrichment]
    S3 --> S4[Detection<br/>Rules / Models]
    S4 --> S5[Alert]
    S5 --> S6[Triage]
    S6 -->|True Positive| S7[Investigation / IR]
    S6 -->|False Positive| S8[Tune / Suppress]
    S7 --> S9[Contain · Eradicate · Recover]
    S8 --> S4
    S9 --> S10[Lessons · New detections]
    S10 --> S4
```

**Explanation:** Detection is a loop. False positives drive tuning; true positives drive investigation and, after resolution, new or improved detections. In the lab, practice each stage with controlled, authorized data.
