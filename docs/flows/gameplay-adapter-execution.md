# Gameplay adapter execution

**Design, M8.** Feature: [F-018](../features/F-018-gameplay-adapters.md).

```mermaid
flowchart LR
  A["Recognize approved game and version"] --> B["Interpret local test state"] --> C["Issue bounded deterministic input"] --> D["Capture completion and score evidence"]
```

Stop on timeout or scope mismatch; prohibit external ranked play.

**Planned implementation:** `src/game_explorer/game_adapters/`. **Planned verification:** `tests/test_game_adapters.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
