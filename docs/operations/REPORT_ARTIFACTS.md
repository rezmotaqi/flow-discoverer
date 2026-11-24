# Report artifact contracts (planned)

M1 generates an offline screen/transition/coverage summary with a screenshot manifest and basic graph. The full M4 bundle adds searchable findings, journey filters, feature inventory and rule classifications, with no external scripts/fonts and with portable evidence links. A claim links to the observation and evidence that supports it. Inaccessible states and limits are explicit; unknown never means absent.

| Bundle | Required artifacts |
|---|---|
| Overview | `EXECUTIVE_SUMMARY.md`, `PLATFORM_OVERVIEW.md`, `FINDINGS.md`, `COVERAGE.md` |
| Screens and journeys | `SCREEN_INVENTORY.md`, `USER_FLOWS.md`, `FLOW_GRAPH.mmd`, graph JSON/GraphML, offline `index.html` |
| Games | `GAME_CATALOG.md`, `GAMEPLAY_RULES.md`, `SCORING_SYSTEM.md` |
| Competitions/rewards | `COMPETITIONS.md`, `LEADERBOARDS.md`, `REWARD_SYSTEM.md`, `MONETIZATION.md` |
| Analysis and provenance | `BUSINESS_RULES.md`, `UX_ANALYSIS.md`, `EVIDENCE.json` |
| M6 comparison | `COMPETITOR_COMPARISON.md`, `FEATURE_MATRIX.csv`, `FEATURE_GAP_ANALYSIS.md`, `XGAME_RECOMMENDATIONS.md`, `comparison.json`, `comparison.html` |

Comparison dimensions: authentication, onboarding, game catalog/modes, matchmaking, scoring, leaderboards, weekly/monthly competitions, rewards, virtual currency, achievements, retention, communities, referrals, monetization, charity, sponsorship and mobile usability. Each applicable dimension records provenance, classification and coverage caveats. Recommendations additionally document expected value, dependencies, complexity and open questions. A comparison reads saved evidence only.

Run bundles are intended to use `artifacts/<target>/<run>/` with `screenshots/`, `observations/`, `transitions/`, `traces/`, `graphs/`, `reports/` and `manifest.json` where supported. Never silently overwrite immutable evidence; generate derived artifacts separately. See [F-009](../features/F-009-evidence-management.md), [F-014](../features/F-014-documentation-generator.md) and [F-015](../features/F-015-competitor-comparison.md).
