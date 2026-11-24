# FeatureFinding

**M4 design only.** Evidence-backed claim on visible product functionality. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `feature_key` | TEXT | Required |
| `description` | TEXT | Required |
| `classification` | TEXT | Required |
| `evidence_ids` | JSON | Required |
| `confidence` | REAL NULL | Optional |
| `generated_at` | TEXT | Required |

**Identity and indexes:** (run_id, feature_key) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Validate evidence IDs and confidence 0–1; distinguish unknown from absent; store findings as versioned derivations. Classification: Derived content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
