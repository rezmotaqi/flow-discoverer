# Action validation

**Design, M1.** Feature: [F-005](../features/F-005-safety-policy-engine.md).

```mermaid
flowchart LR
  A["Read candidate and scope"] --> B["Check origin, route, mode and action"] --> C["Record allow or deny"] --> D["Recheck immediately at execution"]
```

A stale candidate, sensitive action or unexpected network request stops execution.

**Planned implementation:** `src/game_explorer/policies/scope.py`. **Planned verification:** `tests/test_domain.py`; see the [test map](../testing/TEST_MAP.md) for current versus future checks.
