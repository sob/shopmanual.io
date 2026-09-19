---
hide:
  - toc
---

# Nissan NV 3500 - Van Build {#nissan-nv-3500-van-build}

## Project Overview

A Nissan NV 3500 with an accessory electrical system built on top of the
factory wiring. The van runs a **12 V** system: an Odyssey AGM Group 34 START
battery and a second Odyssey AGM Group 34 as the AUX house battery, tied
together through a RedArc BCDC Alpha 50 DC-DC charger and isolated by a 200 A
SGP32 relay with 600 A manual cutoffs. Accessory loads hang off four switch
panels - Rear Powerswitch (A) and (B), a Front Powerswitch, and an Engine Bay
Powerswitch.

Documentation for this build started as draw.io drawings rather than written
pages. Those drawings are still the source of truth for the system-level
picture; this section pulls them onto the site and writes up the parts of the
system that have been decided.

<div class="mobile-nav-only" markdown="1">

## Sections

- **[Power Systems](01-power-systems/index.md)** - Batteries, distribution, and the four switch panels
- **[Starlink Power](01-power-systems/01-starlink-power.md)** - Starlink Advanced Power Supply, 12 V DC direct
- **[Diagrams](02-diagrams/index.md)** - The full set of van drawings, rendered from `Van Electrical.drawio`

</div>

---

## Current Focus

| Area | State |
| :--- | :---- |
| **Starlink power** | Resolved - High Performance dish on a [Starlink Advanced Power Supply](01-power-systems/01-starlink-power.md), 12 V DC direct, replacing the 1000 W inverter ([#4][issue-4]) |
| **House battery** | Two Odyssey AGM Group 34 (START + AUX), BCDC Alpha 50 |
| **Entertainment** | 3x Nvidia Shield + 3x Alpine PKG-RES3HDMI headrest screens |
| **Network** | UniFi UXG Lite gateway in the rear driver's door, powered from a 12 V USB-C outlet on Rear Powerswitch (A) circuit 6; WAN from the Starlink supply's LAN port |
| **Lighting** | KC light bar, bumper, rock, reverse, and fog lights on the engine bay panel |

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
