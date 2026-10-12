#!/usr/bin/env bash
# Read-only guard for deciding whether a daemon isolation probe is safe.
# This validates path separation only; it does not launch a daemon or session.
set -euo pipefail
if [ "$#" -ne 4 ]; then
  echo "usage: $0 PRIVATE_AGENT_DIR PRIVATE_DAEMON_SOCKET LIVE_AGENT_DIR LIVE_DAEMON_SOCKET" >&2
  exit 2
fi
private_store="$(realpath -m -- "$1")"
private_socket="$(realpath -m -- "$2")"
live_store="$(realpath -m -- "$3")"
live_socket="$(realpath -m -- "$4")"

while IFS= read -r entry; do
  case "$entry" in
    PRIME_AGENT_INTERNAL_*=*) echo "REFUSE inherited internal daemon state: ${entry%%=*}" >&2; exit 1 ;;
  esac
done < <(env)

# Root cannot be an isolated store: it contains every other path, and the
# trailing-slash overlap checks below do not model that special case.
[ "$private_store" != / ] && [ "$live_store" != / ] || { echo "REFUSE filesystem root as agent store" >&2; exit 1; }
# Store roots may not equal or contain one another. Socket must be distinct
# from the live socket and must not live inside either store root.
case "$private_store/" in "$live_store/"|"$live_store"/*/) echo "REFUSE overlapping private/live store paths" >&2; exit 1;; esac
case "$live_store/" in "$private_store/"|"$private_store"/*/) echo "REFUSE overlapping private/live store paths" >&2; exit 1;; esac
[ "$private_socket" != "$live_socket" ] || { echo "REFUSE private socket equals live socket" >&2; exit 1; }
case "$private_socket" in "$private_store"/*|"$live_store"/*) echo "REFUSE daemon socket inside an agent store" >&2; exit 1;; esac
case "$private_store" in "$private_socket"/*) echo "REFUSE private store contains daemon socket path" >&2; exit 1;; esac
printf 'PATH_PREFLIGHT_PASS private_store=%s private_socket=%s live_store=%s live_socket=%s\n' "$private_store" "$private_socket" "$live_store" "$live_socket"
printf 'daemon_started=NO session_started=NO\n'
