# Round 8 — promotion round calibration

Claim: a promoted roster `promotion_round` must equal the lane’s `rounds[].promotions` entry’s numeric round. Previously a process-local copy changing harness-integrity’s roster value 4 → 3 exited 0, `verified triples: 4/4` despite its sole recorded promotion in round 4.

Run from project root: `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py` and `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py`. After change, copied mismatches for both actually promoted lanes exit 1, 3/4; absent, string, boolean, or zero roster rounds reject, as do malformed/missing promotion ledger rounds. Legitimate round-4 copy, live four triples and fifth synthetic mint remain positive. These are isolated copied-state mutations, not detected live drift or proof of semantic correctness. MANIFEST and global harness stay read-only.

Falsify if either copied wrong round passes, a valid promoted round-4 fixture fails, or a fifth unpromoted mint requires a roster row. The audit checks the recorded promotion only; it does not validate closure legitimacy or a coordinated forged ledger and roster.
