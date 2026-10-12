# Round 17 — harness-integrity — private persisted source presence

## Claim and scope
Depth candidate: reject an expected minted global triple entry whose persisted `source` is empty or not a string. This is a narrow structural requirement, not a claim about origin, authenticity, provenance, or a particular source value such as `agent`. No live drift was observed. All corruption fixtures below are private synthetic copies.

## Before
The private persisted loader preserved `source: ""` on an expected memory entry and the prior audit had no source check, so this case passed 4/4. Native harness `_validate_entry_shape` requires a nonempty source string on writes; the read audit should apply the same structural presence constraint to each expected subagent, memory, and skill entry.

## Change
The copied audit now requires `isinstance(entry.source, str) and entry.source` for all three entries before accepting a triple. It does not assert `source == "agent"` or infer who created an entry. Mutation fixtures create private persisted copies, load them through `rlm.get_harness_state(...).load()`, and independently blank memory, subagent, and skill source values.

## Verification
- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: exit 0. Private persisted empty-source memory, subagent, and skill mutations each survive loader reload and fail audit at 3/4 with the expected failure. Intact private and fresh live copies pass 4/4.
- The mutation suite also passes its prior version/timestamp, reference, rank/roster, parser, identity, donor-body, and selector controls; fifth-mint fixtures pass 5/5.
- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py`: exit 0, fresh live snapshot 4/4.
- `git diff --check`: clean before commit. No manifest/global harness/provider/daemon changes.

## Verdict and limits
Depth **improved narrowly** for empty or non-string source values on the expected global triple; calibration **unchanged**. Synthetic persisted corruption only. This does not verify source authenticity, meaningfulness beyond nonempty string, or semantic correctness; it establishes no observed live defect and no guarantee about unrelated entries. No scalar score inferred. No merge or push.

Work commit and report-last commit recorded in repository history.
