---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - hvac
  - climate-control
---

# 2.3 HVAC System {#hvac-system}

/// html | div.product-info

**Type:** Custom Electronic A/C + Heat System

**Model:** Restomod Air custom kit — configuration {{ tbd(146) }} (confirm against order)

**Manufacturer:** Restomod Air

**Mounting:** Under-dash (replaces factory TJ HVAC assembly)

**Power Source:** PMU OUT5 (blower motor), OUT17 (A/C clutch)

**Control:** Restomod Air electronic control head

///

## Overview

Custom Restomod Air electronic HVAC system (on order) replaces the factory 2005 TJ HVAC.[^restomod-order] Restomod Air kits are fully electronic — mode and blend doors are servo-driven from the control head — so the factory vacuum mode doors, cable blend door, and dash control panel are all deleted.[^restomod-electronic] This removes the build's only vacuum consumer: no vacuum supply from the R2.8 is required (the diesel makes minimal manifold vacuum anyway, and braking is already vacuum-independent — see [iBooster][brake-booster]).

## PMU Integration

| Circuit      | PMU        | Load     | Control            | Notes                                |
| :----------- | :--------- | :------- | :----------------- | :----------------------------------- |
| Blower Motor | OUT5 (25A) | {{ tbd(146) }} — verify kit blower draw ≤25A | Auto (ignition ON) | Blower speed controlled by Restomod Air control head, not PMU |
| A/C Clutch   | OUT17 (7A) | 3-5A     | In 9 trigger       | Restomod Air control head compressor request → trinary switch → PMU In 9 ({{ tbd(146) }} — verify wire ID against kit diagram on arrival) |

See [PMU Outputs][pmu-outputs] for complete configuration.

## A/C Request Circuit (PMU In 9)

The Restomod Air control head generates the A/C request: when A/C is commanded, its compressor-engage output goes to 12V. That output routes **through the kit's trinary pressure switch** (30 psi low-pressure cutout, 406 psi high-pressure cutout)[^trinary] and then to **PMU In 9**, so the PMU only sees a request when refrigerant pressure is in the safe range. PMU logic then drives OUT17 → compressor clutch.

The trinary switch's third function (electric fan request at 254 psi) is not wired — radiator fan control is handled by the dedicated fan controller with its own coolant sensor (see [Radiator Fan][radiator-fan]); revisit only if condenser airflow proves insufficient.

## R2.8 ECM A/C Integration

The CM2220 ECM used by the R2.8 has no A/C request input pin, so PMU-to-ECM A/C signaling is not applicable for this build. A/C clutch engagement may cause a slight idle dip but not enough to require compensation.

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [PMU Outputs][pmu-outputs] - OUT5 and OUT17 configuration
- [PMU Inputs][pmu-inputs] - In 9 A/C request
- [iBooster][brake-booster] - Vacuum-independent braking (no engine vacuum used anywhere in the build)
- [Radiator Fan][radiator-fan] - Fan control (independent of A/C trinary fan signal)

[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[brake-booster]: 02-brake-booster.md
[radiator-fan]: 06-radiator-fan.md

[^restomod-order]: Owner confirmation, 2026-06-11 — custom kit ordered from restomodair.com. Model/configuration per order confirmation; update this page when the unit arrives.
[^restomod-electronic]: Restomod Air product line is "fully electronic aftermarket a/c system kits" with electronic control heads (no vacuum actuation). restomodair.com, accessed 2026-06-11.
[^trinary]: Restomod Air trinary switch: 30 psi low-pressure cutout, 406 psi high-pressure cutout, electric fan signal at 254 psi. restomodair.com/support/trinary-switch/, accessed 2026-06-11.
