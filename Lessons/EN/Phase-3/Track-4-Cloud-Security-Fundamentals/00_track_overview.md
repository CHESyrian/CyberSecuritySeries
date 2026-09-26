# Track 4 · Cloud Security Fundamentals  
## Shared Responsibility, Identity, and Safe Cloud Lab Habits

**Who this track is for**  
Learners who finished Phase-2 and want a **vendor-agnostic** foundation for cloud security: who is responsible for what, how identity becomes the new perimeter, and how common misconfigurations appear—practiced only in lab, free-tier, or emulator environments you control.

**What you will be able to do by the end**
- Explain the shared responsibility model in plain language
- Apply least-privilege thinking to cloud IAM concepts
- Recognize common storage and network exposure mistakes
- Describe cloud logging/monitoring building blocks
- Produce a security checklist for a minimal cloud or cloud-like lab stack

---

## Prerequisites

- Phase-2 complete (identity, network, logging, crypto stages help most)
- Willingness to use **only** accounts/projects you own (personal lab/free tier/local emulator)
- No production cloud accounts with real customer data

---

## Track organization

| Stage | File | Focus |
|-------|------|-------|
| 0 | This file | Track map, outcomes, safety |
| 4.1 | `01_shared_responsibility.md` | Provider vs customer duties |
| 4.2 | `02_identity_and_least_privilege.md` | Users, roles, keys, temporary credentials *concepts* |
| 4.3 | `03_network_and_exposure.md` | Public endpoints, security groups/NSG ideas, metadata risks (conceptual) |
| 4.4 | `04_storage_and_data.md` | Bucket/blob exposure patterns; encryption at rest *ideas* |
| 4.5 | `05_logging_and_detection_cloud.md` | Audit trails, why central logs matter |
| 4.6 | `06_secure_baseline_checklist.md` | Minimal secure starting point |
| 4.7 | `07_track_capstone_cloud_checklist.md` | Checklist + short risk notes for your lab stack |

---

## Lab setup notes

Preferred options (pick what you can afford/control):

| Option | Notes |
|--------|--------|
| Local emulators / localstack-style tools | No public cloud spend |
| Single free-tier account **you own** | Tight budget alerts; never real secrets in git |
| Cloud-like Kubernetes local cluster | Optional later depth |

**Safety:** Never use employer production accounts for experiments. Enable billing alarms if using paid cloud. Delete open resources after labs.

---

## Safety checkpoints (Track 4)

1. Only cloud projects/accounts registered to you for learning.  
2. No embedding long-lived access keys in code repositories.  
3. Do not scan or attack other tenants’ resources.  
4. Treat public-read storage labs as intentional demos—close them when finished.

---

## Stage summaries

### 4.1 — Shared responsibility  
What the provider secures vs what you must configure; examples for IaaS vs PaaS vs SaaS at a high level.

### 4.2 — Identity and least privilege  
Human vs workload identity; roles over broad admin; rotation and short-lived credentials as goals.

### 4.3 — Network and exposure  
“Default open” anti-patterns; administrative endpoints; metadata service awareness (conceptual).

### 4.4 — Storage and data  
World-readable buckets as a classic failure; encryption and access policies as controls.

### 4.5 — Logging and detection in cloud  
Why API audit logs matter; link to Track 2 skills; retention and who can read logs.

### 4.6 — Secure baseline checklist  
A short, actionable list for a minimal lab deployment (identity, network, storage, logging).

### 4.7 — Capstone  
Apply the checklist to your chosen lab stack; note residual risks and follow-ups.

---

## Companion code

| Area | Location |
|------|----------|
| General crypto/hash | `Codes/Python/08_cryptography/`, `Codes/Bash/08_cryptography/` |
| Track 4 extensions | Policy/checklist generators or safe CLI wrappers added later under `Codes/` |

Vendor CLIs (AWS/Azure/GCP) are optional and only against **your** lab projects.

---

## Deliverables checklist

- [ ] Written shared-responsibility summary for one service model you use  
- [ ] IAM least-privilege notes for a sample lab role  
- [ ] Exposure review (network + storage) for the lab stack  
- [ ] Capstone checklist completed with dated evidence  

---

## How Track 4 relates to other tracks

- **Track 3:** Segmentation and hardening map to cloud network controls.  
- **Track 2:** Cloud audit logs feed the same detection mindset.  
- **Track 1:** Web apps often sit on cloud load balancers and object storage.  
- **Track 5:** Cloud misconfigurations are a common *initial access* story in real breaches—studied here defensively.

---

## Important boundary

Cloud privileges can destroy data and incur cost quickly. This track prioritizes understanding and checklists over aggressive offensive cloud techniques.

**Next step:** When published, start `01_shared_responsibility.md`; meanwhile, inventory any cloud resources you already own and confirm they are lab-only.
