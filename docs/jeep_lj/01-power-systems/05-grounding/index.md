---
hide:
  - toc
---

# 1.5 Grounding Architecture {#grounding-architecture}

Multi-point grounding strategy with high-current grounds to frame rails and low-current grounds to firewall/chassis points.

## Overview

| Ground Point              | Type                   | Location                   | Capacity            | Notes                                              |
| :------------------------ | :--------------------- | :------------------------- | :------------------ | :------------------------------------------------- |
| **START battery (-)**     | Battery Terminal       | Driver rear wheel well     | 7 connections       | See [START Battery Distribution][starter-battery]  |
| **AUX battery (-)**       | Battery Terminal       | Passenger rear wheel well  | 5 connections       | See [AUX Battery Distribution][aux-battery]        |
| **Engine Bay Ground Bus** | Blue Sea 2107 PowerBar | Firewall (engine bay)      | 8 studs (600A)      | See [Engine Bay Ground Bus][engine-bay-ground-bus] |
| **Firewall Stud Bus**     | Blue Sea 2105 MaxiBus  | Firewall (cabin side)      | 14 terminals (250A) | See [Firewall Stud Bus][firewall-stud-bus]         |
| **SwitchPros Ground Bus** | Blue Sea 2105 MaxiBus  | Near SwitchPros controller | 14 terminals (250A) | See [SwitchPros Ground Bus][switchpros-ground-bus] |

## Ground Bus Bars

- **[1.5.1 - Engine Bay Ground Bus][engine-bay-ground-bus]** - Primary infrastructure hub (frame, engine, PMU)
- **[1.5.2 - Firewall Stud Bus][firewall-stud-bus]** - Cabin electronics (BODY PDU, cluster, audio, camera)
- **[1.5.3 - SwitchPros Ground Bus][switchpros-ground-bus]** - Lighting and accessories (headlights, aux lights)

## Testing Requirements

| Test Point                    | Max Voltage Drop | Test Conditions                 |
| :---------------------------- | :--------------- | :------------------------------ |
| Battery to frame rail (front) | <0.1V            | Engine @ 2000 RPM, DC voltmeter |
| Battery to frame rail (rear)  | <0.1V            | Engine @ 2000 RPM, DC voltmeter |
| START battery to AUX battery  | <0.05V           | Engine @ 2000 RPM, DC voltmeter |

**Installation & Testing:** See [Section 1 Installation Checklist][installation]

[installation]: ../../09-installation/01-power-systems-checklist.md#phase-1-foundations
[starter-battery]: ../02-starter-battery-distribution/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[engine-bay-ground-bus]: 01-engine-bay-ground-bus.md
[firewall-stud-bus]: 02-firewall-stud-bus.md
[switchpros-ground-bus]: 03-switchpros-ground-bus.md
