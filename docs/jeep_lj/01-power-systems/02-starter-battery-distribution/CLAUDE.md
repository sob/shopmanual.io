# START battery Distribution - Navigation Guide

## What's Here

Documents START battery power distribution from the driver rear wheel well (Odyssey PC1500).

## Files

### `index.md` - START battery Overview

**Contains:** START battery terminal connection table, direct load connections

**Use when:** Finding what connects to START battery positive terminal

### `01-circuit-breakers.md` - Circuit Breakers

**Contains:** All START battery circuit breaker specifications and ratings (250A → PMU, 80A → BCDC input)

**Use when:** Finding circuit breaker size for PMU, BCDC, or other loads

Note: The START battery has no CONSTANT bus. All loads connect via inline CBs at the battery (within 7" per code) or direct (ECM, grid heater via integrated fusible link).

## Cross-Section References

**To PMU (1.4):** PMU power source via 250A inline circuit breaker - see `01-circuit-breakers.md`

**To BCDC (1.1.3):** BCDC input circuit breaker specifications (80A inline)

**To Grounding (1.5):** START battery negative connections, engine bay ground bus

## Navigation Scenarios

**"What circuit breaker protects the PMU?"** → `01-circuit-breakers.md` (250A inline CB at battery)

**"What connects to START battery positive terminal?"** → `index.md` terminal table

**"Where does BCDC get power?"** → `01-circuit-breakers.md` (80A inline CB at START battery+)

**"Where do radios/intercom get power?"** → PMU outputs (Section 1.4) - OUT6 (GMRS), OUT20 (Intercom)

## When Updating

**Adding new START battery load:**

1. Determine if direct battery connection or CB-protected
2. Update `index.md` terminal table
3. Add circuit breaker in `01-circuit-breakers.md` if needed
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
