# PolicyDecision

**M1 design only.** Auditable result of evaluating a candidate against current scope. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `candidate_id` | TEXT FK | Required |
| `policy_version` | TEXT | Required |
| `checked_at` | TEXT | Required |
| `allowed` | INTEGER | Required |
| `reason_code` | TEXT | Required |

**Identity and indexes:** (run_id, candidate_id, checked_at); (run_id, allowed) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Allowed is 0/1; retain denials and rechecks. Policy reasons are enums, not unsafe page content. Classification: Operational. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
