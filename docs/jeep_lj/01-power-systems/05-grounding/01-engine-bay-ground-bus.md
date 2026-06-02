---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - grounding
  - bus-bar
---

# 1.5.3 Engine Bay Ground Bus {#engine-bay-ground-bus}

/// html | div.product-info
![Blue Sea 2107 PowerBar](../../images/blue-sea-2107-powerbar.jpg){ loading=lazy }

**Type:** High-Current Ground Distribution Bus Bar

**Model:** Blue Sea 2107 PowerBar - 600A BusBar

**Manufacturer:** Blue Sea Systems

**Product Page:** [Blue Sea 2107 PowerBar][bluesea-2107]

**Installation Manual:** [Blue Sea BusBar Installation Guide][bluesea-busbar-guide]

///

## Specifications

- **Capacity:** 600A continuous
- **Terminals:** 8x 3/8"-16 studs
- **Location:** Firewall (engine bay side), near PMU
- **Full Specs:** [Blue Sea 2107][bluesea-2107]

## Stud Assignment

| Stud | Connection                      | Wire Gauge  | Current   | Notes                                                  |
| :--- | :------------------------------ | :---------- | :-------- | :----------------------------------------------------- |
| 1    | START battery-                  | 2/0 AWG     | 600A+     | See [START Battery Distribution][front-battery-ground] |
| 2    | Engine block ground             | 2/0 AWG     | 600A+     | Starter/alternator return path                         |
| 3    | Front frame rail (main chassis) | 2/0 AWG     | 600A+     | Primary infrastructure ground                          |
| 4    | AUX battery reference           | 1/0 AWG     | 75A       | See [START Battery Distribution][front-battery-ground] |
| 5    | PMU ground reference (Pin 25)   | Per harness | <100mA    | Logic/CAN reference only                               |
| 6    | Horn + relay coil grounds       | 14-18 AWG   | ~10A      | Horn (5.4A), starter solenoid coil                     |
| 7    | iBooster (OUT1+10, OUT19)       | 10 AWG      | ~45A peak | Brake booster main + ignition signal                   |
| 8    | Aux cooling fans (OUT7+8)       | 12 AWG      | ~30A      | Oil cooler + PS cooler fans                            |

**Utilization:** 8 of 8 studs used (0 available)

**Direct Battery Connections:** ECM, grid heater, radios, winch, and BCDC connect directly to battery negative - see [START battery Ground][front-battery-ground] and [AUX battery Ground][rear-battery-ground]

## Installation

**Mounting:** Firewall (engine bay side) near PMU

**Torque:** 140 in-lb (3/8"-16 studs)[^bus-torque]

[^bus-torque]: Blue Sea Systems' published terminal torque for the 2107 PowerBar's **3/8"-16 studs is 140 in-lb**. Corrected from the earlier 100-120 in-lb (that 120 in-lb figure is Blue Sea's spec for 5/16"-18 studs — a smaller stud — so the original value undertorqued these 3/8"-16 studs). Source: [Blue Sea Systems 2107 PowerBar 600A BusBar](https://www.bluesea.com/products/2107/PowerBar_600A_BusBar_-_Eight_3_8in-16_Studs__). Verified 2026-05-30.

**Critical:** Clean metal-to-metal connections - remove paint/rust before installation, apply dielectric grease after assembly

## Related Documentation

- [Grounding Architecture Overview][grounding-architecture]
- [START battery Ground][front-battery-ground]
- [AUX battery Ground][rear-battery-ground]
- [START battery Distribution][starter-battery-distribution]

[grounding-architecture]: index.md
[front-battery-ground]: ../02-starter-battery-distribution/index.md
[rear-battery-ground]: ../03-aux-battery-distribution/index.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[bluesea-2107]: https://www.bluesea.com/products/2107/PowerBar_-_600A_BusBar_-_Eight_3_8in-16_Studs
[bluesea-busbar-guide]: https://www.bluesea.com/resources/108
