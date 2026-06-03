---
description: Perform comprehensive electrical engineering analysis of a documentation section
argument-hint: <section-path>
---

# Electrical System Analysis

Analyze the Jeep LJ dual battery electrical system documentation as a senior electrical engineer specializing in low-voltage DC power systems for automotive and off-road applications.

## Argument Validation

**Section to analyze:** `$ARGUMENTS`

If `$ARGUMENTS` is empty or not provided:
1. List available sections in `docs/jeep_lj/`
2. Ask the user which section to analyze
3. Do not proceed until a valid section is specified

If the path doesn't exist, report the error and list valid sections.

## Task Overview

1. **Context gathering** - If analyzing any section other than `01-power-systems`, first read these files for system context:
   - `docs/jeep_lj/01-power-systems/index.md`
   - `docs/jeep_lj/01-power-systems/01-architecture/index.md`
   - `docs/jeep_lj/01-power-systems/04-pmu/01-output-configuration.md`

2. **Section analysis** - Review every `.md` file in `docs/jeep_lj/$ARGUMENTS/`

3. **Cross-references** - Follow links to other sections only when:
   - A specification references another component (verify compatibility)
   - A wire run connects to components in another section
   - Limit cross-reference depth to 1 level (don't follow links from linked files)

## Specialized Roles

Deploy these specialized subagents for focused analysis. Run in parallel where possible.

### Wire Specialist

**Trigger:** Any section with wiring tables or circuit specifications

**Focus:**
- Verify wire gauge calculations for every circuit (load × distance × derating)
- Calculate voltage drop and compare against thresholds
- Check temperature derating is applied correctly for wire location
- Verify wire ampacity exceeds protected circuit rating
- Flag any gauge specified without supporting calculation

**SAE J1128 Reference Data:**
| AWG | Ampacity @30°C | Ampacity @80°C (engine bay) |
|-----|----------------|------------------------------|
| 18  | 16A            | 10A                          |
| 16  | 22A            | 14A                          |
| 14  | 32A            | 20A                          |
| 12  | 41A            | 26A                          |
| 10  | 55A            | 35A                          |
| 8   | 73A            | 46A                          |
| 6   | 101A           | 64A                          |
| 4   | 135A           | 85A                          |
| 2   | 181A           | 114A                         |

**Output:** List of circuits with pass/fail status and calculations shown for any failures.

---

### Integration Checker

**Trigger:** Any section that references components in other sections

**Focus:**
- Cross-check voltage ranges between connected components
- Verify charging profiles match battery chemistry (LiFePO4 vs AGM vs lead-acid)
- Validate PMU output ratings against actual connected loads
- Check CAN bus device addresses for conflicts
- Verify ground reference compatibility between systems
- Confirm fuse/breaker ratings coordinate (upstream clears before downstream)

**Required Cross-References:**
- Battery specs → charger profiles
- PMU outputs → load requirements
- Alternator output → charge controller input limits
- Solar controller → battery charging parameters

**Output:** Compatibility matrix showing verified connections and any conflicts found.

---

### Environmental Reviewer

**Trigger:** All sections (off-road durability is always relevant)

**Focus:**
- Verify IP ratings for connection locations (IP67+ for exposed areas)
- Check wire routing avoids heat sources (exhaust, headers) with adequate clearance
- Confirm securing intervals in high-vibration zones (12-18" max)
- Validate physical protection (loom, conduit, grommets) for abrasion-prone routes
- Assess serviceability - can connections be accessed for trail repairs?
- Check thermal environment matches derating applied

**Location Categories:**
| Location | IP Required | Temp Derating | Vibration Level |
|----------|-------------|---------------|-----------------|
| Engine bay | IP67 | 60-80°C | High |
| Wheel wells | IP67 | 20-50°C | Extreme |
| Under vehicle | IP67 | 40°C | High |
| Cabin/dash | IP40 | 40°C | Low |
| Trunk/cargo | IP40 | 40°C | Medium |

**Output:** Location-by-location assessment with pass/fail for each environmental factor.

---

## Subagent Coordination

**When to deploy specialists:**
- **Always run Environmental Reviewer** - applies to every section
- **Run Wire Specialist** when section contains wiring tables or circuit specs
- **Run Integration Checker** when section references external components

**Parallel execution:** Launch all applicable specialists simultaneously. Each returns findings in standard severity format.

**Consolidation:** Main analysis aggregates specialist findings, deduplicates, and assigns final severity ratings.

Each subagent should return findings in the standard severity format (see Issue Severity below).

## Evaluation Standards

**Primary Standards:**
- **SAE J1128:** Wire sizing, voltage drop limits, temperature derating
- **Off-Road Best Practices:** Wire protection, vibration resistance, water ingress prevention

**Reference Standards (apply selectively):**
- **ABYC E-11:** Dual battery systems, grounding architecture only
- **NEC Article 625:** Where automotive standards don't specify

**Quantified Requirements:**

| Parameter | Threshold |
|-----------|-----------|
| Voltage drop (critical loads) | < 3% |
| Voltage drop (accessories) | < 10% |
| Fuse/CB sizing | 125-160% of max continuous load |
| Wire securing interval | Every 12-18 inches in high-vibration areas |
| Water exposure connections | IP67 minimum |
| Engine bay temperature derating | 60-80°C |
| Cabin temperature derating | 40°C |
| Wheel well temperature derating | 20-50°C |

## Evaluation Checklist

Check in this order (safety-critical first):

### 1. Safety & Protection
- [ ] Overcurrent protection on all continuous-duty circuits (125-160% of load)
- [ ] High-current paths protected from short circuits
- [ ] No fire hazards (undersized wiring, improper routing near heat)
- [ ] Connections in exposed areas sealed to IP67+
- [ ] Wires secured every 12-18" in high-vibration areas
- [ ] Grounding architecture has proper fault current return paths

### 2. Technical Accuracy
- [ ] Wire gauge correct for load and distance (show calculation if wrong)
- [ ] Voltage drop within limits (< 3% critical, < 10% accessory)
- [ ] Temperature derating applied for location
- [ ] All TBD items flagged in documentation

### 3. System Compatibility
- [ ] Component voltage ranges compatible
- [ ] Charging profiles match battery chemistry
- [ ] PMU output ratings sufficient for connected loads
- [ ] No CAN bus conflicts

### 4. Documentation Quality
- [ ] Missing specifications marked as TBD
- [ ] Wire routing paths specified
- [ ] Connection types and locations documented

## Issue Severity Definitions

| Severity | Definition | Examples |
|----------|------------|----------|
| **CRITICAL** | Safety hazard, fire risk, or will cause immediate damage. Must fix before installation. | Undersized wire on high-current circuit; missing fuse on continuous load; exposed connection in water path |
| **ERROR** | Will cause malfunction or premature failure. Must fix before operation. | Wrong voltage drop calculation; incompatible charging profile; incorrect ground reference |
| **WARNING** | Potential problem or suboptimal design. Should fix. | Missing wire routing spec; connection accessibility concern; borderline wire sizing |
| **INFO** | Best practice recommendation or documentation improvement. Nice to have. | Alternative component suggestion; additional testing procedure; clarification needed |

## Output Format

Generate timestamp: `YYYYMMDD-HHMMSS` (e.g., `20251124-143052`)

### Analysis File: `docs/ANALYZE/ANALYSIS-{timestamp}.md`

```markdown
# Electrical Analysis: {section-name}

**Generated:** {timestamp}
**Section:** `$ARGUMENTS`
**Files analyzed:** {count}

## Summary

- Critical: {count}
- Errors: {count}
- Warnings: {count}
- Info: {count}

## Context Documents Reviewed

- [List files read for context]

## Analysis by Subsection

### {subsection-name}

**File:** `path/to/file.md`

#### Findings

[Detailed findings organized by severity]

#### Calculations Verified

[Show any wire gauge or voltage drop calculations checked]

---

[Repeat for each subsection]

## Cross-Reference Verification

[Any compatibility issues found when checking linked components]
```

### Issues File: `docs/ANALYZE/ISSUES-{timestamp}.md`

```markdown
# Issues: {section-name}

**Generated:** {timestamp}
**Section:** `$ARGUMENTS`

## Summary

| Severity | Count |
|----------|-------|
| CRITICAL | {n} |
| ERROR | {n} |
| WARNING | {n} |
| INFO | {n} |

## Issues

| ID | Severity | File | Line | Description | Recommendation |
|----|----------|------|------|-------------|----------------|
| 001 | CRITICAL | path/file.md | 45 | Description | Fix recommendation |
| 002 | ERROR | path/file.md | 102 | Description | Fix recommendation |

## Untracked TBDs

TBDs found in analyzed files that do **not** have a matching open `tbd` GitHub issue (the tracker at `docs/jeep_lj/tbd-tracker.md` renders those issues).

| File | Line | TBD Item | Action |
|------|------|----------|--------|
| path/file.md | 23 | Description of TBD | Add to tracker |

**Note:** Compare each Outstanding Item found against the TBD tracker. Only list items that are missing from the tracker. If all TBDs are tracked, state "All TBDs are tracked in central tracker."
```

## Completion Criteria

Analysis is complete when:

1. All `.md` files in the section have been reviewed
2. All checklist items have been evaluated
3. All findings are categorized by severity
4. Both output files are written
5. Summary counts match detailed findings

Report completion status and file locations when done.
