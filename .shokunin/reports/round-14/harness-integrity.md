# Round 14 — harness-integrity — payload identity

**Base:** `1f888d5c5fb69204cc8c48d5c6283012a3598eb1`
**Work commit:** `3aab2803a4cf8a015a91a78d522150915b6fd775`
**Scope:** `.shokunin/harness-integrity/**` and this report only.

## Finding and change

`audit.py` located each expected harness entry through `state.entries[kind][expected_key]`, but did not check the retrieved payload's own `HarnessEntry.id`. The live loader allows key and payload ID to differ. On the baseline, a private deep-copy mutation that changed only the harness-integrity subagent payload ID while retaining its expected dictionary key exited 0 and reported 4/4.

The audit now checks payload ID against the expected ID for the subagent, memory, and skill. The mutation suite adds one isolated copied-state control per kind. No real global state is edited.

## Verification

Run from the repository root with the project kernel environment:

- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` — exit 0. All assertions pass; each of the three payload-ID mutations is rejected at 3/4; intact and fresh live snapshots pass 4/4. Existing mutation controls remain, including authorized promotion, roster and rank negatives, fifth synthetic mint positives (5/5), prior identity/content and selector controls.
- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` — exit 0; live snapshot reports 4/4.
- `git diff --check` — passed before commit.

## Axis verdicts

- **Depth: improved narrowly.** The audit detects a mismatch between key-derived expected ID and payload ID for each of the three triple entry kinds.
- **Calibration: improved narrowly.** The synthetic copied-state false pass is rejected while intact and fresh live positives remain passing.

No numeric score inferred. The mismatch was a synthetic fixture, not observed live drift. This change does not claim semantic correctness, completeness of all runtime state invariants, or runtime behavior attestation.

## Exact scope and exclusions

Changed only:
- `.shokunin/harness-integrity/corpus/knowledge/audit.py`
- `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py`
- `.shokunin/harness-integrity/corpus/lessons/round-14-identity.md`
- `.shokunin/harness-integrity/corpus/README.md`
- `.shokunin/harness-integrity/LOG.md`
- `.shokunin/harness-integrity/SCORECARD.md`
- `.shokunin/reports/round-14/harness-integrity.md` (this report; committed last)

No MANIFEST, global harness, runtime source, or other lane was changed. No push, provider, or daemon action.


## Review correction — supersedes the R14 proposal and verdict above

Independent review found that the runtime loader in `harness.py` (lines 550–552) overwrites each loaded payload `id` from its dictionary key. Therefore the tested key/payload mismatch is a private copied-state invariant, not a persisted mismatch that ordinarily reaches this audit through the runtime loader. The earlier suggestion that this establishes live persisted triple-integrity improvement was not supported.

Corrected axis verdict: **depth unchanged/unprovable for live persisted triple integrity**; **calibration unchanged**. There is **no axis advance** for R14. The private copied-state test still demonstrates that this audit rejects such a fabricated in-memory mismatch, but it is not evidence of a production-reachable corruption path or improved live-state coverage. The implementation and original test evidence are retained; this appended correction supersedes their two-axis-improvement interpretation. The original report also incorrectly stated `git diff --check` passed: review found trailing spaces on the two metadata lines. They have now been removed in this correction commit.
