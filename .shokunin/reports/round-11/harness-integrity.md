# Round 11 — harness-integrity

## Change and evidence
Canonical mint schema names `minted: [id...]` (docs/shokunin-workflow.md:62; skills/shokunin/SKILL.md:127) and repeatedly treats IDs as `<id>` (workflow lines 71–92); it states no letters-only restriction. The checklist parser previously used `[a-z-]+`, narrower than this canonical placeholder.

Before the fix, a process-local copied fifth lane `specialist-2` with copied triple/books and matching checklist row falsely failed: `verified triples: 4/5`, `FAIL: checklist lanes`. The mutation test now preserves the ordinary fifth-lane positive and adds that synthetic digit-bearing fifth-mint fixture. `audit.py` accepts it at 5/5 after the parser permits lowercase initial plus lowercase letters, digits, and hyphens. This is a synthetic-only compatibility result, not a real mint or observed live failure.

Work commit: `5a55d01f8b6f9c8f2245fb7cc464febb0358e0bc`.

## Validation
- Native `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: exit 0; existing positives (intact/promoted 4/4, ordinary synthetic fifth 5/5, fresh live 4/4), digit-bearing synthetic 5/5, and existing missing-ID/import, wrong-callable, rank/roster/round, duplicate mint, unmatched checklist, and six copied identity negatives retained.
- Native `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py`: exit 0, live 4/4.
- `git diff --check`: exit 0. No global harness, MANIFEST, source, or push changes.

## Owned-axis verdict
Depth **unchanged**: no deeper audit coverage claim. Calibration **improved** narrowly: a previously false-rejecting synthetic ID consistent with the unconstrained canonical schema is now accepted, while controls remain. No real deployment impact is claimed. Synthetic-only limit applies.
