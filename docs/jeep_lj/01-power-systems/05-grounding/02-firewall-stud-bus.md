---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - grounding
  - bus-bar
---

# 1.5.4 Firewall Stud Bus {#firewall-stud-bus}

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
- **Location:** Firewall (cabin side), accessible from dash
- **Full Specs:** [Blue Sea 2105][bluesea-2105]

## Stud/Terminal Assignment

| Stud/Terminal            | Connection                 | Wire Gauge  | Distance  | Max Current    | Notes                                                   |
| :----------------------- | :------------------------- | :---------- | :-------- | :------------- | :------------------------------------------------------ |
| **Stud 1 (5/16")**       | **Chassis Ground (INPUT)** | **4 AWG ✓** | **~2 ft** | **~50A total** | **Primary bus ground - to firewall**                    |
| Stud 2 (5/16")           | **\[Available\]**            | -           | -         | -              | Future high-current ground                              |
| Terminal 1 (#10-24)      | Command Touch CT4          | 14 AWG ✓    | ~3 ft     | <1A            | Steering column controller logic ground                 |
| Terminal 2 (#10-24)      | WS-51C Wiper Controller    | 16 AWG ✓    | ~2 ft     | ~5A            | Dash wiper control - see [Wiper System][wiper-system]   |
| Terminal 3 (#10-24)      | BODY PDU                   | 14 AWG ✓    | ~4 ft     | ~3A            | Relay coil/logic ground only (high-side switching)      |
| Terminal 4 (#10-24)      | Dakota Digital Cluster     | 16 AWG ✓    | ~2 ft     | <1A            | Instrument cluster logic ground                         |
| Terminal 5 (#10-24)      | Dakota Digital BIM         | 16 AWG ✓    | ~2 ft     | <1A            | Body interface module                                   |
| Terminal 6 (#10-24)      | Fusion MS-RA670 Head Unit  | 14 AWG ✓    | ~2 ft     | ~5A            | Audio head unit - see [Audio System][audio-system]      |
| Terminal 7 (#10-24)      | MLC-RW LED Controller      | 16 AWG ✓    | ~2 ft     | ~3A            | Audio RGB controller - see [Audio System][audio-system] |
| Terminal 8 (#10-24)      | WolfBox Camera/Mirror      | 16 AWG ✓    | ~2 ft     | ~5A            | Rearview mirror/camera system                           |
| Terminal 9 (#10-24)      | **\[Available\]**            | -           | -         | -              | Future dash electronics                                 |
| Terminals 10-12 (#10-24) | **\[Available\]**            | -           | -         | -              | Future expansion (3 terminals)                          |

**Utilization:** 9 of 14 used (1 stud + 8 terminals used, 1 stud + 4 terminals available)

**Purpose:** Clean ground reference for cabin electronics - keep separate from high-current grounds to minimize noise

## Installation

**Mounting:** Firewall (cabin side), close to dash electronics

**Ground Path:** Bus → chassis ground (4 AWG, handles ~50A total load) → START battery negative bus (via 2/0 AWG main chassis ground)

**Critical:** Clean metal-to-metal connection to firewall/chassis, protected from water/moisture

## Related Documentation

- [Grounding Architecture Overview][grounding-architecture]
- [Engine Bay Ground Bus][engine-bay-ground-bus]
- [BODY PDU][body-rtmr]
- [Audio System][audio-system]
- [Wiper System][wiper-system]

[grounding-architecture]: index.md
[engine-bay-ground-bus]: 01-engine-bay-ground-bus.md
[body-rtmr]: ../03-aux-battery-distribution/03-body-pdu.md
[audio-system]: ../../06-audio-systems/index.md
[wiper-system]: ../../02-engine-systems/04-wipers.md
[bluesea-2105]: https://www.bluesea.com/products/2105/MaxiBus_250A_BusBar_-_Two_5_16in-18_Studs_and_Twelve_10-24_Screws
