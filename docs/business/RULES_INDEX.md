# RULES INDEX

| ID | Rule / rationale | Enforcement |
|---|---|---|
| BR-001 | Observations and states are distinct | Fingerprint + store tests |
| BR-002 | URL alone cannot identify a state | Same-route fixture states |
| BR-003 | Prohibited actions cannot be selected | Candidate and transport rules |
| BR-004 | Important findings need provenance | Report evidence links |
| BR-005 | Inferred rulings are labeled | M4 gate |
| BR-006 | External prize claims prohibited | No external runs |
| BR-007 | Interrupted runs preserve saved progress | SQLite; resume is M3 |
| BR-008 | Credentials must not enter model context | No model or auth in M1 |
| BR-009 | Not observed is not absent | Coverage and future comparison gate |
| BR-010 | Historical evidence is never overwritten silently | Content-addressed screenshots |

See [exploration](EXPLORATION_RULES.md), [identity](STATE_RECOGNITION.md), [evidence](EVIDENCE_CLASSIFICATION.md), [safety](SAFETY_POLICIES.md), and [coverage](COVERAGE_RULES.md).
