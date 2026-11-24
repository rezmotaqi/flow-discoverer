# Interrupted run recovery

**Design, M3.** Feature: [F-011](../features/F-011-resumable-exploration.md).

```mermaid
flowchart LR
  A["Load last checkpoint"] --> B["Acquire single owner and restore scope"] --> C["Reconcile actual state and pending intent"] --> D["Resume safe remaining frontier"]
```

Stop for manual review if profile identity or side effects are uncertain.

**Planned implementation:** `src/game_explorer/exploration/checkpoints.py`. **Planned verification:** `tests/test_recovery.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
