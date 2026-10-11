# harness-integrity — round 3 (2026-10-11)

Owned axes: calibration **improved**, depth **unchanged**. One falsifiable calibration move: reject a present skill with an invalid import independently of the missing-skill mutation. No L2 dispatched: the bounded, local, deep-copy fixture did not warrant sub-lanes. No push, global harness mutation, manifest mutation or source-tree edit. The existing SHONEN boxes have named round-1/2 independent verification; this new fixture awaits independent review.

## Work performed
- Added an invalid-import deep-copy negative while preserving missing-ID and intact/fresh controls: `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py:29-56` at `ecb330761fbcf80f293517d2a8e3514bbfc3f0d6`.
- Ran `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` after the work commit: exit 0; missing skill 3/4 exit 1, invalid import 3/4 exit 1, intact 4/4 exit 0, fresh live 4/4 exit 0. Documented assumptions and limits at `.shokunin/harness-integrity/corpus/lessons/round-3-calibration.md:3-5`.
- Ran live `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py`: exit 0, 4/4; retained read-only scope in `.shokunin/harness-integrity/LOG.md:23-27`. `git show --format= --name-only ecb330761fbcf80f293517d2a8e3514bbfc3f0d6` lists only five owned paths.

## Landed changes
- `.shokunin/harness-integrity/LOG.md:23-27` documents the calibration claim, controls, boundaries and proposed (not applied) harness refinement. Work commit `ecb330761fbcf80f293517d2a8e3514bbfc3f0d6` carries `mutation_test.py`, lesson, corpus index, scorecard and LOG. `git rev-parse HEAD` returned this hash immediately before this report was written.

## Before → after measurements
- Calibration **improved**, at work commit `ecb330761fbcf80f293517d2a8e3514bbfc3f0d6`: before (round-2 fixture) negatives 1/1 rejected, positives 2/2 accepted; after negatives 2/2 rejected, positives 2/2 accepted. Counting command: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` (exit 0). Each named line reports its asserted audit exit code and triple count: missing skill exit 1 3/4, invalid import exit 1 3/4, intact copy exit 0 4/4, fresh live exit 0 4/4. The new exact failure is `FAIL: harness-integrity: skill reference invalid: No module named 'shokunin_missing_reference_probe'`. No claim about other invalid callables, semantic content or future state.
- Depth **unchanged**, at the same commit: before and after `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → exit 0 and 4/4; `git show --format= --name-only ecb330761fbcf80f293517d2a8e3514bbfc3f0d6` contains no audit or checklist change. The extra detector validates an existing audit rule, not new audit breadth.

## SHONEN
- [x] Real decision tables/error patterns/checklists with cited sources — named non-author verifiers `round1-independent-review` and `round2-independent-review`, `.shokunin/harness-integrity/LOG.md:20-21`; round-3 addition pending independent review.
- [x] End-to-end domain task executed and logged — named non-author verifiers `round1-independent-review` and `round2-independent-review`, `.shokunin/harness-integrity/LOG.md:20-21`; round-3 addition pending independent review.
- [x] Instructions executable without oral context — named non-author verifiers `round1-independent-review` and `round2-independent-review`, `.shokunin/harness-integrity/LOG.md:20-21`; round-3 addition pending independent review.
- [x] No cross-domain bleed; PROVINCE remains accurate — named non-author verifiers `round1-independent-review` and `round2-independent-review`, `.shokunin/harness-integrity/LOG.md:20-21`; `git show --format= --name-only ecb330761fbcf80f293517d2a8e3514bbfc3f0d6` proves this round work scope, pending independent review.
