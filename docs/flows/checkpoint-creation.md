# Checkpoint creation

**Design, M3.** Feature: [F-011](../features/F-011-resumable-exploration.md).

```mermaid
flowchart LR
  A["Finalize observed outcome"] --> B["Compute new frontier cursor"] --> C["Commit checkpoint revision"] --> D["Retain prior audit history"]
```

An unfinished attempt remains uncertain until reconciled.

**Planned implementation:** `src/game_explorer/exploration/checkpoints.py`. **Planned verification:** `tests/test_recovery.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
