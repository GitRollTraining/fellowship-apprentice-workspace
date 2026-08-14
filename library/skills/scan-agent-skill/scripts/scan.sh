#!/usr/bin/env bash
set -euo pipefail

readonly expected_version="2.0.13"
readonly scanner_bin="${FELLOWSHIP_SKILL_SCANNER_BIN:-skill-scanner}"

usage() {
  echo "Usage: $0 <skill-directory|SKILL.md|skill.md>" >&2
  exit 2
}

[[ $# -eq 1 ]] || usage

target="$1"
if [[ -d "$target" ]]; then
  skill_directory="$target"
  if [[ -f "$target/SKILL.md" ]]; then
    skill_file="SKILL.md"
  elif [[ -f "$target/skill.md" ]]; then
    skill_file="skill.md"
  else
    echo "No SKILL.md or skill.md found in: $target" >&2
    exit 2
  fi
elif [[ -f "$target" ]]; then
  skill_directory="$(dirname -- "$target")"
  skill_file="$(basename -- "$target")"
  case "$skill_file" in
    SKILL.md|skill.md) ;;
    *)
      echo "Expected a skill directory, SKILL.md, or skill.md: $target" >&2
      exit 2
      ;;
  esac
else
  echo "Skill path does not exist: $target" >&2
  exit 2
fi

if ! command -v "$scanner_bin" >/dev/null 2>&1; then
  echo "skill-scanner is not installed." >&2
  echo "After user approval, install the pinned tool with:" >&2
  echo "  pipx install cisco-ai-skill-scanner==$expected_version" >&2
  exit 127
fi

installed_version="$("$scanner_bin" --version 2>/dev/null || true)"
if [[ "$installed_version" != "skill-scanner $expected_version" ]]; then
  echo "Expected skill-scanner $expected_version, got: ${installed_version:-unknown}" >&2
  echo "After user approval, install the pinned version with:" >&2
  echo "  pipx install --force cisco-ai-skill-scanner==$expected_version" >&2
  exit 2
fi

# LiteLLM otherwise makes a best-effort model-pricing request during import, even when the LLM
# analyzer is disabled. Force its bundled map so the default scan does not initiate network access.
export LITELLM_LOCAL_MODEL_COST_MAP=True

exec "$scanner_bin" scan "$skill_directory" \
  --skill-file "$skill_file" \
  --policy balanced \
  --format markdown \
  --no-render-markdown \
  --detailed \
  --fail-on-severity high
