# ExplorationObjective

**M2 design only.** Typed objective snapshot defining prioritization. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `kind` | TEXT DEFAULT general | Required |
| `instruction` | TEXT NULL | Optional |
| `constraints_json` | TEXT | Required |

**Identity and indexes:** run_id; (run_id, id) unique for scoped references Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Immutable per run revision; custom instructions are redacted and cannot change authorization. Classification: Operational. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
