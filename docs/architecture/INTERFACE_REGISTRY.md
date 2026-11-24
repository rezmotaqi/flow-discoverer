# Interface registry

| Contract | Inputs → outputs | Errors / effects | Consumer |
|---|---|---|---|
| Browser driver (`core.models.Driver`) | validated start URL, observation and resolved candidate → `Capture` or action completion | Browser session only; typed execution error | Explorer |
| Observation (`core.models.Observation`) | sanitized title/route/structured text, elements, language, HTTP/modal/auth markers → immutable data | No raw DOM, credentials or executable instructions | State/action/report |
| State (`state.recognize.fingerprint`) | Observation → versioned logical state hash | Pure; preserves meaningful controls and semantic markers | Explorer/storage |
| Action (`core.models.Candidate`) | typed kind and observed element → stable ID | No executable payload; selectors live only in the adapter | Policy/driver |
| Policy (`policies.scope.Policy`) | target, observed candidate → allowed / denied + reason | Pure; deny by default; check again before execution | Explorer/driver |
| Planner (`exploration.engine`) | observations and BFS frontier → bounded next action | Never override policy; fail closed on replay drift | Explorer |
| Evidence (`evidence.files.EvidenceFiles`) | redacted PNG → relative content-addressed file and checksum | Writes immutable files, raises on budget or collision | Browser pipeline/storage/reporting |
| Reporting (`reporting.offline`) | persisted run snapshot → portable artifacts | No network, no raw executable content | CLI |
| Android / LLM / comparison | Future contracts, not implemented | Model may propose candidate IDs only; comparison reads stored evidence | M2 / M6 / M7 |

`core.models` is shared and provider-neutral. The test mapping is in [TEST_MAP](../testing/TEST_MAP.md).

## Planned extension contracts

| Interface and consumer | Input → output | Boundary and validation |
|---|---|---|
| `LLMProvider`, advisory planner and analysis | Budgeted redacted request → typed recommendation/classification plus nullable usage | Provider errors or invalid IDs trigger deterministic fallback; no driver/tools. F-010 / `test_llm`. |
| `CheckpointStore`, recovery and recording | Scoped run/expected revision + cursor → new checkpoint or conflict | Atomic compare-and-advance; pending attempt reconciled separately. F-011 / `test_recovery`. |
| `AndroidDriver`, planner | Scoped package/activity and validated candidate → provider-neutral capture or outcome | No browser URL requirement or generic ADB execution. F-017 / `test_android`. |
| `ComparisonService`, CLI/reporting | Compatible run snapshots and evidence → classified findings and coverage caveats | Read-only, no live target; missing or incompatible evidence remains unknown. F-015 / `test_comparison`. |

Compatibility: publish schema versions for persistent state IDs and external artifacts; coordinate any breaking contract change with downstream feature owners. Report plan names and proposed types as such until integration tests verify them. See the [test map](../testing/TEST_MAP.md).
