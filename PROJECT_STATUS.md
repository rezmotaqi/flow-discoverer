# Current project status

| Milestone | Status |
|---|---|
| M0 — foundation | Tested locally; awaiting explicit user acceptance. Editable CLI, reference fixture, development tooling and project documentation are in place. |
| M1 — deterministic explorer | Planned. The automation driver, state/graph and SQLite storage, and screenshot reports do not exist yet. |
| M2–M9 | Initial specifications exist; no implementation or milestone validation. |

- Verified checks: see [validation](docs/testing/VALIDATION_STATUS.md). No known critical defect in checks run; [known limitations](docs/testing/KNOWN_ISSUES.md) are separate from verified behavior.
- Branch: `codex/m0-m1-foundation`; the local tip is authoritative (`git log -1 --oneline`). No PR is attached. For publication status check `git status --short --branch` and the current upstream, not this document.
- Next engineering task: [T-002](docs/tasks/active/T-002.md), then T-003/T-004, after M0 review. No real target is authorized; all test traffic was local synthetic traffic.
