# F-011 — Resumable exploration

**Objective / problem.** Recover interrupted runs without forgetting work or replaying uncertain side effects.

**Scope and contract.** Commit frontier and proposed action intent, then outcome and checkpoint with monotonically increasing revision. resume(run_id) acquires one owner and validates schema, scope, session and actual state before selecting pending work. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Completed attempts and committed evidence remain immutable. An uncertain action becomes a reconciliation/manual stop, not an automatic retry. Missing/mismatched checkpoint or profile fails closed; cancellation saves safe progress. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Force process interruption around attempt boundaries, resume without duplicate completed actions, reject second writers and profile drift, keep prior evidence hashes. Test path(s): `tests/test_recovery.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M3; prerequisites: F-007, F-008; source: `src/game_explorer/exploration/checkpoints.py`. Decisions: [ADR-002](../architecture/ADR/ADR-002-sqlite-evidence.md), [ADR-008](../architecture/ADR/ADR-008-durable-frontier.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
