# ADR 002 sqlite evidence

Status: adopted for M1 (F-008, F-009). Use SQLite with explicit migration version and foreign keys, plus immutable checked PNGs. A server DB and BLOB-only files add initial overhead or hurt portability. Byte-identical files deduplicate per run. An interrupted write can leave an orphan file; do not automatically delete historical evidence.
