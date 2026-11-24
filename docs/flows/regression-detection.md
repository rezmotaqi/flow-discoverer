# Regression detection

**Design, M9.** Feature: [F-016](../features/F-016-regression-detection.md).

```mermaid
flowchart LR
  A["Select comparable same-target runs"] --> B["Normalize dynamic noise and align states"] --> C["Compare transitions, features, rules and visuals"] --> D["Report evidence and replay candidates"]
```

Report incomplete runs as such; generated tests remain review-only.

**Planned implementation:** `src/game_explorer/analysis/regression.py`. **Planned verification:** `tests/test_regression.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
