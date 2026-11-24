# ActionCandidate

**M1 design only.** Typed action proposed from observed controls. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `source_state_id` | TEXT FK | Required |
| `observation_id` | TEXT FK | Required |
| `semantic_key` | TEXT | Required |
| `kind` | TEXT | Required |
| `descriptor_json` | TEXT | Required |
| `priority` | INTEGER DEFAULT 0 | Required |

**Identity and indexes:** UNIQUE(run_id, source_state_id, semantic_key); (run_id, source_state_id) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Descriptors are bounded data, no executable payload or credentials. Regenerate deterministically as permitted. Classification: Redacted content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
