# rlm-dispatch — round 8 report

## Work performed
- Audited the R7 path comparison against the actual round-2 observed `rlm-subagent.json` fields and value. It records absolute `sessionFile` `/home/vgpnk/.prime/agent/session-artifacts/01a12d0c-9c40-7153-9d7f-967a6e189ec5/sub-52e968c6/01a12d0c-e484-7627-b92e-d6138e736572.jsonl` with `childId=sub-52e968c6`, `sessionDir` for that child, model, and completed status; see `.shokunin/reports/round-7/rlm-dispatch.md` and the local observed artifact. Existing verifier compares resolved supplied `sessionFile` with registry path and separately checks child directory basename / collect child id.
- Checked all eight documented synthetic fixture scenarios against baseline verifier from `984a3a6` and current verifier. In README order both yielded `0/1/0/1/1/0/1/1` (reproduction command: eight invocations in `.shokunin/rlm-dispatch/corpus/verification/README.md`, with baseline loaded from `git show 984a3a6:...`; outputs recorded in round-8 work transcript).
- `git diff --check` passed. No verifier or fixture changes were warranted.

## Landed changes
- Recorded the audit and unchanged axis verdicts in `.shokunin/rlm-dispatch/LOG.md`; updated planned move in `SCORECARD.md`. Work commit: `aeb8d34da52a8958d409d24fb96bc93f4ab00e09`.
- Work commit author and committer: `rlm-dispatch-shokunin <rlm-dispatch@shokunin.local>` (verified with `git show -s --format=... HEAD`). The report is committed separately after this work commit.

## Before → after measurements
- Calibration question: can symlink alias normalization cause a material false accept/reject for recorded receipt structure? No: an alias resolving to the same file denotes that same underlying session file; a distinct file has a distinct resolved path. The registry field is observed context for binding, not authentication, and no authenticity claim is made.
- Baseline `984a3a6` and current verifier fixture exits were identical: `0/1/0/1/1/0/1/1`. No fixture behavior changed. Synthetic only; no live runtime, provider authentication, or usage-depletion evidence is claimed.

## Axis verdicts
- Operability: **unchanged** — no verifier/code change; all eight regression fixture outcomes preserved.
- Calibration: **unchanged** — no concrete material false accept/reject found within the observed receipt shape; no unsupported cryptographic or undocumented-field requirements introduced. No axis advanced; preserve code.

## SHONEN
- [~] Real decision tables/error patterns/checklists with cited sources — prior cited procedure remains; round 8 audited against round-2 observed registry documented in the R7 report.
- [~] End-to-end domain task executed and logged — synthetic verifier audit only; no new live RLM task.
- [~] Instructions executable without oral context — ran the eight README scenarios against baseline and current verifier.
- [~] No cross-domain bleed; PROVINCE remains accurate — only `.shokunin/rlm-dispatch/**` and this report changed.

## Limits
- No live RLM operation or usage-depletion inference. No changes outside `.shokunin/rlm-dispatch/**` and `.shokunin/reports/round-8/rlm-dispatch.md`; no MANIFEST/global/source edits or push.
