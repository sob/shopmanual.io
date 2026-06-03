---
description: Reconcile source TBD markers against open GitHub `tbd` issues
---

# Verify TBD Tracking

The source of truth for TBD items is **GitHub Issues labeled `tbd`** (the
`docs/jeep_lj/tbd-tracker.md` page just renders them). This command checks that
source TBD markers and open issues stay in sync.

**Search Path:** `docs/jeep_lj/` (exclude `CLAUDE.md`, `tbd-tracker.md`, `.claude/`, `ANALYZE/`)

**Issues:** `gh issue list -R sob/drawings --label tbd --state open --limit 300 --json number,title,body,labels`

## Checks to Perform

### 1. Find all TBD markers in source files

Search all `.md` files under `docs/jeep_lj/` for:
- "TBD" (case insensitive)
- "TODO" outside of Outstanding Items sections
- "UNKNOWN" / "unknown" used as a placeholder value

### 2. Source → Issues (untracked TBDs)

For each TBD found in a source file, confirm an **open** `tbd` issue exists for
it — match on the `Source:` path in the issue body and/or the topic in the
title. Flag any source TBD with no matching open issue.

### 3. Issues → Source (stale issues)

For each open `tbd` issue, read its `Source:` file and confirm the TBD still
exists there. Flag issues whose source:
- no longer contains the TBD (resolved in docs but issue still open), or
- points to a file that no longer exists.

### 4. Label hygiene

Flag any open `tbd` issue missing a required facet label:
- `project/<vehicle>` (e.g. `project/jeep-lj`)
- `priority/<level>` (`critical` | `high` | `medium` | `low` | `verify`)
- `area/<section>` (e.g. `area/power-systems`)

Also flag obvious priority mismatches (e.g. a part number needed before ordering
marked `priority/low` → should be `high`).

## Exclusions

Skip when scanning source:
- `CLAUDE.md` files (navigation guides; they reference the TBD process)
- `tbd-tracker.md` (renders issues — not a source of TBDs)
- anything in `.claude/` or `docs/ANALYZE/`
- `index.md` files that only link to the tracker

## Output Format

**Untracked source TBDs (need an issue):**
| File | Line | TBD Text | Suggested priority | Suggested area |
|------|------|----------|--------------------|----------------|

**Stale open issues (resolved in source):**
| Issue | Title | Source file | Current state | Action |
|-------|-------|-------------|---------------|--------|

**Label problems:**
| Issue | Title | Missing / wrong label |
|-------|-------|------------------------|

## After Audit (with approval)

1. **Open issues** for untracked source TBDs:
   ```bash
   gh issue create -R sob/drawings --title "<topic>" \
     --body "<description>

   Source: <path>" \
     --label tbd --label project/jeep-lj --label priority/<level> --label area/<section>
   ```
2. **Close** issues resolved in source: `gh issue close <n> -R sob/drawings -c "<resolution>"`
3. **Fix labels:** `gh issue edit <n> -R sob/drawings --add-label area/<section>`

No markdown table to edit and no counts to update — the tracker page and the
landing-page blocks refresh from issues on the next build.
