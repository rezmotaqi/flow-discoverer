# Feature registry

Generated from [registry metadata](../../.project/registry.json). Do not edit directly.

| ID | Name | Milestone | Status | Priority | Owner | Dependencies | Verification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [F-001](../../docs/features/F-001-browser-automation-driver.md) | Browser automation driver | M1 | PLANNED | P0 | unassigned | F-022 | — |
| [F-002](../../docs/features/F-002-observation-engine.md) | Observation engine | M1 | PLANNED | P0 | unassigned | F-001 | — |
| [F-003](../../docs/features/F-003-state-fingerprinting.md) | State fingerprinting | M1 | PLANNED | P0 | unassigned | F-002 | — |
| [F-004](../../docs/features/F-004-action-discovery.md) | Action discovery | M1 | PLANNED | P0 | unassigned | F-002 | — |
| [F-005](../../docs/features/F-005-safety-policy-engine.md) | Safety policy engine | M1 | PLANNED | P0 | unassigned | F-004 | — |
| [F-006](../../docs/features/F-006-navigation-graph.md) | Navigation graph | M1 | PLANNED | P0 | unassigned | F-003, F-008 | — |
| [F-007](../../docs/features/F-007-exploration-planner.md) | Exploration planner | M1 | PLANNED | P0 | unassigned | F-005, F-006, F-009 | — |
| [F-008](../../docs/features/F-008-persistent-storage.md) | Persistent storage | M1 | PLANNED | P0 | unassigned | F-003 | — |
| [F-009](../../docs/features/F-009-evidence-management.md) | Evidence management | M1 | PLANNED | P0 | unassigned | F-002 | — |
| [F-010](../../docs/features/F-010-omnirouter-integration.md) | OmniRouter integration | M2 | PLANNED | P2 | unassigned | F-005, F-007 | — |
| [F-011](../../docs/features/F-011-resumable-exploration.md) | Resumable exploration | M3 | PLANNED | P2 | unassigned | F-007, F-008 | — |
| [F-012](../../docs/features/F-012-human-intervention.md) | Human intervention | M3 | PLANNED | P2 | unassigned | F-001, F-011 | — |
| [F-013](../../docs/features/F-013-business-rule-extraction.md) | Business rule extraction | M4 | PLANNED | P2 | unassigned | F-002, F-009, F-010 | — |
| [F-014](../../docs/features/F-014-documentation-generator.md) | Documentation generator | M1 | PLANNED | P0 | unassigned | F-006, F-009 | — |
| [F-015](../../docs/features/F-015-competitor-comparison.md) | Competitor comparison | M6 | PLANNED | P2 | unassigned | F-013, F-014 | — |
| [F-016](../../docs/features/F-016-regression-detection.md) | Regression detection | M9 | DEFERRED | P2 | unassigned | F-006, F-011, F-014 | — |
| [F-017](../../docs/features/F-017-android-driver.md) | Android driver | M7 | DEFERRED | P2 | unassigned | F-001, F-002 | — |
| [F-018](../../docs/features/F-018-gameplay-adapters.md) | Gameplay adapters | M8 | DEFERRED | P2 | unassigned | F-001, F-005 | — |
| [F-019](../../docs/features/F-019-internal-qa-automation.md) | Internal QA automation | M5 | PLANNED | P2 | unassigned | F-007, F-012, F-014 | — |
| [F-020](../../docs/features/F-020-continuous-integration.md) | Continuous integration | M9 | DEFERRED | P2 | unassigned | F-016, F-022 | — |
| [F-021](../../docs/features/F-021-human-guided-recording.md) | Human-guided recording | M3 | PLANNED | P2 | unassigned | F-002, F-009, F-012 | — |
| [F-022](../../docs/features/F-022-repository-context-tooling.md) | Repository context tooling | M0 | TESTED | P0 | integration | — | [evidence](../../docs/testing/VALIDATION_STATUS.md) |
