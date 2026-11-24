# Dependency map

Feature/task dependency edges are authored in [.project/registry.json](../../.project/registry.json). Use `make context TASK=<id>` for a bounded dependency summary.

Integration order: foundation and core contracts → driver/observation and policy → state/evidence/storage → explorer → offline reports/CLI → fixture integration review. Model and mobile integrations must depend on the contracts, not directly on browser internals.
