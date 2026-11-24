# F-004 — Action discovery

**Objective / problem.** Expose discoverable interactions as bounded data instead of executable commands.

**Scope and contract.** Observation → deterministic candidate IDs with source state, action type, element, description, expected outcome, risk, required scope and priority. M1 supports links and approved local buttons; typed fill, select, scroll, wait, back and intervention require their own policies. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Prefer stable semantics. Missing, duplicate or ambiguous targets fail closed; do not click a stale locator. Unsupported, hidden or disabled controls are not executed. Model output can propose only a previously supplied candidate ID. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Test equivalent semantic keys, duplicates, unknown actions, disabled controls, sensitive forms, untrusted text and expected denial metadata. Test path(s): `tests/test_domain.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-002; source: `src/game_explorer/actions/discover.py`. Decisions: [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md), [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
