# ModelInvocation

**M2 design only.** Usage telemetry without persisted prompts or secrets. See [registry conventions](../ENTITY_REGISTRY.md), [relationships](../RELATIONSHIPS.md) and [migration policy](../MIGRATIONS.md).

| Field | Proposed type / default | Presence |
|---|---|---|
| `id` | TEXT PK | Required |
| `run_id` | TEXT FK | Required |
| `role` | TEXT | Required |
| `model_alias` | TEXT | Required |
| `request_tokens` | INTEGER NULL | Optional |
| `response_tokens` | INTEGER NULL | Optional |
| `latency_ms` | INTEGER | Required |
| `outcome` | TEXT | Required |
| `attempted_at` | TEXT | Required |

**Identity and indexes:** (run_id, role, attempted_at); (run_id, outcome) Foreign keys are scoped to the associated target or run; JSON evidence references need service-level validation if not materialized into join tables.

**Lifecycle, validation and privacy:** Nonnegative metrics, NULL means unavailable. No request/response body, tokens used for authentication, or full provider URLs. Classification: Operational. Delete only through authorized retention with provenance and reference checks; no silent cascade across historical runs.

**Migration:** Introduce only with its milestone and test clean creation, required fields, uniqueness and reference integrity. Preserve existing IDs on later schema changes.
