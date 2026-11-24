# Logical data relationships

Design baseline; no SQLite schema is implemented. JSON reference lists may be normalized to join tables. The [entity registry](ENTITY_REGISTRY.md) defines field contracts and milestone boundaries.

```mermaid
erDiagram
  TARGET ||--o{ RUN : scopes
  RUN ||--o{ OBJECTIVE : snapshots
  RUN ||--o{ STATE : discovers
  RUN ||--o{ CHECKPOINT : commits
  RUN ||--o{ INVOCATION : meters
  STATE ||--o{ OBSERVATION : groups
  OBSERVATION ||--o{ EVIDENCE : supports
  STATE ||--o{ CANDIDATE : offers
  CANDIDATE ||--o{ POLICY_DECISION : checks
  CANDIDATE ||--o{ ATTEMPT : executes
  POLICY_DECISION ||--o{ ATTEMPT : authorizes
  STATE ||--o{ TRANSITION : source
  STATE o|--o{ TRANSITION : destination
  ATTEMPT o|--o| TRANSITION : records
  STATE ||--o{ FRONTIER : queues
  RUN ||--o{ FEATURE_FINDING : derives
  RUN ||--o{ BUSINESS_RULE : derives
  RUN ||--o{ USER_JOURNEY : derives
  TRANSITION }o--o{ USER_JOURNEY : traverses
  EVIDENCE }o--o{ FEATURE_FINDING : supports
  EVIDENCE }o--o{ BUSINESS_RULE : supports
  RUN }o--o{ COMPARISON_FINDING : compares
  EVIDENCE }o--o{ COMPARISON_FINDING : supports
```
