# ComparisonFinding

**M6 design only.** A conclusion or uncertainty across evidence from selected runs. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `comparison_key` | TEXT | Required |
| `dimension` | TEXT | Required |
| `input_run_ids` | JSON | Required |
| `evidence_ids` | JSON | Required |
| `classification` | TEXT | Required |
| `description` | TEXT | Required |
| `recommendation_json` | TEXT NULL | Optional |
| `created_at` | TEXT | Required |

**Identity and indexes:** (comparison_key, dimension); (comparison_key, classification) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Require source provenance and coverage qualification. Never trigger fresh browsing or product changes. Classification: Derived content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
