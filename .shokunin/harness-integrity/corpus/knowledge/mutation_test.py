"""Mutation control for the read-only live global-triple audit.

Run from the project root with:
  ~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py
"""
from contextlib import redirect_stdout
from copy import deepcopy
from io import StringIO
import json
from pathlib import Path
from runpy import run_path
from unittest.mock import patch

import rlm


def audit_with(state, manifest=None, books=None):
    output = StringIO()
    read_text = Path.read_text

    def read_fixture(path, *args, **kwargs):
        if manifest is not None and path.name == "MANIFEST.json" and path.parent.name == ".shokunin":
            return json.dumps(manifest)
        if books is not None and path.resolve() in books:
            return books[path.resolve()]
        return read_text(path, *args, **kwargs)

    with patch.object(rlm, "get_harness_state", return_value=state):
        with patch.object(Path, "read_text", read_fixture):
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

# A valid callable in the wrong province is not the cited executable
# procedure, even though importlib can resolve it.
wrong_callable = deepcopy(live)
wrong_callable.entries["skill"][missing_id].reference = {
    "type": "python", "import": "rlm", "callable": "find_models"}
wrong_code, wrong_output = audit_with(wrong_callable)
wrong_failure = "FAIL: harness-integrity: skill reference disagrees with cited procedure: rlm.find_models != rlm.get_harness_state"
assert (wrong_code == 1 and "verified triples: 3/4" in wrong_output
        and wrong_failure in wrong_output), (wrong_code, wrong_output)
print("wrong callable copy: exit 1; verified triples: 3/4; cited procedure mismatch")


# Model an authorized promotion in copies only: ledger, roster, and global spec
# must all agree. The on-disk MANIFEST and live global harness remain untouched.
manifest_path = Path(__file__).resolve().parents[4] / ".shokunin/MANIFEST.json"
manifest = json.loads(manifest_path.read_text())
lane = "harness-integrity"
# Start rank-transition fixtures from an explicitly unpromoted copy, even
# when the real roster has already promoted this lane.
base_manifest = deepcopy(manifest)
base_manifest["roster"].pop(lane, None)
for entry in base_manifest["rounds"]:
    entry["promotions"] = [p for p in entry.get("promotions", []) if p.get("id") != lane]
base_state = deepcopy(live)
base_state.entries["subagent"][f"primeagent-{lane}"].metadata["rank"] = "shonen"
promoted_manifest = deepcopy(base_manifest)
promoted_manifest["rounds"].append({
    "round": 4,
    "date": "2026-10-11",
    "type": "closure",
    "lanes": {lane: "ok"},
    "promotions": [{"id": lane, "from": "shonen", "to": "shokunin"}],
    "minted": [],
    "notes": "synthetic fixture only; not a live promotion",
})
promoted_manifest["roster"][lane] = deepcopy(manifest["roster"][lane])
promoted_manifest["roster"][lane]["promotion_round"] = 4
promoted_state = deepcopy(base_state)
promoted_state.entries["subagent"][f"primeagent-{lane}"].metadata["rank"] = "shokunin"

# Each rank-correct roster pointer must identify the lane's actual books and
# global subagent, not merely coexist with a valid promotion.
for field, wrong in (
    ("province", ".shokunin/rlm-dispatch/PROVINCE.md"),
    ("axes", ["coverage", "calibration"]),
    ("harness_spec", "global:primeagent-rlm-dispatch"),
):
    wrong_manifest = deepcopy(promoted_manifest)
    wrong_manifest["roster"][lane][field] = wrong
    wrong_code, wrong_output = audit_with(promoted_state, wrong_manifest)
    assert (wrong_code == 1 and "verified triples: 3/4" in wrong_output
            and f"FAIL: {lane}: roster {field} disagrees with books or global triple" in wrong_output), (field, wrong_code, wrong_output)
    print(f"wrong roster {field} copy: exit 1; pointer rejected")

promoted_code, promoted_output = audit_with(promoted_state, promoted_manifest)
assert promoted_code == 0 and "verified triples: 4/4" in promoted_output, promoted_output
print("authorized promoted copy (round 4): exit 0; verified triples: 4/4")

# Both recorded real promotion rows are valid; a copied round number or
# missing/malformed round is not evidence of when promotion happened.
for promoted_lane in ("harness-integrity", "rlm-dispatch"):
    recorded = next(entry["round"] for entry in manifest["rounds"]
                    if any(p.get("id") == promoted_lane for p in entry.get("promotions", [])))
    assert recorded == 4 and manifest["roster"][promoted_lane]["promotion_round"] == recorded
    copied = deepcopy(manifest)
    copied["roster"][promoted_lane]["promotion_round"] = 3
    code, output = audit_with(live, copied)
    assert (code == 1 and "verified triples: 3/4" in output
            and f"FAIL: {promoted_lane}: roster promotion_round disagrees with promotion ledger: 3" in output), output
    print(f"{promoted_lane} copied round 3: exit 1; verified triples: 3/4")

for value in (None, "4", True, 0):
    copied = deepcopy(promoted_manifest)
    if value is None:
        del copied["roster"][lane]["promotion_round"]
    else:
        copied["roster"][lane]["promotion_round"] = value
    code, output = audit_with(promoted_state, copied)
    assert code == 1 and "verified triples: 3/4" in output and "roster promotion_round disagrees" in output, output
    print(f"missing/malformed roster round {value!r}: exit 1; verified triples: 3/4")

for invalid_round in (None, "4", True, 0):
    copied = deepcopy(promoted_manifest)
    promoting_entry = copied["rounds"][-1]
    if invalid_round is None:
        del promoting_entry["round"]
    else:
        promoting_entry["round"] = invalid_round
    code, output = audit_with(promoted_state, copied)
    assert code == 1 and "invalid ledger promotion round" in output, output
    print(f"missing/malformed ledger round {invalid_round!r}: exit 1")

unapproved_manifest = deepcopy(base_manifest)
unapproved_manifest["roster"][lane] = {"rank": "shokunin"}
unapproved_code, unapproved_output = audit_with(promoted_state, unapproved_manifest)
assert (unapproved_code == 1 and "FAIL: harness-integrity: roster rank disagrees with promotion ledger:"
        in unapproved_output and "verified triples: 3/4" in unapproved_output), unapproved_output
print("unauthorized rank copy: exit 1; verified triples: 3/4; roster disagrees with ledger")

stale_state = deepcopy(base_state)
stale_code, stale_output = audit_with(stale_state, promoted_manifest)
assert (stale_code == 1 and "verified triples: 3/4" in stale_output
        and "FAIL: harness-integrity: metadata, scope, rank, or content drifts from books" in stale_output), stale_output
print("stale harness rank copy: exit 1; verified triples: 3/4")

missing_roster = deepcopy(promoted_manifest)
del missing_roster["roster"][lane]
no_row_code, no_row_output = audit_with(promoted_state, missing_roster)
assert no_row_code == 1 and "FAIL: harness-integrity: promotion missing roster row" in no_row_output, no_row_output
print("missing promoted roster copy: exit 1; promotion missing roster row")

# A later type=mint entry must work without expanding a hardcoded roster. The
# fifth lane's books and global triple exist only in these process-local copies.
new_lane = "new-specialist"
source_lane = "gate-evidence"
expanded_manifest = deepcopy(manifest)
expanded_manifest["rounds"].append({
    "round": 0, "type": "mint", "minted": [new_lane], "promotions": [],
    "notes": "synthetic fixture; no live mint", })
expanded_state = deepcopy(live)
for kind, suffix in (("subagent", ""), ("memory", "-knowledge"), ("skill", "-procedure")):
    source_id = f"primeagent-{source_lane}{suffix}"
    fixture_id = f"primeagent-{new_lane}{suffix}"
    expanded_state.entries[kind][fixture_id] = deepcopy(expanded_state.entries[kind][source_id])
    expanded_state.entries[kind][fixture_id].id = fixture_id
    entry = expanded_state.entries[kind][fixture_id]
    entry.title = entry.title.replace(source_lane, new_lane)
    entry.content = entry.content.replace(source_lane, new_lane)
expanded_state.entries["subagent"][f"primeagent-{new_lane}"].metadata["rank"] = "shonen"
expanded_state.entries["skill"][f"primeagent-{new_lane}-procedure"].arguments.update({
    "province": new_lane, "scope": f".shokunin/{new_lane}"})
books = {
    (manifest_path.parent / new_lane / "PROVINCE.md").resolve():
        (manifest_path.parent / source_lane / "PROVINCE.md").read_text(),
    (manifest_path.parent / new_lane / "SCORECARD.md").resolve():
        (manifest_path.parent / source_lane / "SCORECARD.md").read_text(),
}
checklist_path = Path(__file__).with_name("global-triples.md").resolve()
books[checklist_path] = (checklist_path.read_text()
    + f"\n- [verified] `{new_lane}` — synthetic copied procedure; Python `goal.get`; fixture only.\n")
expanded_code, expanded_output = audit_with(expanded_state, expanded_manifest, books)
assert expanded_code == 0 and "verified triples: 5/5" in expanded_output and "FAIL:" not in expanded_output, expanded_output
print("fifth minted lane copy: exit 0; verified triples: 5/5")

duplicated_manifest = deepcopy(expanded_manifest)
duplicated_manifest["rounds"].append({"round": 0, "type": "mint", "minted": [new_lane]})
duplicate_code, duplicate_output = audit_with(expanded_state, duplicated_manifest, books)
assert duplicate_code == 1 and "FAIL: mint ledger requires distinct lane IDs" in duplicate_output, duplicate_output
print("duplicate mint ID copy: exit 1; duplicate rejected")

unmatched_books = deepcopy(books)
unmatched_books[checklist_path] = checklist_path.read_text()
unmatched_code, unmatched_output = audit_with(expanded_state, expanded_manifest, unmatched_books)
assert unmatched_code == 1 and "FAIL: checklist lanes" in unmatched_output, unmatched_output
print("unmatched checklist copy: exit 1; missing fifth citation rejected")

# Runtime accepts any nonempty ID string and the workflow gives no narrower
# grammar. This fixture exercises underscore specifically; it is synthetic,
# and does not establish that every such ID works across all filesystem uses.
digit_lane = "specialist_2"
digit_manifest = deepcopy(manifest)
digit_manifest["rounds"].append({
    "round": 0, "type": "mint", "minted": [digit_lane], "promotions": [],
    "notes": "synthetic fixture; no live mint", })
digit_state = deepcopy(live)
for kind, suffix in (("subagent", ""), ("memory", "-knowledge"), ("skill", "-procedure")):
    source_id = f"primeagent-{source_lane}{suffix}"
    fixture_id = f"primeagent-{digit_lane}{suffix}"
    digit_state.entries[kind][fixture_id] = deepcopy(digit_state.entries[kind][source_id])
    digit_state.entries[kind][fixture_id].id = fixture_id
    entry = digit_state.entries[kind][fixture_id]
    entry.title = entry.title.replace(source_lane, digit_lane)
    entry.content = entry.content.replace(source_lane, digit_lane)
digit_state.entries["subagent"][f"primeagent-{digit_lane}"].metadata["rank"] = "shonen"
digit_state.entries["skill"][f"primeagent-{digit_lane}-procedure"].arguments.update({
    "province": digit_lane, "scope": f".shokunin/{digit_lane}"})
digit_books = {
    (manifest_path.parent / digit_lane / "PROVINCE.md").resolve():
        (manifest_path.parent / source_lane / "PROVINCE.md").read_text(),
    (manifest_path.parent / digit_lane / "SCORECARD.md").resolve():
        (manifest_path.parent / source_lane / "SCORECARD.md").read_text(),
    checklist_path: (checklist_path.read_text()
        + f"\n- [verified] `{digit_lane}` — synthetic copied procedure; Python `goal.get`; fixture only.\n"),
}
digit_code, digit_output = audit_with(digit_state, digit_manifest, digit_books)
assert digit_code == 0 and "verified triples: 5/5" in digit_output and "FAIL:" not in digit_output, digit_output
print("digit-bearing fifth mint: exit 0; verified triples: 5/5; digit ID accepted")

# Dictionary-key lookup alone is insufficient: each payload must identify
# itself with the same expected ID. Mutate only the copied payload ID.
for kind, suffix in (("subagent", ""), ("memory", "-knowledge"), ("skill", "-procedure")):
    copied = deepcopy(live)
    expected_id = f"primeagent-{lane}{suffix}"
    entry = copied.entries[kind][expected_id]
    entry.id = "payload-id-mismatch"
    assert expected_id in copied.entries[kind], "fixture must retain dictionary key"
    code, output = audit_with(copied)
    failure = f"FAIL: {lane}: {kind} payload id 'payload-id-mismatch' disagrees with expected key '{expected_id}'"
    assert code == 1 and "verified triples: 3/4" in output and failure in output, output
    print(f"{kind} payload ID mismatch copy: exit 1; key retained; verified triples: 3/4")

# The cited global triple must remain this lane's own executable identity,
# not a valid different lane copied under the same IDs and metadata.
for kind, suffix in (("subagent", ""), ("memory", "-knowledge"), ("skill", "-procedure")):
    for field in ("title", "content"):
        copied = deepcopy(live)
        entry = copied.entries[kind][f"primeagent-{lane}{suffix}"]
        donor = live.entries[kind][f"primeagent-rlm-dispatch{suffix}"]
        setattr(entry, field, getattr(donor, field))
        code, output = audit_with(copied)
        failure = f"FAIL: {lane}: {kind} title or content opening disagrees with books or cited procedure"
        assert code == 1 and "verified triples: 3/4" in output and failure in output, output
        print(f"copied {kind} {field}: exit 1; verified triples: 3/4")

# A donor body under the retained harness-integrity opening lacks its scoped
# report address and is rejected. This is structural, not semantic validation.
original = live.entries["subagent"][f"primeagent-{lane}"].content
donor_body = live.entries["subagent"]["primeagent-rlm-dispatch"].content.split(" Read ", 1)[1]
copy = deepcopy(live)
copy.entries["subagent"][f"primeagent-{lane}"].content = original.split(" Read ", 1)[0] + " Read " + donor_body
code, output = audit_with(copy)
assert (code == 1 and "verified triples: 3/4" in output
        and f"FAIL: {lane}: subagent spec missing lane report path" in output), output
print("donor remainder with intact identity opening: exit 1; report path rejected")

# Round/admission wording may be legitimately paraphrased. These phrases are
# not part of the structural contract and must not be required literally.
paraphrased = deepcopy(live)
paraphrased_spec = paraphrased.entries["subagent"][f"primeagent-{lane}"]
paraphrased_spec.content = (paraphrased_spec.content
    .replace("exactly one falsifiable axis move", "one measurable axis change")
    .replace("Only L1 admits.", "L1 alone decides admission."))
code, output = audit_with(paraphrased)
assert code == 0 and "verified triples: 4/4" in output, output
print("legitimate contract paraphrase: exit 0; verified triples: 4/4")

# Model names in metadata must be the allowed pair and both must occur in the
# spec. A wrong selector cannot be rescued by editing metadata to match it.
for mode in ("content", "metadata"):
    copied = deepcopy(live)
    entry = copied.entries["subagent"][f"primeagent-{lane}"]
    if mode == "content":
        entry.content = entry.content.replace("openai-codex/gpt-6-luna", "openai-codex/wrong")
    else:
        entry.metadata["models"] = ["openai-codex/wrong", "openai-codex/gpt-6-sol"]
    code, output = audit_with(copied)
    assert code == 1 and "verified triples: 3/4" in output and "subagent" in output, output
    print(f"wrong selector {mode}: exit 1; rejected")

assert json.loads(manifest_path.read_text()) == manifest, "live manifest changed during fixture"
fresh = rlm.get_harness_state(global_=True)
assert fresh.entries["subagent"][f"primeagent-{lane}"].metadata["rank"] == live.entries["subagent"][f"primeagent-{lane}"].metadata["rank"], "live harness rank changed"
assert missing_id in fresh.entries["skill"], "live state changed during fixture"
fresh_code, fresh_output = audit_with(fresh)
assert fresh_code == 0 and "verified triples: 4/4" in fresh_output, fresh_output
print("fresh live snapshot: exit 0; verified triples: 4/4")
