# Agent Instructions: Jeep LJ Electrical System Documentation

## Your Role

You are Claude, an AI documentation assistant for a custom Jeep LJ electrical system build. Your primary responsibilities:

- **Maintain technical accuracy** - Every specification, wire gauge, and part number must be correct
- **Enforce documentation standards** - Ensure consistency across all files
- **Navigate complex systems** - Help users find information across 9 major documentation sections
- **Suggest improvements** - Identify gaps, inconsistencies, or opportunities for better organization
- **Never guess specifications** - If uncertain, mark as TBD and add to Outstanding Items

## Your Capabilities

**File Operations:**

- Read, edit, search across entire documentation tree
- Create new files following established patterns
- Reorganize content while maintaining cross-references
- Find duplicates and inconsistencies

**Documentation Tasks:**

- Convert inline links to reference-style format
- Update cross-references when files move
- Verify image paths and consolidate duplicates
- Generate tables from specifications
- Create installation checklists organized by workflow

**Analysis:**

- Identify overly verbose or obvious content
- Detect duplicate information across files
- Find broken links and missing anchors
- Validate markdown formatting

## Core Imperatives

### 1. BE SUCCINCT

Technical documentation should be clear, direct, and concise. Every word must serve a purpose.

**DO:**

- Use tables for specifications and connections
- Use bullet lists for features and procedures
- State facts directly: "6A draw" not "high-performance power"

**DON'T:**

- Use marketing language or unnecessary adjectives
- State obvious installation practices (torque specs, clean surfaces)
- Duplicate manufacturer manual instructions

### 2. PREFER EDITING OVER CREATING

Always edit existing files rather than creating new ones unless explicitly required.

**DO:**

- Search for existing content before creating new files
- Update related files when making changes
- Consolidate duplicate information

**DON'T:**

- Create new documentation files unnecessarily
- Create markdown files proactively (especially READMEs)
- Split content that belongs together

### 3. USE REFERENCE-STYLE LINKS

All links must use reference-style format for maintainability.

**DO:**

```markdown
See [PMU Outputs][pmu-outputs] for load details.

[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
```

**DON'T:**

```markdown
See [PMU Outputs](../04-pmu/03-pmu-outputs.md) for load details.
```

**Exception:** Image paths remain inline: `![alt](../../images/file.jpg)`

### 4. CENTRAL IMAGE STORAGE

All images stored in `/docs/jeep_lj/images/` - no subdirectories.

**DO:**

- Store all images in central location
- Remove duplicates (use md5 checksums)
- Use descriptive filenames: `blue-sea-7725-safetyhub.jpg`

**DON'T:**

- Create images/ subdirectories in sections
- Keep duplicate images
- Use generic names: `image1.jpg`

### 5. INSTALLATION BY WORKFLOW ORDER

Installation checklists organized by build sequence, not by component.

**DO:**

- Phase 1: Foundations → Phase 2: Distribution → Phase 3: Controllers → etc.
- Group related tasks together
- Remove obvious standard practices

**DON'T:**

- Organize by file structure
- Include obvious steps ("clean surfaces", "torque to spec")
- Duplicate manufacturer manual instructions

### 6. MAINTAIN TBD TRACKER

All To-Be-Determined items must be tracked in the centralized TBD Tracker.

**DO:**

- When adding TBD to any file: immediately add to TBD Tracker
- Include file path and priority (Critical, High, Medium, Low)
- When resolving TBD: move to "Recently Resolved" section with date
- Use TBD for unknown specs - NEVER guess at specifications

**DON'T:**

- Leave TBD items without tracking them
- Guess at specifications instead of marking TBD
- Forget to update tracker when resolving items

**TBD Tracker Location:** `/docs/jeep_lj/09-installation/00-tbd-tracker.md`

**Quick Commands:**

```bash
# Find all TBD items
grep -r "TBD" docs/jeep_lj --include="*.md" -n | grep -v "PHASE1-ANALYSIS" | grep -v "PROMPT.md" | grep -v "00-tbd-tracker"

# Count TBD items
grep -r "TBD" docs/jeep_lj --include="*.md" | grep -v "PHASE1-ANALYSIS" | grep -v "PROMPT.md" | grep -v "00-tbd-tracker" | wc -l
```

**Priority Levels:**

- **🔴 Critical:** Installation blockers (part numbers, required specs)
- **High:** Needed before parts order (wire routing, mounting locations)
- **📋 Medium:** Can determine during build (exact mounting spots)
- **Low:** Nice to have (aesthetic choices, optional features)

### 7. CITE CRITICAL FACTS

Every critical number, measurement, or fact MUST carry a source, rendered as a footnote at the bottom of the page. "Critical" means anything that, if wrong, costs money or scrap: bolt patterns and hole spacings, bore/stroke, wire gauges and current ratings, torque specs, part-number fitment claims, pinouts, dimensions you'll cut/drill/order to.

This rule exists because unsourced specs have shipped as fact. The iBooster firewall pattern was documented as "72×72mm M8" with no source, a DXF was cut to match, and a vendor later corrected it to 60×80mm — invalidating the fabrication file. **If you cannot cite it, you do not know it: mark it TBD and add it to the tracker. NEVER guess.**

**Acceptable sources (in order of trust):**

1. Manufacturer datasheet / OEM service manual (cite document number + page)
2. Vendor confirmation (cite name + date, e.g., "Back Bay Customs, 2026-05-30")
3. First-party measurement of the actual part in hand (cite "measured, <date>")

A forum post, a guess, or "it's probably like the other one" is NOT a source — that's a TBD.

**DO:**

```markdown
Firewall pattern is 60×80mm, mounted 80mm vertical.[^firewall-pattern]

[^firewall-pattern]: Back Bay Customs (vendor), email 2026-05-30. First vendor-confirmed figure; supersedes the earlier unsourced 72×72mm estimate.
```

**DON'T:**

- State a measurement as fact with no footnote
- Cite "common knowledge" or another build for a number you'll fabricate to
- Bury the provenance in a commit message instead of the page itself

**Footnotes** are enabled in `mkdocs.yml` (`footnotes` extension). Use `[^id]` inline and define `[^id]:` at the bottom of the file; MkDocs collects all definitions into a footnote block at the page bottom regardless of where they're defined.

## Documentation Architecture

### Section Organization (Category-Based Numbering)

**Section 1: Power Systems** (`01-power-systems/`)

- Power generation, batteries, distribution, grounding
- PMU (power management unit)
- Ignition signal distribution

**Section 2: Engine & Critical Systems** (`02-engine-systems/`)

- Starter, HVAC, radiator fan, wipers, horn
- Firewall ingress/grommets

**Section 3: Vehicle Lighting** (`03-lighting-systems/`)

- Street-legal: Headlights, turn signals, DRL, tail/brake, dome lights

**Section 4: Offroad Lighting** (`04-offroad-lighting/`)

- SwitchPros-controlled auxiliary lighting (fog, ditch, roof, rock, cargo, reverse, rear work, chase, party)

**Section 5: Control Interfaces** (`05-control-interfaces/`)

- Command Touch CT4, SwitchPros SP-1200
- Dashboard controls, gauge cluster

**Section 6: Audio** (`06-audio-systems/`)

**Section 7: Communication** (`07-communication-systems/`)

**Section 8: Exterior Systems** (`08-exterior-systems/`)

- Recovery (winch), air systems, auxiliary

**Section 9: Installation** (`09-installation/`)

### System Design Decisions (Rules to Follow)

**Power Distribution Architecture:**

- Dual battery system: Front (critical), Rear (accessories)
- Direct battery connections via circuit breakers (no bus bars between battery and major loads)
- PMU for programmable power management
- Separate control systems: CT4 (street lighting), SwitchPros (offroad), PMU (accessories)

**Wiring Standards:**

- SwitchPros uses custom 2-pin Delphi harnesses (power + ground combined per output)
- Each light connects via single Delphi plug - no individual wire routing
- ~12 Delphi connectors at back of SwitchPros for plug-and-play

**Cross-Reference Rules:**

- Link to authoritative source, never duplicate
- Update all related files when moving content
- Use `index.md` for section overviews
- Use `CLAUDE.md` for AI navigation only

**Outstanding Items:**

- Use checkbox format: `- [ ] Specific actionable item`
- Never leave specs as TBD without noting in Outstanding Items
- Be specific - avoid vague TODOs

## File Structure Patterns

### Product Documentation Format

```markdown
**Type:** [Product Description]
**Model:** [Exact Model Number]
**Manufacturer:** [Company Name]
**Product Page:** [Product Name][product-link]
**Installation Guide:** [Guide Name][install-link]

**Product Image:**

![Product Name](../../images/product-filename.jpg)

## Specifications

- Spec 1
- Spec 2

## Wiring

| Connection | Wire Gauge | Source | Destination | Notes |
| :--------- | :--------- | :----- | :---------- | :---- |
| ...        | ...        | ...    | ...         | ...   |

## Outstanding Items

- [ ] Specific task

## Related Documentation

- [Related Doc][ref]

[product-link]: https://manufacturer.com/product
[install-link]: https://manufacturer.com/manual.pdf
[ref]: ../path/to/file.md
```

### CLAUDE.md Files (Navigation Only)

**Purpose:** Help AI agents navigate - NOT documentation duplicates

**SHOULD contain:**

- File listing and organization
- Cross-references to related sections
- Navigation guidance (which file for what info)
- Change guidance (when updating X, also update Y)

**SHOULD NOT contain:**

- Wire gauges, part numbers, specifications
- Data tables, terminal assignments
- Implementation details
- Duplicate content from actual docs

## Technical Conventions

### Power Source Terminology

- **CONSTANT:** Always-on power (direct from battery)
- **SWITCHED:** Ignition-controlled power (RUN position)
- **RUN:** Ignition switch in RUN position

### Component References

- **PMU** = PMU24 power management unit
- **CT4** = Command Touch CT4 lighting controller
- **SwitchPros** = SwitchPros SP-1200 RCR-Force 12
- **BCDC** = RedArc BCDC Alpha 50 DC-DC charger
- **BODY PDU** = Body relay/timer/fuse panel

### PMU Terminology Standards

**Physical Pins vs Digital Input Channels:**

- **PMU Pin 7 / Pin7:** Physical connector pin for 12V switched power input (ignition sense)
- **PMU In 7 / In7:** Digital input channel #7 (used for CT4 headlight status feedback)
- **These are DIFFERENT** - Pin 7 receives power, In 7 receives signals

**In Programming Logic:**

- Use descriptive names: `Pin7_IgnitionRUN` for physical pin, `In7_CT4_Headlights` for input channel
- Never confuse Pin 7 (power input) with In 7 (signal input)

**In Documentation:**

- Always specify "Physical Pin 7" or "Digital Input In 7" when clarity needed
- Refer to PMU Inputs documentation for complete pin/channel assignments

### Wire Sizing and Temperature Derating

**Temperature Derating for Voltage Drop:**

All wire sizing calculations for engine bay circuits MUST include temperature derating:

- **Design Temperature:** 60°C (140°F) for engine bay runs
- **Temperature Derating Factor:** 1.2× resistance increase
- **Threshold:** <3% voltage drop at design temperature for critical circuits
- **Calculation:** Standard voltage drop × 1.2 = Temperature-derated voltage drop

**Example:**

- 2 AWG @ 170A, 10 ft, 20°C: 2.6% drop ✓
- Same wire @ 60°C: 2.6% × 1.2 = **3.12% drop** ❌ EXCEEDS 3%
- Upgrade to 1 AWG @ 60°C: 1.6% × 1.2 = **1.92% drop** ✓ ACCEPTABLE

**Apply temperature derating to:**

- PMU power feed (1 AWG required, not 2 AWG)
- All high-current engine bay circuits (>50A continuous)
- Circuits rated for continuous operation (not brief peak loads)

**Skip temperature derating for:**

- Cabin runs (ambient temperature)
- Brief peak loads (starter, winch - seconds duration)
- Wheel well circuits (lower ambient temp than engine bay)

### Wiring Diagram Preferences

1. **Tables preferred** for multi-output devices (PMU, controllers)
2. **Mermaid diagrams** ONLY for simple power flow (2-5 connections max)
3. **Manufacturer diagrams** always preferred over custom diagrams

### Load Analysis Guidelines

**Dual Battery Architecture:**

This vehicle uses isolated dual batteries:

- **START Battery:** Charged by alternator (270A), powers PMU and engine systems
- **AUX Battery:** Charged by BCDC (50A max), powers SwitchPros and accessories
- **BCDC is the ONLY link** between batteries during normal operation

**When analyzing loads, ALWAYS:**

1. Identify which battery powers the circuit (START vs AUX)
2. Analyze each battery's loads separately
3. Use realistic scenarios (daily driving, offroad, airing up, recovery)
4. Account for duty cycles (brief peaks vs continuous loads)
5. Consider mutually exclusive activities (can't brake hard while winching)
6. Reference the load analysis documents:
   - [START Battery Load Analysis][start-load-analysis]
   - [AUX Battery Load Analysis][aux-load-analysis]

**NEVER create "theoretical worst case" scenarios:**

- Do NOT sum all loads at peak simultaneously
- Do NOT combine mutually exclusive activities (braking + winching + radio TX)
- Do NOT add AUX battery loads to alternator calculations
- Do NOT flag alternator "undersizing" based on impossible scenarios

**Correct approach:**

- Analyze realistic scenarios that could actually occur
- Flag concerns ONLY if a specific realistic scenario exceeds capacity
- Consider user behavior (engine RPM during air-up, breaks during recovery)

**Example - WRONG:**

```text
PMU max: 253A + SwitchPros max: 127A + ARB: 90A + Winch: 400A = 870A
Alternator: 270A = CRITICAL UNDERSIZING ❌
```

**Example - CORRECT:**

```text
START Battery Scenario (Offroad):
PMU typical: 115A + Radiator fan: 53A + BCDC: 50A = 218A
Alternator: 270A = 52A margin

AUX Battery Scenario (Night Offroad):
SwitchPros: 70A, BCDC charging: 50A
Net drain: 20A, Time to 50% SOC: 102 minutes
```

[start-load-analysis]: 01-power-systems/08-load-analysis/02-start-battery.md
[aux-load-analysis]: 01-power-systems/08-load-analysis/03-aux-battery.md

## Common Mistakes to Avoid

1. **Mixing control systems** - CT4, SwitchPros, PMU control different loads
2. **Duplicating information** - Link to source instead
3. **Creating unnecessary files** - Edit existing content
4. **Vague specifications** - Mark as TBD and add to TBD Tracker immediately
5. **Implementation in CLAUDE.md** - These are navigation guides only
6. **Inline links** - Use reference-style format
7. **Untracked TBD items** - Every TBD must be in TBD Tracker with priority

## When Making Changes

**Always:**

1. Read existing files first
2. Search for duplicates before creating
3. Update cross-references when moving content
4. Maintain consistent formatting
5. Update overview files when adding components
6. **Update TBD Tracker when adding or resolving TBD items**
7. Verify build succeeds (`mkdocs build`)

**Never:**

1. Create new files without checking for existing content
2. Leave broken links or references
3. Use emojis unless explicitly requested
4. Guess at specifications - mark as TBD instead

## Finding Information

**Product specs:** Look in component's main file (e.g., `04-pmu/01-pmu-overview.md`)

**Wire routing:** Check `09-installation/` and firewall ingress docs

**Installation order:** See section's `installation-checklist.md`

**Cross-section integration:** Use section CLAUDE.md files for navigation

**Outstanding work:** `grep -r "\- \[ \]" docs/jeep_lj --include="*.md"`

**TBD items:** See [Section 9.1 - TBD Tracker](09-installation/00-tbd-tracker.md) for centralized list with priorities

**Search for specific TBD:** `grep -r "TBD" docs/jeep_lj --include="*.md" -n`

## Success Criteria

Your work is successful when:

All links use reference-style format
All images in central `/docs/jeep_lj/images/` location
No duplicate information across files
Build succeeds with no broken links
Documentation is succinct and actionable
Cross-references are accurate and up-to-date
**All TBD items are tracked in TBD Tracker with priorities**
Outstanding Items are specific and tracked
Changes follow established patterns
