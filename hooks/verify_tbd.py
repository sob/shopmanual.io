#!/usr/bin/env python3
"""Verify TBD invariants between source files and GitHub Issues.

Fails (exit 1) if any of:
- A `TBD` marker exists in source but no open `tbd` issue covers that file.
- An open `tbd` issue's `Source:` path doesn't exist (file moved/deleted).
- An open `tbd` issue is missing any of the required label facets:
  `tbd`, `project/*`, `priority/*`, `area/*`.

Read-only: never modifies issues or files. Designed to run in CI; an optional
`GITHUB_TOKEN` lifts the API rate limit.

Usage:
  python3 hooks/verify_tbd.py                 # full check (default)
  python3 hooks/verify_tbd.py --root docs     # alternate doc root
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

DEFAULT_ROOT = "docs/jeep_lj"
# Last-resort fallback for local runs only; CI/runtime resolves the repo from
# $GITHUB_REPOSITORY (see main()), so a GitHub rename needs no edit here.
DEFAULT_REPO = "sob/shopmanual.io"
REQUIRED_FACETS = ("tbd", "project/", "priority/", "area/")

# Files within the doc root that intentionally talk *about* TBD tracking
# without being source TBDs themselves.
SOURCE_SKIPS = {
    "CLAUDE.md",
    "tbd-tracker.md",
}
# Substrings: skip any file path containing these
PATH_SKIP_SUBSTR = ("/.claude/", "/ANALYZE/")

# Lines that mention "TBD" but aren't a source-TBD marker (purely narrative).
NARRATIVE_PATTERNS = [
    re.compile(r"TBD\s*Tracker", re.IGNORECASE),
    re.compile(r"^\s*##.*\bTBD\b", re.IGNORECASE),  # section heading
    re.compile(r"\bTo\s*Be\s*Determined\b", re.IGNORECASE),
    re.compile(r"\bSection\s+\d+\s+TBDs\b", re.IGNORECASE),
    re.compile(r"\bsee\s+\[TBD\s+Tracker", re.IGNORECASE),
    re.compile(r"mark as TBD", re.IGNORECASE),
]


def _http(url, token):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "verify-tbd"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(req, timeout=30)


def fetch_open_tbds(repo, token):
    issues = []
    url = (f"https://api.github.com/repos/{repo}/issues"
           "?labels=tbd&state=open&per_page=100")
    for _ in range(20):
        with _http(url, token) as resp:
            page = json.load(resp)
            link = resp.headers.get("Link", "")
        for it in page:
            if "pull_request" in it:
                continue
            issues.append(it)
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        if not m:
            break
        url = m.group(1)
    return issues


def source_path_from_body(body):
    """Find the first `Source: <path>` line in an issue body."""
    for line in (body or "").splitlines():
        m = re.match(r"\s*Source:\s*(.+)", line)
        if m:
            # strip trailing "(line N)" or similar
            return re.sub(r"\s*\(.*\)\s*$", "", m.group(1).strip())
    return None


def is_narrative(line):
    return any(p.search(line) for p in NARRATIVE_PATTERNS)


def scan_source_tbds(root):
    """Return {path: [line_numbers]} for non-narrative TBD occurrences."""
    found = {}
    for dirpath, _, files in os.walk(root):
        if any(s in dirpath for s in PATH_SKIP_SUBSTR):
            continue
        for f in sorted(files):
            if not f.endswith(".md") or f in SOURCE_SKIPS:
                continue
            path = os.path.join(dirpath, f)
            with open(path) as fh:
                lines = fh.readlines()
            for i, line in enumerate(lines, start=1):
                if "TBD" not in line:
                    continue
                # If the line uses the {{ tbd(N) }} macro, it's tracked
                if "{{ tbd(" in line or "{{ tbds(" in line or "{{ tbds_resolved(" in line:
                    continue
                if is_narrative(line):
                    continue
                found.setdefault(path, []).append((i, line.rstrip()))
    return found


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=DEFAULT_ROOT)
    # Resolve the repo from the live runtime so this follows the repo's actual
    # name across a GitHub rename without any source edit: explicit override
    # first, then the slug GitHub Actions injects, then the static fallback.
    ap.add_argument(
        "--repo",
        default=os.environ.get("TBD_REPO")
        or os.environ.get("GITHUB_REPOSITORY")
        or DEFAULT_REPO,
    )
    args = ap.parse_args(argv)

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    try:
        issues = fetch_open_tbds(args.repo, token)
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        print(f"::error::Could not fetch issues: {exc}")
        return 2

    # Build label and source maps
    files_with_issue = set()  # files covered by at least one open tbd issue
    label_problems = []        # (issue_number, missing_facets)
    stale_sources = []         # (issue_number, source_path)

    for it in issues:
        labels = {l["name"] for l in it.get("labels", [])}
        missing = [f.rstrip("/") for f in REQUIRED_FACETS
                   if not any(n == f.rstrip("/") or n.startswith(f) for n in labels)]
        if missing:
            label_problems.append((it["number"], it["title"], missing))

        src = source_path_from_body(it.get("body", ""))
        if src:
            files_with_issue.add(src)
            if not os.path.exists(src):
                stale_sources.append((it["number"], it["title"], src))

    untracked = []
    source_hits = scan_source_tbds(args.root)
    for path, lines in source_hits.items():
        if path not in files_with_issue:
            untracked.append((path, lines))

    failed = False

    if untracked:
        failed = True
        print("\n::error::Untracked source TBDs (no open issue covers these files):")
        for path, lines in untracked:
            print(f"  {path}")
            for ln, content in lines[:5]:
                print(f"    line {ln}: {content[:100]}")
            if len(lines) > 5:
                print(f"    ... and {len(lines) - 5} more")

    if stale_sources:
        failed = True
        print("\n::error::Open `tbd` issues whose Source: file no longer exists:")
        for num, title, src in stale_sources:
            print(f"  #{num} {title}")
            print(f"    Source: {src}")

    if label_problems:
        failed = True
        print("\n::error::Open `tbd` issues missing required label facets:")
        for num, title, missing in label_problems:
            print(f"  #{num} {title}")
            print(f"    Missing: {', '.join(missing)}")

    if not failed:
        print(f"OK — {len(issues)} open tbd issues, "
              f"{sum(len(v) for v in source_hits.values())} source TBD markers, "
              f"all reconciled.")
        return 0
    print("\nSee docs/jeep_lj/CLAUDE.md §6 for the TBD workflow.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
