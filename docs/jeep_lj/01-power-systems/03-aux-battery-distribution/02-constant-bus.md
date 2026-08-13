---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - bus-bar
---

# 1.3.2 Firewall CONSTANT Bus Bar {#firewall-constant-bus}

/// html | div.product-info
![Blue Sea 2105 MaxiBus](../../images/blue-sea-2105-maxibus.jpg){ loading=lazy }

**Type:** Bus Bar

**Model:** Blue Sea 2105 MaxiBus (250A) or 2107 PowerBar (600A)

**Manufacturer:** Blue Sea Systems

**Product Page:** [MaxiBus 250A][product-link]

///

## Overview

Forward distribution bus mounted on the firewall (passenger cabin side). Receives a single protected feed from the AUX battery and fans out to the cabin/firewall-mounted accessory controllers.

**Location:** Firewall (cabin side, passenger area), co-located with SwitchPros power module, BODY PDU, and JL Audio amplifier.

!!! info "Two-Stage Distribution Architecture"
This bus is stage two of the AUX battery's two-stage distribution (battery → inline CBs → this bus → per-load CBs). See [AUX Battery Distribution][rear-battery] for the full architecture and battery-side wiring.

## Specifications

- **Rating:** 250A continuous (Blue Sea 2105) or 600A (2107 if oversized for future expansion)
- **Terminals:** 14× 1/4"-20 studs (2105) or 8× 3/8"-16 studs (2107)
- **Wire Range:** Up to 2/0 AWG (2105) or 4/0 AWG (2107)
- **Features:** Tin-plated copper, corrosion resistant
- **Recommendation:** 2105 is sufficient for ~154A combined load; 2107 if future expansion is anticipated

## Input Feed (from AUX battery)

| From                    | Cable     | Distance | Protection                | Voltage Drop @ 200A | Notes                                          |
| :---------------------- | :-------- | :------- | :------------------------ | :------------------ | :--------------------------------------------- |
| **AUX battery+**        | 2/0 AWG   | ~13 ft   | 300A CB at battery (<7") | ~2.0% @ 20°C        | Routed via cabin trunk — see {{ tbd(75) }}     |

## Load Distribution

| Connection                 | Wire Gauge | Distance | Voltage Drop  | Protection | Load      | Notes                           |
| :------------------------- | :--------- | :------- | :------------ | :--------- | :-------- | :------------------------------ |
| **Feed INPUT**             | 2/0 AWG    | ~13 ft   | <1.5% @ 20°C  | 300A CB (at battery) | ~154A max | From AUX battery via cabin trunk |
| [SwitchPros][switchpros]   | 2 AWG      | ~2 ft    | <0.5% @ 20°C  | 150A CB    | ~100A max | Auxiliary lighting              |
| [BODY PDU][body-rtmr]      | 2 AWG      | ~2 ft    | <0.5% @ 20°C  | 100A CB    | ~54A max  | Cabin circuits                  |

**Combined max realistic load:** ~154A (well within 250A bus rating, comfortable in 600A bus)

**Stud utilization:** 3 of 14 used on 2105 (11 available), or 3 of 8 on 2107 (5 available)

## Circuit Breakers (co-located with bus)

Both per-load CBs mount within 7" of the bus on a small bracket near the cluster:

| Load | CB Rating | Model | Notes |
|:-----|:---------:|:------|:------|
| SwitchPros | 150A | Mechanical Products 174-S2-150-2 | 150% of max load |
| BODY PDU | 100A | Mechanical Products 174-S2-100-2 | 185% of max load |

See [Circuit Breakers][circuit-breakers] for full specs.

## Related Documentation

**Power Systems:**

- [AUX battery Distribution][rear-battery] - Battery terminal connections and inline CBs
- [Circuit Breakers][circuit-breakers] - Full CB list (battery side + firewall side)

**Connected Systems:**

- [SwitchPros RCR-Force 12][switchpros] - Auxiliary lighting controller (power module at firewall)
- [BODY PDU][body-rtmr] - Cabin convenience circuits
- [Installation Checklist][installation] - Bus bar mounting procedure

[product-link]: https://www.bluesea.com/products/2105/MaxiBus_Insulating_Base_-_Four_1_4in-20_Studs
[rear-battery]: index.md
[circuit-breakers]: 01-circuit-breakers.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
[installation]: ../../09-installation/01-power-systems-checklist.md#phase-2-power-distribution
