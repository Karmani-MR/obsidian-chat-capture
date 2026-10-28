#!/usr/bin/env bash
# Optional helper: downloads Dataview, Templater, Calendar and Obsidian Git into a vault
# so they load the first time you open it (after you click "Trust author and enable plugins").
# Mirrors what Obsidian's community-plugin browser does: reads each plugin's manifest.json
# from its GitHub repo, then downloads the matching release files.
#
# Usage:   ./install-plugins.sh                  (uses ./vault-template)
#          ./install-plugins.sh "/path/to/vault"   (any vault)
set -euo pipefail

VAULT="${1:-$(cd "$(dirname "$0")" && pwd)/../vault-template}"
PLUGIN_DIR="$VAULT/.obsidian/plugins"

if [ ! -d "$VAULT/.obsidian" ]; then
  echo "Could not find $VAULT/.obsidian — pass the vault folder as the first argument." >&2
  exit 1
fi

# id|github-repo
PLUGINS=(
  "dataview|blacksmithgu/obsidian-dataview"
  "templater-obsidian|SilentVoid13/Templater"
  "calendar|liamcain/obsidian-calendar-plugin"
  "obsidian-git|Vinzent03/obsidian-git"
)

for entry in "${PLUGINS[@]}"; do
  id="${entry%%|*}"
  repo="${entry##*|}"
  dest="$PLUGIN_DIR/$id"
  mkdir -p "$dest"

  version=$(curl -fsSL "https://raw.githubusercontent.com/$repo/HEAD/manifest.json" \
    | sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -n1)
  if [ -z "$version" ]; then
    echo "  ! Could not read version for $id — install it from Obsidian's plugin browser instead." >&2
    continue
  fi

  echo "Installing $id $version ..."
  base="https://github.com/$repo/releases/download/$version"
  curl -fsSL "$base/main.js"       -o "$dest/main.js"
  curl -fsSL "$base/manifest.json" -o "$dest/manifest.json"
  # styles.css is optional for some plugins
  curl -fsSL "$base/styles.css"    -o "$dest/styles.css" 2>/dev/null || rm -f "$dest/styles.css"
done

echo
echo "Done. Open the vault in Obsidian and choose 'Trust author and enable plugins'."
echo "Then enable Templater > 'Trigger Templater on new file creation' (see README Quick start step 5)."
