# Navigation graph updates

**Design, M1.** Feature: [F-006](../features/F-006-navigation-graph.md).

```mermaid
flowchart LR
  A["Persist allowed attempt intent"] --> B["Execute and observe result"] --> C["Commit outcome and optional destination"] --> D["Read directed multigraph projection"]
```

Failures retain the attempt without a fabricated destination.

**Planned implementation:** `src/game_explorer/storage/store.py`. **Planned verification:** `tests/test_store.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
