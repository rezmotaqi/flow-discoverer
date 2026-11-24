# ADR-008 — Recover from durable intent and observation

**Status / features:** Proposed • F-008, F-011.

**Decision and context.** Persist attempt intent and committed outcome separately; reconcile actual state before retry. Serialize checkpoint revision and use a single active writer per run.

**Alternatives and reasoning.** Exactly-once browser effects are not guaranteed across process death; replay-from-scratch duplicates actions and loses auditability.

**Consequences and trade-offs.** Partial effects remain explicitly uncertain. Recovery may require human input; no automatic retry of an uncertain side effect. Require idempotent record writes and interruption tests.
