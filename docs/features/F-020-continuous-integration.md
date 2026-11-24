# F-020 — Continuous integration

**Objective / problem.** Make routine QA and documentation verification reproducible in CI.

**Scope and contract.** CI runs lint, types, docs, unit and fixture browser tests; optionally compare approved internal baselines. Keep artifacts private and bounded; retain partial test diagnostics without application secrets. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** No default external exploration or external monitoring. Internal schedules must be explicitly authorized; CI config uses isolated credentials and protected retention/access. Network provider tests remain opt-in. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Run CI on an approved branch, verify no default external target paths, retention policies and evidence preservation on test failure. Test path(s): `tests/test_ci_contract.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M9; prerequisites: F-016, F-022; source: `.github/workflows/`. Decisions: [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md), [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
