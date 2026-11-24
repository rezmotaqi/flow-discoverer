# F-008 — Persistent storage

**Objective / problem.** Preserve evidence and measurable progress independently of a live browser or model conversation.

**Scope and contract.** Transactional SQLite run/observation/state/candidate/decision/attempt/evidence operations. Use run-scoped foreign keys and identity constraints; version migrations explicitly, and expose only read-only queries to reports. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** No secrets or absolute artifact paths in persistent records. Idempotent inserts where logical uniqueness is defined. On interruption retain open attempts for M3 reconciliation; never assume exactly-once remote browser effects. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Temporary DB tests for rollback, unique identities, FK failure, version mismatch, concurrent reads and interrupted attempts; fixture produces a usable offline snapshot. Test path(s): `tests/test_store.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-003; source: `src/game_explorer/storage/store.py`. Decisions: [ADR-002](../architecture/ADR/ADR-002-sqlite-evidence.md), [ADR-008](../architecture/ADR/ADR-008-durable-frontier.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
