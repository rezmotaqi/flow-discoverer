# Transition

**M1 design only.** Multigraph edge with outcome; target may be unknown. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `from_state_id` | TEXT FK | Required |
| `to_state_id` | TEXT FK NULL | Optional |
| `attempt_id` | TEXT FK NULL | Optional |
| `via` | TEXT | Required |
| `outcome` | TEXT | Required |
| `occurred_at` | TEXT | Required |

**Identity and indexes:** (run_id, from_state_id); (run_id, to_state_id); attempt_id unique when non-null Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Parallel edges/self-loops retained. Only successful traversable edges are used for known paths. M1 may project from attempts instead of a separate table. Classification: Redacted content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
