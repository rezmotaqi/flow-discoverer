# F-018 — Gameplay adapters

**Objective / problem.** Support deterministic practice in authorized isolated QA games without coupling exploration to real-time input.

**Scope and contract.** Versioned registry for Pong, Nine Men’s Morris and Sky Flap. Recognize supported builds, interpret state, send bounded input, detect completion and return score/result evidence with timeout. Cross-component types, callers and effects are indexed in the [interface registry](../architecture/INTERFACE_REGISTRY.md). Persistent records, where applicable, follow the [entity registry](../database/ENTITY_REGISTRY.md).

**Business rules, errors and limits.** Use deterministic game logic and optional light vision, not LLM calls in a control loop. External ranked play, reward farming, unsupported builds and real transactions are prohibited; permitted practice may be recorded manually. See the [rule index](../business/RULES_INDEX.md). Anything outside the stated scope is a non-goal for this feature.

**Acceptance and tests.** For each adapter, verify isolated launch, bounded completion and result provenance; wrong version and attempts outside the test scope fail closed. Test path(s): `tests/test_game_adapters.py`. See [milestone gates](../testing/ACCEPTANCE_CRITERIA.md).

**Implementation / dependencies.** Planned, not implemented or validated. Paths are proposed; check the registry before handoff. M8; prerequisites: F-001, F-005; source: `src/game_explorer/game_adapters/`. Decisions: [ADR-004](../architecture/ADR/ADR-004-fixture-scope.md). Current status: [feature registry](../planning/FEATURE_REGISTRY.md); verification: [validation log](../testing/VALIDATION_STATUS.md).
