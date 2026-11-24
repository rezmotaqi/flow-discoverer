# F-005 — Safety policy engine

**Objective / problem.** Enforce user authorization independently of planner behavior.

**Scope and contract.** Policy.evaluate(scope, state, candidate) → allow/deny, reason and version. Runtime revalidation checks current state, action identity and browser transport; record all decisions, including denials. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Default deny for unknown actions, links outside scope, form submits, payment, account changes, ranked play, secrets and non-approved external activity. M1 only serves the bundled fixture. Future external/internal policies must not weaken shared prohibitions or rely on webpage claims. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Tests show invalid schemes, deceptive origin forms, stale DOM, state-changing actions, off-origin requests and redirects fail closed. Prompt text cannot grant permissions. Test path(s): `tests/test_domain.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-004; source: `src/game_explorer/policies/scope.py`. Decisions: [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md), [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
