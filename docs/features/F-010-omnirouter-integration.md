# F-010 — OmniRouter integration

**Objective / problem.** Use optional AI understanding and prioritization without allowing a model to control the browser.

**Scope and contract.** Provider request receives bounded redacted state, objective, eligible IDs, recent outcomes and frontier summary. Return schema-validated ranking, capabilities and usage. Separate planner/vision/analysis models; support configured fallbacks and text-only deterministic operation. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Strict response validation and deterministic fallback for timeout, quota, unsupported schema and hostile input. Bound retries, backoff, concurrency, requests and tokens; cancel cooperatively. Treat model and page text as untrusted. Never forward secrets or entire graph history. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Mock objective-specific rankings, invalid IDs, prompt injection, wrong capability, rate limit, malformed responses and exhausted budget. Live checks are opt-in, scoped and capped. Test path(s): `tests/test_llm.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M2; prerequisites: F-005, F-007; source: `src/game_explorer/llm/`. Decisions: [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md), [ADR-005](../architecture/ADR/ADR-005-bounded-model-provider.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
