# harness-integrity append-only log

## Mint 2026-10-11
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: `.shokunin/mints/harness-integrity.md`; sources: `.shokunin/harness-integrity/corpus/knowledge/seed.md`.
- Next falsifiable move: execute one bounded read-only task, cite before/after, and have L1 judge every owned axis.

## Round 1 — 2026-10-11 — depth
- Claim: the seed corpus had no verified global-triple audit; the new cited checklist and executable read-only audit verify all four minted triples against `.shokunin/MANIFEST.json` and resolve their Python skill references. Before count: `git ls-tree -r --name-only 44a08fd0eeb22c7ed9766aae4675dd452eff232a .shokunin/harness-integrity/corpus/knowledge | grep -c global-triples.md` → 0 (grep exits 1 on zero). After count: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → `verified triples: 4/4` (exit 0), on the work commit identified in the round report.
- Work: `.shokunin/harness-integrity/corpus/knowledge/global-triples.md` cites contract, manifest, and four books; `corpus/knowledge/audit.py` checks state via read-only `rlm.get_harness_state(global_=True)`, import resolution and repo drift. No global mutation, MANIFEST edit, source edit, child dispatch, or remote push.
- Verdict: depth **improved** for the observed snapshot; calibration **unchanged** (no independent content review or before/after calibration claim). This does not certify semantic correctness or future freshness. L1 judges admission; no self-promotion.
- Next falsifiable move: compare `MANIFEST.json` rank/roster changes with current global metadata after L1 integrates closure; report mismatches without modifying either authority.

## Round 2 — 2026-10-11 — calibration
- Claim: round-1 `audit.py` returned 4/4 without a corruption control; adding a process-local deep-copy mutation test makes one missing skill independently falsifiable, while an intact-copy guard rejects false positives and a fresh live snapshot verifies no mutation leaked. Baseline and detector commands, counts, and commit are in the round-2 report; the reproducible test is `corpus/knowledge/mutation_test.py`.
- Work: `corpus/knowledge/mutation_test.py` removes only a skill ID from a deep copy and monkeypatches the lookup during `run_path(audit.py)`; `corpus/lessons/round-2-calibration.md` describes the detector, guard and limits. No global harness, MANIFEST, domain source, child dispatch or push changed.
- Verdict: calibration **improved** for this one missing-ID detection and intact-copy false-positive guard; depth **unchanged** (the underlying audit and four-triple checklist were not extended). L1 judges admission; no self-promotion. Negative generalization to other corruption classes is not claimed.
- Next falsifiable move: test a changed callable reference in an isolated deep-copy fixture, provided the current round is independently judged and the intended axis remains lowest.
