# F-019 — Internal QA automation

**Objective / problem.** Produce reproducible findings from an explicitly authorized X-Game test environment.

**Scope and contract.** A reviewed QA target profile enumerates scope, synthetic accounts, expected catalog/history, matchmaking/results scenarios and evidence retention. Run reports and approved journey transcripts are reviewed by the owner. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** No production infrastructure or real transactions. Resolve authorization, data boundaries and manual account provisioning outside the repository. Do not infer competitor or X-Game permission from public availability. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Demonstrate auth, profile/history, catalog, matchmaking and result journeys in authorized test scope with reviewer sign-off and portable evidence. Test path(s): `tests/test_internal_qa.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M5; prerequisites: F-007, F-012, F-014; source: `configs/targets/`. Decisions: [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md), [ADR-007](../architecture/ADR/ADR-007-manual-session-security.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
