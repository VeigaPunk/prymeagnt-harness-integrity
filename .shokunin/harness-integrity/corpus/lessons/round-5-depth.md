# Round 5 — depth: ledger-wide mint membership

Claim: `rounds[0].minted` plus a four-ID limit falsely rejects a later valid mint. `audit.py` now derives unique IDs across every `type=mint` ledger entry, checks unique checklist citations against those IDs, and verifies each against cited books and global triples. The deep-copy fifth-mint fixture returns 5/5; duplicate ID and missing checklist citation return exit 1. Existing four-lane rank/reference/ID mutation controls remain.

Run from project root: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` and `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py`. Assertions check exit and failure text, not merely counts. No live mint, global harness mutation or MANIFEST edit occurs. This does not assert that a future mint has valid semantics; its global entries require a separately controlled fixture or a fresh live cited audit.
