# harness-integrity — round 6 (depth)

Work commit: `fdb8b5190dd96f97e77e651fa153106072e5a10c` (`harness-integrity-shokunin <harness-integrity@shokunin.local>`). One axis-move: depth; calibration also judged.

## Work performed
- `.shokunin/harness-integrity/corpus/knowledge/audit.py`: validates promoted roster `province`, `axes`, `harness_spec` against lane book path/axes and global subagent ID; mismatched lane no longer counted verified. Unrostered shonen remains valid.
- `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: three independent copied-state wrong-pointer negatives while rank and global triple stay correct; retains four-lane, synthetic fifth mint, and rank controls. `global-triples.md` and `lessons/round-6-depth.md` explain bounds; `SCORECARD.md`, `LOG.md`, corpus index record results. No live authority mutated or push attempted.

## Landed changes
- `.shokunin/harness-integrity/LOG.md` round-6 entry and the code, lesson, scorecard, index above landed together in work commit `fdb8b5190dd96f97e77e651fa153106072e5a10c`; this report was written afterward.

## Before → after measurements
- Before work, added expected-rejection assertion for rank-correct wrong `province` in copied promoted manifest failed: audit exit 0 and verified 4/4. The same field-check omission affected `axes` and `harness_spec` (no separate pre-patch execution recorded for those two). At work commit `fdb8b51`, `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` exits 0: each wrong-pointer copy exits 1 and verifies 3/4; intact, authorized promotion and fresh-live pass 4/4; synthetic fifth mint passes 5/5; prior unauthorized-rank, stale-spec, missing-roster, missing-ID/reference, duplicate mint/checklist negatives reject. `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exits 0, live 4/4. `git diff --check` and `git show --check --oneline HEAD` exit 0, rerun after work commit.
- **Depth: improved** for copied roster pointer integrity. **Calibration: unchanged**: no live divergent roster observed and no independent verification of a real drift event. L1 judges admission; this is not a claim that real drift was caught.

## SHONEN
Promoted in round 4; `SHONEN.md` removed. Historical receipts: [x] cited decision/checklist by `round1-independent-review`; [x] end-to-end narrow triple audit by `round2-independent-review`; [x] executable instructions by `round3-promotion-review`; [x] province boundary by `rank-transition-independent-review`. These are historical non-author reviews recorded in `LOG.md`, not new round-6 verification.

## Proposed self-update (not applied)
L1 may refine global `primeagent-harness-integrity-procedure` to require three isolated roster-pointer negatives alongside promoted/fifth-mint positives and existing rank controls; update `primeagent-harness-integrity-knowledge` with baseline false acceptance and copied-state limit. Preserve subagent rank/province/axes. Falsify if any copied wrong pointer passes, consistent promoted row fails, or unrostered valid fifth mint fails. No global triple mutation made.
