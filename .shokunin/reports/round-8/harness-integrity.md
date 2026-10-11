# harness-integrity — round 8 (calibration)

Work commit: `cfd84ca8cb9d8c22e2b2e8c2b9cfc17c1c8f4f7b` (`harness-integrity-shokunin <harness-integrity@shokunin.local>`). One axis-move: calibration; depth also judged.

## Work performed
- `.shokunin/harness-integrity/corpus/knowledge/audit.py`: promoted roster `promotion_round` now matches the numeric round in its lane's ledger promotion. Missing, string, boolean and nonpositive rounds reject; unpromoted fifth mint still needs no roster row. No global or ledger mutation.
- `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: copied wrong-round negatives for both real promoted lanes, valid synthetic round-4 promotion positive, malformed/missing round negatives, and previous fifth-mint and four-lane controls.
- `.shokunin/harness-integrity/corpus/lessons/round-8-calibration.md`, corpus index, scorecard and LOG record the claim and limits.

## Landed changes
- `.shokunin/harness-integrity/LOG.md` round-8 entry and the listed files landed in work commit `cfd84ca8cb9d8c22e2b2e8c2b9cfc17c1c8f4f7b`; this report was written afterward. MANIFEST, global harness, source, and other lanes unchanged; no push.

## Before → after measurements
- Before the edit, a copied manifest changing harness-integrity's `promotion_round` 4 → 3 against its round-4 ledger promotion passed `audit_with` exit 0, `verified triples: 4/4` (project kernel interpreter; fixture method in `mutation_test.py`). At work commit `cfd84ca8cb9d8c22e2b2e8c2b9cfc17c1c8f4f7b`, `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` exits 0; both copied promoted-lane wrong-round checks now exit 1, 3/4; valid round-4 promoted copy, intact and fresh-live controls pass 4/4; fifth synthetic mint passes 5/5; earlier rank, roster, callable, import, duplicate mint, and checklist negatives still reject. Missing/malformed roster and ledger round copies reject. `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exits 0, live 4/4. `git diff --check` and `git show --check --oneline HEAD` exit 0.
- **Calibration: improved** for detecting copied roster promotion-round drift against the recorded promotion. **Depth: unchanged**; no new semantic or live drift conclusion. L1 judges admission. A coordinated forged ledger and roster remains outside this comparison.

## SHONEN
Promoted in round 4; `SHONEN.md` removed. Historical receipts: [x] cited decision/checklist by `round1-independent-review`; [x] narrow end-to-end audit by `round2-independent-review`; [x] executable instructions by `round3-promotion-review`; [x] province boundary by `rank-transition-independent-review`. No new non-author review claimed for round 8.

## Proposed self-update (not applied)
L1 may update global procedure/memory to require copied wrong-promotion-round negatives for both promoted lanes, valid round-4 positive and fifth mint positive. Falsify if wrong round passes or valid promotion/mint fails. No global triple mutation made.
