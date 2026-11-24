# F-016 — Regression detection

**Objective / problem.** Identify meaningful application changes and candidate regressions between comparable runs.

**Scope and contract.** Diff same-target runs by normalized states, transitions, visible features, rule evidence, authentication boundaries and visual differences. Replay only approved fixture journeys under current policy. Export candidate Playwright tests as review-only artifacts. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Do not infer removal from missing coverage, equivalent environment differences or failure to authenticate. Dynamic noise normalization must not mask meaningful changes. Never execute unrestricted generated test code. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Compare fixture revisions, test incomplete coverage and dynamic noise, replay approved actions and reject changed policy or identity; include old and new evidence. Test path(s): `tests/test_regression.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M9; prerequisites: F-006, F-011, F-014; source: `src/game_explorer/analysis/regression.py`. Decisions: [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md), [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md), [ADR-008](../architecture/ADR/ADR-008-durable-frontier.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
