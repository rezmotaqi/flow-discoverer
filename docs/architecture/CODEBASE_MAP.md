# Codebase map

| Area under `src/game_explorer` | Public entry / responsibility | Work | Tests |
|---|---|---|---|
| `cli`, `core/config.py`, `fixtures/` | CLI, TargetConfig, authorized synthetic reference app | T-001 | test_foundation |
| `core/models.py`, `drivers/`, `observation/`, `policies/`, `actions/` | Driver, PlaywrightDriver, Observation, discovery, Policy | T-002 / F-001,002,004,005 | test_domain, test_browser |
| `state/`, `storage/`, `exploration/` | fingerprint, SQLite RunStore, BFS explorer and multigraph | T-003 / F-003,006,007,008 | test_domain, test_store, test_browser |
| `evidence/`, `reporting/` | EvidenceFiles, offline reports and graph exports | T-004 / F-009,014 | test_store, test_browser |
| `scripts/project_context.py`, `.project/registry.json` | Context packets, registry/index generation and validation | T-001 / F-022 | test_foundation |

Entities and constraints: [database registry](../database/ENTITY_REGISTRY.md). Contract changes: [interface registry](INTERFACE_REGISTRY.md).
