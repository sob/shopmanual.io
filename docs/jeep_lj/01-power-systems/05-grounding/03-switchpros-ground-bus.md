---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - grounding
  - bus-bar
---

# 1.5.5 SwitchPros Ground Bus {#switchpros-ground-bus}

/// html | div.product-info
![Blue Sea 2105 MaxiBus](../../images/blue-sea-2105-maxibus.jpg){ loading=lazy }

**Type:** Low-Current Ground Distribution Bus Bar

**Model:** Blue Sea 2105 MaxiBus

**Manufacturer:** Blue Sea Systems

**Product Page:** [Blue Sea 2105 MaxiBus][bluesea-2105]

///

## Specifications

- **Capacity:** 250A AC/DC continuous, 300V AC / 48V DC max
- **Terminals:** 12x #10-24 screws, 2x 5/16"-18 studs
- **Location:** Firewall (passenger cabin side), co-located with SwitchPros power module
- **Full Specs:** [Blue Sea 2105][bluesea-2105]

## Stud/Terminal Assignment

| Stud/Terminal           | Connection                        | Wire Gauge    | Distance     | Max Current     | Notes                                  |
| :---------------------- | :-------------------------------- | :------------ | :----------- | :-------------- | :------------------------------------- |
| **Stud 1 (5/16")**      | **Chassis Ground (INPUT)**        | **1/0 AWG ✓** | **Variable** | **~100A total** | **Primary bus ground - to frame rail** |
| Stud 2 (5/16")          | **\[Available\]**                   | -             | -            | -               | Future high-current ground             |
| Terminal 1 (#10-24)     | SwitchPros controller             | 14 AWG ✓      | ~2 ft        | <1A             | Controller logic ground (via harness)  |
| Terminal 2 (#10-24)     | Headlights (LP6) - pair 1         | 16 AWG ✓      | ~10 ft       | ~8A             | See [Headlights][headlights]           |
| Terminal 3 (#10-24)     | Headlights (LP6) - pair 2         | 16 AWG ✓      | ~10 ft       | ~8A             | See [Headlights][headlights]           |
| Terminal 4 (#10-24)     | Tail/brake/reverse (PMU OUT21+22) | 16 AWG ✓      | ~12 ft       | ~6A             | Integrated unit, single ground wire    |
| Terminal 5 (#10-24)     | DRL/Parking (PMU OUT14)           | 16 AWG ✓      | ~10 ft       | ~8A             | Front marker/DRL lights                |
| Terminal 6 (#10-24)     | Roof lights (8x XL Sport)         | 14 AWG ✓      | ~8 ft        | ~18A            | Single circuit via XL Linkable harness |
| Terminal 7 (#10-24)     | Ditch lights                      | 16 AWG ✓      | ~8 ft        | ~8A             | Auxiliary lighting                     |
| Terminal 8 (#10-24)     | Rock lights                       | 16 AWG ✓      | ~6 ft        | ~5A             | Auxiliary lighting                     |
| Terminals 9-12 (#10-24) | **\[Available\]**                   | -             | -            | -               | Future expansion (4 terminals)         |

**Utilization:** 9 of 14 used (1 stud + 8 terminals used, 1 stud + 4 terminals available)

**Purpose:** Lighting ground return for all SwitchPros-controlled loads

## Installation

**Mounting:** Firewall (cabin side, passenger area), bolted near SwitchPros power module so all load returns terminate locally

**Ground Path:** Bus → chassis ground (1/0 AWG, handles ~100A total lighting load) at firewall chassis point → main grounding network

**Critical:** Clean metal-to-metal connection to chassis at firewall, accessible for lighting ground wires

## Related Documentation

- [Grounding Architecture Overview][grounding-architecture]
- [Engine Bay Ground Bus][engine-bay-ground-bus]
- [SwitchPros SP-1200][switchpros-sp1200]
- [Offroad Lighting][offroad-lighting]

[grounding-architecture]: index.md
[engine-bay-ground-bus]: 01-engine-bay-ground-bus.md
[switchpros-sp1200]: ../../05-control-interfaces/02-switchpros-sp1200.md
[offroad-lighting]: ../../04-offroad-lighting/index.md
[bluesea-2105]: https://www.bluesea.com/products/2105/MaxiBus_250A_BusBar_-_Two_5_16in-18_Studs_and_Twelve_10-24_Screws
[headlights]: ../../03-lighting-systems/02-headlights.md
