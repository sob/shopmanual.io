---
hide:
  - toc
---

# Nissan NV 3500 - Van Build {#nissan-nv-3500-van-build}

## Project Overview

A 2018 Nissan NV 3500 (5.6 L V8, lifted, 35" tires) with an accessory
electrical system built on top of the factory wiring. The van runs a **12 V** system: an Odyssey AGM Group 34 START
battery and a second Odyssey AGM Group 34 as the AUX house battery, in a
Genesis Offroad dual battery tray with a Redarc BCDC Alpha 50 DC-DC charger
between them. The AUX battery feeds two switch panels, Rear Powerswitch (A)
and (B), through a 200 A SGP32 relay, and can run with the key off. An Engine Bay Powerswitch for
the KC exterior lighting is planned. A Viper alarm with SmartStart remote start
is tapped into the factory wiring through T-harnesses behind the driver-side
dash.

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
- **[Body Electrical](03-body-electrical/index.md)** - Viper SmartStart, and the BCM → CAN → IPDM E/R exterior lighting path
- **[Service & Maintenance](04-service/index.md)** - Vehicle details, service history, relearn and oil change procedures

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
| **Viper wiring** | Headlight fault [traced to the Viper bundle](03-body-electrical/01-viper-smartstart.md#fault-2026-09) and resolved (owner, 2026-09-25). The bundle still needs a wiggle test, securing, and a code clear |
| **Drivetrain** | Transmission and cylinder 7 [concerns](04-service/index.md#concerns) not yet diagnosed. An engine/transmission replacement (ZF 8HP raised) and a 4x4 conversion are under consideration |
| **GMRS radio** | [Midland MXT575][mxt575], 50 W, moving over from the Jeep LJ (owner, 2026-09-25). Where it mounts and what powers it are not decided; Rear Powerswitch (B) has five spare circuits |

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
[mxt575]: https://midlandusa.com/products/mxt575-micromobile-gmrs-two-way-radio
