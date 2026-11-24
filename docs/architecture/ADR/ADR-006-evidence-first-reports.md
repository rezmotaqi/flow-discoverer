# ADR-006 — Evidence-first reporting and comparison

**Status / features:** Proposed • F-009, F-013–F-016.

**Decision and context.** Separate direct observation, claims, inference and unknowns. Link factual statements to immutable evidence IDs and generate offline artifacts from snapshots.

**Alternatives and reasoning.** Generating only AI summaries is faster to prototype but loses provenance and obscures coverage differences. Raw files alone do not communicate product conclusions.

**Consequences and trade-offs.** Treat coverage as sampled; mark missing evidence and comparison uncertainty. Reports must escape untrusted data and validate references.
