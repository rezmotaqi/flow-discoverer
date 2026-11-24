# BusinessRule

**M4 design only.** Evidence-grounded observed behavior or stated product rule. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `feature_area` | TEXT | Required |
| `description` | TEXT | Required |
| `conditions_json` | TEXT | Required |
| `inputs_json` | TEXT | Required |
| `outputs_json` | TEXT | Required |
| `evidence_ids` | JSON | Required |
| `confidence` | REAL NULL | Optional |
| `exceptions_json` | TEXT | Required |
| `questions_json` | TEXT | Required |
| `classification` | TEXT | Required |

**Identity and indexes:** (run_id, feature_area); (run_id, classification) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Five documented classifications; observed and advertised require relevant evidence. Preserve contradictions and unresolved questions. Classification: Derived content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
