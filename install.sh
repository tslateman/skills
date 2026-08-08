#!/usr/bin/env bash
set -euo pipefail

DEST="${HOME}/.claude/plugins/skills"
REPO="https://github.com/tslateman/skills.git"
PLUGINS_JSON="${HOME}/.claude/plugins/installed_plugins.json"

if ! command -v git >/dev/null; then
  echo "git required." >&2
  exit 1
fi

if ! command -v jq >/dev/null; then
  echo "jq required for plugin registration. Install with: brew install jq" >&2
  exit 1
fi

if [[ -d "${DEST}" ]]; then
  git -C "${DEST}" pull --ff-only
  echo "skills updated."
else
  mkdir -p "$(dirname "${DEST}")"
  git clone "${REPO}" "${DEST}"
  echo "skills installed to ${DEST}"
fi

mkdir -p "$(dirname "${PLUGINS_JSON}")"
if [[ ! -f "${PLUGINS_JSON}" ]]; then
  echo '{"version":2,"plugins":{}}' >"${PLUGINS_JSON}"
fi

VERSION=$(jq -r '.version' "${DEST}/.claude-plugin/plugin.json")
NOW=$(date -u +"%Y-%m-%dT%H:%M:%S.000Z")
SHA=$(git -C "${DEST}" rev-parse HEAD)

TMP=$(mktemp)
trap 'rm -f "${TMP}"' EXIT

jq --arg path "${DEST}" --arg ver "${VERSION}" --arg now "${NOW}" --arg sha "${SHA}" \
  '.plugins["skills@local"] = [{
    scope: "user",
    installPath: $path,
    version: $ver,
    installedAt: $now,
    lastUpdated: $now,
    gitCommitSha: $sha
  }]' "${PLUGINS_JSON}" >"${TMP}"

mv "${TMP}" "${PLUGINS_JSON}"
trap - EXIT

echo "skills registered. Restart Claude Code to load."
