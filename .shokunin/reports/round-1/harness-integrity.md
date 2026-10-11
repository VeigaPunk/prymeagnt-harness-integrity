# harness-integrity — round 1

Owned axes: depth, calibration. One axis-move: depth. Work commit: `c1ee05b6d0089fbed42bf1a25e215dd3b359f035` (`git rev-parse HEAD` when this report was written). Domain sources and global harness were read-only; no L2 lanes were warranted for a four-entry, bounded audit, so L2 is not-dispatched. Remote push and MANIFEST/global harness mutation are L1-owned.

## Work performed
- Read the mint triple and probation contract (`docs/shokunin-workflow.md:68-97`, `skills/shokunin/SKILL.md:78-103`) and reconciled `.shokunin/MANIFEST.json` `rounds[0].minted` with live global state (`.shokunin/harness-integrity/corpus/knowledge/global-triples.md:3-20`, `c1ee05b6d0089fbed42bf1a25e215dd3b359f035`).
- Added a cited checklist for all four triples (`.shokunin/harness-integrity/corpus/knowledge/global-triples.md:11-20`, `c1ee05b6d0089fbed42bf1a25e215dd3b359f035`).
- Executed the read-only runtime audit at `c1ee05b6d0089fbed42bf1a25e215dd3b359f035`: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → `verified triples: 4/4; lanes: harness-integrity, rlm-dispatch, gate-evidence, skill-discovery` (exit 0); callable imports resolved, but skill functions were not invoked (`.shokunin/harness-integrity/corpus/knowledge/audit.py:20-72`).

## Landed changes
- `.shokunin/harness-integrity/corpus/knowledge/global-triples.md:1-20`, `corpus/knowledge/audit.py:1-72`, `corpus/README.md:3-7`, and `SCORECARD.md:1-11` record the one depth move; linked in `.shokunin/harness-integrity/LOG.md:7-12`, carried by `c1ee05b6d0089fbed42bf1a25e215dd3b359f035`. The report is a separate, later commit.

## Before → after measurements
- **Depth claim** — before at `44a08fd0eeb22c7ed9766aae4675dd452eff232a`: `git ls-tree -r --name-only 44a08fd0eeb22c7ed9766aae4675dd452eff232a .shokunin/harness-integrity/corpus/knowledge | grep -c global-triples.md` → `0` (grep exit 1). After at `c1ee05b6d0089fbed42bf1a25e215dd3b359f035`: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → `verified triples: 4/4` (exit 0). **Verdict: improved** for this live-state snapshot, not a version-pinned or semantic certification.
- **Calibration verdict: unchanged** — no independent reviewer or before/after calibration measurement. The limits are explicit at `.shokunin/harness-integrity/corpus/knowledge/global-triples.md:5-9`; no pass is inferred.

## SHONEN
- [~] Real sourced checklist: `.shokunin/harness-integrity/corpus/knowledge/global-triples.md:3-20`; non-author verification pending.
- [~] End-to-end read-only triple task: `.shokunin/harness-integrity/LOG.md:7-12` and audit output above; non-author verification pending.
- [~] Standalone execution instructions: `.shokunin/harness-integrity/corpus/knowledge/global-triples.md:5-9` and `audit.py:1-5`; non-author verification pending.
- [~] Province boundary: `.shokunin/harness-integrity/PROVINCE.md:1-14`, no outside-scope edits in `c1ee05b6d0089fbed42bf1a25e215dd3b359f035`; non-author verification pending.

No open operator question. L1 must independently judge admission; the empty probation roster is expected per `docs/shokunin-workflow.md:94-97`.
