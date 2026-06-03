---
tags:
  - lighting
  - offroad
  - switchpros-controlled
hide:
  - toc
---

# Section 4: Offroad & Auxiliary Lighting {#offroad-auxiliary-lighting}

Non-DOT-required lighting circuits controlled by the SwitchPros SP-1200 controller.

!!! info "Controller Documentation"
See [SwitchPros SP-1200][switchpros-sp-1200] for complete specifications, wiring, and installation.

## Baja Designs Zone Lighting

Lighting organized by [Baja Designs Zone System][bd-zones], optimized for specific use cases:

| BD Zone | Purpose          | Lumens | Lights                | Lens  | Pattern        |
| :-----: | :--------------- | -----: | :-------------------- | :---- | :------------- |
|    1    | Fog/Dust         |  8,000 | 1x BD S8 10"          | Amber | Wide Cornering |
|    2    | Ditch/Peripheral |  8,800 | 2x BD LP4 Pro         | Clear | Driving/Combo  |
|   3+4   | Primary Forward  | 72,000 | 8x BD XL Sport        | Clear | Mixed          |
|    6    | Rock Lights      |  1,200 | 6x KC Cyclone V2      | Clear | Flood          |
|    7    | Cargo            |      — | 2x BD S2 Sport Flush  | Clear | Work/Scene     |
|    8    | Reverse          |  4,520 | 2x BD Squadron Sport  | Clear | Wide Cornering |
|    8    | Rear Work        |  3,800 | 2x BD S1 Black        | Clear | Work/Scene     |
|    —    | Chase/Safety     |      — | 1x BD RTL-S 30"       | Amber | Rear-facing    |
|    —    | Footwell         |      — | 4x LED4Life RGBW Pods | RGB   | Flood          |

**Total Forward:** 88,800 lumens (white) + 8,000 lumens (amber)
**Total Rear:** 7,600 lumens | **Rock:** 1,200 lumens

**Not implemented:** Zone 5 (Racer Spot), Zone 51 (Laser) - not needed for trail use.

[bd-zones]: https://www.bajadesigns.com/help/lighting-zones/

## Control Systems

| Circuit                                  | Controller                               | Page                               |
| :--------------------------------------- | :--------------------------------------- | :--------------------------------- |
| Roof, Ditch, Fog, Rock, Chase, Rear Work | [SwitchPros SP-1200][switchpros-sp-1200] | See controller for wiring          |
| Cargo Lights                             | Physical switch                          | [Cargo Lights][cargo-lights]       |
| Reverse Lights                           | [PMU Out 18][tail-brake-reverse]         | [Reverse Lights][reverse-lights]   |
| RTL-S Brake/Running                      | PMU/OEM                                  | [Chase Lights][chase-lights]       |
| Footwell                                 | [JL Audio MLC-RW][audio-systems]         | [Footwell Lights][footwell-lights] |

[tail-brake-reverse]: ../03-lighting-systems/04-tail-brake-reverse.md

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [SwitchPros SP-1200][switchpros-sp-1200] - Controller specifications, pinouts, and installation
- [Control Interfaces Overview][control-interfaces-overview] - All control interfaces
- [Vehicle Lighting][vehicle-lighting-overview] - Street-legal and DOT-required lighting circuits

[switchpros-sp-1200]: ../05-control-interfaces/02-switchpros-sp1200.md
[control-interfaces-overview]: ../05-control-interfaces/index.md
[vehicle-lighting-overview]: ../03-lighting-systems/01-lighting-overview.md
[install-checklist]: ../09-installation/01-power-systems-checklist.md
[chase-lights]: 04-chase-lights.md
[cargo-lights]: 07-cargo-lights.md
[reverse-lights]: 10-reverse-lights.md
[footwell-lights]: 09-footwell-lights.md
[audio-systems]: ../06-audio-systems/05-led-controller.md
