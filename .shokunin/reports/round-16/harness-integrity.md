# harness-integrity — round 16

- Owned axes: depth, calibration. Single move: depth, structural timestamps of expected global triple entries.
- Isolated worktree `craft/harness-r16-time`, base `119f01067c45eb9a8e8514bd1327645e0364669f`. Work commit `60e889405b6979a84a26fea9433aa8ce43aacc76`; author and committer both `harness-integrity-shokunin <harness-integrity@shokunin.local>`.

## Evidence
- Baseline audit did not check timestamps: the scouted private persisted JSON mutations (`created_at='not-a-date'`, naive `created_at`, reversed `updated_at`) passed 4/4. Installed loader preserves these values; installed `_now` produces aware UTC ISO timestamps and ordinary update advances `updated_at`. The former is synthetic corruption evidence, not an observed live drift or proof of historical authenticity.
- `audit.py` now parses both fields via `datetime.fromisoformat`, checks each UTC offset exists, and requires `created_at <= updated_at`, for every expected minted subagent, memory, and skill. This checks structural validity only, not genuine time of creation, historical monotonicity, provenance, or semantic content.
- `mutation_test.py` copies actual persisted global JSON to private temporary paths, verifies intact private loader state 4/4, writes each mutation separately, explicitly calls `.load()` on the cached state, confirms the loader retained the mutation, and expects audit exit 1 / 3/4. Memory cases cover malformed creation, naive creation, and reversed ordering; subagent and skill have representative malformed timestamp cases. Existing R15 negative-version mutants remain rejected 3/4 each. No live global harness write.
- Native commands from repository root: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` exited 0 (intact 4/4, five timestamp negatives 3/4, three version negatives 3/4, prior suite including synthetic fifth mint 5/5 and authorized promotion 4/4, fresh live 4/4). `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` exited 0, live 4/4; `git diff --check` exited 0 before work commit. Twelve expected live triples have present timestamps and passed the new audit.

## Per-axis verdict
- **Depth: improved narrowly** for detecting these structurally malformed/naive/reversed timestamp values on expected triples.
- **Calibration: unchanged.** No second axis move or scalar score.

Assumption: timestamp structural consistency is useful for persisted expected triples; no claim of timestamp authenticity. Constants changed: none; test fixture dates are synthetic. No manifest, global harness, provider, daemon, source runtime, push, merge, or promotion changes.
