# Master plan

Deliver reproducible, evidence-backed software discovery, then semantic analysis and comparison. Start with local authorized browser QA. A pure deterministic policy and planner must precede AI. Keep the record of observation, execution and evidence on disk, independent of provider conversations. Use shared driver and typed domain contracts to support additional surfaces without coupling reporting to a browser.

T-001 establishes packaging, docs and fixture. T-002–T-004 deliver the first useful local explorer with a reference graph. Follow [roadmap](ROADMAP.md) and [milestone gates](MILESTONES.md) for the remaining work. Add one boundary at a time and prove it with unit, integration and real-browser fixture tests. Use local commits and reviewed PRs; explicit user acceptance is separate from passing tests.

Risk priorities: unauthorized side effects → fail closed; private data → no real targets and redact fixture sensitive fields before persistence; loops/duplicate evidence → content identity and bounded BFS; misleading claims → evidence IDs and coverage qualifiers. See [risks](RISKS.md).
