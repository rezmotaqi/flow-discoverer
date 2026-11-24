# Architecture

YAML configuration → scoped driver → sanitized observation → fingerprint + candidate discovery → policy → bounded deterministic BFS → SQLite records + immutable evidence → offline report. Browser actions and evidence generation are local; reports use saved data only. Later AI receives redacted data and returns schema-validated suggestions, not instructions.

See [contracts](INTERFACE_REGISTRY.md), [codebase map](CODEBASE_MAP.md), and [security](SECURITY.md).
