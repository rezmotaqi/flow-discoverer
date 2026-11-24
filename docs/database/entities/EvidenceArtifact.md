# EvidenceArtifact

**M1 design only.** Provenance for an immutable local artifact. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `target_id` | TEXT FK | Required |
| `run_id` | TEXT FK | Required |
| `state_id` | TEXT FK | Required |
| `observation_id` | TEXT FK | Required |
| `captured_at` | TEXT | Required |
| `relative_path` | TEXT | Required |
| `kind` | TEXT | Required |
| `sha256` | TEXT | Required |
| `byte_count` | INTEGER | Required |
| `redaction` | TEXT | Required |

**Identity and indexes:** (run_id, observation_id); (run_id, sha256); UNIQUE(observation_id, kind, sha256) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Path must be contained, hash verified, bytes append-only and optionally deduplicated. Report omissions explicitly. Classification: Redacted evidence. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
