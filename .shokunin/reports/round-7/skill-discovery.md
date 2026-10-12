# Skill discovery R7 — preflight false-pass correction

Date: 2026-10-11
Branch: `craft/skill-discovery-r7`
Agent identity: `skill-discovery-shonen <skill-discovery@shokunin.local>` (author and committer)

## Axis and evidence

**Operability** was the sole axis move; freshness was judged as well. Auditing `.shokunin/skill-discovery/corpus/probes/daemon-isolation-preflight.sh` found a concrete false pass in its fake-path guard. Before the change, an isolated invocation with private store `/`, a distinct private socket under a temporary directory, and an ordinary live store/socket passed and printed `PATH_PREFLIGHT_PASS`. Since `/` contains all filesystem locations, it cannot be an isolated store; the previous textual descendant checks failed to treat the root path as the universal container.

Added a minimal explicit refusal for `/` as either private or live store. Before/after test receipts:

```text
BEFORE: env -i PATH="$PATH" bash "$P" / "$T/private.sock" "$T/live-store" "$T/live.sock"
        PATH_PREFLIGHT_PASS ...; exit 0
AFTER:  same arguments
        REFUSE filesystem root as agent store; exit 1
```

Control fixture with distinct ordinary fake stores/sockets still passed (`exit 0`); A private socket nested under its private store refused (`exit 1`). Inherited `PRIME_AGENT_INTERNAL_PROBE=1` still refused (`exit 1`). Symlinked store alias to live store was canonicalized by `realpath -m` and refused (`exit 1`). All checks used only temporary fake paths and `env -i`; no daemon, session, or reload started.

Probe change: `.shokunin/skill-discovery/corpus/probes/daemon-isolation-preflight.sh`. R4 private install and R5 fresh-process inventory probes were not changed. No MANIFEST/global/source/push or shared installation changes.

## Axis verdict proposal

- **Operability: improved.** A previously demonstrated false-positive acceptance is now refused. This improves guard reliability only; it does not establish daemon isolation or authorize launch.
- **Freshness: unchanged.** No daemon-backed task, session, or reload was performed. SHONEN end-to-end box 2 remains unchecked.

## Limits

The probe remains only a conservative path/environment preflight and does not establish that the CLI uses the supplied paths or that all daemon state is private. Continue not to launch without an independently verified isolated daemon route. Existing R4/R5 evidence remains bounded to private installation plus fresh-process discovery, not daemon reload.
