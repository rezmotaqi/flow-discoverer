# Llm action selection

**Design, M2.** Feature: [F-010](../features/F-010-omnirouter-integration.md).

```mermaid
flowchart LR
  A["Build bounded redacted context"] --> B["Check model capabilities and budget"] --> C["Validate ranking of supplied IDs"] --> D["Policy rechecks eligible candidate"]
```

Provider failure or invalid output falls back to deterministic ordering.

**Planned implementation:** `src/game_explorer/llm/`. **Planned verification:** `tests/test_llm.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
