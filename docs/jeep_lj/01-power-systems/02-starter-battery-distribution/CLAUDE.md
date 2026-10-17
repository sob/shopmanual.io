---
search:
  exclude: true
---

# START battery Distribution - Navigation Guide

## What's Here

Documents START battery power distribution from the driver rear wheel well (Odyssey PC1500).

## Files

### `index.md` - START battery Overview

**Contains:** START battery terminal connection table, direct load connections

**Use when:** Finding what connects to START battery positive terminal

### `01-circuit-breakers.md` - Circuit Protection

**Contains:** START battery-post MRBF terminal fuse specifications (PMU, BCDC input, START+ Forward Distribution Bus master) plus the engine-bay forward-bus load CBs and inline fuses (fan, iBooster, CT4, PBS-I)

**Use when:** Finding the fuse or breaker size for PMU, BCDC, the forward bus, or other loads

Note: Most START loads are protected by MRBF terminal fuses on the battery post or connect direct (ECM, grid heater via integrated fusible link). The radiator fan, iBooster, CT4, and PBS-I sit on a **START+ Forward Distribution Bus** (engine bay), fed by a single master MRBF at the battery post — see `index.md#start-forward-bus` and STANDARDS-EXCEPTIONS.md. TCU is on PMU OUT15.

## Cross-Section References

**To PMU (1.4):** PMU power source via MRBF terminal fuse at the START post - see `01-circuit-breakers.md`

**To BCDC (1.1.3):** BCDC input MRBF terminal fuse specification

**To Grounding (1.5):** START battery negative connections, engine bay ground bus

## Navigation Scenarios

**"What protects the PMU feed?"** → `01-circuit-breakers.md` (MRBF terminal fuse at the START post)

**"What connects to START battery positive terminal?"** → `index.md` terminal table

**"Where does BCDC get power?"** → `01-circuit-breakers.md` (MRBF terminal fuse at START battery+)

**"Where do radios/intercom get power?"** → PMU outputs (Section 1.4) - OUT6 (GMRS), OUT20 (Intercom)

## When Updating

**Adding new START battery load:**

1. Determine if direct battery connection or fuse/CB-protected
2. Update `index.md` terminal table
3. Add the fuse or circuit breaker in `01-circuit-breakers.md` if needed
4. Update grounding files (Section 1.5)

**Changing wire gauge or distance for a circuit:**

This page is the **single source of truth** for wire specifications. When updating wire specs, you must also update all pages that reference the circuit:

| Circuit               | Also Update                                                              |
| :-------------------- | :----------------------------------------------------------------------- |
| Alternator            | `01-power-generation/02-alternator.md`                                   |
| Starter               | `02-engine-systems/01-starter.md`                                        |
| PMU24                 | `04-pmu/01-pmu-overview.md`                                              |
| BCDC Alpha 50         | `01-power-generation/03-bcdc.md`, `03-aux-battery-distribution/index.md` |
| Engine Bay Ground Bus | `05-grounding/01-engine-bay-ground-bus.md`                               |
| Radio Grounds         | `07-communication-systems/index.md`                                      |

**If circuit passes through firewall:** Also update `02-engine-systems/07-firewall-ingress.md`
