---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - grid-heater
  - cummins
---

# 2.7 Grid Heater System {#27-grid-heater-system}

/// html | div.product-info

**Type:** Cold-start air intake heater

**Model:** Grid Heater Relay

**Part Number:** Cummins 5467024

**Manufacturer:** Cummins

**Mounting:** Engine bay near intake manifold

**Power Source:** START battery+ direct (via fusible link, 40-80A) — ⚠️ current unverified[^grid-current]

[^grid-current]: ⚠️ UNVERIFIED. Cummins does not publish a current draw for grid-heater part 5467024 on the R2.8 (spec flyer 5410825 / install guide 5504137 give no amperage); commonly-cited 95-110A figures are for Dodge/Ram 5.9/6.7 heaters, not this part (checked 2026-05-30). The 40-80A / 80A element values are engineering estimates — confirm by element-resistance measurement during install (already tracked as a Verification item).

**Control:** Direct ECM control (pins 46/21)

///

## Specifications

| Spec              | Value                                              |
| :---------------- | :------------------------------------------------- |
| Type              | Cold-start air intake heater                       |
| Relay part number | Cummins 5467024                                    |
| Coil control      | ECM pins 46/21 (~0.5–1A)                           |
| Element current   | 40–80A (design estimate)[^grid-current]            |
| Duty cycle        | 3–5 s during cold start (ECM-controlled)           |
| Protection        | Integrated fusible link                            |

## Wiring Summary

**Two-Stage Design:** ECM pins 46/21 (1A) → relay coil → relay switches high current (40-80A) directly from battery to element.

```mermaid
flowchart LR
    ECM["Cummins ECM<br/>Pins 46/21"]
    RELAY["Grid Heater Relay<br/>Cummins 5467024"]
    BATT["START battery+<br/>(Direct Connection)"]
    GND["START battery-"]
    ELEMENT["Grid Heater Element<br/>40-80A"]

    ECM -->|"~1A coil control"| RELAY
    BATT -->|"Fusible Link<br/>40-80A"| RELAY
    RELAY -->|"40-80A switched"| ELEMENT
    ELEMENT --> GND

    style ECM fill:#d1d5db,color:#000
    style RELAY fill:#d1d5db,color:#000
    style BATT fill:#ffd93d,color:#000
    style GND fill:#ffd93d,color:#000
    style ELEMENT fill:#d1d5db,color:#000
```

## Design Rationale

- **ECM controls it directly** (not PMU): the ECM already has engine temperature and timing data, so triggering the relay itself avoids a PMU signal passthrough and frees a PMU output slot.
- **Power bypasses the CONSTANT bus bar and PMU outputs**: 40-80A for only 3-5 seconds doesn't justify routing through distribution — a direct battery connection with fusible link protection minimizes voltage drop and connection complexity.

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [PMU Power Distribution][pmu-power-distribution] - Engine bay power management
- [START Battery Distribution][starter-battery-distribution] - Direct battery connections

[install-checklist]: ../09-installation/02-engine-systems-checklist.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[starter-battery-distribution]: ../01-power-systems/02-starter-battery-distribution/index.md
