---
hide:
  - navigation
  - toc
---

<section class="sm-hero">
  <div class="sm-hero__inner">
    <p class="sm-hero__eyebrow">Project vehicle build manuals</p>
    <h1 class="sm-hero__title">Every wire and every part, written down.</h1>
    <p class="sm-hero__lede">shopmanual.io is a living build manual for my project vehicles — wiring diagrams, part numbers, and the reasoning behind every decision, kept in one searchable place.</p>
    <p class="sm-hero__actions">
      <a class="sm-btn sm-btn--primary" href="jeep_lj/">Explore the Jeep LJ build</a>
      <a class="sm-btn sm-btn--ghost" href="#projects">See all projects</a>
    </p>
  </div>
</section>

<section class="sm-mission">
  <p class="sm-mission__text">Build knowledge has a way of vanishing — buried in forum threads, scribbled on receipts, or living only in your head until the moment you need it. This site is the fix: document it properly, once, and keep it current.</p>
</section>

<section class="sm-section" id="projects">
  <h2 class="sm-section__title">In the garage</h2>
  <p class="sm-section__sub">Pick a build to dive in.</p>
  <div class="sm-cards sm-cards--projects">
    <a class="sm-card" href="jeep_lj/">
      <span class="sm-card__icon">🚙</span>
      <span class="sm-card__title">Jeep Wrangler LJ</span>
      <span class="sm-card__desc">A 2006 LJ with a Cummins R2.8 turbo-diesel swap and a ground-up electrical rebuild: dual isolated batteries, programmable power management, keyless start, and a full lighting, audio, and recovery package.</span>
      <span class="sm-card__cta">Explore the build →</span>
    </a>
    <a class="sm-card sm-card--soon" href="nissan_nv/">
      <span class="sm-card__icon">🚐</span>
      <span class="sm-card__title">Nissan NV 3500 <span class="sm-card__badge">Coming soon</span></span>
      <span class="sm-card__desc">A van platform build. Just getting started — check back as the documentation comes together.</span>
      <span class="sm-card__cta">Project home →</span>
    </a>
    <a class="sm-card sm-card--soon" href="jeep_jku/">
      <span class="sm-card__icon">🚙</span>
      <span class="sm-card__title">Jeep Wrangler JKU <span class="sm-card__badge">Coming soon</span></span>
      <span class="sm-card__desc">Early notes and plans. Nothing wired up here yet.</span>
      <span class="sm-card__cta">Project home →</span>
    </a>
  </div>
</section>

<section class="sm-section">
  <h2 class="sm-section__title">How it's built</h2>
  <p class="sm-section__sub">A documentation pipeline more than a website — everything is plain text, version-controlled, and rebuilt automatically.</p>
  <div class="sm-cards sm-cards--features">
    <div class="sm-card sm-card--static">
      <span class="sm-card__icon">📝</span>
      <span class="sm-card__title">Markdown + MkDocs</span>
      <span class="sm-card__desc">Every page is plain Markdown, built into a fast static site (Material / Zensical) and deployed on Cloudflare Pages.</span>
    </div>
    <div class="sm-card sm-card--static">
      <span class="sm-card__icon">📐</span>
      <span class="sm-card__title">draw.io schematics</span>
      <span class="sm-card__desc">Wiring diagrams are drawn in draw.io and auto-exported to crisp PNGs by a GitHub Action — the <code>.drawio</code> files stay the single source of truth.</span>
    </div>
    <div class="sm-card sm-card--static">
      <span class="sm-card__icon">⚙️</span>
      <span class="sm-card__title">CI pipelines</span>
      <span class="sm-card__desc">GitHub Actions keep the diagram exports in sync and verify documentation invariants on every push.</span>
    </div>
    <div class="sm-card sm-card--static">
      <span class="sm-card__icon">🏷️</span>
      <span class="sm-card__title">Issues as the tracker</span>
      <span class="sm-card__desc">Unresolved specs live as GitHub issues and render live into the pages; CI fails the build if a spec is left <code>TBD</code> without one.</span>
    </div>
    <div class="sm-card sm-card--static">
      <span class="sm-card__icon">🖨️</span>
      <span class="sm-card__title">Print &amp; PDF</span>
      <span class="sm-card__desc">A print-site plugin folds an entire manual into one binder-ready, hole-punched layout.</span>
    </div>
    <a class="sm-card" href="https://github.com/sob/shopmanual.io">
      <span class="sm-card__icon">🐙</span>
      <span class="sm-card__title">Open on GitHub</span>
      <span class="sm-card__desc">It's all a public repo, and every page has an “Edit” link straight to its source.</span>
      <span class="sm-card__cta">View the repo →</span>
    </a>
  </div>
  <p class="sm-section__foot">Use the search box up top to jump to any part, wire gauge, or system by name.</p>
</section>
