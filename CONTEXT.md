# Project context

Game Explorer discovers authorized application states and journeys, records evidence, and will compare features and business rules without treating missing coverage as absence. The first customer use case is X-Game product benchmarking and QA.

Python 3.12, Playwright Chromium, Typer, Pydantic YAML config, SQLite and offline reports. The core owns authorization and execution; optional AI planning is a later layer. M0 establishes the development foundation and fixture; M1 is deterministic, loopback-only fixture exploration. No external target or production environment is enabled.

Start with [current status](PROJECT_STATUS.md), then [task registry](docs/planning/TASK_REGISTRY.md) and `make context TASK=<id>`. For cross-component work use the [contracts](docs/architecture/INTERFACE_REGISTRY.md) and [codebase map](docs/architecture/CODEBASE_MAP.md). For releases and deferred scope see the [roadmap](docs/planning/ROADMAP.md). For installation and use see [README](README.md). For continuation see [handoff](CONTEXT_HANDOFF.md).
