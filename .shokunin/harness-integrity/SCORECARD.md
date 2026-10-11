# harness-integrity scorecard — probation baseline

Owned axes: depth, calibration. Scores are not assigned without a measured craft round.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a`: `git ls-tree -r --name-only 44a08fd0eeb22c7ed9766aae4675dd452eff232a .shokunin/harness-integrity/corpus/knowledge | grep -c global-triples.md` → 0; round 1: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → 4/4 at round-work HEAD (hash in report). A score 0–10 is not inferred from this count. | round 1 |
| calibration | unmeasured | baseline at `git rev-parse HEAD`; no round yet | mint |

planned: depth — four cited global triples with live read-only callable resolution; next round re-run against fresh harness state before relying on the snapshot. Calibration remains unmeasured, with no independent non-author review.
retired: none.
