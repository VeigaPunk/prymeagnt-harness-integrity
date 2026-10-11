# harness-integrity — round 2 (2026-10-11)

Owned axes: depth, calibration. One axis-move: calibration. Falsifiable claim: the prior 4/4 audit cannot alone show detection; a copied missing-skill triple must yield a nonzero audit and 3/4, while an intact copy and a fresh live snapshot must each return 0 and 4/4. The one missing-ID detector is not evidence for other corruption classes. L2 not dispatched: this bounded local fixture did not warrant sub-lanes.

## Work performed
- Re-ran baseline live read-only audit: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → exit 0, `verified triples: 4/4`; source `.shokunin/harness-integrity/corpus/knowledge/audit.py:1-7`.
- Added in-process deep-copy negative control, intact-copy false-positive guard, and fresh live-state guard: `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py:27-49`; documented limits and commands in `.shokunin/harness-integrity/corpus/lessons/round-2-calibration.md:1-14`.
- Logged calibration **improved** (one missing-skill rejection and two clean controls) and depth **unchanged** (original audit unchanged): `.shokunin/harness-integrity/LOG.md:14-18`; scorecard evidence `.shokunin/harness-integrity/SCORECARD.md:8`. No trade, no scalar verdict, no independent SHONEN verifier.

## Landed changes
- `LOG.md` round-2 entry (`.shokunin/harness-integrity/LOG.md:14-18`) ties the mutation fixture, lesson, corpus index and scorecard update to work commit `6df67ef9d7760f88373393703df31c04f3193c6c` (present via `git rev-parse HEAD` immediately before this report was written). No source, MANIFEST, global-harness or sibling book changes. Push/review/judgment are L1-owned, not claimed here.

## Before → after measurements
- Calibration claim at work commit `6df67ef9d7760f88373393703df31c04f3193c6c`: before, baseline command `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → exit 0, `verified triples: 4/4` (no mutated-control result in round 1); after, `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` → exit 0, `intact copy: exit 0; verified triples: 4/4`, `corrupted copy: exit 1; verified triples: 3/4; FAIL: harness-integrity: missing skill:primeagent-harness-integrity-procedure`, `fresh live snapshot: exit 0; verified triples: 4/4`. Counting command is the test invocation, whose assertions inspect audit exit codes, counts and failure line; outputs were re-run after work commit. False-positive guard is intact copy; original state remains read-only and the fresh live snapshot stays 4/4. This measures only one mutation, not semantic integrity or future state.
- Depth, unchanged: baseline and after both run `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → exit 0, `verified triples: 4/4` at `6df67ef9d7760f88373393703df31c04f3193c6c`; no new audit rule or depth claim. No 0–10 score is inferred.

## SHONEN
- [~] Real decision tables/error patterns/checklists with cited sources: `.shokunin/harness-integrity/corpus/knowledge/global-triples.md:1-27` and `corpus/lessons/round-2-calibration.md:1-14`; non-author verifier pending.
- [~] End-to-end domain task executed and logged: `.shokunin/harness-integrity/LOG.md:14-18`, `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py:27-49`; non-author verifier pending.
- [~] Instructions executable without oral context: `.shokunin/harness-integrity/corpus/lessons/round-2-calibration.md:1-14`; non-author verifier pending.
- [~] No cross-domain bleed; PROVINCE remains accurate: `.shokunin/harness-integrity/PROVINCE.md:1-13` and work-commit scoped paths (`git show --format= --name-only 6df67ef9d7760f88373393703df31c04f3193c6c`); non-author verifier pending.
