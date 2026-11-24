# ExplorationRun

**M1 design only.** Lifecycle, budgets, build and target scope for one execution. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `target_id` | TEXT FK | Required |
| `scope_fingerprint` | TEXT | Required |
| `mode` | TEXT | Required |
| `status` | TEXT DEFAULT running | Required |
| `started_at` | TEXT | Required |
| `finished_at` | TEXT NULL | Optional |
| `stop_reason` | TEXT NULL | Optional |
| `limits_json` | TEXT | Required |
| `producer_version` | TEXT | Required |

**Identity and indexes:** target_id, started_at; status Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Create before automation, finalize with explicit status and reason; unfinished runs are incomplete. Classification: Operational. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
