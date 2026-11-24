# ActionAttempt

**M1 design only.** Durable intent and outcome for an actual execution. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `candidate_id` | TEXT FK | Required |
| `decision_id` | TEXT FK | Required |
| `sequence` | INTEGER | Required |
| `status` | TEXT | Required |
| `started_at` | TEXT | Required |
| `ended_at` | TEXT NULL | Optional |
| `error_code` | TEXT NULL | Optional |

**Identity and indexes:** UNIQUE(run_id, sequence); (run_id, candidate_id, status) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Pending first; finalize once. Timeouts and interruptions can leave uncertainty. Do not store raw exceptions. Classification: Operational. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
