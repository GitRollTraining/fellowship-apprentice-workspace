#!/usr/bin/env bash
# symcheck.sh — broken-symlink sweep after any structural mutation.
#
# Usage: symcheck.sh <tree-root>
# Output: one broken symlink per line (path relative to tree-root). Empty output + exit 0 = clean.
# Exit: 0 = no broken symlinks, 1 = at least one broken, 2 = usage error.
#
# Run over the WHOLE tree after ANY move — not just the moved subtree. Relative symlinks break
# when an ANCESTOR directory of either endpoint changes depth: the link's text never changes,
# so text-grep discovery cannot see this failure class. Only resolution testing catches it.
# find errors (unreadable dirs) pass through to stderr — ANY stderr means the sweep may be
# incomplete; resolve before trusting a clean result.
#
# EXIT CODE IS NOT THE GATE.  On any KB carrying pre-existing broken symlinks this returns 1 on
# EVERY run, forever — so never wrap it in `set -e`, and never read the code through a pipe
# (`symcheck.sh . | tee` gives you tee's status, not symcheck's).  **The gate is the DELTA against
# a baseline captured BEFORE the mutation, compared as a SET** — a COUNT against a baseline taken
# from a DIFFERENT tree is not a gate at all: it silently allows as many new breakages as the count
# gap.  (Round 02's own gate did exactly that and passed while two new broken symlinks existed.)
#
# Pruned, matching refscan: nested checkouts (a worktree/submodule's `.git` is a FILE, so its whole
# duplicate tree would otherwise be scanned — and its broken links are not yours) and vendored dirs.
# Only DIRECTORIES are pruned by name: a SYMLINK named node_modules is still a symlink and is tested.
set -uo pipefail

[[ $# -eq 1 ]] || { echo "usage: symcheck.sh <tree-root>" >&2; exit 2; }
ROOT="$1"
[[ "$ROOT" != "/" ]] && ROOT="${ROOT%/}"
[[ -d "$ROOT" ]] || { echo "symcheck: tree-root not a directory: $ROOT" >&2; exit 2; }

VENDOR=(.git node_modules .venv venv __pycache__)
PRUNE=()
for v in "${VENDOR[@]}"; do PRUNE+=(-name "$v" -o); done
while IFS= read -r -d '' g; do
  d="$(dirname "${g#./}")"
  [[ "$d" == "." || -z "$d" ]] && continue          # the root's own .git — not nested
  PRUNE+=(-path "$ROOT/$d" -o)
done < <(cd "$ROOT" && find . -mindepth 2 -name .git -print0 2>/dev/null | LC_ALL=C sort -z)
unset 'PRUNE[${#PRUNE[@]}-1]'                        # drop the trailing -o

broken=0
while IFS= read -r -d '' link; do
  printf '%s\n' "${link#"$ROOT"/}"
  broken=1
done < <(find "$ROOT" -type d \( "${PRUNE[@]}" \) -prune -o -type l ! -exec test -e {} \; -print0)

exit "$broken"
