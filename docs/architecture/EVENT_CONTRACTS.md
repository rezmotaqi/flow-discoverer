# EVENT CONTRACTS

M1 uses SQLite records, not a message bus. The primary lifecycle is running → completed, limited, failed, or interrupted. Attempt records distinguish uncompleted, successful, noteworthy HTTP failures and browser errors. Add an external event contract only when a consumer exists.
