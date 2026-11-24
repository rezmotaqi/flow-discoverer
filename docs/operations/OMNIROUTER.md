# OmniRouter setup and verification (planned, M2)

Not available in the current CLI. `doctor` only checks local Chromium. Do not try a live provider until F-010 ships and the deployment and spending cap are authorized. Routine tests use a mock transport.

| Setting | Purpose |
|---|---|
| `LLM_BASE_URL` | Explicitly configured compatible endpoint; no provider by default |
| `LLM_API_KEY` | Approved secret injection, never YAML, Git, logs, prompts or doctor output |
| `LLM_PLANNER_MODEL`, `LLM_VISION_MODEL`, `LLM_ANALYSIS_MODEL` | Role-specific aliases; optional vision/analysis, independently verified |
| `LLM_TIMEOUT_SECONDS`, `LLM_MAX_RETRIES`, `LLM_TOKEN_BUDGET` | Per-attempt time, retry and per-run token caps |
| `HTTP_PROXY`, `HTTPS_PROXY`, `NO_PROXY` | Operator transport config; never serialize values into a run artifact |

Use a local environment and a least-privilege key scoped to a controlled deployment. Do not assume structured outputs, vision or usage fields. The future provider doctor will separate reachability, text, schema and vision checks and opt in before spending tokens. Treat authentication failure, throttling, unsupported capabilities, offline operation and invalid output as recoverable to deterministic planning; report the reason without the raw payload. See [F-010](../features/F-010-omnirouter-integration.md) and [ADR-005](../architecture/ADR/ADR-005-bounded-model-provider.md).
