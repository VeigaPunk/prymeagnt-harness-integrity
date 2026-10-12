# harness-integrity — round 13

- Axis set: depth, calibration. Intended move: depth.
- Claim: detect a copied subagent spec whose identity opening is intact but whose remainder is replaced by a donor lane, while retaining legitimate copied-state positives and live verification.

## Work performed
- Added narrow required-fragment checks for the lane report path, `openai-codex/gpt-6-luna`, `openai-codex/gpt-6-sol`, the one-axis contract, and the L1 admission boundary in `.shokunin/harness-integrity/corpus/knowledge/audit.py`.
- Added copied-state tests for the donor-body substitution and each isolated required-fragment loss in `.shokunin/harness-integrity/corpus/knowledge/mutation_test.py`.
- Consulted mint contract: `docs/shokunin-workflow.md:73-76` specifies subagent spec content; `docs/shokunin-workflow.md:108-125` defines one-axis move and admission rule. Executable round template in `skills/shokunin/templates/round-prompt.md` documents the report path and exact contract; `skills/shokunin/SKILL.md` documents mint form and selectors.
- Evidence: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` passed all controls; fresh `.shokunin/harness-integrity/corpus/knowledge/audit.py` exited 0 with 4/4.

## Landed changes
- Structural contract checks and copied-state controls; recorded in `.shokunin/harness-integrity/LOG.md` Round 13; work commit `e5d52893d2779086c8e3aa6e79446a19cfb7a2ce`.
- Author/committer identity: `harness-integrity-shokunin <harness-integrity@shokunin.local>`.

## Before → after measurements
- Donor remainder with intact harness-integrity opening: before change, copied audit exit 0 / 4/4; after, exit 1 / 3/4, missing lane report path. Synthetic copied-state mutation; not observed live drift.
- Removed each checked condition independently (selectors, one-axis phrase, L1 boundary): each exits 1 / 3/4. Donor body carries another lane's report path, so this checks lane specificity.
- Existing mutation suite positives retained: authorized promoted copy 4/4, synthetic fifth mint 5/5, digit-bearing fifth mint 5/5; prior missing-entry, reference, roster, copied-identity, mint-ID/citation controls pass.
- Fresh live audit: 4/4. Global state and MANIFEST were not changed.

## Axis verdicts
- **Depth — improved** narrowly: detects a copied spec remainder that abandons several mint-required dispatch-contract features while preserving its identity opening.
- **Calibration — unchanged**: tests measure only selected structural conditions; no calibration axis claim was made.

## Limits
Substring presence is not semantic evidence that a clause is operative or truthful. This does not establish exact round-template fidelity, runtime model admission, actual dispatch behavior, general semantic quality, or future freshness. It is copied-state testing plus a current mutable-global snapshot. No global harness edits, MANIFEST edits, source-tree changes, or push.

## SHONEN
- [ ] Real decision tables/error patterns/checklists with cited sources — untouched.
- [ ] End-to-end domain task executed and logged — not assessed in this round.
- [ ] Instructions executable without oral context — not assessed in this round.
- [ ] No cross-domain bleed with accurate PROVINCE — not assessed in this round.

Report commit hash: written after work commit `e5d52893d2779086c8e3aa6e79446a19cfb7a2ce`.


## Reviewer correction — supersedes initial R13 contract claim
The initial report's claim that literal one-axis and L1 admission phrases supplied a robust structural check is withdrawn. Those checks were removed: phrase matching could reject valid paraphrases and be defeated by inert appended text. The corrected audit checks only (1) the lane-specific report address is present, (2) subagent metadata models are exactly `openai-codex/gpt-6-luna` and `openai-codex/gpt-6-sol`, and (3) both metadata selectors occur in spec text. It does **not** test semantic or operative round-contract clauses.

Correction work commit: `ef2945b3b0717bd7134488d90aee1ca960af82d9`.

### Corrected evidence and verdict
- Donor remainder with the harness-integrity opening: exit 1 / 3/4 because the donor lacks its own lane-specific report address.
- Legitimate paraphrase of one-axis and L1 admission wording: exit 0 / 4/4.
- Wrong selector in content and wrong selector metadata: each exit 1 / 3/4.
- Existing copied-state controls, authorized promotion 4/4, synthetic fifth/digit mint 5/5, and live audit 4/4 retained.
- Corrected verdict: depth **improved narrowly** for tested dispatch-address and selector-presence drift; calibration **unchanged**. No semantic contract-fidelity, runtime model admission/routing, actual dispatch, or future-state claim. Substring presence can still be inert; this is not a generic semantic validator.
