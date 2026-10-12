# Harness-integrity round 9 — depth

## Work performed
- Reproduced prior copied-state false pass: copied rlm-dispatch subagent title/content into harness-integrity triple without changing ID or metadata; old `audit.py` exited 0, verified 4/4 (`corpus/lessons/round-9-depth.md`).
- Added narrow title/opening-content identity checks for subagent, memory and skill; six isolated copied mismatches now each exit 1 and verify 3/4 (`corpus/knowledge/audit.py`, `mutation_test.py`).
- Native controls: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` exits 0, including promoted R4 positive 4/4, synthetic fifth mint 5/5, all prior negatives, fresh live 4/4. `audit.py` exits 0, live 4/4. `git diff --check` exits 0. No global/MANIFEST mutation.

## Landed changes
- `LOG.md` round-9 entry, `SCORECARD.md` round-9 measurement, corpus lesson, index, checklist and native scripts landed in work commit `14738d932b85a6b0b9182cdeff7ef60f46e6ed2b` (harness-integrity-shokunin).

## Before → after measurements
- Depth: old copied other-lane subagent title/content under valid ID and unchanged metadata exited 0 (4/4) → six isolated copied title/content mutations exit 1 (3/4). Counting command: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py`, measured at work commit `14738d932b85a6b0b9182cdeff7ef60f46e6ed2b`. **Improved**, copied-state only; no live drift.
- Calibration: live `audit.py` 4/4, synthetic fifth mint 5/5 and authorized promotion 4/4 preserved. **Unchanged**; no semantic content attestation, colluding book/harness edits, or non-author R9 review.

## SHONEN
- [x] Province/corpus established — named non-author round1-independent-review, per earlier LOG; promoted at R4.
- [x] Three verified rounds — named round3-promotion-review, per earlier LOG; promoted at R4.
- [x] Independent round checks — named rank-transition-independent-review, per earlier LOG; promoted at R4.
- [x] Promotion judgment — L1 round-4 closure-correction, per earlier LOG.

L1 decides R9 admission. Report written after work commit; no push.
