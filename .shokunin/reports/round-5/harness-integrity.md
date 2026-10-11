# harness-integrity — round 5 (depth)

Work commit: `3917c3ca598f2d4fa422dc95fc9434946a842de8` (`harness-integrity-shokunin <harness-integrity@shokunin.local>`). One axis-move: depth; owned calibration also judged.

## Work performed
- `corpus/knowledge/audit.py`: derives unique minted IDs from every `rounds[]` `type=mint` entry, rejects duplicate IDs and checklist mismatch, verifies each cited province/scorecard and global triple. Before it used `rounds[0].minted` and required exactly four.
- `corpus/knowledge/mutation_test.py`: isolated deep-copy fifth mint/complete triple/books/checklist positive and duplicate-ID/unmatched-checklist negatives; retains prior four-lane promoted/unpromoted, missing-ID and invalid-reference controls. `corpus/knowledge/global-triples.md` and `lessons/round-5-depth.md` state cited scope and limits.
- `SCORECARD.md`, `LOG.md`, `corpus/README.md`: record this bounded round and next falsifiable claim. No `MANIFEST.json`, live global harness, or remote push changed.

## Landed changes
- `LOG.md` round-5 entry and code/lesson above landed together in work commit `3917c3ca598f2d4fa422dc95fc9434946a842de8` (report written only after work commit).

## Before → after measurements
- Before `3917c3c`: audit used first mint + exact four; a later complete fifth minted lane would be rejected. After at `3917c3c`, command `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` exits 0: copied fifth mint 5/5 exit 0; duplicate ID and unmatched checklist exit 1; intact, authorized-promoted and fresh-live 4/4 exit 0; prior five negatives rejected. `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exits 0, live 4/4. `git diff --check` exits 0. All rerun after work commit.
- **Depth: improved** for ledger-wide membership and fixture-tested later mint. **Calibration: unchanged**: no real fifth global entry or independent review; existing mutation controls preserved. L1 judges admission. Fifth lane is synthetic only; any new mint's actual global harness entries and citations require separate controlled fixture/fresh live audit. Neither semantic quality nor future-state integrity proven.

## SHONEN
Promoted in round 4; `SHONEN.md` removed. Previously verified boxes: [x] cited decision/checklist by `round1-independent-review`; [x] end-to-end narrow triple audit by `round2-independent-review`; [x] executable instructions by `round3-promotion-review`; [x] province boundary by `rank-transition-independent-review`. These are historical non-author receipts in `LOG.md`, not new round-5 verification.

## Proposed self-update (not applied)
L1 may update global `primeagent-harness-integrity-procedure` to require audit across every `type=mint` entry plus fifth-mint positive/duplicate-ID/unmatched-checklist fixture controls, and `primeagent-harness-integrity-knowledge` to state that four minted IDs is snapshot-specific. Falsify if a legitimate fifth mint with complete cited books/global triple is rejected, or duplicate/checklist mismatch is accepted. No global harness mutation was made.
