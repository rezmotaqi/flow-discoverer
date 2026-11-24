# F-003 — State fingerprinting

**Objective / problem.** Recognize logical application states even when URLs are shared or visual noise changes.

**Scope and contract.** Pure fingerprint(Observation) → versioned state signature. Use canonical route, structure, text, available controls, auth, modal and HTTP class. Persist observation independently and record the fingerprint algorithm version. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Normalize contrasting Persian/Arabic variants, whitespace and explicit volatility, not permission or meaningful business distinctions. Stable serialization is required across runs. Unknown auth must not merge into known authorization. Semantic similarity and perceptual hashes are later, conservative opt-ins. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Unit fixtures cover stable clock changes, Persian equivalents, distinct modal/play/permission states and rejection of false merges. Real Chromium matches the fixture reference graph. Test path(s): `tests/test_domain.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-002; source: `src/game_explorer/state/recognize.py`. Decisions: [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
