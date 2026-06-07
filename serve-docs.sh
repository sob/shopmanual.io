#!/usr/bin/env bash
# Serve the documentation locally with live reload.
#
# Self-bootstrapping: creates a local .venv (gitignored) on first run and
# installs the preview toolchain into it, so you never have to fight the system
# pip / Xcode Python. Subsequent runs reuse the venv and start instantly.
#
# Note: production builds with Zensical (see build.sh); Zensical isn't on PyPI,
# so local preview uses MkDocs + Material, which renders the same content.
set -euo pipefail

cd "$(dirname "$0")"

VENV=".venv"
if [[ ! -x "$VENV/bin/mkdocs" ]]; then
  echo "Setting up preview environment in $VENV (first run only)..."
  python3 -m venv "$VENV"
  "$VENV/bin/python" -m pip install --quiet --upgrade pip
  "$VENV/bin/pip" install --quiet \
    mkdocs-material \
    mkdocs-macros-plugin \
    mkdocs-autorefs \
    mkdocs-print-site-plugin
fi

echo "Documentation will be available at: http://127.0.0.1:8000"
echo "Press Ctrl+C to stop the server"
echo ""

# Match the production repo so the TBD macros resolve against GitHub.
export GITHUB_REPOSITORY="${GITHUB_REPOSITORY:-sob/shopmanual.io}"
exec "$VENV/bin/mkdocs" serve "$@"
