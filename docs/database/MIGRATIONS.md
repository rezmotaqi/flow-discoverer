# MIGRATIONS

M1 uses a versioned baseline schema, with no assumptions about older installations. Reject an unsupported on-disk version rather than mutating or dropping data. Document a backed-up, tested forward migration before increasing the version.
