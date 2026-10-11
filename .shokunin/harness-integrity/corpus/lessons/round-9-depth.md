# Round 9 — depth: triple identity drift

Before: copied `harness-integrity` subagent `title` and `content` from the real `rlm-dispatch` subagent while retaining harness-integrity's ID, correct metadata, and other triple fields. The prior audit exited 0 and verified 4/4, though its claimed executable lane instructions had become another lane's. This is a copied-state false accept, **not observed live global drift**. The same problem applies to separately copied memory and skill titles/content.

After: compare each triple's title and opening identity claim to its own independently read province/axes/ledger rank and cited procedure. Six isolated mutations (three kinds × title/content) each exit 1 and verify 3/4. The live snapshot remains 4/4 and the synthetic distinct fifth mint 5/5 after assigning the copied fixture its own identity; prior rank, roster, and reference negatives remain rejects. Run from the project root:

```sh
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/mutation_test.py
~/.prime/agent/kernel-venv/bin/python .shokunin/harness-integrity/corpus/knowledge/audit.py
```

This guards opening identity drift, not full semantic accuracy, source citation validity, or colluding edits to books and global text. No global harness or MANIFEST mutation.
