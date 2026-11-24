# F-021 — Human-guided recording

**Objective / problem.** Capture a permitted manual journey through UI paths that automation should not attempt.

**Scope and contract.** A headed recording session uses shared observation, evidence and graph layers. User starts/stops, adds approved notes, marks important screens and explicitly pauses sensitive steps; exported journey separates human from automatic edges. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Opening a login or sensitive boundary suppresses screenshots/text until policy authorizes recording again. No recording of passwords, OTP, other users’ private data or unapproved scope. Manual logs must not become executable replay by default. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Record a fixture journey with note and marked screen; simulate privacy boundary, cancellation and off-origin navigation; verify evidence is absent for suppressed steps. Test path(s): `tests/test_recording.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M3; prerequisites: F-002, F-009, F-012; source: `src/game_explorer/recording/session.py`. Decisions: [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md), [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md), [ADR-007](../architecture/ADR/ADR-007-manual-session-security.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
