# Observation

**M1 design only.** One sanitized view, separate from logical state. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `state_id` | TEXT FK | Required |
| `captured_at` | TEXT | Required |
| `route` | TEXT | Required |
| `title` | TEXT | Required |
| `language` | TEXT | Required |
| `auth` | TEXT | Required |
| `modal` | TEXT NULL | Optional |
| `http_status` | INTEGER NULL | Optional |
| `payload_json` | TEXT | Required |
| `redaction` | TEXT | Required |

**Identity and indexes:** (run_id, state_id, captured_at) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Append-only; preserve bounded, redacted originals. Never store input values, raw DOM or session data. Classification: Redacted content. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
