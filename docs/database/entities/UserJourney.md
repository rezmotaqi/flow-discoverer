# UserJourney

**M4 design only.** Ordered path through known states with provenance and replay status. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `title` | TEXT | Required |
| `transition_ids` | JSON | Required |
| `evidence_ids` | JSON | Required |
| `approval_status` | TEXT DEFAULT unapproved | Required |
| `created_at` | TEXT | Required |

**Identity and indexes:** (run_id, created_at); approval_status Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Only contiguous known traversals; manual and automated actions distinguishable. Store explicit review separately from derived results. Classification: Derived content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
