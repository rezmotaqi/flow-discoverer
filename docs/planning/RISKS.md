# Risks

| Risk | Mitigation | Gate |
|---|---|---|
| Unapproved network or side effects | Exact loopback origin, GET-only transport, origin and scope checks, no redirects in M1 | T-002 |
| Sensitive evidence | Known synthetic scope, suppress credentials and payment screens, minimize captured text and mask fields | T-002, T-004 |
| Same URL or dynamic evidence misidentified | Composite versioned fingerprint, explicit fixture markers, separate observations | T-003 |
| Interruption leaves uncertainty | Transactional transitions, unfinished attempt markers; no resume until M3 reconciles them | T-003 |
| Unknown mistaken for absent | Evidence-first outputs, explicit coverage and limit reasons | T-004 |
| Agent context drift | One compact metadata source, link and index checks, handoff | T-001 |
