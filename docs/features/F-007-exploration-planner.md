# F-007 — Exploration planner

**Objective / problem.** Expand useful fixture states reproducibly without unbounded loops or hidden actions.

**Scope and contract.** Deterministic BFS over state identities; enumerate and record candidate decisions once per source, restore known paths and recheck identity, stop on frontier exhaustion or named limits. Future AI may reorder eligible candidates, never execute them. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Bound state count, action/depth quotas, duration, storage and per-state attempts; count replay interactions, enforce delay, and reconcile uncertain transitions before any retry. Report replay drift, depth and omitted branches. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Fixture reference states and representative journey found; loops terminate, limits cause explicit incomplete outcomes, repeated runs produce equivalent normalized topology. Test path(s): `tests/test_browser.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-005, F-006, F-009; source: `src/game_explorer/exploration/engine.py`. Decisions: [ADR-002](../architecture/ADR/ADR-002-sqlite-evidence.md), [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md), [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
