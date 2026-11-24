# Entity registry

**Design baseline, not a deployed schema.** No SQLite schema exists yet. M1 records are specified below; later entities are staged contracts. Physical names and migrations require review before implementation.

| Entity | Earliest milestone | Purpose |
|---|---|---|
| [Target](entities/Target.md) | M1 | Authorized application and versioned scope. |
| [ExplorationRun](entities/ExplorationRun.md) | M1 | Lifecycle, budgets, build and target scope for one execution. |
| [ExplorationObjective](entities/ExplorationObjective.md) | M2 | Typed objective snapshot defining prioritization. |
| [Observation](entities/Observation.md) | M1 | One sanitized view, separate from logical state. |
| [ApplicationState](entities/ApplicationState.md) | M1 | Versioned logical screen identity. |
| [ActionCandidate](entities/ActionCandidate.md) | M1 | Typed action proposed from observed controls. |
| [ActionAttempt](entities/ActionAttempt.md) | M1 | Durable intent and outcome for an actual execution. |
| [Transition](entities/Transition.md) | M1 | Multigraph edge with outcome; target may be unknown. |
| [ExplorationFrontier](entities/ExplorationFrontier.md) | M3 | Durable queue of remaining state/candidate work. |
| [EvidenceArtifact](entities/EvidenceArtifact.md) | M1 | Provenance for an immutable local artifact. |
| [FeatureFinding](entities/FeatureFinding.md) | M4 | Evidence-backed claim on visible product functionality. |
| [BusinessRule](entities/BusinessRule.md) | M4 | Evidence-grounded observed behavior or stated product rule. |
| [UserJourney](entities/UserJourney.md) | M4 | Ordered path through known states with provenance and replay status. |
| [PolicyDecision](entities/PolicyDecision.md) | M1 | Auditable result of evaluating a candidate against current scope. |
| [ModelInvocation](entities/ModelInvocation.md) | M2 | Usage telemetry without persisted prompts or secrets. |
| [RunCheckpoint](entities/RunCheckpoint.md) | M3 | Versioned cursor for safe recovery. |
| [ComparisonFinding](entities/ComparisonFinding.md) | M6 | A conclusion or uncertainty across evidence from selected runs. |

## Shared conventions

IDs are opaque strings. Temporal fields are UTC ISO 8601; JSON fields contain validated structures, not arbitrary executable data. Non-null fields are required unless a default is described. `*_id` references the corresponding named entity. Embedded ordered reference lists can become join tables without changing their public typed contracts. Relationship diagrams show conceptual records; a projection is not a claim of a separate physical table.

Enforce same-run relationships even when IDs are globally unique. Keep credentials and private session bytes out of the DB. All deletion requires explicit authorized retention and checks for dependent evidence/records. See [migrations](MIGRATIONS.md) and [relationships](RELATIONSHIPS.md).
