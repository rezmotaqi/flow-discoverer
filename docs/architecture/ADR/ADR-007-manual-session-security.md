# ADR-007 — Explicit human intervention and profile isolation

**Status / features:** Proposed • F-012, F-019, F-021.

**Decision and context.** Enable opt-in headed interventions with checkpoint and recording suppression. Store isolated authorized profiles outside Git under least privilege.

**Alternatives and reasoning.** Automated credentials or shared browser profiles increase exposure. Discarding all sessions would be safer initially but prevents authorized recovery and authenticated QA.

**Consequences and trade-offs.** Verify scope before and after intervention, support expiry and revocation, and test no export/model exposure. M0/M1 support no authenticated execution.
