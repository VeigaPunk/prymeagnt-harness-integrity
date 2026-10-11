"""Mutation control for the read-only live global-triple audit.

Run from the project root with:
  ~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py
"""
from contextlib import redirect_stdout
from copy import deepcopy
from io import StringIO
from pathlib import Path
from runpy import run_path
from unittest.mock import patch

import rlm


def audit_with(state):
    output = StringIO()
    with patch.object(rlm, "get_harness_state", return_value=state):
        with redirect_stdout(output):
            try:
                run_path(str(Path(__file__).with_name("audit.py")), run_name="__main__")
            except SystemExit as exc:
                exit_code = exc.code
            else:
                exit_code = 0
    return exit_code, output.getvalue()


live = rlm.get_harness_state(global_=True)
intact = deepcopy(live)
corrupted = deepcopy(live)
missing_id = "primeagent-harness-integrity-procedure"
assert missing_id in corrupted.entries["skill"], "fixture key missing from live state"
del corrupted.entries["skill"][missing_id]

control_code, control_output = audit_with(intact)
assert control_code == 0 and "verified triples: 4/4" in control_output, control_output
print("intact copy: exit 0; verified triples: 4/4")

mutant_code, mutant_output = audit_with(corrupted)
expected = f"FAIL: harness-integrity: missing skill:{missing_id}"
assert mutant_code == 1 and "verified triples: 3/4" in mutant_output and expected in mutant_output, mutant_output
print(f"missing skill copy: exit 1; verified triples: 3/4; {expected}")

invalid_ref = deepcopy(live)
invalid_ref.entries["skill"][missing_id].reference["import"] = "shokunin_missing_reference_probe"
ref_code, ref_output = audit_with(invalid_ref)
ref_failure = "FAIL: harness-integrity: skill reference invalid: No module named 'shokunin_missing_reference_probe'"
assert ref_code == 1 and "verified triples: 3/4" in ref_output and ref_failure in ref_output, ref_output
print(f"invalid import copy: exit 1; verified triples: 3/4; {ref_failure}")

fresh = rlm.get_harness_state(global_=True)
assert missing_id in fresh.entries["skill"], "live state changed during fixture"
fresh_code, fresh_output = audit_with(fresh)
assert fresh_code == 0 and "verified triples: 4/4" in fresh_output, fresh_output
print("fresh live snapshot: exit 0; verified triples: 4/4")
