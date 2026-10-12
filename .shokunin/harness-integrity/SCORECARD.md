# harness-integrity scorecard — probation baseline

Owned axes: depth, calibration. Scores are not assigned without a measured craft round.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a`: `git ls-tree -r --name-only 44a08fd0eeb22c7ed9766aae4675dd452eff232a .shokunin/harness-integrity/corpus/knowledge | grep -c global-triples.md` → 0; round 1: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py` → 4/4 at round-work HEAD (hash in report). A score 0–10 is not inferred from this count. | round 1 |
| calibration | unmeasured | round-2 baseline live `audit.py` → 4/4; `mutation_test.py` → intact copy exit 0 (4/4), removed skill exit 1 (3/4), fresh live exit 0 (4/4); commands and measured work commit in `.shokunin/reports/round-2/harness-integrity.md`. No 0–10 score inferred. | round 2 |

planned: calibration — round-3 mutation suite rejects missing ID and nonexistent import (negative 2/2), accepts intact copy and fresh live (positive 2/2); run `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` and see `corpus/lessons/round-3-calibration.md`. Depth still requires fresh read-only audits before relying on a snapshot. Round-3 controls await non-author verification.
retired: none.

round 5 measured (axis depth, no scalar inferred): baseline audit hardcodes `rounds[0].minted` and four lanes. On work commit (hash in round-5 report), `mutation_test.py` passes fifth mint copied-state 5/5, duplicate-ID and unmatched-checklist negatives exit 1, and retains four-lane controls; live `audit.py` passes 4/4. Depth improves for a future-ledger structural fixture; calibration unchanged pending non-author review. No numerical 0–10 score inferred.

round 6 measured (axis depth, no scalar inferred): baseline copied rank-correct wrong roster `province` exited 0 and verified 4/4 despite divergence; after work commit (hash in round-6 report), `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` rejects wrong `province`, `axes`, `harness_spec` separately at exit 1, 3/4. Valid four-lane and fifth synthetic mint pass; prior rank negatives reject; live `audit.py` passes 4/4. Depth improved for roster pointer integrity; calibration unchanged absent live divergent roster and independent review. No 0–10 score inferred.

round 7 measured (axis calibration, no scalar inferred): copied reference to valid `rlm.find_models` falsely passed 4/4 exit 0 before the change, despite checklist citation `rlm.get_harness_state`; after work commit (hash in round-7 report), `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` rejects copied wrong callable 3/4 exit 1, retains intact/fresh-live 4/4 and synthetic fifth mint 5/5, and prior negative guards. Live `audit.py` 4/4 exit 0. Calibration improved for this isolated cited-reference mismatch; depth unchanged; no numeric score inferred.

round 4 measured (axis calibration, no scalar inferred): at `c8129fd`, rank was hardcoded `shonen`, so a real shokunin promotion could not pass despite matched manifest/harness. After work commit (hash in round-4 report), run `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: positive 3/3 (intact 4/4, promoted copy 4/4, fresh live 4/4), negative 5/5 (missing skill 3/4, invalid import 3/4, unauthorized roster 3/4, stale harness 3/4, missing roster fails). `audit.py` fresh live remains 4/4. Calibration improved; depth unchanged; no numerical score inferred. Earlier round-3 "planned" status above is historical, not current.

round 9 measured (axis depth, no scalar inferred): copied wrong-lane title/content previously passed 4/4 (isolated subagent title/content baseline). At R9 work commit (hash in report), `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` rejects six separately copied title/content claims 3/4, retains authorized round-4 rank positive 4/4 and fifth synthetic mint 5/5; live `audit.py` passes 4/4. Depth improved for opening triple-identity consistency; calibration unchanged; no live drift or numeric score inferred.

round 8 measured (axis calibration, no scalar inferred): copied promoted harness-integrity roster `promotion_round=3` falsely exited 0, 4/4 against ledger promotion R4 before work. At R8 work commit (hash in report), `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` rejects copied round mismatch for both promoted lanes 3/4, retains authorized round-4 positive 4/4 and synthetic fifth mint 5/5; `audit.py` live 4/4. Calibration improved for isolated mismatch detection; depth unchanged. No live drift or numerical score inferred.


## L1 correction — reviewed R10–R12 (2026-10-12)
Supersedes stale planned text above that leaves R3 controls awaiting verification: L1 has reviewed the R10 no-axis clarification and R11/R12 reports. R10 depth/calibration unchanged. R11 and R12 calibration improved narrowly for the synthetic digit-bearing and underscore IDs/citations; depth unchanged. Their native copied-state suites passed, including 5/5 for the added synthetic fifth-mint case; live audit remained 4/4. See `.shokunin/harness-integrity/LOG.md` and `.shokunin/reports/round-11/harness-integrity.md`, `.shokunin/reports/round-12/harness-integrity.md`. Limits: synthetic parser cases/current snapshot only, no real-world impact or unrestricted ID grammar claim. The separate global procedure v6 L1 self-refinement validation (native fixtures 5/5, live 4/4) is procedure maintenance, not a new craft round. No axis score or rank is assigned; historical entries above are retained.


## Round 13 — depth move (2026-10-12)
- Claim: a donor-body substitution preserving the lane opening that previously passed the live audit should fail a copied-state fixture, while intact/promotion/fifth-mint positives remain passing.
- Before → after: the specified donor-body mutant went from audit exit 0 / 4/4 before the change to exit 1 / 3/4 after; isolated removal of report path, volume selector, one-axis phrase, and L1 admission phrase each exits 1 / 3/4. `mutation_test.py` retains authorized promotion 4/4 and synthetic fifth mint 5/5 (including digit-bearing IDs), and live `audit.py` remains 4/4.
- Verdicts: depth **improved** for structural detection; calibration **unchanged**. No numeric score inferred. Limits: substring presence is not semantic proof, no full template fidelity/runtime admission check, copied-state only, current snapshot only. Evidence and work commit `e5d52893d2779086c8e3aa6e79446a19cfb7a2ce`: `.shokunin/reports/round-13/harness-integrity.md`.


## Round 13 correction — superseding verdict scope
The initial R13 claim that the audit structurally checked one-axis and L1 admission clauses is superseded. Literal phrase tests were removed after review found false rejection of paraphrases and inert-appendix false acceptance. Revised checks cover only lane-specific report-address presence and selector presence matching an exact allowed metadata pair. Donor remainder rejected; legitimate paraphrase accepted; wrong selector content and metadata rejected; prior controls and live 4/4 retained. Depth is improved narrowly for those tested address/selector-presence mutations; calibration unchanged. This does not validate round-contract semantics, operative content, or runtime admission. No scalar score inferred.


## Round 14 — depth and calibration move (2026-10-12)
- Baseline: copied subagent payload ID mutation with unchanged dictionary key exited 0 / 4/4. After the change, separate subagent, memory, and skill payload-ID mismatches each exit 1 / 3/4; intact copy and fresh live audit exit 0 / 4/4. Native full mutation suite passes and retains prior controls, including fifth synthetic mint 5/5 and promotion fixtures.
- Verdict: depth **improved** narrowly for payload-ID detection; calibration **improved** narrowly for rejecting this tested synthetic false pass while retaining intact positive. No numeric score inferred. No live drift, semantic correctness, or runtime attestation claimed. Evidence: `.shokunin/reports/round-14/harness-integrity.md`.
