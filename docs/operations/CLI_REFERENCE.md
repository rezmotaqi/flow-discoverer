# CLI REFERENCE

| Command | Purpose |
|---|---|
| `init --workspace PATH` | Create local artifact workspace |
| `doctor` | Launch local headless Chromium without visiting a target |
| `targets list` / `targets validate fixture` | List/validate supported configuration |
| `fixture serve --port 8765` | Serve the synthetic application on loopback |

Code 0 succeeds, 1 is a runtime error, 2 is invalid usage/configuration. See `game-explorer --help` for installed commands.

## Planned commands — not available yet

| Milestone | Command contract |
|---|---|
| M1 | `explore TARGET --mode internal-qa --headed --max-actions N --max-depth N`, `status RUN_ID`, `states RUN_ID` |
| M1/M4 | `report RUN_ID --format all`, `graph RUN_ID --format mermaid`, `evidence EVIDENCE_ID` |
| M2 | `explore TARGET --objective OBJECTIVE`; general, competitions, monetization, games, journey, regression and bounded custom goals |
| M3 | `record TARGET`, `resume RUN_ID` |
| M5/M6 | Authorized target profiles only; external observation requires reviewed permission scope and infrastructure |
| M6 | `compare TARGET_A TARGET_B`, using stored runs with documented selection or explicit run IDs |
| M9 | `diff OLD_RUN_ID NEW_RUN_ID`, `replay JOURNEY_ID --mode internal-qa` |

Proposed cancellation result: exit 130. See the [roadmap](../planning/ROADMAP.md) and [report contracts](REPORT_ARTIFACTS.md).
