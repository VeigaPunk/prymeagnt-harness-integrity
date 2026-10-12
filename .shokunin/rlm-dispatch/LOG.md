# rlm-dispatch append-only log

## Mint 2026-10-11
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: `.shokunin/mints/rlm-dispatch.md`; sources: `.shokunin/rlm-dispatch/corpus/knowledge/seed.md`.
- Next falsifiable move: execute one bounded read-only task, cite before/after, and have L1 judge every owned axis.


## Round 1 — 2026-10-11
- Added an explicit-selector admission decision table, distinguishing lookup from admission and settlement evidence; corpus entry cites capability survey, smoke procedure, and rerun receipt.
- Live `rlm.find_models("OpenAI", limit=20)` returned selector `openai-codex/gpt-6-luna` (also `openai-codex/gpt-6-sol`). No lane-owned spawn was performed. The parent-provided receipt identifies child `sub-9bfd0406`; durable explicit-selector admission evidence is in `verification/smoke-test-rerun-20261011.log`.
- Operability: improved (live exact-selector discovery, parent-reported completed scout, and durable published explicit-selector receipt support an actionable decision table; the ephemeral scout registry itself was not independently inspected). Calibration: unchanged (no new runtime admission evidence to test calibration).

## L1 closure correction — round 1
- Supersedes the preceding optimistic operability verdict: the pre-existing published receipt count stayed **1 → 1** at baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a` and work commit `f12210537e8b2f0246c78547a82f28feb7cd2c62` using `grep -c "Smoke test 2 rerun" verification/smoke-test-rerun-20261011.log`. Operability is **unprovable-but-better**, calibration **unchanged**. The decision table is useful but its assigned receipt-count claim did not improve. L1 does not admit round 1; retain the work as a candidate and run a genuinely independent admission exercise in a subsequent round.

- Evidence: `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-selector-admission.md`; live REPL output; parent request sent through `agent_message`.

- Parent later supplied corroboration: child `sub-9bfd0406`, explicit `openai-codex/gpt-6-luna` selector, reported completed via `rlm.list_subagents()` plus child `agent_message`; ephemeral registry was not independently inspected. Durable prior explicit-selector evidence remains the published rerun log. This does not establish a lane-owned spawn.

## Round 2 — 2026-10-11
- Executed one self-owned read-only child probe with explicit `openai-codex/gpt-6-luna`; handle, registry, model_change, child reply, and terminal collect receipt agree. Early collect polls remained running despite child briefly appearing idle; terminal status was later observed by re-polling.
- Durable redacted receipt: `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-round2-admission.md`; corpus index row appended in `.shokunin/rlm-dispatch/corpus/README.md`.
- Operability: improved (first independently performed, durable lane-owned selector-admission and terminal-settlement receipt; count 0 → 1 in assigned round-2 receipts corpus, command/report details). Calibration: improved (independent runtime admission and terminal evidence confirms the procedure's distinction between admission, transient idle, and settlement). These are lane proposals; L1 judges.
- No >=8 wave: assignment specifies one bounded self-owned probe, not a multi-lane task.

## Independent review receipts — rounds 1–2
- `round1-independent-review` at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` verified sourced admission table and owned province, but no new lane-owned spawn (boxes 2/3 deferred). `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f` independently read depth-2 child transcript and registry: openai-codex/gpt-6-luna model_change, exact `rlm-dispatch-round2-ok` reply and parent collect done/settled=True/error=None after 49,509ms. Recommends SHONEN boxes 1–4 for bounded explicit-selector admission/settlement only. L1 records verifier names; rank remains shonen until >=3 verified rounds.

## Round 3 — 2026-10-11
- Added a read-only fixed-selector receipt verifier and sanitized positive/negative fixtures at `corpus/verification/`; reproducible command and checks are in the round-3 report.
- Validation outcome: positive fixture accepted (exit 0); wrong provider/model plus running/unsettled fixture rejected (exit 1). This is synthetic fixture evidence, not a new runtime admission receipt.
- Operability: improved (a reusable local verifier now detects wrong routing and unsettled receipts; baseline had no verifier). Calibration: unchanged (no additional live admission/settlement observation; fixture checks only validate the verifier implementation).
- Proposed harness self-refinement: add an RLM-dispatch procedure requiring local sanitized fixture-based checks after runtime receipts, with explicit separation of synthetic verifier tests from live admission evidence. Falsification: reject this proposal if a subsequent independent lane cannot reproduce the positive/negative exits from the documented command on the committed fixtures, or if the verifier mutates inputs / makes network calls. Awaiting L1 approval; no global harness edit made.

## Independent review — round 3
- Named non-author `round3-promotion-review` at `c8129fdf789e1de9fc17900b1a3b0cea6634abe0` independently reran fixture valid exit 0, wrong route/unsettled exit 1, source input hashes unchanged. R3 operability improved/calibration unchanged, but r1 failed; only 2/3 admitted verified rounds, so no promotion despite four SHONEN boxes. Synthetic verifier is NOT authenticated live provenance.


## Round 4 — 2026-10-11
- Added read-only correlation checks to the sanitized receipt verifier: registry `childId` must match the session directory basename and collect `rlm_child_id`; the sole assistant text reply must match collect `answer_preview`. Schema basis: round-2 receipt records registry child ID and collect `rlm_child_id`/`answer_preview` (corpus knowledge entry); session directory is keyed by child ID in recorded runtime artifacts. No new mandatory receipt keys beyond those observed fields were introduced.
- Falsifiable measure: the mixed-child fixture (registry/session child `sub-fixture-a`, settlement child `sub-fixture-b`) passed the prior verifier (`PASS`, exit 0) and is now rejected with `collect child ID does not match registry childId` (exit 1). Documented five commands retain the previous valid and invalid cases, and add linked-positive and wrong-reply negatives.
- Operability: improved (mixed-child counterfeit accepted → rejected; reproducible synthetic fixture checks). Calibration: unchanged (synthetic fixtures validate implementation only, not authenticated live provenance).
- All fixture data is sanitized and synthetic; no live provenance or runtime receipt is claimed. No non-OpenAI selector was used for a live spawn.

## Independent review and L1 decision
- Named non-author `growth-and-dispatch-review` at `291ecd39187451187377d11f3913f49f20c427f1` independently reran five synthetic fixture outcomes 0/1/0/1/1 and old verifier against same mixed-child fixture PASS exit0 versus new FAIL exit1. L1 admits R4 operability improved/calibration unchanged; rounds 2,3,4 are three admitted independently verified rounds (round 1 remains failed). All four SHONEN boxes have named prior non-author verification. L1 authorizes narrow shonen→shokunin promotion; no claim of authenticated live receipt from synthetic tests.


## Round 5 — 2026-10-11
- Tightened the read-only verifier to require every session `model_change` event to match the documented permitted `openai-codex/gpt-6-luna` selector. Added synthetic two-matching-events positive and late-forbidden-switch negative fixtures; retained all five prior fixture outcomes.
- Falsifiable measure: before change, baseline verifier accepted `late-forbidden-switch` (PASS, exit 0) because only the first route was checked; current verifier rejects it with `session provider/model mismatch` (exit 1). Current seven fixture outcomes: 0/1/0/1/1/0/1 in README order.
- Calibration: improved for recorded selector consistency (a route-change counterfeit that previously passed is rejected); this remains synthetic test evidence only, not authenticated live provenance or evidence of provider authentication/model usage depletion. Operability: unchanged (same verifier workflow and existing checks).
- No network calls or mutation of receipt inputs; no global harness edits, push, or source changes.

## Independent review and L1 judgment
- Named non-author roster-and-selector-review at 92a8dba reran seven fixture exits 0/1/0/1/1/0/1; old verifier accepted later forbidden selector (exit0), new rejects (exit1). L1 admits R5 calibration improved/operability unchanged. This is synthetic verifier behavior, not live provider authentication or documented OpenAI usage depletion.

## R6 independent review and L1 judgment
- Named non-author preflight-and-noaxis-review at a30472f reran seven synthetic fixture exits 0/1/0/1/1/0/1, inspected installed RLM collect `answer_preview: str|None` with no documented truncation or equality guarantee. L1 records R6 operability/calibration unchanged, no admitted axis move or speculative verifier change; no usage depletion evidence.


## Round 7 — 2026-10-11
- Inspected the exact round-2 live observed registry `.sessionFile` field: `rlm-subagent.json` records `sessionFile` alongside `childId`, `sessionDir`, model, and status; the receipt previously reproduced only child ID/model/status. The verifier did not compare this field to the supplied session path.
- Added a sanitized swapped-session fixture: registry points to the legitimate session path, but caller supplies a copied alternate session under the same `sub-fixture-a` directory name. Before change, verifier PASS (exit 0); after change, FAIL `session path does not match registry sessionFile` (exit 1). Existing seven fixture outcomes remain 0/1/0/1/1/0/1; new eighth is 1. All are synthetic verifier tests, not live authentication/provider/usage evidence.
- Operability: improved (a same-child-ID, swapped-session counterfeit previously passed and now fails; exact round-2 registry field supports the check). Calibration: unchanged (only verifier fixture behavior changed; no new live RLM observation).

## R8/R7 independent review and L1 judgment
- Named non-author promotion-and-session-review at 984a3a6 reran eight synthetic fixtures 0/1/0/1/1/0/1/1; old verifier false PASS same-child swapped-session, updated rejects via observed registry sessionFile. L1 admits R7 operability improved/calibration unchanged; path binding is not authenticated provenance and repo-relative fixtures require repo-root invocation.


## Round 8 — 2026-10-11
- Calibration audit target: determine whether `Path(...).resolve()` comparison of observed registry `sessionFile` and supplied session path has a material false accept/reject for the recorded RLM receipt structure. The round-2 observed registry contains an absolute `sessionFile` naming the JSONL under its child session directory (`.../sub-52e968c6/01a12d0c-e484-7627-b92e-d6138e736572.jsonl`); artifact path and fields are recorded in round 7 report. No additional undocumented field or cryptographic authenticity requirement was assumed.
- No material counterexample found: a symlink alias resolving to the same session file identifies the same underlying file, while distinct files resolve differently; registry value is not an authentication anchor by itself. This check cannot establish authenticity, and no such claim is made.
- Baseline verifier at `984a3a6` and current verifier returned the same eight fixture outcomes in README order: 0/1/0/1/1/0/1/1. Thus existing false-positive/false-negative controls neither improved nor regressed. Synthetic-only; no runtime or usage-depletion inference.
- Operability: unchanged. Calibration: unchanged; no axis advance. Preserve verifier code and prior fixtures. Evidence/report: `.shokunin/reports/round-8/rlm-dispatch.md`.
