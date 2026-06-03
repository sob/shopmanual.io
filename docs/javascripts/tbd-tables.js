// Enhance generated TBD tables (class "tbd-table") with sort + filter.
// Uses simple-datatables (loaded via extra_javascript). No-op if absent.
document.addEventListener('DOMContentLoaded', function () {
  if (typeof simpleDatatables === 'undefined') return;
  document.querySelectorAll('table.tbd-table').forEach(function (table) {
    new simpleDatatables.DataTable(table, {
      searchable: true,   // live filter box
      sortable: true,     // click headers to sort (=> group by Priority/Area)
      paging: false,      // show all rows
      perPageSelect: false,
      labels: { searchTitle: 'Filter TBD items', placeholder: 'Filter…' }
    });
  });
});
