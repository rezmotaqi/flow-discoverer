# Target

**M1 design only.** Authorized application and versioned scope. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `display_name` | TEXT | Required |
| `platform` | TEXT | Required |
| `origin_or_package` | TEXT | Required |
| `scope_fingerprint` | TEXT | Required |
| `config_json` | TEXT | Required |
| `created_at` | TEXT | Required |

**Identity and indexes:** id; unique scope revision if multiple snapshots are stored Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Configuration may evolve; prior run scope fingerprints remain immutable. Never store auth values. Classification: Operational scope. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
