---
search:
  exclude: true
---

# PMU24 - Navigation Guide

## What's Here

Documents ECUMaster PMU24 programmable power management unit configuration and assignments.

## Files

### `index.md` - PMU Navigation Hub

**Contains:** Links to all PMU documentation

**Use when:** Starting point for PMU-related information

### `01-pmu-overview.md` - PMU Overview

**Contains:** Product specifications, features, mounting location

**Use when:** Finding PMU specs, capacity, or physical installation details

### `02-pmu-outputs.md` - PMU Outputs

**Contains:** Complete output assignment table for all 24 outputs

**Use when:** Finding what load is assigned to which output

### `03-pmu-inputs.md` - PMU Inputs

**Contains:** Digital/analog input assignments, CAN bus integration

**Use when:** Finding input configuration or CAN bus details

### `04-pmu-programming.md` - PMU Programming

**Contains:** Logic examples and configuration software details

**Use when:** Understanding PMU logic or configuration process

## Cross-Section References

**To START battery (1.2):** PMU power source via circuit breaker

**To Engine Systems (2):** Radiator fan, HVAC blower, starter relay, wipers, horn

**To Lighting (3):** DRL, brake lights, reverse lights

**To Control Interfaces (4):** Dakota Digital cluster, Command Touch CT4 power

**To Grounding (1.5):** PMU ground connection

## Navigation Scenarios

**"What's connected to PMU OUT14?"** → `02-pmu-outputs.md` output table

**"How does PMU connect to J1939 CAN bus?"** → `03-pmu-inputs.md`

**"What's the DRL auto-off logic?"** → `04-pmu-programming.md`

**"Where does PMU get power?"** → START battery (1.2) circuit breakers

**"What inputs does PMU use?"** → `03-pmu-inputs.md`

## When Updating

**Changing output assignment:**

1. Update `02-pmu-outputs.md` output table
2. Update affected system docs (Sections 2, 3, 4)
3. Verify total load capacity

**Adding new input:**

1. Update `03-pmu-inputs.md` input table
2. Update programming logic in `04-pmu-programming.md` if needed

**Adding logic example:**

1. Update `04-pmu-programming.md` only
2. Reference existing input/output assignments
