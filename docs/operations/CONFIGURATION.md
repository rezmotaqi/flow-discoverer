# CONFIGURATION

Use `configs/fixture.yaml`: canonical 127.0.0.1 URL with explicit port, listed safe document paths, prohibited paths, keyed UI button allowlists, viewport and bounded run limits. No credential or arbitrary external target fields. All extra fields are rejected. Relative defaults are resolved from the current working directory.

## Future target extensions

After authorization review, add versioned target permission provenance, scoped origins/packages, platform and viewport profile, languages, authentication strategy, objective(s), interaction/action/depth/time/state/model/artifact budgets, action allowlist, prohibited routes, approval requirements, optional adapters and retention settings. Keep permission and secret storage separate: profile references may identify a secured local session, never embed bytes or credentials. Candidate real platforms are discovery leads only; no availability, eligibility or permission is implied by the config design.
