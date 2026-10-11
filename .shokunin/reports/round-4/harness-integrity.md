# harness-integrity — round 4 (2026-10-11)

Owned axes: **depth, calibration**. One axis move: **calibration** of rank-transition safety (operability of the existing audit; no new axis). Work commit: `2fa231e4e158f1ae2c00fb01e5153dda01aa9282`, lane identity `harness-integrity-shokunin <harness-integrity@shokunin.local>`.

## Work performed
- `corpus/knowledge/audit.py` derives expected rank from `MANIFEST.json` mint and valid promotion ledger and checks roster rank against it, rather than hardcoding `shonen`; compares global subagent rank to this expectation. See work commit and `corpus/knowledge/global-triples.md`.
- `corpus/knowledge/mutation_test.py` uses deep copies of manifest and harness and process-local patched reads to exercise authorized promotion and unauthorized mismatches. See `corpus/lessons/round-4-calibration.md` and work commit; no real promotion or global write.
- Updated `LOG.md`, `SCORECARD.md`, and corpus index in work commit. Source files read-only; no MANIFEST/global harness/SHONEN edit, no child dispatch, no push.

## Landed changes
- `LOG.md` Round 4 records the falsifiable claim, per-axis verdict, limitations and proposed (not applied) global refinement; all work is in `2fa231e4e158f1ae2c00fb01e5153dda01aa9282`.

## Before → after measurements
- Baseline `c8129fd`: audit rank check was literal `spec.metadata.get("rank") != "shonen"`; valid promoted manifest/spec would be rejected. Baseline native command `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` passed existing 2/2 negative and 2/2 positive controls (missing skill and invalid import each exit 1 / 3/4; intact and fresh each exit 0 / 4/4).
- Work commit `2fa231e4e158f1ae2c00fb01e5153dda01aa9282`: same command exits 0; positive **3/3**: intact copy 4/4, copied ledger+roster+spec legitimate promotion 4/4, fresh live 4/4. Negative **5/5**: missing skill 3/4 exit 1; invalid import 3/4 exit 1; unauthorized roster/spec rank with no promotion 3/4 exit 1; stale spec rank with recorded promotion 3/4 exit 1; missing promoted roster exit 1. Standalone `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exits 0 / 4/4 on live snapshot. `git diff --check` exits 0. The on-disk manifest and live rank are asserted unchanged by the fixture.
- **Calibration improved** on simulated valid/invalid rank transitions while retaining round-3 controls. **Depth unchanged**: still four minted triples and no broader semantic verification. No scalar score or live promotion is claimed. Reviewer/L1 decides admission.

## SHONEN
- [x] Real sourced decision/checklist — previously verified by non-author `round1-independent-review` / `round2-independent-review` at `65a1d7b` / `68b4257`; no new independent review claimed here.
- [x] End-to-end domain task — same named previous non-author reviewers; round-4 test is synthetic only.
- [x] Executable instructions without oral context — same named previous non-author reviewers; fresh round-4 command above is reproducible.
- [x] No cross-domain bleed / province accurate — same named previous non-author reviewers; scope remains `.shokunin/harness-integrity/**` plus this report.

Self-refinement proposal **for L1 only**, not applied: update global procedure skill to instruct rank validation via mint→promotion ledger→roster and copied-state positive/negative tests; update global knowledge to cite observed 4/4 and negative receipts; leave subagent province/axes untouched. Falsify if an authorized matching promotion fails, an unauthorized mismatch passes, or existing mutation guards regress. No global harness authorization was assumed.
