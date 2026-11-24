# Test map

**Implemented:** `tests/test_foundation.py` covers CLI, configuration, fixture HTTP behavior and project metadata.

| Stage | Planned suites | Key evidence |
|---|---|---|
| M1 | `test_domain`, `test_store`, `test_browser` | Persian and state identity, candidate/policy denial, persistence, evidence integrity, real-browser fixture graph and offline report |
| M2 | `test_llm` | Mock provider, objective ordering, schema/capability, injection rejection, budgets and failure recovery |
| M3 | `test_recovery`, `test_intervention`, `test_recording` | Forced interruption, deduplication, permission/scope/profile isolation, human journey recording |
| M4 | `test_analysis`, `test_browser` | Evidence classifications, reports and portable provenance |
| M5/M6 | `test_internal_qa`, `test_comparison` | Authorized test journeys and offline competitor matrix |
| M7/M8 | `test_android`, `test_game_adapters` | Authorized fixture state and deterministic result handling |
| M9 | `test_regression`, `test_ci_contract` | Normalized baselines, safe replay, no default external schedules |

See [verified runs](VALIDATION_STATUS.md), [test strategy](TEST_STRATEGY.md) and [acceptance gates](ACCEPTANCE_CRITERIA.md).
