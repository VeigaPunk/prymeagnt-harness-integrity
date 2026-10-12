# Round 14 — payload-ID identity check

Baseline at parent commit `1f888d5c5fb69204cc8c48d5c6283012a3598eb1`: `audit.py` indexed each expected entry by dictionary key but did not verify the payload `HarnessEntry.id`. A copied live state with only the `primeagent-harness-integrity` subagent payload ID changed to `wrong-payload-id` still exited 0 and reported 4/4.

The audit now compares each fetched subagent, memory, and skill payload ID to its expected key-derived ID. The mutation suite separately changes only each of those three payload IDs in a deep-copied state while retaining the dictionary key; each now exits 1, reports 3/4, and names the expected and actual IDs. The unchanged copied state remains 4/4. All previous mutation controls remain in the same suite, including invalid/missing identity, rank/promotion, roster pointers, fifth mint, copied title/content, selector and prior structural controls. Fresh live audit remains 4/4.

Reproduction from repo root:
- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` — exit 0; all assertions pass; three payload-ID negatives rejected, intact/fresh positives 4/4, fifth-mint positives 5/5.
- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` — exit 0; current live snapshot 4/4.

Depth **improved** narrowly for payload-ID mismatch detection in the three expected entries. Calibration **improved** narrowly: the tested copied-state false pass is rejected without rejecting the intact copy. This does not attest semantic correctness, all state invariants, or runtime behavior; the mismatch was synthetic, not observed live drift. No global harness, manifest, runtime source, or other lane was changed. No push or provider/daemon action.
