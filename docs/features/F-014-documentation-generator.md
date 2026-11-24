# F-014 — Documentation generator

**Objective / problem.** Publish offline documentation from saved evidence, not fresh browsing.

**Scope and contract.** M1: run summary, screens, transitions, derived graph and screenshot manifest. M4: evidence-backed features, journeys, rules, coverage and structured output bundle documented in reporting operations. Reader needs no browser session or provider. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** All links are portable and inputs escaped in rendered HTML, Markdown and structured exports. Claims distinguish observation, advertising, inference and unknowns; coverage never implies completeness without independent state inventory. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Verify offline gallery, searchable findings, evidence ID/hash resolution, graph and journey display, safe rendering of untrusted strings and reproducible deterministic reports. Test path(s): `tests/test_browser.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-006, F-009; source: `src/game_explorer/reporting/offline.py`. Decisions: [ADR-002](../architecture/ADR/ADR-002-sqlite-evidence.md), [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
