# skill-discovery append-only log

## Mint 2026-10-11
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: `.shokunin/mints/skill-discovery.md`; sources: `.shokunin/skill-discovery/corpus/knowledge/seed.md`.
- Next falsifiable move: execute one bounded read-only task, cite before/after, and have L1 judge every owned axis.

## Round 1 — 2026-10-11
- Added a sourced, actionable checklist separating installed-file presence, frontmatter validation, fresh-process discovery, and existing-process reload; includes a read-only `prime-agent prompt` probe and explicitly marks reload unrun. Evidence: `corpus/lessons/2026-10-11-skill-discovery-checklist.md` §§1–4; source contracts: `scripts/install-skills.sh:12-49`, `docs/capability-survey.md:1.2`, `verification/smoke-test.log` Checks 0d–0e, installed `skill-creator/SKILL.md` Frontmatter/Verification.
- Safe fresh-process probe run in the assigned worktree: `prime-agent prompt 2>/dev/null | grep -nE 'godspeed|shokunin|ufo' | head -9`; returned all three names and installed-file locations at `/home/vgpnk/.prime/agent/skills/`. This validates the probe only for this environment; no install or interactive reload was run.
- Operability checkpoint count: before 0 actionable lane checklist checkpoints (seed only cited sources, no procedure); after 4 distinct checks in the lesson. Freshness is not improved by this documentation move; the cited survey and runtime snapshot are dated 2026-10-11 and should be rechecked before reuse.
- Verdict proposal for L1: operability improved; freshness unchanged. Evidence is a sourced checklist plus a successful safe fresh-process probe; no assertion of reload success.


## Round 2 — 2026-10-11
- Added read-only repeatable freshness probe at `corpus/probes/freshness.sh`: records date, CLI version, source commit, source SHA-256/mtime, candidate installed-copy SHA-256/mtime, and fresh-process winning discovery location; returns nonzero on drift or missing inventory. Command: `.shokunin/skill-discovery/corpus/probes/freshness.sh`.
- Evidence: run at 2026-10-11T19:20:17-03:00, prime-agent 0.10.0, source commit `65a1d7b8215bf1bb764c0c9957f217a930f27b78`; all 3 source skills discovered from `~/.prime/agent/skills`; godspeed installed copy hash matched, while shokunin and ufo hashes differed. All three `~/.agents/skills` candidates differed. Probe output is recorded in round report. No source/install/reload mutation.
- Operability preserved; freshness probe makes drift falsifiable/reproducible and flags observed drift. L1 verdict proposal: freshness improved, operability unchanged.
- Provenance: [1/2] primary evidence is live probe output and source script; [2/2] interpretation of whether non-winning `~/.agents` candidates count as owned installations remains open at `.shokunin/l0-questions.md`; candidate copies are reported separately, not treated as actual discovery winner.

## L1 non-author review correction — round 2
- Supersedes only the inaccurate SCORECARD phrase “drift for all 3 skills”: reviewer `round2-independent-review` independently reran `.shokunin/skill-discovery/corpus/probes/freshness.sh` at integrated commit `68b425729ffbceb2d4fdfc59d1e154a52360de3f` and saw **2 of 3 winning `~/.prime/agent/skills` copies drift** (shokunin, ufo), godspeed matched; **all 3 non-winning `~/.agents/skills` candidates drift**. Exit 1 reports real drift and is not a passing installation check. `source_mtime` uses worktree time rather than commit metadata, and missing installed candidates are silently skipped; probe does not certify installation completeness. Freshness verdict remains improved for detection capability only.

## Round 3 — 2026-10-11
- Corrected `corpus/probes/freshness.sh` to fail on missing primary/winning installed target and winning hash drift, while reporting non-winning competing copies as informational only. Added isolated fixture controls for source, primary, competing roots, and inventory input; live mode remains read-only. Fresh inventory path must equal the expected primary target. Evidence: probe implementation and fixture test output; no installation or reload performed.
- Positive fixture: all three primary targets exist and match source, inventory resolves to primary, all competing candidates are stale; exit 0, competing drift informational. Negative fixtures: missing all primary targets despite inventory entries exited 1; replacing one winner with stale content exited 1. Both outputs showed no failure caused by competing candidate drift itself.
- Operability move measurement: before, probe silently skipped absent target files and failed for stale non-winning candidate copies; after, separate fixture correctly passes with matching winners/stale competitors and fails for absent or drifted winners. Counting command: `grep -c 'winning_installed=.*MISSING' .shokunin/skill-discovery/corpus/probes/freshness.sh` and `grep -c '(informational)' ...`; behavior validated by isolated runs. Freshness unchanged: no actual installed file, install or reload checked this round.
- Verdict proposal for L1: operability improved; freshness unchanged. End-to-end install/reload remains unrun, so SHONEN box 2 remains unchecked. Existing L0 question from round 2 about ownership of non-winning `~/.agents/skills` candidates remains open; routed around by treating them informationally.

## Independent review receipts — rounds 1–2
- `round1-independent-review` at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` independently counted four checkpoints and repeated fresh `prime-agent prompt` inventory. `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f` independently reran freshness probe: exit 1 indicating drift (2/3 winning copies, 3/3 non-winning candidates), fresh inventory 3/3, and checked own province scope. Recommends boxes 1, 3, 4 for documented checks; box 2 only for read-only discovery/freshness task, **not** actual install + reload lifecycle. L1 conservatively leaves box 2 unchecked until an isolated end-to-end lifecycle is exercised. Rank remains shonen.

## Independent review — round 3
- Named non-author `round3-promotion-review` at `c8129fdf789e1de9fc17900b1a3b0cea6634abe0` independently exercised isolated positive fixture exit 0, absent/drifted winner and inventory mismatch exit 1, and verified fixture cleanup. R3 operability improved/freshness unchanged, 3/3 verified rounds for read-only work, but SHONEN actual isolated install/reload end-to-end box remains unchecked; no promotion.

## Round 4 — 2026-10-11
- Added `corpus/probes/isolated-lifecycle.sh`: builds a disposable valid markdown skill, installs with `scripts/install-skills.sh` into a private scratch project's `.prime/agent/skills`, validates file/frontmatter, then runs fresh `prime-agent prompt --cwd <scratch>` and checks discovered name/location. Reproducible command: `.shokunin/skill-discovery/corpus/probes/isolated-lifecycle.sh`; observed exit 0, output named the isolated target path. The installer accepts both `SKILLS_SOURCE` and a positional target; confirmed by source at `scripts/install-skills.sh` lines 4-9, 22-23 and execution. Scratch directory is trap-cleaned.
- Attempted `prime-agent prompt --cwd <scratch> --skill <path>`; CLI rejects `--skill` for the `prompt` subcommand. Top-level `prime-agent --skill <path> --no-session --print ...` reached model inference but failed with `402 Insufficient balance`, so it is not used as evidence. The regular fresh-process inventory did discover the isolated skill via the private project's path.
- No separate daemon-backed disposable session was started, and `/reload` was not exercised; the candidate route used fresh-process inventory instead. Therefore actual install + discovery is demonstrated, but daemon reload lifecycle remains unverified; SHONEN box 2 stays unchecked. Temporary run output is not durable evidence; committed probe enables reproduction.
- Operability verdict proposal: **improved** (previously fixture-level absence/drift behavior; now an end-to-end private install/frontmatter/fresh-process discovery workflow is reproducible). Freshness: **unchanged** (no live installed tree or daemon reload state inspected). No shared skill dirs, settings, prompt, or live TUI were changed.

## R4 independent review and L1 decision
- Named non-author gate-and-skill-r4-review at 10e7b98 reran private install/frontmatter/fresh-process inventory exit0, verified path and scratch removal. L1 admits R4 operability improved/freshness unchanged. No separate daemon reload or live shared install; SHONEN end-to-end box stays unchecked. Top-level inference 402 is route-specific, not documented OpenAI-only model usage depletion.


## Round 5 — 2026-10-11 (freshness axis)
- Investigated documented CLI lifecycle (`prime-agent --help`, `help status/attach/doctor/shutdown`) and live receipts: `prime-agent status` => no background services; `prime-agent list` showed many existing sessions; `ps` showed shared daemon PID 3336 and workers. `shutdown` stops every agent/services and no documented private daemon/socket start path surfaced, so avoided any daemon/session/reload action.
- Fallback is deliberately **not daemon reload**. `corpus/probes/fresh-process-inventory.sh` uses only private temporary `--cwd` inventory and scratch `.prime/agent/skills`; before/after separate `prime-agent prompt` processes saw absent then present new skill. Exit 0; process/scratch/hash receipts and bounds are in `.shokunin/reports/round-5/skill-discovery.md`. Scratch removed by trap. No model calls, shared install/settings/TUI edits, MANIFEST/global/source edits.
- Freshness unchanged: new-process inventory discovery measured; existing process reload not. Operability unchanged; R4 private install pass preserved. SHONEN box 2 unchecked.

## R5 independent review and L1 judgment
- Named non-author goal-boundary-and-freshness-review at bff8d3d reran private fresh-process inventory before/after with distinct CLI PIDs and scratch cleanup. It confirms only fresh process discovery, not live daemon reload. L1 records R5 freshness unchanged/operability unchanged: NO admitted axis advancement and no promotion; SHONEN end-to-end remains unchecked.

## R6 independent review and L1 judgment
- Named non-author preflight-and-noaxis-review at a30472f tested daemon path/env preflight: fake distinct paths pass; same socket, overlapping store, inherited PRIME_AGENT_INTERNAL_* each refuse. No daemon/session/reload launched; L1 records R6 freshness/operability unchanged and SHONEN end-to-end unchecked; preflight is not authorization to launch.

## Round 7 — 2026-10-11 (operability axis)
- Audited fake-path cases in `corpus/probes/daemon-isolation-preflight.sh`. Symlinked store aliases were already canonicalized by `realpath -m` and refused; a concrete false pass remained: private store `/` with an otherwise distinct socket and live store passed because slash-root containment was not represented by the trailing-slash overlap checks.
- Added a minimal guard refusing `/` as either private or live store. Before fixture: isolated invocation with private store `/`, private socket in scratch, ordinary live store/socket printed `PATH_PREFLIGHT_PASS` and exited 0. After fixture: same invocation prints `REFUSE filesystem root as agent store`, exits 1. Positive distinct fake paths still exit 0; nested-socket and inherited-state refusal remain checked. All tests used fake temporary paths / `env -i`; no daemon, session, or reload launched.
- Operability proposal: improved (preflight now rejects an observed isolation false pass). Freshness unchanged; this is not proof of private daemon isolation and does not advance freshness or SHONEN box 2. Existing R4 private install and R5 fresh inventory remain untouched.
