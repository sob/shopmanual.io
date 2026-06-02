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
_CACHE = {"issues": None}


def _repo_slug():
    """owner/name from mkdocs.yml repo_url (read from disk, engine-independent)."""
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


def _fetch_tbds():
    """Open issues labeled `tbd` via the GitHub REST API. None on failure.

    Uses urllib (stdlib) so it runs anywhere the build runs -- including
    Cloudflare Pages, which has no `gh` CLI. The repo is public, so anonymous
    requests work; set GITHUB_TOKEN / GH_TOKEN to raise the rate limit.
    """
    repo = _repo_slug()
    if not repo:
        return None
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "tbd-macros"}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    url = (f"https://api.github.com/repos/{repo}/issues"
           "?labels=tbd&state=open&per_page=100")
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
                names = {l["name"] for l in it.get("labels", [])}
                priority = next(
                    (n.split("/", 1)[1] for n in names if n.startswith("priority/")),
                    None,
                )
                issues.append({
                    "number": it["number"],
                    "title": it["title"],
                    "url": it.get("html_url", ""),
                    "desc": _first_line(it.get("body", "")),
                    "projects": {n.split("/", 1)[1] for n in names if n.startswith("project/")},
                    "areas": {n.split("/", 1)[1] for n in names if n.startswith("area/")},
                    "priority": priority,
                })
            if not url:
                break
    except (urllib.error.URLError, TimeoutError, ValueError, OSError):
        return None
    return issues


def _issues():
    if _CACHE["issues"] is None:
        _CACHE["issues"] = _fetch_tbds()
    return _CACHE["issues"]


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
             scope=None, group_by="priority", show_empty=False):
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

        if group_by == "priority":
            blocks = []
            for lvl in PRIORITY_ORDER:
                group = [it for it in sel if it["priority"] == lvl]
                if group or show_empty:
                    blocks.append(_admonition(lvl, group))
            return "\n\n".join(blocks) if blocks else _none_note()

        return _admonition(None, sel) if (sel or show_empty) else _none_note()


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
            lines.append(f"    - [{it['title']} (#{it['number']})]({it['url']}){dash}")
    else:
        lines.append("    _No open items._")
    return "\n".join(lines)


def _none_note():
    return '!!! success "No open TBD items"\n\n    Nothing outstanding here. \U0001F389\n'
