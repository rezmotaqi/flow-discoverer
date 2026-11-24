# ADR-005 — Bound the advisory model layer

**Status / features:** Proposed • F-010, F-013.

**Decision and context.** Keep browser authority and deterministic fallback local. Use a configurable OpenAI-compatible provider for ranking, vision and analysis; validate typed results and charge a bounded budget per operation.

**Alternatives and reasoning.** A model-controlled browser and mandatory server conversations make policy enforcement and repeatability harder. A purely deterministic mode remains useful and must work independently.

**Consequences and trade-offs.** Use disposable redacted requests, strategy-specific capability metadata, mock contract tests and safe fallbacks. Cap both latency and estimated token spend; actual usage may be unavailable.
