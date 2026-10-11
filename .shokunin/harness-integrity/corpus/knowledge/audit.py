"""Read-only, live audit of the four minted global harness triples.

Run from the project root with the prime-agent kernel venv:
  ~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py
"""
import importlib
import json
import re
from pathlib import Path

import rlm

root = Path(__file__).resolve().parents[4]
manifest = json.loads((root / ".shokunin/MANIFEST.json").read_text())
state = rlm.get_harness_state(global_=True)
checklist = (Path(__file__).parent / "global-triples.md").read_text()
claimed = re.findall(r"^- \[verified\] `([a-z-]+)` ", checklist, re.MULTILINE)
lanes = manifest["rounds"][0]["minted"]
errors = []
verified = []
if len(lanes) != 4 or len(set(lanes)) != 4:
    errors.append(f"mint roster expected four distinct lanes, got {lanes!r}")
if sorted(claimed) != sorted(lanes):
    errors.append(f"checklist lanes {claimed!r} differ from manifest mint {lanes!r}")

# A minted lane is shonen until the ledger records its promotion. A roster row
# must agree with that ledger; neither a row nor an executable spec alone can
# authorize a rank transition.
expected_ranks = {lane: "shonen" for lane in lanes}
for round_entry in manifest["rounds"]:
    for promotion in round_entry.get("promotions", []):
        lane = promotion.get("id")
        if (lane not in expected_ranks
                or promotion.get("from") != "shonen"
                or promotion.get("to") != "shokunin"
                or expected_ranks.get(lane) != "shonen"):
            errors.append(f"invalid rank promotion: {promotion!r}")
        else:
            expected_ranks[lane] = "shokunin"
for lane, row in manifest["roster"].items():
    if lane not in expected_ranks:
        errors.append(f"unminted roster lane: {lane}")
    elif not isinstance(row, dict) or row.get("rank") != expected_ranks[lane] or expected_ranks[lane] == "shonen":
        errors.append(f"{lane}: roster rank disagrees with promotion ledger: {row!r}")
for lane, rank in expected_ranks.items():
    if rank == "shokunin" and lane not in manifest["roster"]:
        errors.append(f"{lane}: promotion missing roster row")

for lane in lanes:
    prefix = f"primeagent-{lane}"
    ids = {"subagent": prefix, "memory": prefix + "-knowledge", "skill": prefix + "-procedure"}
    missing = [f"{kind}:{entry_id}" for kind, entry_id in ids.items()
               if entry_id not in state.entries[kind]]
    if missing:
        errors.append(f"{lane}: missing {', '.join(missing)}")
        continue
    spec = state.entries["subagent"][ids["subagent"]]
    memory = state.entries["memory"][ids["memory"]]
    skill = state.entries["skill"][ids["skill"]]
    province = (root / ".shokunin" / lane / "PROVINCE.md").read_text()
    scorecard = (root / ".shokunin" / lane / "SCORECARD.md").read_text()
    owned = re.search(r"^Owns: (.+)$", province, re.MULTILINE)
    axes = re.search(r"^Owned axes: ([^.]+)\.", scorecard, re.MULTILINE)
    if not owned or not axes:
        errors.append(f"{lane}: missing province or axes declaration")
        continue
    expected_axes = [part.strip() for part in axes.group(1).split(",")]
    ref = skill.reference
    target = ref.get("import") or ref.get("python_import")
    function = ref.get("callable")
    try:
        if ref.get("type") != "python" or not isinstance(target, str) or not isinstance(function, str):
            raise ValueError("expected Python import and callable reference")
        if not callable(getattr(importlib.import_module(target), function)):
            raise ValueError("reference resolves but is not callable")
    except (ImportError, AttributeError, ValueError, TypeError) as exc:
        errors.append(f"{lane}: skill reference invalid: {exc}")
        continue
    if (spec.metadata.get("province") != owned.group(1).removesuffix(".")
            or spec.metadata.get("axes") != expected_axes
            or spec.metadata.get("rank") != expected_ranks[lane]
            or skill.arguments.get("province") != lane
            or skill.arguments.get("axes") != expected_axes
            or skill.arguments.get("scope") != f".shokunin/{lane}"
            or not all(entry.scope == "global" and entry.content for entry in (spec, memory, skill))):
        errors.append(f"{lane}: metadata, scope, rank, or content drifts from books")
        continue
    verified.append(lane)

print(f"verified triples: {len(verified)}/{len(lanes)}; lanes: {', '.join(verified)}")
print(f"global harness: {state.file_path}")
for error in errors:
    print(f"FAIL: {error}")
if errors:
    raise SystemExit(1)
