# ADR-009 — Map Android into provider-neutral exploration contracts

**Status / features:** Proposed • F-017, F-018.

**Decision and context.** Treat activity and package as typed screen identity and session scope, rather than encoding them as browser URLs. Plug driver and game adapter capabilities into policy.

**Alternatives and reasoning.** A duplicate mobile stack diverges; forcing browser assumptions into Android breaks both abstractions.

**Consequences and trade-offs.** Use an authorized Android fixture and test equivalence of reports, privacy, action budgets and failures. Appium dependencies are deferred until M7.
