#!/usr/bin/env bash
# Cloudflare Pages build entrypoint.
#
# Zensical does not honor MkDocs `exclude_docs`, so it renders every *.md under
# docs_dir — including the AI-only CLAUDE.md navigation guides that MkDocs skips.
# We can't exclude them at build time, so we build the full site and then prune
# the published CLAUDE pages from the output. (They're also kept out of the
# search index via `search: { exclude: true }` frontmatter in each CLAUDE.md.)
#
# Set the Cloudflare Pages "Build command" to:  bash build.sh
set -euo pipefail

# Install the generator + plugins (Cloudflare provides Python). Keep this list
# in sync with the plugins referenced by mkdocs.yml.
pip install --quiet zensical mkdocs-print-site-plugin

zensical build --clean

# Remove published CLAUDE.md pages (directory-URL output -> ".../CLAUDE/").
SITE_DIR="${ZENSICAL_SITE_DIR:-site}"
pruned=0
while IFS= read -r -d '' dir; do
  rm -rf "$dir"
  pruned=$((pruned + 1))
done < <(find "$SITE_DIR" -type d -name CLAUDE -print0)
# Defensive: also handle non-directory-URL output (".../CLAUDE.html").
find "$SITE_DIR" -type f -name 'CLAUDE.html' -delete

echo "build.sh: pruned ${pruned} CLAUDE page(s) from ${SITE_DIR}/"
