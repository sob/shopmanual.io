# AUX battery Distribution - Navigation Guide

## What's Here

Documents rear wheel well power distribution from the AUX battery (Dakota Lithium 135Ah LiFePO4).

## Files

### `index.md` - AUX battery Overview

**Contains:** AUX battery terminal connection table, direct load connections

**Use when:** Finding what connects to AUX battery positive terminal

### `01-circuit-breakers.md` - Circuit Breakers

**Contains:** All AUX battery circuit breaker specifications and ratings

**Use when:** Finding circuit breaker size for SwitchPros, BODY PDU, or other loads

### `02-constant-bus.md` - Firewall CONSTANT Bus Bar

**Contains:** Blue Sea 2105 MaxiBus specifications, stud assignments, load distribution at firewall

**Use when:** Finding firewall CONSTANT bus capacity, available studs, or what connects to the bus

Note: AUX battery itself has NO local CONSTANT bus. Battery has 4 stacked terminal lugs + 2 inline CBs (300A master forward feed + 150A SafetyHub local).

### `03-body-pdu.md` - BODY PDU

**Contains:** Body relay/timer/fuse panel specifications and circuit assignments

**Use when:** Finding BODY PDU specifications or fuse assignments

## Cross-Section References

**To SwitchPros (5.2):** SwitchPros power source via circuit breaker

**To BODY PDU loads:** Audio systems (Section 6), cabin circuits

**To BCDC (1.1.3):** BCDC output connection, charging details

**To Grounding (1.5):** AUX battery negative connections, ground reference cable

**To START battery (1.2):** BCDC input circuit breaker

## Navigation Scenarios

**"What circuit breaker protects SwitchPros?"** → `01-circuit-breakers.md`

**"What connects to AUX battery positive terminal?"** → `index.md` terminal table

**"What connects to the CONSTANT bus bar?"** → `02-constant-bus.md` stud assignments

**"What's powered by BODY PDU?"** → `03-body-pdu.md` circuit assignments

**"How does AUX battery get charged?"** → BCDC (1.1.3)

## When Updating

**Adding new AUX battery load:**

1. Determine if direct battery connection or CONSTANT bus connection
2. Update `index.md` terminal table OR `02-constant-bus.md` stud table
3. Add circuit breaker in `01-circuit-breakers.md` if needed
4. Update grounding files (Section 1.5)

**Changing wire gauge or distance for a circuit:**

This page is the **single source of truth** for wire specifications. When updating wire specs, you must also update all pages that reference the circuit:

| Circuit                        | Also Update                                                                  |
| :----------------------------- | :--------------------------------------------------------------------------- |
| BCDC Alpha 50                  | `01-power-generation/03-bcdc.md`, `02-starter-battery-distribution/index.md` |
| Winch (+/-)                    | `08-exterior-systems/01-winch.md`                                            |
| CONSTANT Bus Bar               | `02-constant-bus.md`                                                         |
| SwitchPros                     | `05-control-interfaces/02-switchpros-sp1200.md`                              |
| JL Audio MV800/8i Amp          | `06-audio-systems/index.md`                                                  |
| START Battery Ground Reference | `02-starter-battery-distribution/index.md`                                   |

**Changing BODY PDU circuits:**

1. Update `03-body-pdu.md` circuit table
2. Update affected system docs (Section 6)
