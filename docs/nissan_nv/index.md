---
hide:
  - toc
---

# Nissan NV 3500 - Van Build {#nissan-nv-3500-van-build}

## Project Overview

A Nissan NV 3500 with an accessory electrical system built on top of the
factory wiring. The van runs a **12 V** system: an Odyssey AGM Group 34 START
battery and a second Odyssey AGM Group 34 as the AUX house battery, in a
Genesis Offroad dual battery tray with a Redarc BCDC Alpha 50 DC-DC charger
between them. The AUX battery feeds two switch panels, Rear Powerswitch (A)
and (B), through a 200 A SGP32 relay, and can run with the key off. An Engine Bay Powerswitch for
the KC exterior lighting is planned.

Documentation for this build started as draw.io drawings rather than written
pages. The *As Built* page of `Van Electrical.drawio` and the pages below are
now the reference for what is in the van; the older drawings are kept on the
[Diagrams](02-diagrams/index.md) page as design history.

<div class="mobile-nav-only" markdown="1">

## Sections

- **[Power Systems](01-power-systems/index.md)** - Batteries, distribution, and the switch panels
- **[Starlink Power](01-power-systems/01-starlink-power.md)** - Starlink Advanced Power Supply, 12 V DC direct
- **[Batteries & Charging](01-power-systems/02-batteries-charging.md)** - Genesis dual battery tray, BCDC Alpha 50, SGP32 rear feed
- **[Switch Panels](01-power-systems/03-switch-panels.md)** - Circuit assignments for Rear Powerswitch (A) and (B)
- **[Diagrams](02-diagrams/index.md)** - The full set of van drawings, rendered from `Van Electrical.drawio`

</div>

---

## Current Focus

| Area | State |
| :--- | :---- |
| **Starlink power** | Resolved - High Performance dish on a [Starlink Advanced Power Supply](01-power-systems/01-starlink-power.md), 12 V DC direct, replacing the 1000 W inverter ([#4][issue-4]) |
| **House battery** | Two Odyssey AGM Group 34 (START + AUX) in a Genesis Offroad dual tray, BCDC Alpha 50; [600 A AUX isolator planned](01-power-systems/02-batteries-charging.md#planned) |
| **Entertainment** | 3x Alpine PKG-RES3HDMI headrest screens on Rear Powerswitch (A) 1-3; power for the 3x Nvidia Shields is TBD now the inverter is out |
| **Network** | UniFi UXG Lite gateway in the rear driver's door below the Starlink supply, powered from a 12 V USB-C outlet on Rear Powerswitch (A) circuit 6; WAN from the supply's LAN port |
| **Lighting** | KC light bar, bumper, rock, reverse, and fog lights on a [planned Engine Bay Powerswitch](01-power-systems/03-switch-panels.md#engine-bay) |

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
