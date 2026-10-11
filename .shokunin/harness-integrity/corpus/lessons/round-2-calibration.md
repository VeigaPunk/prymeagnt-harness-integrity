# Round 2 — calibration control (2026-10-11)

Source: `corpus/knowledge/audit.py` (round-1 read-only audit); `corpus/knowledge/mutation_test.py` (this round). The audit reads `rlm.get_harness_state(global_=True)` and requires each minted lane's subagent/memory/skill IDs. The test patches only the lookup in its process, passing a deep copy; no global state or repository source is written.

Run from the project root using the prime-agent kernel environment:

```sh
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py
```

Baseline live audit: exit 0, `verified triples: 4/4`. Intact deep-copy control: exit 0, `4/4` (false-positive guard). Deliberately remove only `primeagent-harness-integrity-procedure` from the copied `skill` mapping: audit exits 1, `3/4`, with `FAIL: harness-integrity: missing skill:primeagent-harness-integrity-procedure`. Fetch a fresh live snapshot after the fixture: exit 0, `4/4` (no mutation leaked). The script asserts these values and exits nonzero on a mismatch.

Limits: these are current mutable-harness observations, not a pinned attestation. The test proves detection of one missing ID only; it does not assert detection of all corruptions or certify semantic content.
