# F-015 — Competitor comparison

**Objective / problem.** Compare authorized saved runs and produce findings that distinguish gaps from limited observation.

**Scope and contract.** Comparison consumes selected run IDs/baselines and evidence, maps standardized dimensions, and exports the comparison bundle in reporting operations. Recommendations state evidence, expected value, dependencies, complexity and unresolved questions. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Observed, Advertised, Inferred, Not observed, Not accessible and Not applicable remain distinct. Missing coverage is not negative evidence; mismatched mode/language/time is surfaced. No fresh exploration or automated application changes. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Compare two fixture versions; prove conflicting observations, insufficient coverage and inaccessible scenarios remain distinct; verify offline HTML/CSV/JSON and evidence references. Test path(s): `tests/test_comparison.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M6; prerequisites: F-013, F-014; source: `src/game_explorer/comparison/`. Decisions: [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
