# F-006 — Navigation graph

**Objective / problem.** Preserve observed user journeys, including failures, loops, parallel actions and unknown destinations.

**Scope and contract.** Run store exposes a directed multigraph of states and attempts. Export stable JSON, Mermaid, GraphML and offline HTML; compute shortest traversable paths over successful edges only. Preserve evidence and outcomes per edge. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Do not create a destination for denied or failed actions unless independently observed; represent self loops and alternative actions separately. Escaped labels are inert. Authentication boundaries and unexplored leaves are distinct. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Check two actions between the same states, self loop, HTTP failure, evidence linkage and shortest path. Round-trip the supported export formats without network. Test path(s): `tests/test_store.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-003, F-008; source: `src/game_explorer/storage/store.py`. Decisions: [ADR-002](../architecture/ADR/ADR-002-sqlite-evidence.md), [ADR-003](../architecture/ADR/ADR-003-policy-first-bfs.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
