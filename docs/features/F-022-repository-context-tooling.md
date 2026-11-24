# F-022 — Repository context tooling

**Objective / problem.** Make repository context reusable without repeated indexing or cross-agent contract drift.

**Scope and contract.** Canonical registry → generated feature/task/component/dependency indexes; CLI prints bounded task packet and validates links, dependencies, state and evidence. Root onboarding, scope ownership and handoff provide minimal entry. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Do not bundle repository contents or infer implementation from file existence. Planned references explicitly say planned; acceptance requires recorded approval. Shared schemas and integration changes require coordination. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Verify generated index drift, invalid dependencies, missing links, spec coverage and project task packet output with test_foundation; keep working tree and remote state explicit in handoff. Test path(s): `tests/test_foundation.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Implemented and tested; see the verification record. M0; prerequisites: none; source: `scripts/project_context.py`, `.project/registry.json`. Decisions: [agent workflow](../agent/DEVELOPMENT_WORKFLOW.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
