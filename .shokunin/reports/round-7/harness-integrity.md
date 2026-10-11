# harness-integrity — round 7 (calibration)

Work commit: `223b93ac0833b26448fb307551acf9a7420e3731` (`harness-integrity-shokunin <harness-integrity@shokunin.local>`). One axis-move: calibration; depth also judged.

## Work performed
- `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: isolated deep-copy mutation substitutes valid `rlm.find_models` for the cited `rlm.get_harness_state`; baseline before audit edit exited 0, verified 4/4 (expected-rejection assertion failed). It now exits 1, verifies 3/4 with a cited-procedure mismatch. No live authority was changed.
- `.shokunin/harness-integrity/corpus/knowledge/audit.py`: check that an imported callable also matches the lane's existing `global-triples.md` procedure citation. `global-triples.md`, `lessons/round-7-calibration.md`, `SCORECARD.md`, `LOG.md` and index explain the bound.

## Landed changes
- `.shokunin/harness-integrity/LOG.md` round-7 entry and the above files landed together in work commit `223b93ac0833b26448fb307551acf9a7420e3731`; this report was written afterward. Neither global harness nor MANIFEST, source files or other lanes were edited; no push.

## Before → after measurements
- Before edit, `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` failed its newly added expected-rejection assertion: wrong-callable audit exit 0, verified 4/4. At work commit `223b93a`, rerunning that same command exits 0: wrong-callable audit exit 1, verified 3/4; intact and fresh-live audit controls exit 0, 4/4; copied fifth mint exits 0, 5/5; existing missing-ID/import, roster, rank, duplicate and checklist negatives reject. `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exits 0, live 4/4. `git diff --check` and `git show --check --oneline HEAD` exit 0.
- **Calibration: improved** for one copied valid-but-wrong executable reference against its independent citation. **Depth: unchanged** (same current live four triples, no new semantic verification). L1 judges admission; no live corruption or independent round-7 review is claimed. Coordinated citation/reference corruption remains out of scope.

## SHONEN
Promoted in round 4; `SHONEN.md` removed. Historical receipts: [x] cited decision/checklist by `round1-independent-review`; [x] narrow end-to-end audit by `round2-independent-review`; [x] executable instructions by `round3-promotion-review`; [x] province boundary by `rank-transition-independent-review`. Historical non-author reviews, not new round-7 verification.

## Proposed self-update (not applied)
L1 may refine global procedure to require the copied resolvable wrong-callable negative and intact/fifth-mint positives; memory may record the observed copied false accept, not a live corruption event. Falsify if wrong-callable passes or intact/fifth-mint positive fails. No global triple mutation made.
