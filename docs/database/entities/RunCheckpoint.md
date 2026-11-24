# RunCheckpoint

**M3 design only.** Versioned cursor for safe recovery. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `revision` | INTEGER | Required |
| `state_id` | TEXT FK NULL | Optional |
| `pending_attempt_id` | TEXT FK NULL | Optional |
| `scope_fingerprint` | TEXT | Required |
| `profile_ref` | TEXT NULL | Optional |
| `cursor_json` | TEXT | Required |
| `created_at` | TEXT | Required |

**Identity and indexes:** UNIQUE(run_id, revision); (run_id, created_at) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Commit with frontier revision/attempt outcomes where possible. Only opaque profile refs; validate schema/scope and actual state. Classification: Restricted metadata. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
