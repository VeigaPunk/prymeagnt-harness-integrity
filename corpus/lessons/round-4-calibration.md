# Round 4 — rank-transition calibration (2026-10-11)

Sources: `docs/shokunin-workflow.md` describes the manifest as fleet-canonical roster/rank and the `shonen → shokunin` gate as a recorded promotion with a global harness update; installed `~/.prime/agent/skills/shokunin/SKILL.md` §Promotion gates and §Bookkeeping specify `rounds[].promotions` and roster. The `corpus/knowledge/audit.py` baseline at `c8129fd` compared every executable rank to literal `shonen`, rejecting a real promotion even when manifest and harness agreed.

From repository root run:

```sh
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py
```

The audit starts the four `rounds[0].minted` lanes at `shonen`, applies only valid `shonen → shokunin` ledger transitions, checks promoted lanes have roster rows whose `rank` matches, and compares each executable subagent's rank to that expected rank. An unminted roster lane, duplicate/invalid promotion, premature roster row, missing promoted roster row, or stale executable rank produces a `FAIL` and nonzero exit. It does not validate the reviewer's promotion evidence or claim that synthetically promoted lanes were actually promoted.

The mutation suite deep-copies the live state and manifest. A process-local `Path.read_text` patch supplies a copied promoted manifest only to the audit's `MANIFEST.json` read. Positive controls: intact unpromoted copy 4/4 exit 0, synthetic matching promotion ledger+roster+global spec 4/4 exit 0, fresh live snapshot 4/4 exit 0. Negatives: original missing skill and invalid import each 3/4 exit 1, synthetic promoted spec with no ledger (unauthorized rank) 3/4 exit 1, promotion ledger+roster with stale harness rank 3/4 exit 1, and promotion ledger+spec with missing roster exit 1. The test asserts the on-disk manifest and fresh global rank remain unchanged. All rank fixtures are simulated; no live global harness mutation, roster edit, or promotion is authorized by this lesson. Future promotion shapes beyond `shonen → shokunin` remain outside this audit's scope.
