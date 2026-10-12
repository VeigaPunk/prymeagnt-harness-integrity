# harness-integrity — round 15

- Owned axes: depth, calibration. Single move: depth (expected triple version integrity).
- Work commit: `e83022cfdf5381a67e64617fc8f17dcd0591c6a2` on isolated worktree `craft/harness-r15-version`, based on `082d7ce`. Author **and** committer: `harness-integrity-shokunin <harness-integrity@shokunin.local>`.

## Evidence and provenance
- Previous R14 premise was false: installed prime-agent kernel `rlm/harness.py:563-571` retains integer `-1` while loading persisted JSON. `HarnessEntry.version = 1` (`:199`) and the normal update path increments (`:763`); this establishes the positive-integer version expectation, not authenticated historical provenance. Baseline audit lacked version checks; a corrupted expected triple could pass 4/4. Do not infer the ordinary API creates negative versions.
- `audit.py` now checks `type(entry.version) is int and entry.version >= 1` for each expected minted subagent/memory/skill. No changes to runtime, global harness, or manifest.
- `mutation_test.py` copies the **real persisted global JSON** to a private temporary directory. Per kind, intact private loader-path state agrees with live version and audits 4/4; the copied JSON is then edited to `version: -1`, and its cached `rlm.get_harness_state(state_dir=private,global_=True)` object is explicitly `.load()`-reloaded. Loader preserves `-1`; audit rejects each of three isolated mutations at 3/4. This is a synthetic private persisted-payload corruption test, not observed live drift. The explicit reload accounts for `get_harness_state` cache behavior; it does not claim repeated gets refresh the cache.
- Native project environment commands from repo root: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` exited 0, including intact copy 4/4, twelve live expected versions positive, all prior mutation controls (authorized promoted 4/4, synthetic fifth minted 5/5, digit-bearing fifth minted 5/5, negative cases), and fresh live snapshot 4/4. `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exited 0, live 4/4. `git diff --check` exited 0 before work commit.

## Per-axis verdict
- **Depth: improved**, narrowly: the audit now detects private persisted corruption of the expected triple's version in subagent, memory, and skill. All baseline positives retained.
- **Calibration: unchanged.** Mutation controls bound the depth claim; no separate calibration axis move.

Limits: current snapshot and expected triples only; positive versions do not attest to semantic content, the correctness or monotonicity of history, provenance, runtime dispatch, or future state. Private tests do not show live corruption. No global harness write, provider call, daemon change, push, merge, or rank change.
