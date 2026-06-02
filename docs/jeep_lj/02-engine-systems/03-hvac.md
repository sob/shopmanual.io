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

**Type:** Factory HVAC System

**Model:** 2005 TJ/LJ HVAC Assembly

**Manufacturer:** Chrysler/Jeep (OEM)

**Mounting:** Factory under-dash location

**Power Source:** PMU OUT5 (blower motor), OUT17 (A/C clutch)

**Control:** Factory TJ HVAC control panel

///

## Overview

Factory 2005 TJ HVAC system retained. Uses vacuum-operated mode doors, cable-operated temperature blend door, and factory dash control panel. Requires only 2 PMU outputs.

## PMU Integration

| Circuit      | PMU        | Load     | Control            | Notes                                |
| :----------- | :--------- | :------- | :----------------- | :----------------------------------- |
| Blower Motor | OUT5 (25A) | ~20A max | Auto (ignition ON) | Factory resistor pack controls speed |
| A/C Clutch   | OUT17 (7A) | 3-5A     | In 9 trigger       | Factory A/C button → PMU In 9        |

See [PMU Outputs][pmu-outputs] for complete configuration.

## Control Methods

| Function                  | Control Type               | PMU Involvement     |
| :------------------------ | :------------------------- | :------------------ |
| Blower Speed              | Electrical (resistor pack) | OUT5 provides power |
| A/C On/Off                | Electrical (PMU switched)  | In 9 triggers OUT17 |
| Temperature               | Mechanical (cable)         | None                |
| Mode (defrost/vent/floor) | Vacuum                     | None                |
| Recirculation             | Vacuum                     | None                |

## Vacuum System

**Source:** R2.8 intake manifold → check valve → reservoir → firewall → factory HVAC controls

**Components:** 10-15 ft vacuum line (1/4" ID), check valve, vacuum reservoir, tee fittings

## R2.8 ECM A/C Integration

The CM2220 ECM used by the R2.8 has no A/C request input pin, so PMU-to-ECM A/C signaling is not applicable for this build. A/C clutch engagement may cause a slight idle dip but not enough to require compensation.

## Outstanding Items

None - design complete. See [installation checklist][install-checklist] for build tasks.

## Related Documentation

- [PMU Outputs][pmu-outputs] - OUT5 and OUT17 configuration

[install-checklist]: ../09-installation/02-engine-systems-checklist.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
