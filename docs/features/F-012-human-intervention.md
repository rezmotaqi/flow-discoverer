# F-012 — Human intervention

**Objective / problem.** Let a human complete allowed authentication or review where policy must stop automation.

**Scope and contract.** Persist checkpoint and minimal blocker; hand control to an explicitly authorized headed browser. User finishes permitted manual login, OAuth or OTP. Resume validates resulting origin, identity and permission; isolated authorized profiles are optional. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Do not request user secrets in logs or model inputs; disable recording while auth UI is active. Session files are local, excluded from Git, least privilege, with expiry and invalidation. Never solve CAPTCHA or bypass access controls. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Test manual timeouts, cancellation, secret exclusion, profile isolation and expired or off-origin sessions; validate resume against an authorized fixture only. Test path(s): `tests/test_intervention.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M3; prerequisites: F-001, F-011; source: `src/game_explorer/recording/intervention.py`. Decisions: [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md), [ADR-007](../architecture/ADR/ADR-007-manual-session-security.md), [ADR-008](../architecture/ADR/ADR-008-durable-frontier.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
