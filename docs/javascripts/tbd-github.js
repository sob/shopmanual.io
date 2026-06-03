// GitHub-issues-style behavior for TBD lists rendered by tbd_macros (.ghi).
// Operates on the static rows (data-* attributes) so content works without JS.
//
// Query syntax in the search box (tokens AND together):
//   label:<name>        row must have this label            (AND across labels)
//   priority:<level>    row priority is one of these         (OR within priority)
//   area:<slug>         row has one of these areas           (OR within area)
//   project:<slug>      row has one of these projects        (OR within project)
//   <free text>         substring match on the title         (AND across words)
//   is:open / is:*      ignored (every item is an open issue)
(function () {
  'use strict';

  function parseQuery(q) {
    const f = { text: [], label: [], priority: [], area: [], project: [] };
    const tokens = q.match(/"[^"]*"|\S+/g) || [];
    for (let tok of tokens) {
      const m = tok.match(/^([a-zA-Z]+):(.*)$/);
      if (m) {
        const key = m[1].toLowerCase();
        const val = m[2].replace(/^"|"$/g, '').toLowerCase();
        if (key in f) { if (val) f[key].push(val); continue; }
        if (key === 'is' || key === 'no' || key === 'type' || key === 'state') continue;
      }
      f.text.push(tok.replace(/^"|"$/g, '').toLowerCase());
    }
    return f;
  }

  function rowMatches(row, f) {
    const labels = (row.dataset.labels || '').split(/\s+/).filter(Boolean);
    const areas = (row.dataset.areas || '').toLowerCase().split(/\s+/).filter(Boolean);
    const projects = (row.dataset.projects || '').toLowerCase().split(/\s+/).filter(Boolean);
    const title = row.dataset.title || '';
    const priority = (row.dataset.priority || '').toLowerCase();

    // labels: AND (must contain every requested label)
    if (!f.label.every(l => labels.includes(l))) return false;
    // priority/area/project: OR within each qualifier
    if (f.priority.length && !f.priority.includes(priority)) return false;
    if (f.area.length && !f.area.some(a => areas.includes(a))) return false;
    if (f.project.length && !f.project.some(p => projects.includes(p))) return false;
    // free text: AND (each word a substring of the title)
    if (!f.text.every(w => title.includes(w))) return false;
    return true;
  }

  function tokensOf(input) {
    return (input.value.match(/"[^"]*"|\S+/g) || []);
  }

  function setTokens(input, tokens) {
    input.value = tokens.join(' ') + (tokens.length ? ' ' : '');
  }

  function toggleToken(input, token) {
    const tokens = tokensOf(input);
    const i = tokens.findIndex(t => t.toLowerCase() === token.toLowerCase());
    if (i >= 0) tokens.splice(i, 1); else tokens.push(token);
    setTokens(input, tokens);
  }

  function sortRows(list, mode) {
    const rows = Array.from(list.querySelectorAll('.ghi-row'));
    const cmp = {
      priority: (a, b) => (+a.dataset.rank - +b.dataset.rank) ||
                          (+b.dataset.number - +a.dataset.number),
      newest:   (a, b) => (b.dataset.created || '').localeCompare(a.dataset.created || ''),
      oldest:   (a, b) => (a.dataset.created || '').localeCompare(b.dataset.created || ''),
      title:    (a, b) => (a.dataset.title || '').localeCompare(b.dataset.title || ''),
    }[mode] || null;
    if (!cmp) return;
    rows.sort(cmp).forEach(r => list.appendChild(r));
  }

  function apply(container) {
    const input = container.querySelector('.ghi-search');
    const list = container.querySelector('.ghi-list');
    const f = parseQuery(input.value);
    let visible = 0;
    container.querySelectorAll('.ghi-row').forEach(row => {
      const ok = rowMatches(row, f);
      row.hidden = !ok;
      if (ok) visible++;
    });
    const nEl = container.querySelector('.ghi-n');
    if (nEl) nEl.textContent = String(visible);
    const empty = container.querySelector('.ghi-empty');
    if (empty) empty.hidden = visible !== 0;

    // sync facet checkmarks with the parsed query
    container.querySelectorAll('.ghi-menu-item').forEach(item => {
      const q = item.dataset.qualifier, v = (item.dataset.value || '').toLowerCase();
      const on = (f[q] || []).includes(v);
      item.setAttribute('aria-checked', on ? 'true' : 'false');
    });
    const sort = container.dataset.sort || 'priority';
    container.querySelectorAll('.ghi-sort').forEach(s =>
      s.setAttribute('aria-checked', s.dataset.sort === sort ? 'true' : 'false'));
  }

  function wire(container) {
    const input = container.querySelector('.ghi-search');
    if (!input) return;
    container.dataset.sort = container.dataset.sort || 'priority';

    input.addEventListener('input', () => apply(container));

    // facet menu items -> toggle the qualifier token
    container.querySelectorAll('.ghi-menu-item').forEach(item => {
      item.addEventListener('click', e => {
        e.preventDefault();
        toggleToken(input, item.dataset.qualifier + ':' + item.dataset.value);
        apply(container);
      });
    });

    // label pills -> add/remove label:<name>
    container.querySelectorAll('.ghi-label').forEach(pill => {
      pill.addEventListener('click', e => {
        e.preventDefault();
        toggleToken(input, 'label:' + pill.dataset.label);
        apply(container);
      });
    });

    // sort menu
    container.querySelectorAll('.ghi-sort').forEach(s => {
      s.addEventListener('click', e => {
        e.preventDefault();
        container.dataset.sort = s.dataset.sort;
        sortRows(container.querySelector('.ghi-list'), s.dataset.sort);
        const dd = s.closest('details'); if (dd) dd.open = false;
        apply(container);
      });
    });

    // close open dropdowns when clicking elsewhere
    document.addEventListener('click', e => {
      container.querySelectorAll('details.ghi-dd[open]').forEach(dd => {
        if (!dd.contains(e.target)) dd.open = false;
      });
    });

    sortRows(container.querySelector('.ghi-list'), container.dataset.sort);
    apply(container);
  }

  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.ghi').forEach(wire);
  });
})();
