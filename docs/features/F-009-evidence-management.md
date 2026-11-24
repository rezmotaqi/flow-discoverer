# F-009 — Evidence management

**Objective / problem.** Make factual report claims traceable to portable, immutable evidence.

**Scope and contract.** Evidence store writes content-addressed PNGs and records evidence ID, target/run/state/observation, time, relative path, MIME/hash and redaction disposition. Any derived artifact has separate identity and input references. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Verify bytes and path containment, deduplicate identical blobs without collapsing provenance, apply compression only before assigning the final hash. Budget failures leave an explicit omission, never a dangling reference. Retention needs authorized, recorded deletion and must not silently rewrite history. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** Verify hash, file portability, deduplication, atomic publication, path traversal rejection, redaction metadata, quota and read-after-move. Test path(s): `tests/test_store.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M1; prerequisites: F-002; source: `src/game_explorer/evidence/files.py`. Decisions: [ADR-002](../architecture/ADR/ADR-002-sqlite-evidence.md), [ADR-006](../architecture/ADR/ADR-006-evidence-first-reports.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
