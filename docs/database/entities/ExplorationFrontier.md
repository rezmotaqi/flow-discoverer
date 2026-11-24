# ExplorationFrontier

**M3 design only.** Durable queue of remaining state/candidate work. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `state_id` | TEXT FK | Required |
| `candidate_id` | TEXT FK NULL | Optional |
| `order_key` | INTEGER | Required |
| `depth` | INTEGER | Required |
| `status` | TEXT DEFAULT pending | Required |
| `checkpoint_revision` | INTEGER | Required |

**Identity and indexes:** (run_id, status, order_key); unique logical work key per run Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Version order; lease work to one active owner, reconcile uncertain items instead of replaying. Classification: Operational. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
