# harness-integrity scorecard — probation baseline

Owned axes: depth, calibration. Scores are not assigned without a measured craft round.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a`: `git ls-tree -r --name-only 44a08fd0eeb22c7ed9766aae4675dd452eff232a .shokunin/harness-integrity/corpus/knowledge | grep -c global-triples.md` → 0; round 1: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → 4/4 at round-work HEAD (hash in report). A score 0–10 is not inferred from this count. | round 1 |
| calibration | unmeasured | round-2 baseline live `audit.py` → 4/4; `mutation_test.py` → intact copy exit 0 (4/4), removed skill exit 1 (3/4), fresh live exit 0 (4/4); commands and measured work commit in `.shokunin/reports/round-2/harness-integrity.md`. No 0–10 score inferred. | round 2 |

planned: calibration — round-3 mutation suite rejects missing ID and nonexistent import (negative 2/2), accepts intact copy and fresh live (positive 2/2); run `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` and see `corpus/lessons/round-3-calibration.md`. Depth still requires fresh read-only audits before relying on a snapshot. Round-3 controls await non-author verification.
retired: none.

round 4 measured (axis calibration, no scalar inferred): at `c8129fd`, rank was hardcoded `shonen`, so a real shokunin promotion could not pass despite matched manifest/harness. After work commit (hash in round-4 report), run `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: positive 3/3 (intact 4/4, promoted copy 4/4, fresh live 4/4), negative 5/5 (missing skill 3/4, invalid import 3/4, unauthorized roster 3/4, stale harness 3/4, missing roster fails). `audit.py` fresh live remains 4/4. Calibration improved; depth unchanged; no numerical score inferred. Earlier round-3 "planned" status above is historical, not current.
