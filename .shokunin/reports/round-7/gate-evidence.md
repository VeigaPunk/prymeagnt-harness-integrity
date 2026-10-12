# Gate-evidence — round 7

## Bounded calibration move

**Falsifiable claim:** At baseline `da99ff203b9c69707d2ae86eb956cee2ae7415ae`, the pinned parent-projection comparator existed but no R7 report recorded an actual parent-supplied projection comparison. After this round, the report records a parent-supplied redacted projection and the result of the comparator against the pinned benign Git whitespace gate. This tests only the comparator contract and this local Git gate; it is not authenticated autonomous telemetry.

**Inputs and evidence:** L1 supplied the allowlisted projection observed at `2026-10-12T01:09:54.569634+00:00`: goal status `active`, `tokens_used=6636364`, `time_used_seconds=10517`, `token_budget=null`. The comparator was run as:

`python3 .shokunin/gate-evidence/corpus/live/compare_parent_receipt.py --base 52d573bdf502cb1416d65c0756106db9d5b3bde2 --candidate bc1bb3c572981158f8ac0b4994d3333741650886 < /tmp/projection2.json`

It exited 0; the receipt reports `git diff --check` exit 0 (`pass`), and labels provenance as parent-supplied and not program-verified. The comparator explicitly leaves `autonomous_gate`, `acceptance`, `loop_stop`, and `mission_goal` `not-assessed`; no goal completion call was made. Earlier supplied projection at `01:09:10.860478Z` was also compared to the same pins and yielded exit 0. These are two separate observations, not a causal or trend inference.

**Validation:** `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` passed: synthetic projection and null parsing, objective/secret and non-UTC rejection, actual pinned Git pass, and stdin whitespace negative control. `git diff --check` passed for the working tree before documentation edits. The test is a contract test, not verification of parent status or autonomous gate correctness.

**Owned-axis verdicts:** **Calibration improved narrowly** from no R7 actual parent-supplied comparison recorded to one recorded redacted projection plus a reproducible pinned benign Git gate result. **Coverage unchanged:** no policy branch or classification added. No score assigned. No host acceptance, autonomous telemetry, mission-goal success, or stop claim. SHONEN end-to-end box remains unchecked; no promotion.

**Limits:** Projection is supplied by L1 and is not authenticated by this comparator. The Git check is not the configured host autonomous gate and does not establish tests, acceptance, goal completion, or loop-stop state. The deadline and goal objective are intentionally excluded from the projection/report.
