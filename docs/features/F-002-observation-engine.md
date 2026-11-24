# F-002 — Observation engine

**Objective / problem.** Capture rendered user-visible facts without collecting raw page data or credentials.

**Scope and contract.** Return Observation plus optional Capture bytes: timestamp/provenance at persistence, route, title, heading, sanitized visible text, roles/names, safe link metadata, modal/auth status, HTTP/error/readiness signals, language and viewport. Bounding boxes are optional. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Keep original Persian/RTL text separately from normalization; bound output; omit hidden text, volatile markers and sensitive values. Explicitly record screenshot suppression. Never persist raw DOM or cookies; general-site redaction is not implied by fixture masking. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Fixture captures Persian, a modal and a broken route; screenshot/text do not contain seeded email or credential fields; oversized data is truncated explicitly. Test path(s): `tests/test_browser.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-001; source: `src/game_explorer/observation/snapshot.py`. Decisions: [ADR-001](../architecture/ADR/ADR-001-python-chromium.md), [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
