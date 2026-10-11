# Global triple audit — round 1 (2026-10-11)

Sources: `docs/shokunin-workflow.md:68-97` requires subagent, memory, and skill per mint; `skills/shokunin/SKILL.md:78-103` describes the global store and `skills/shokunin/SKILL.md:311-315` makes the manifest authoritative for roster/rank, harness authoritative for executable state. `.shokunin/MANIFEST.json` currently contains four minted lanes in its first `type=mint` entry; the audit derives lanes from every `type=mint` entry, regardless of position. The runtime's `rlm/harness.py:218-233` checks the *shape* of Python references; this audit additionally imports and resolves each referenced callable.

Read-only procedure from project root (do not dump secrets or mutate the global store):

```sh
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py
```

The executable audit checks distinct lane IDs across every `MANIFEST.json` `rounds[]` `type=mint` entry and rejects duplicate mint IDs or a nonmatching/duplicate checklist citation; it checks each lane's `subagent`/`memory`/`skill` ID triple, global scope, nonempty content, subagent rank/province/axes against its repo-local `PROVINCE.md:3` and `SCORECARD.md:3`, skill scope/axes/province, promoted roster province/axes/harness_spec pointers against the lane books and triple ID, and that the Python `import` and `callable` resolve in the prime-agent kernel runtime. It does **not** call the skills, test model admission, certify semantic quality of content, or prove no future drift. Every run is a fresh snapshot of a mutable global store, not a version-pinned harness attestation.

## Checklist (live snapshot; re-run before reliance)

- [verified] `harness-integrity` — `primeagent-harness-integrity` (subagent), `primeagent-harness-integrity-knowledge` (memory), `primeagent-harness-integrity-procedure` (skill); Python `rlm.get_harness_state`; `.shokunin/harness-integrity/PROVINCE.md:3`, `SCORECARD.md:3`.
- [verified] `rlm-dispatch` — `primeagent-rlm-dispatch` (subagent), `primeagent-rlm-dispatch-knowledge` (memory), `primeagent-rlm-dispatch-procedure` (skill); Python `rlm.find_models`; `.shokunin/rlm-dispatch/PROVINCE.md:3`, `SCORECARD.md:3`.
- [verified] `gate-evidence` — `primeagent-gate-evidence` (subagent), `primeagent-gate-evidence-knowledge` (memory), `primeagent-gate-evidence-procedure` (skill); Python `goal.get`; `.shokunin/gate-evidence/PROVINCE.md:3`, `SCORECARD.md:3`.
- [verified] `skill-discovery` — `primeagent-skill-discovery` (subagent), `primeagent-skill-discovery-knowledge` (memory), `primeagent-skill-discovery-procedure` (skill); Python `rlm.get_harness_state`; `.shokunin/skill-discovery/PROVINCE.md:3`, `SCORECARD.md:3`.

Round-5 fixture: `mutation_test.py` adds a copied fifth mint entry, copied global triple, synthetic province/scorecard and checklist citation without changing live authorities. It expects 5/5 success, then rejects a duplicate mint ID and an unmatched checklist. Existing four-lane rank/ID/reference controls remain. The fifth lane is synthetic, **not** a fifth verified live lane; a real mint must add a separately controlled fixture or live cited books and global entries before claiming verification.

Failure decision: if the command exits nonzero, do not call the affected triple verified. Report the specific `FAIL:` line to L1; only L1 may change global harness or `MANIFEST.json`. The rank check uses mint chronology (shonen), validated `rounds[].promotions` transitions, and roster rank (required on promotion); a changed roster without a valid ledger promotion fails. A future promotion must update the roster and executable harness spec together before this audit can verify it.
