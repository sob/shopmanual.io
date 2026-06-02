---
hide:
  - toc
---

# 1.2 START battery Distribution (Driver Rear Wheel Well) {#starter-battery-distribution}

/// html | div.product-info
![Odyssey PC1500 Battery Terminals](../../images/odyssey-pc1500.jpg){ loading=lazy }
///

## Overview

The START battery (driver rear wheel well) provides power for critical engine and safety systems:

1. **Direct high-current** → Starter (no CB), alternator charging input (no CB)
2. **Circuit breaker protected** → PMU (250A CB), BCDC (80A CB)
3. **Direct low-current** → ECM, grid heater (fusible link protection)

See [Circuit Breakers][circuit-breakers] for complete CB specifications. All CBs mounted in rear wheel well within 7" of battery (code compliant).

!!! info "Single Source of Truth"
This page is the authoritative source for all START battery wire specs (gauge, distance, voltage drop). Component pages reference here. For battery specs see [Section 1.1][batteries]. For ground bus bars see [Section 1.5][grounding].

## START battery Positive Terminal (6 connections)

| Circuit                    | Destination          | Wire Gauge  | Distance | Current  | Voltage Drop    | Protection   |
| :------------------------- | :------------------- | :---------- | :------- | :------- | :-------------- | :----------- |
| [Alternator][alternator]   | Engine bay           | 2/0 AWG     | 8 ft     | 270A     | 2.81% @ 60°C    | None         |
| [Starter][starter]         | Engine bay           | 2/0 AWG     | 6 ft     | 400-600A | 1.9-3.9% @ 20°C | None         |
| [PMU24][pmu]               | Engine bay           | 2/0 AWG     | ~7 ft    | 250A max | 2.4% @ 60°C     | 250A CB      |
| ECM                        | Engine bay           | Per Cummins | Short    | <5A      | Negligible      | Fusible link |
| [Grid Heater][grid-heater] | Engine bay           | Per Cummins | Short    | ~80A     | Negligible      | Fusible link |
| [BCDC Alpha 50][bcdc]      | Passenger rear wheel well | 4 AWG       | ~6 ft    | 50A      | 0.94% @ 20°C    | 80A CB       |

All circuit breakers mounted within 7" of battery (ABYC/NEC compliant). See [Circuit Breakers][circuit-breakers].

## START battery Negative Terminal (7 connections)

| Circuit                                    | Destination          | Wire Gauge  | Distance | Current    | Voltage Drop  |
| :----------------------------------------- | :------------------- | :---------- | :------- | :--------- | :------------ |
| [Engine Bay Ground Bus][engine-ground-bus] | Engine bay           | 2/0 AWG     | ~8 ft    | 600A+ peak | <0.1V @ 60°C  |
| ECM                                        | Engine bay           | 12 AWG      | Short    | <5A        | Negligible    |
| [Grid Heater][grid-heater]                 | Engine bay           | Per Cummins | Short    | ~80A       | Negligible    |
| [AUX Battery][aux-battery]                 | Passenger rear wheel well | 1/0 AWG     | 5-6 ft   | 75A max    | <0.05V @ 20°C |
| [G1 GMRS Radio][radios]                    | Dashboard            | 10 AWG      | ~8 ft    | 15A TX     | 1.2% @ 20°C   |
| [STX Intercom][radios]                     | Dashboard            | 10 AWG      | ~8 ft    | 5A         | 0.4% @ 20°C   |

Radio grounds direct to battery for RF noise isolation. ECM/grid heater via Cummins harness to isolate from starter spikes.

## Related Documentation

- [Power Generation][power-gen] - Battery and alternator specifications
- [Circuit Breakers][circuit-breakers] - Complete CB specifications
- [Grounding Architecture][grounding] - Ground bus bars
- [PMU24][pmu] - Power management unit
- [BCDC Alpha 50][bcdc] - DC-DC charger to AUX battery
- [Starter System][starter] - Starter specifications
- [Alternator][alternator] - Charging system
- [AUX battery Distribution][aux-battery] - Aux/accessory battery system

[pmu]: ../04-pmu/index.md
[bcdc]: ../01-power-generation/03-bcdc.md
[batteries]: ../01-power-generation/01-batteries.md
[grid-heater]: ../../02-engine-systems/07-grid-heater.md
[grounding]: ../05-grounding/index.md
[engine-ground-bus]: ../05-grounding/01-engine-bay-ground-bus.md
[power-gen]: ../01-power-generation/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[starter]: ../../02-engine-systems/01-starter.md
[alternator]: ../01-power-generation/02-alternator.md
[radios]: ../../07-communication-systems/index.md
[circuit-breakers]: 01-circuit-breakers.md
