"""Read-only, live audit of all ledger-minted global harness triples.

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
cited_references = re.findall(
    r"^- \[verified\] `([a-z][a-z0-9_-]*)` .*?; Python `([a-zA-Z_][\w.]*)`;",
    checklist, re.MULTILINE)
claimed = [lane for lane, _ in cited_references]
minted = [lane for entry in manifest["rounds"] if entry.get("type") == "mint"
          for lane in entry.get("minted", [])]
lanes = list(dict.fromkeys(minted))
errors = []
verified = []
if not lanes or len(minted) != len(lanes):
    errors.append(f"mint ledger requires distinct lane IDs, got {minted!r}")
if len(claimed) != len(set(claimed)) or sorted(claimed) != sorted(lanes):
    errors.append(f"checklist lanes {claimed!r} differ from manifest mints {lanes!r}")

# A minted lane is shonen until the ledger records its promotion. A roster row
# must agree with that ledger; neither a row nor an executable spec alone can
# authorize a rank transition.
expected_ranks = {lane: "shonen" for lane in lanes}
promotion_rounds = {}
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
            promotion_round = round_entry.get("round")
            if type(promotion_round) is not int or promotion_round < 1:
                errors.append(f"{lane}: invalid ledger promotion round: {promotion_round!r}")
            else:
                promotion_rounds[lane] = promotion_round
for lane, row in manifest["roster"].items():
    if lane not in expected_ranks:
        errors.append(f"unminted roster lane: {lane}")
    elif not isinstance(row, dict) or row.get("rank") != expected_ranks[lane] or expected_ranks[lane] == "shonen":
        errors.append(f"{lane}: roster rank disagrees with promotion ledger: {row!r}")
    elif type(row.get("promotion_round")) is not int or row["promotion_round"] != promotion_rounds.get(lane):
        errors.append(f"{lane}: roster promotion_round disagrees with promotion ledger: {row.get('promotion_round')!r}")
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
    try:
        province = (root / ".shokunin" / lane / "PROVINCE.md").read_text()
        scorecard = (root / ".shokunin" / lane / "SCORECARD.md").read_text()
    except FileNotFoundError:
        errors.append(f"{lane}: missing province or scorecard book")
        continue
    owned = re.search(r"^Owns: (.+)$", province, re.MULTILINE)
    axes = re.search(r"^Owned axes: ([^.]+)\.", scorecard, re.MULTILINE)
    if not owned or not axes:
        errors.append(f"{lane}: missing province or axes declaration")
        continue
    expected_axes = [part.strip() for part in axes.group(1).split(",")]
    row = manifest["roster"].get(lane)
    roster_drift = (isinstance(row, dict) and expected_ranks[lane] == "shokunin"
                    and (type(row.get("promotion_round")) is not int
                         or row["promotion_round"] != promotion_rounds.get(lane)))
    if isinstance(row, dict):
        pointers = {
            "province": f".shokunin/{lane}/PROVINCE.md",
            "axes": expected_axes,
            "harness_spec": f"global:{ids['subagent']}",
        }
        for field, expected in pointers.items():
            if row.get(field) != expected:
                errors.append(f"{lane}: roster {field} disagrees with books or global triple")
                roster_drift = True
    ref = skill.reference
    target = ref.get("import") or ref.get("python_import")
    function = ref.get("callable")
    cited = dict(cited_references).get(lane)
    try:
        if ref.get("type") != "python" or not isinstance(target, str) or not isinstance(function, str):
            raise ValueError("expected Python import and callable reference")
        if not callable(getattr(importlib.import_module(target), function)):
            raise ValueError("reference resolves but is not callable")
    except (ImportError, AttributeError, ValueError, TypeError) as exc:
        errors.append(f"{lane}: skill reference invalid: {exc}")
        continue
    actual = f"{target}.{function}"
    if actual != cited:
        errors.append(f"{lane}: skill reference disagrees with cited procedure: {actual} != {cited}")
        continue
    domain = owned.group(1).removesuffix(".")
    rank_word = "promoted" if expected_ranks[lane] == "shokunin" else "probationary"
    identity = {
        "subagent": (spec, f"{lane} — prime-agent specialist ({expected_ranks[lane]})",
                     f"You are {lane}, a {rank_word} prime-agent shokunin. Province: {domain}. Owned axes: {', '.join(expected_axes)}."),
        "memory": (memory, f"{lane} cited domain facts", f"Prime-agent specialization: {domain}."),
        "skill": (skill, f"{lane} craft procedure",
                  f"Executable REPL craft procedure for {lane} (reference resolves to `{cited}`;"),
    }
    identity_drift = False
    for kind, (entry, title, opening) in identity.items():
        if entry.title != title or not entry.content.startswith(opening):
            errors.append(f"{lane}: {kind} title or content opening disagrees with books or cited procedure")
            identity_drift = True
    if identity_drift:
        continue
    required_spec_fragments = {
        "lane report path": f".shokunin/reports/round-<N>/{lane}.md",
    }
    for label, fragment in required_spec_fragments.items():
        if fragment not in spec.content:
            errors.append(f"{lane}: subagent spec missing {label}")
            identity_drift = True
    allowed_models = {"openai-codex/gpt-6-luna", "openai-codex/gpt-6-sol"}
    models = spec.metadata.get("models")
    if not isinstance(models, list) or len(models) != 2 or set(models) != allowed_models:
        errors.append(f"{lane}: subagent model metadata is not the allowed OpenAI selector pair")
        identity_drift = True
    elif not all(model in spec.content for model in models):
        errors.append(f"{lane}: subagent content omits a metadata model selector")
        identity_drift = True
    if identity_drift:
        continue
    if (spec.metadata.get("province") != domain
            or spec.metadata.get("axes") != expected_axes
            or spec.metadata.get("rank") != expected_ranks[lane]
            or skill.arguments.get("province") != lane
            or skill.arguments.get("axes") != expected_axes
            or skill.arguments.get("scope") != f".shokunin/{lane}"
            or not all(entry.scope == "global" and entry.content for entry in (spec, memory, skill))):
        errors.append(f"{lane}: metadata, scope, rank, or content drifts from books")
        continue
    if roster_drift:
        continue
    verified.append(lane)

print(f"verified triples: {len(verified)}/{len(lanes)}; lanes: {', '.join(verified)}")
print(f"global harness: {state.file_path}")
for error in errors:
    print(f"FAIL: {error}")
if errors:
    raise SystemExit(1)
