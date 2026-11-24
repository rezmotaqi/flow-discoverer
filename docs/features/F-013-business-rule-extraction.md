# F-013 — Business rule extraction

**Objective / problem.** Document visible product rules without presenting marketing claims or guesses as verified internals.

**Scope and contract.** Analyze redacted observations into typed rules with feature, conditions, inputs/outputs, evidence IDs, confidence, exceptions and unresolved questions. Preserve raw observed phrase separately from interpretation. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Labels: OBSERVED, ADVERTISED, INFERRED, CONTRADICTORY, UNKNOWN. Important claims require evidence, contradictions retain both sides, and private architecture/revenue/security assumptions are excluded. Reject invented evidence IDs or unverified translations. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Fixture proves observed mock score, advertised tournament eligibility, conflicts, unknowns and Persian evidence mapping. Mock malformed or hallucinated model results. Test path(s): `tests/test_analysis.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M4; prerequisites: F-002, F-009, F-010; source: `src/game_explorer/analysis/rules.py`. Decisions: [ADR-005](../architecture/ADR/ADR-005-bounded-model-provider.md), [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
