# F-001 — Browser automation driver

**Objective / problem.** Provide an isolated browser driver for real rendered QA surfaces, not an HTTP-only scraper.

**Scope and contract.** Launch/close and navigate in a fresh browser context; expose readiness, validated link/button execution and capture via the provider-neutral Driver protocol. Reserve fill, select, keyboard, scroll, back/reload and session restore for verified extensions. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Exact fixture origin and document routes; deny unsupported methods, redirects, new contexts and connections outside policy. Never forward browser exception details that may contain data. Bound operation time, close context even on failure, and handle 404 as an observed result rather than inventing a destination. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Real Chromium launches; an allowed link and in-page modal work; off-origin, redirect, download and POST attempts are blocked; context state does not leak across runs. Test path(s): `tests/test_browser.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-022; source: `src/game_explorer/drivers/playwright.py`. Decisions: [ADR-001](../architecture/ADR/ADR-001-python-chromium.md), [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
