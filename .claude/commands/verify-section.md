---
description: Audit a documentation section for quality and consistency
argument-hint: <section-path>
---

# Verify Documentation Section

Audit and fix the specified documentation section for quality and consistency issues.

**Section path:** $ARGUMENTS (e.g., `01-power-systems` or `01-power-systems/04-pmu`)

## Checks to Perform and Fix

### 1. Content Quality
- **Duplicate content** - Remove repeated tables, specs, or text; link to authoritative source
- **Broken links** - Fix or remove broken reference-style links
- **Inline links** - Convert to reference-style format per CLAUDE.md
- **TBD tracking** - Open a `tbd` GitHub issue (labels: tbd, project/*, priority/*, area/*) for any untracked TBD; run `/verify-tbd` to reconcile
- **Outstanding items** - Make checkbox items specific and actionable, or mark "None - design complete"
- **Image paths** - Fix paths to point to `docs/jeep_lj/images/`

### 2. Missing Required Information
- **Product pages must have:** Type, Manufacturer, Model/Part Number, Power Source, Mounting location
- **Wiring tables must have:** Wire Gauge column with actual values (not just in Notes)
- **All pages must have:** Outstanding Items section, Related Documentation section
- **Flag as TBD:** Any missing specs that cannot be determined from context

### 3. Verbose Content (Remove or Condense)
- **Obvious installation steps** - Remove "torque to spec", "clean surfaces", "use proper tools"
- **Marketing language** - Remove superlatives like "high-performance", "premium quality"
- **Redundant explanations** - Don't explain what a component does if it's obvious from context
- **Duplicate manufacturer manual content** - Link to manual instead of reproducing
- **Excessive ASCII diagrams** - Replace with simple bullet lists or tables where clearer
- **Repetitive safety warnings** - One warning per hazard type, not repeated in every section

### 4. Product Page Format (for files with product specs)

**Required Structure:**
```markdown
---
hide:
  - toc
tags:
  - product-details
  - [section-tag]
  - [component-tag]
---

# Section.Subsection Component Name {#anchor}

/// html | div.product-info
![Product Image](../../images/product-image.jpg){ loading=lazy }

**Type:** [Product type/description]

**Model:** [Model number]

**Part Number:** [Part number if applicable]

**Manufacturer:** [Company name]

**Product Page:** [Product Name][product-link]

**Mounting:** [Installation location]

**Power Source:** [Power connection details]

[Additional specs as needed...]

///

## [Content sections...]

## Outstanding Items

[Checkbox items or "None - design complete. See [installation checklist][install-checklist] for build tasks."]

## Related Documentation

- [Related Doc][ref-link]

[product-link]: https://...
[ref-link]: ../path/to/file.md
```

**Fix these issues:**
- Add `product-details` tag if missing
- Wrap product specs in `/// html | div.product-info` block
- Move image inside product-info block (for right alignment)
- Add `{ loading=lazy }` to images
- Add missing standard fields: Type, Model/Part Number, Manufacturer, Product Page, Mounting, Power Source
- Add Outstanding Items section if missing
- Add Related Documentation section if missing
- Convert inline links to reference-style

### 5. Section Index Pages (index.md)

**Fix these issues:**
- Add overview paragraph if missing
- Add links to all subsection files
- Remove duplicate content (replace with links)

### 6. Wiring/Connection Tables

**Standard format:**
```markdown
| Circuit | Source | Destination | Wire Gauge | Current | Notes |
|:--------|:-------|:------------|:-----------|:--------|:------|
```

**Fix these issues:**
- Reorder columns to match standard
- Add Wire Gauge column if missing
- Add Current/load values if known

## Execution

1. Find all .md files in the section (excluding CLAUDE.md)
2. For each file, check against standards above
3. **Fix issues directly** - edit files to match standards
4. Update TBD tracker if new TBD items found
5. Summarize changes made at the end
