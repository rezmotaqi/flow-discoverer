# ApplicationState

**M1 design only.** Versioned logical screen identity. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `fingerprint` | TEXT | Required |
| `algorithm_version` | TEXT | Required |
| `route` | TEXT | Required |
| `classification` | TEXT NULL | Optional |
| `first_depth` | INTEGER | Required |
| `first_seen_at` | TEXT | Required |

**Identity and indexes:** UNIQUE(run_id, algorithm_version, fingerprint); (run_id, route) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Depth ≥ 0 and nonempty signature; preserve distinct modal/auth/meaningful states. Classification: Redacted content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
