#!/usr/bin/env bash
# Answers one question: what has moved upstream since library/ was cut?
# Run as `bash .maintainers/canon-check.sh`, on a machine that has the source repositories
# checked out. Not an apprentice-facing tool - see .maintainers/README.md.
#   GONE   the upstream file was renamed, moved or deleted
#   MOVED  the upstream file was edited; this copy is behind
#   LOCAL  this copy was edited here, which library/ says must not happen
#   WEB    the source is a URL, not a file on this machine, so staleness cannot be decided here
set -uo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CANON="$ROOT/.maintainers/CANON.md"
[[ -s "$CANON" ]] || { echo "FATAL: no .maintainers/CANON.md at $ROOT"; exit 2; }
h(){ shasum -a 256 "$1" 2>/dev/null | cut -c1-64; }
gone=0; moved=0; local_=0; ok=0; unresolved=0; web=0
while IFS= read -r line; do
  [[ -z "$line" ]] && continue
  comp=$(cut -f1 <<<"$line"); repo=$(cut -f2 <<<"$line"); src=$(cut -f3 <<<"$line")
  shipped=$(cut -f5 <<<"$line"); at_src=$(cut -f7 <<<"$line")
  if [[ "$(h "$ROOT/$comp")" != "$shipped" ]]; then
    echo "LOCAL    $comp   edited here since the cut"; local_=$((local_+1))
  fi
  if [[ "$repo" == "authored" ]]; then
    [[ "$(h "$ROOT/$comp")" == "$shipped" ]] && ok=$((ok+1))
    continue
  fi
  # A web source has no path to stat. Without this it reports GONE on every run, and a gate that
  # is always red for a known reason is a gate nobody reads.
  if [[ "$src" == http://* || "$src" == https://* ]]; then
    echo "WEB      $comp   <- $src"; web=$((web+1)); continue
  fi
  src="${src/#\~\//$HOME/}"
  if [[ ! -e "$src" ]]; then
    echo "GONE     $comp   <- $src"; gone=$((gone+1)); continue
  fi
  now="$(h "$src")"
  if [[ "$now" != "$at_src" ]]; then
    echo "MOVED    $comp   <- $src"; moved=$((moved+1))
  else ok=$((ok+1)); fi
done < <(awk '/^```tsv/{f=1;next} /^```/{if(f)exit} f' "$CANON")
echo
echo "in sync: $ok   moved upstream: $moved   gone upstream: $gone   edited locally: $local_   web sources: $web"
[[ $((moved+gone+local_)) -eq 0 ]] && echo "nothing has moved since the cut" || echo "the rows above are decisions, not errors"
exit 0
