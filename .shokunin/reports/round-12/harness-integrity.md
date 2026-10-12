# Round 12 — harness-integrity

## Premise and evidence

The live runtime implementation validates explicit harness entry IDs only as nonempty strings (`rlm/harness.py`, `_require_text`); the workflow documents `<id>` and uses it in `minted`, paths, and identity templates but specifies no character grammar (`docs/shokunin-workflow.md:62, 85-92`; `skills/shokunin/SKILL.md:127`). This supports testing an underscore ID, not claiming that every nonempty string works across every downstream path or tool.

At baseline commit `314935a`, the checklist citation regex allowed lowercase letters, digits, and hyphens but not underscores. Applying that baseline regex to a synthetic `specialist_2` citation yields no match; the corrected regex captures it. In the isolated copied fifth-mint fixture, adding `specialist_2` with copied books/triple and matching citation changes the audit result to exit 0, `verified triples: 5/5`. This is a synthetic false-reject reproduction, not a real mint or observed live failure.

## Work and validation

Work commit: `1da56c9f87f2e4ad093faf5d0d2d782bb377109d`.

- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py`: exit 0. Existing intact/promoted positives, ordinary fifth mint, mutation negatives, duplicate/checklist controls, identity controls, and fresh live 4/4 retained; underscore fixture 5/5.
- `~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py`: exit 0; live `verified triples: 4/4`.
- `git diff --check`: exit 0.

The parser now permits `_` alongside its previously allowed lowercase letters, digits, and hyphens. No global harness, manifest, source, or other lane changed; no push.

## Owned-axis verdict

Calibration **improved** narrowly: the copied underscore-ID citation that the baseline parser rejects is now accepted, with prior controls retained. Depth **unchanged**: no broader coverage claim. Scope is the tested underscore case and current live snapshot only; no claim of unrestricted ID grammar or real-world impact.
