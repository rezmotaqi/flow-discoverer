# F-017 — Android driver

**Objective / problem.** Explore a permitted Android fixture while reusing evidence and planning contracts.

**Scope and contract.** Android adapter uses Appium/UiAutomator2 and a selected emulator or explicitly authorized test device. Map activity, accessibility tree and screenshots to shared observations and actions without imposing browser routes. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** No private apps, other device data, unrestricted ADB access or auth bypass. Device/package context changes stop automation. Explicitly document permission, transport, redaction and restoration before enabling. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Authorized Android fixture exposes equivalent state, policy, graph and report records; device/app mismatch and unknown actions fail closed. Test path(s): `tests/test_android.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M7; prerequisites: F-001, F-002; source: `src/game_explorer/drivers/android.py`. Decisions: [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md), [ADR-009](../architecture/ADR/ADR-009-android-driver-boundary.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
