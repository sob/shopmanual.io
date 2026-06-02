# Grounding Architecture - Navigation Guide

## What's Here

Documents ground bus bars for the electrical system. Direct battery ground connections are documented in the respective battery distribution pages.

## Files

### `index.md` - Grounding Overview

**Contains:** Grounding principles, architecture overview, testing procedures

**Use when:** Understanding overall grounding strategy

### `01-engine-bay-ground-bus.md` - Engine Bay Ground Bus

**Contains:** Engine bay ground bus bar specifications and connections

**Use when:** Finding engine bay ground bus connections

### `02-firewall-stud-bus.md` - Firewall Ground Bus

**Contains:** Cabin electronics ground bus bar specifications and connections

**Use when:** Finding firewall/cabin ground bus connections

### `03-switchpros-ground-bus.md` - SwitchPros Ground Bus

**Contains:** Lighting/accessories ground bus bar specifications and connections

**Use when:** Finding SwitchPros ground bus connections

## Cross-Section References

**To Battery Distribution (1.2, 1.3):** Direct battery negative connections documented there

**To Power Generation (1.1):** Alternator, BCDC grounding

**To All Sections:** Ground connection locations for all components

## Navigation Scenarios

**"Where does \[component\] ground?"** → Check appropriate ground file or battery distribution

**"What grounds directly to battery negative?"** → See battery distribution pages (1.2, 1.3)

**"What connects to engine bay ground bus?"** → `01-engine-bay-ground-bus.md`

**"Where are the ground buses located?"** → `index.md` overview

## When Updating

**Adding component with direct battery ground:**

1. Update battery distribution page (1.2 or 1.3)

**Adding component to ground bus:**

1. Update appropriate bus file (01, 02, or 03)
2. Verify bus bar stud availability

**Moving ground connection:**

1. Update old ground location file
2. Update new ground location file
3. Update component's primary documentation
