"""
Macros module: render open "TBD" GitHub issues as Material admonitions.

Engine: targets Zensical's native macros module (zensical.extensions.macros),
which Zensical auto-maps from the `plugins: macros:` entry in mkdocs.yml. Also
works under the classic mkdocs-macros-plugin for local `mkdocs serve`.

Source of truth is GitHub Issues labeled `tbd`. Each issue also carries:
  - project/<slug>   one per vehicle   (e.g. project/jeep-lj)
  - area/<slug>      doc section        (e.g. area/power-systems)
  - priority/<level> critical|high|medium|low|verify

Usage in any page:
  {{ tbds() }}                         this page's project + area, grouped by priority
  {{ tbds(area='power-systems') }}     same project, a different area
  {{ tbds(scope='project') }}          every TBD for this page's vehicle
  {{ tbds(project='nissan-nv') }}      explicit vehicle, all areas
  {{ tbds(scope='all') }}              everything open

Issues are fetched once per build (lazy, cached) and filtered in memory. If the
fetch fails (no gh / no token), pages render a notice instead of breaking.
"""

import datetime
import html
import json
import os
import re
import urllib.error
import urllib.request

import jinja2

# priority slug -> (display label, Material admonition type, leading emoji, sort order)
PRIORITY_META = {
    "critical": ("Critical", "danger", "\U0001F534", 0),   # 🔴
    "high":     ("High",     "warning", "", 1),
    "medium":   ("Medium",   "info", "\U0001F4CB", 2),      # 📋
    "low":      ("Low",      "note", "\U0001F4DD", 3),      # 📝
    "verify":   ("Verify",   "question", "\U0001F50D", 4),  # 🔍
}
PRIORITY_ORDER = sorted(PRIORITY_META, key=lambda k: PRIORITY_META[k][3])

# Build-lifetime cache. None == not fetched yet; a list == fetched (possibly empty).
_CACHE = {"issues": None, "closed": None, "comments": {}}


def _http_headers():
    h = {"Accept": "application/vnd.github+json", "User-Agent": "tbd-macros"}
    tok = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if tok:
        h["Authorization"] = f"Bearer {tok}"
    return h


def _repo_slug():
    """owner/name of the repo: $GITHUB_REPOSITORY when set (so it follows the
    live name across a rename), else mkdocs.yml repo_url (read from disk,
    engine-independent)."""
    env_slug = os.environ.get("GITHUB_REPOSITORY")
    if env_slug:
        return env_slug
    cfg = os.path.join(os.path.dirname(os.path.abspath(__file__)), "mkdocs.yml")
    try:
        with open(cfg, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None
    m = re.search(r"^\s*repo_url:\s*(\S+)", text, re.MULTILINE)
    if not m:
        return None
    m2 = re.search(r"github\.com[:/]+([^/]+/[^/\s]+?)(?:\.git)?$", m.group(1).rstrip("/"))
    return m2.group(1) if m2 else None


def _next_link(link_header):
    """Extract the rel="next" URL from a GitHub Link response header, if any."""
    for part in (link_header or "").split(","):
        m = re.search(r'<([^>]+)>;\s*rel="next"', part)
        if m:
            return m.group(1)
    return None


def _fetch_tbds(state="open"):
    """Issues labeled `tbd` via the GitHub REST API. None on failure.

    Uses urllib (stdlib) so it runs anywhere the build runs -- including
    Cloudflare Pages, which has no `gh` CLI. The repo is public, so anonymous
    requests work; set GITHUB_TOKEN / GH_TOKEN to raise the rate limit.
    """
    repo = _repo_slug()
    if not repo:
        return None
    headers = _http_headers()

    url = (f"https://api.github.com/repos/{repo}/issues"
           f"?labels=tbd&state={state}&per_page=100")
    issues = []
    try:
        for _ in range(20):  # pagination safety bound
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                page = json.load(resp)
                url = _next_link(resp.headers.get("Link", ""))
            for it in page:
                if "pull_request" in it:        # /issues also returns PRs
                    continue
                labels = [{"name": l["name"], "color": l.get("color", "")}
                          for l in it.get("labels", [])]
                names = {l["name"] for l in labels}
                priority = next(
                    (n.split("/", 1)[1] for n in names if n.startswith("priority/")),
                    None,
                )
                issues.append({
                    "number": it["number"],
                    "title": it["title"],
                    "url": it.get("html_url", ""),
                    "desc": _first_line(it.get("body", "")),
                    "labels": labels,                       # name+color, in order
                    "projects": {n.split("/", 1)[1] for n in names if n.startswith("project/")},
                    "areas": {n.split("/", 1)[1] for n in names if n.startswith("area/")},
                    "priority": priority,
                    "created": it.get("created_at", ""),
                    "closed": it.get("closed_at", ""),
                    "author": (it.get("user") or {}).get("login", ""),
                    "comments_url": it.get("comments_url", ""),
                    "comments_count": it.get("comments", 0),
                })
            if not url:
                break
    except (urllib.error.URLError, TimeoutError, ValueError, OSError):
        return None
    return issues


def _fetch_last_comment(comments_url):
    """Fetch the last comment on an issue. '' on failure or no comments.

    Cached per URL so re-renders within a single build are free.
    """
    if not comments_url:
        return ""
    if comments_url in _CACHE["comments"]:
        return _CACHE["comments"][comments_url]
    body = ""
    try:
        req = urllib.request.Request(comments_url + "?per_page=100",
                                     headers=_http_headers())
        with urllib.request.urlopen(req, timeout=30) as resp:
            comments = json.load(resp)
        if comments:
            body = (comments[-1].get("body") or "").strip()
    except (urllib.error.URLError, TimeoutError, ValueError, OSError):
        body = ""
    _CACHE["comments"][comments_url] = body
    return body


def _issues():
    if _CACHE["issues"] is None:
        _CACHE["issues"] = _fetch_tbds("open")
    return _CACHE["issues"]


def _closed_issues():
    if _CACHE["closed"] is None:
        _CACHE["closed"] = _fetch_tbds("closed")
    return _CACHE["closed"]


_SINCE_RE = re.compile(r"^\s*(\d+)\s*([dwmy]?)\s*$", re.IGNORECASE)


def _parse_since(spec):
    """Parse a 'since' spec ('90d', '6m', '1y', '2026-01-01', None) -> aware datetime or None."""
    if not spec:
        return None
    if isinstance(spec, datetime.datetime):
        return spec
    m = _SINCE_RE.match(str(spec))
    if m:
        n = int(m.group(1))
        unit = (m.group(2) or "d").lower()
        days = n * {"d": 1, "w": 7, "m": 30, "y": 365}[unit]
        return datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days)
    # ISO date fallback
    try:
        return datetime.datetime.strptime(str(spec)[:10], "%Y-%m-%d").replace(
            tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def _parse_iso(iso):
    if not iso:
        return None
    try:
        return datetime.datetime.strptime(iso[:19], "%Y-%m-%dT%H:%M:%S").replace(
            tzinfo=datetime.timezone.utc)
    except ValueError:
        return None


def _first_line(body):
    for line in (body or "").splitlines():
        line = line.strip()
        if line and not line.lower().startswith("source:"):
            return line
    return ""


def _derive(src_uri):
    """Derive (project, area) from a page source path.

    Handles section pages and section index pages, which collapse to fewer
    path segments:
      jeep_lj/index.md                      -> ('jeep-lj', None)
      jeep_lj/01-power-systems/index.md     -> ('jeep-lj', 'power-systems')
      jeep_lj/01-power-systems/04-pmu/x.md  -> ('jeep-lj', 'power-systems')
    """
    path = re.sub(r"\.md$", "", (src_uri or "").strip("/"))
    parts = [p for p in path.split("/") if p]
    if parts and parts[-1] == "index":      # drop trailing section index
        parts = parts[:-1]
    project = parts[0].replace("_", "-") if parts else None
    area = re.sub(r"^\d+[-_]", "", parts[1]) if len(parts) >= 2 else None
    return project, area


def _page_src_uri(ctx):
    """Current page source path from the render context.

    Zensical exposes it as page.path; mkdocs as page.file.src_uri.
    """
    page = None
    if ctx is not None:
        try:
            page = ctx.get("page")
        except Exception:
            page = None
    if not page:
        return ""
    src = getattr(page, "path", None)            # Zensical
    if src:
        return src
    return getattr(getattr(page, "file", None), "src_uri", "") or ""  # mkdocs


def define_env(env):

    @env.macro
    @jinja2.pass_context
    def tbds(ctx, project=None, area=None, priority=None,
             scope=None, group_by="priority", show_empty=False,
             layout="admonitions"):
        issues = _issues()
        if issues is None:
            return ('!!! failure "TBD tracker unavailable"\n\n'
                    "    Could not reach the GitHub issues API at build time "
                    "(network or rate limit). Set `GITHUB_TOKEN` to raise the limit.\n")

        # auto-derive project/area from the current page unless overridden
        d_project, d_area = _derive(_page_src_uri(ctx))
        if project is None:
            project = d_project
        if scope in ("project", "all"):
            area = None          # widen to whole vehicle
        elif area is None:
            area = d_area
        if scope == "all":
            project = None       # everything

        sel = []
        for it in issues:
            if project and project not in it["projects"]:
                continue
            if area and area not in it["areas"]:
                continue
            if priority and it["priority"] != priority:
                continue
            sel.append(it)

        # GitHub-issues-style list (filter bar + faceted dropdowns + label pills).
        if layout == "github":
            return _github(sel) if (sel or show_empty) else _none_note()

        # Admonitions grouped by priority (default).
        if group_by == "priority":
            blocks = []
            for lvl in PRIORITY_ORDER:
                group = [it for it in sel if it["priority"] == lvl]
                if group or show_empty:
                    blocks.append(_admonition(lvl, group))
            return "\n\n".join(blocks) if blocks else _none_note()

        return _admonition(None, sel) if (sel or show_empty) else _none_note()

    @env.macro
    def tbd(n, label="TBD"):
        """Inline cell-level marker linked to GitHub issue #n.

        Open issue   -> '<label> #N' as a link.
        Closed issue -> first sentence/line of the resolution (last comment),
                        with a small clickable '#N' suffix pointing to the
                        closed issue.
        Missing      -> '<label> #N' linked, with a warning marker.
        """
        if not isinstance(n, int):
            try:
                n = int(n)
            except (TypeError, ValueError):
                return f"{label} (#?)"

        # Search open issues first
        for it in (_issues() or []):
            if it["number"] == n:
                return (f'<a href="{html.escape(it["url"])}" target="_blank" '
                        f'rel="noopener">{html.escape(label)} #{n}</a>')
        # Then closed
        for it in (_closed_issues() or []):
            if it["number"] == n:
                resolution = ""
                if it.get("comments_count"):
                    resolution = _fetch_last_comment(it["comments_url"])
                if not resolution:
                    resolution = it.get("desc") or it["title"]
                # First sentence (or first 200 chars)
                snippet = re.split(r"(?<=[.!?])\s+", resolution.strip(), maxsplit=1)[0]
                if len(snippet) > 200:
                    snippet = snippet[:197].rstrip() + "…"
                snippet = snippet.replace("|", "\\|")
                return (f'{snippet} '
                        f'<a href="{html.escape(it["url"])}" target="_blank" '
                        f'rel="noopener" title="Closed issue #{n}">#{n}</a>')
        # Not found in either list
        repo = _repo_slug() or "sob/drawings"
        return (f'<a href="https://github.com/{repo}/issues/{n}" '
                f'target="_blank" rel="noopener" '
                f'title="Issue not found in tbd-labeled list">⚠️ {html.escape(label)} #{n}</a>')

    @env.macro
    @jinja2.pass_context
    def tbds_resolved(ctx, since="90d", project=None, area=None, scope=None,
                      limit=None):
        """Render closed `tbd` issues as a markdown table: Item | Resolution | Date.

        `since` is a window like '90d' / '6m' / '1y' or an ISO date; pass None
        for full history. Resolution is the last comment on the issue (which
        is what `gh issue close -c "..."` posts).
        """
        items = _closed_issues()
        if items is None:
            return ('!!! failure "Resolved TBDs unavailable"\n\n'
                    "    Could not reach the GitHub issues API at build time.\n")

        # auto-derive project/area like tbds() does
        d_project, d_area = _derive(_page_src_uri(ctx))
        if project is None:
            project = d_project
        if scope in ("project", "all"):
            area = None
        elif area is None:
            area = d_area
        if scope == "all":
            project = None

        cutoff = _parse_since(since)
        sel = []
        for it in items:
            if project and project not in it["projects"]:
                continue
            if area and area not in it["areas"]:
                continue
            closed_dt = _parse_iso(it["closed"])
            if cutoff and (closed_dt is None or closed_dt < cutoff):
                continue
            sel.append(it)

        sel.sort(key=lambda it: it["closed"], reverse=True)
        if limit:
            sel = sel[: int(limit)]

        if not sel:
            return ('!!! success "No resolved TBDs in window"\n\n'
                    "    Nothing has been closed in this window.\n")

        rows = ["| Item | Resolution | Date |", "| :--- | :--------- | :--- |"]
        for it in sel:
            resolution = ""
            if it.get("comments_count"):
                resolution = _fetch_last_comment(it["comments_url"])
            if not resolution:
                resolution = it.get("desc") or "_(closed without comment)_"
            # Collapse newlines and pipes so we don't break the table.
            resolution = re.sub(r"\s*\n+\s*", " ", resolution).replace("|", "\\|")
            title_link = (f'<a href="{html.escape(it["url"])}" target="_blank" '
                          f'rel="noopener">{html.escape(it["title"])} '
                          f'(#{it["number"]})</a>')
            date = _fmt_date(it["closed"]) or it["closed"][:10]
            rows.append(f"| {title_link} | {resolution} | {date} |")
        return "\n".join(rows)


def _admonition(level, items):
    if level is None:
        label, kind, emoji = "Open Items", "info", ""
    else:
        label, kind, emoji, _ = PRIORITY_META[level]
    title = f"{emoji + ' ' if emoji else ''}{label} ({len(items)})"
    lines = [f'!!! {kind} "{title}"', ""]
    if items:
        for it in items:
            dash = f" — {it['desc']}" if it["desc"] else ""
            link = (f'<a href="{html.escape(it["url"])}" target="_blank" '
                    f'rel="noopener">{html.escape(it["title"])} '
                    f'(#{it["number"]})</a>')
            lines.append(f"    - {link}{dash}")
    else:
        lines.append("    _No open items._")
    return "\n".join(lines)


_OPEN_ICON = (
    '<svg class="ghi-state" viewBox="0 0 16 16" width="16" height="16" '
    'aria-hidden="true"><path d="M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3Z">'
    '</path><path d="M8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 '
    '0 6.5 6.5 0 0 0-13 0Z"></path></svg>'
)


def _contrast(hex_color):
    """Pick readable text color (dark/light) for a label background, like GitHub."""
    h = (hex_color or "").lstrip("#")
    if len(h) != 6:
        return "#1f2328"
    try:
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return "#1f2328"
    # perceived luminance
    lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
    return "#1f2328" if lum > 0.6 else "#ffffff"


def _fmt_date(iso):
    """'2026-05-30T22:15:35Z' -> 'May 30, 2026' (empty on failure)."""
    if not iso:
        return ""
    try:
        d = datetime.datetime.strptime(iso[:10], "%Y-%m-%d")
    except ValueError:
        return ""
    return f"{d.strftime('%b')} {d.day}, {d.year}"


def _label_pill(name, color):
    """A GitHub-style colored label pill that is clickable to filter."""
    bg = f"#{color}" if color else "#ededed"
    fg = _contrast(color)
    return (f'<button type="button" class="ghi-label" data-label="{html.escape(name)}" '
            f'style="--lbl-bg:{bg};--lbl-fg:{fg};">{html.escape(name)}</button>')


def _github(items):
    """Render items as a GitHub-issues-style list: a bordered box with a header
    count, a filter/search bar (GitHub query syntax), faceted dropdowns
    (Labels / Priority / Area / Project / Sort), and rows with colored label
    pills. All open issues, pre-sorted by priority for the no-JS view.

    Filtering/sorting is done client-side (tbd-github.js) over the rendered
    rows via their data-* attributes, so content still shows without JS.
    """
    def sort_key(it):
        meta = PRIORITY_META.get(it["priority"])
        rank = meta[3] if meta else 99
        return (rank, -it["number"])

    rows = sorted(items, key=sort_key)

    # Build facet option lists from the data actually present.
    all_labels = {}
    priorities, areas, projects = set(), set(), set()
    for it in rows:
        for lb in it["labels"]:
            all_labels[lb["name"]] = lb["color"]
        if it["priority"]:
            priorities.add(it["priority"])
        areas.update(it["areas"])
        projects.update(it["projects"])

    def menu(title, qualifier, options, colored=False):
        items_html = []
        for opt in options:
            swatch = ""
            if colored:
                c = all_labels.get(opt, "")
                swatch = (f'<span class="ghi-swatch" '
                          f'style="background:#{c or "ededed"}"></span>')
            items_html.append(
                f'<button type="button" class="ghi-menu-item" '
                f'data-qualifier="{qualifier}" data-value="{html.escape(opt)}">'
                f'<span class="ghi-check">✓</span>{swatch}'
                f'{html.escape(opt)}</button>')
        return (f'<details class="ghi-dd"><summary>{title} '
                f'<span class="ghi-caret">▾</span></summary>'
                f'<div class="ghi-menu">{"".join(items_html)}</div></details>')

    sort_menu = (
        '<details class="ghi-dd ghi-dd--right"><summary>Sort '
        '<span class="ghi-caret">▾</span></summary><div class="ghi-menu">'
        '<button type="button" class="ghi-sort" data-sort="priority">Priority</button>'
        '<button type="button" class="ghi-sort" data-sort="newest">Newest</button>'
        '<button type="button" class="ghi-sort" data-sort="oldest">Oldest</button>'
        '<button type="button" class="ghi-sort" data-sort="title">Title</button>'
        '</div></details>')

    facets = [
        menu("Labels", "label", sorted(all_labels), colored=True),
        menu("Priority", "priority", PRIORITY_ORDER),
        menu("Area", "area", sorted(areas)),
        menu("Project", "project", sorted(projects)),
    ]

    out = ['<div class="ghi" markdown="0">']
    out.append('<div class="ghi-toolbar">')
    out.append('<div class="ghi-search-wrap">'
               '<svg class="ghi-search-icon" viewBox="0 0 16 16" width="16" '
               'height="16" aria-hidden="true"><path d="M10.68 11.74a6 6 0 0 1-7.922-8.982'
               ' 6 6 0 0 1 8.982 7.922l3.04 3.04a.749.749 0 0 1-.326 1.275.749.749 0 0 1'
               '-.734-.215ZM11.5 7a4.499 4.499 0 1 0-8.997 0A4.499 4.499 0 0 0 11.5 7Z">'
               '</path></svg>'
               '<input type="text" class="ghi-search" value="is:open " '
               'aria-label="Filter TBD issues" '
               'placeholder="Filter by label:, priority:, area:, project: or text"></div>')
    out.append('<div class="ghi-filters">' + "".join(facets) + sort_menu + '</div>')
    out.append('</div>')  # toolbar

    out.append('<div class="ghi-box">')
    out.append(f'<div class="ghi-head">{_OPEN_ICON}'
               f'<span class="ghi-count"><span class="ghi-n">{len(rows)}</span> Open</span>'
               f'</div>')
    out.append('<ul class="ghi-list">')
    for it in rows:
        meta = PRIORITY_META.get(it["priority"])
        rank = meta[3] if meta else 99
        names = " ".join(lb["name"] for lb in it["labels"])
        pills = "".join(_label_pill(lb["name"], lb["color"]) for lb in it["labels"])
        meta_bits = [f'#{it["number"]}']
        when = _fmt_date(it["created"])
        if when:
            meta_bits.append(f'opened on {when}')
        if it["author"]:
            meta_bits.append(f'by {html.escape(it["author"])}')
        sub = " ".join(meta_bits)
        out.append(
            f'<li class="ghi-row" data-number="{it["number"]}" data-rank="{rank}" '
            f'data-title="{html.escape(it["title"].lower(), quote=True)}" '
            f'data-labels="{html.escape(names.lower(), quote=True)}" '
            f'data-priority="{html.escape(it["priority"] or "")}" '
            f'data-areas="{html.escape(" ".join(sorted(it["areas"])))}" '
            f'data-projects="{html.escape(" ".join(sorted(it["projects"])))}" '
            f'data-created="{html.escape(it["created"])}">'
            f'{_OPEN_ICON}'
            f'<div class="ghi-main">'
            f'<a class="ghi-title" href="{html.escape(it["url"])}" '
            f'target="_blank" rel="noopener">'
            f'{html.escape(it["title"])}</a> '
            f'<span class="ghi-labels">{pills}</span>'
            f'<div class="ghi-meta">{html.escape(sub)}</div>'
            f'</div></li>')
    out.append('</ul>')
    out.append('<div class="ghi-empty" hidden>No TBD items match your filters.</div>')
    out.append('</div>')  # box
    out.append('</div>')  # ghi
    return "\n" + "\n".join(out) + "\n"


def _none_note():
    return '!!! success "No open TBD items"\n\n    Nothing outstanding here. \U0001F389\n'
