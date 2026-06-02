---
hide:
  - toc
---

# Section 1: Power Systems {#power-systems}

## System Overview

The Jeep LJ uses a dual-battery electrical system with intelligent power distribution and programmable power management.

### Power Generation & Storage

- **START battery:** Odyssey PC1500 (850 CCA, 68 Ah) in driver wheel well - critical systems only
- **AUX battery:** Dakota Lithium 135Ah LiFePO4 (108 Ah usable, heated BMS) in passenger wheel well - accessories, winch (jump start capable)
- **RedArc BCDC Alpha 50:** DC-DC charger/isolator - batteries operate independently when isolated
- **270A Alternator:** Charges START battery, BCDC charges AUX battery from front

See [Power Generation](01-power-generation/index.md) for complete details on batteries, alternator, BCDC, and solar charging.

### Power Distribution

Both batteries use CONSTANT bus bars for organized distribution with individual circuit breaker protection:

- **[START battery Distribution](02-starter-battery-distribution/index.md):** CONSTANT bus (Blue Sea 2107, 600A) feeds PMU, SafetyHub, BCDC
- **[AUX battery Distribution](03-aux-battery-distribution/index.md):** CONSTANT bus (Blue Sea 2104, 225A) feeds SwitchPros, BODY PDU

The system replaces the factory TIPM with modular programmable controllers:

- **[PMU24](04-pmu/index.md):** 24-channel programmable power management - engine bay critical circuits
- **[BODY PDU](03-aux-battery-distribution/03-body-pdu.md):** Cabin convenience circuits - radio, USB, heated seats, camera
- **[SafetyHub](03-aux-battery-distribution/04-safetyhub.md):** High-current safety circuits - ARB compressor, winch contactor

Ground distribution architecture:

- **[Grounding Architecture](05-grounding/index.md):** Battery grounds, engine bay ground bus, firewall stud bus, distributed grounding system

---

## Wiring Standards

| Standard | Specification | Notes |
| :------- | :------------ | :---- |
| **Connections** | Soldered + marine heat shrink | Waterproof, vibration-resistant |
| **Connectors** | Deutsch DT series (IP68) | Engine bay and exterior locations |
| **Securing** | Every 12-18" | High-vibration areas (engine bay, wheel wells, frame rails) |
| **Securing** | Every 24" | Low-vibration areas (cabin, trunk) |
| **Loom** | Split loom or braided sleeving | Abrasion protection where routed against metal |
| **Grommets** | Rubber with sealant | All firewall and body penetrations |
| **Temp derating** | 60°C for engine bay | Ampacity calculations must use derated values |
| **Temp derating** | 30°C for cabin/wheel well | Standard ampacity values acceptable |

See [Wire Distance Reference][wire-distance] for routing distances and gauge specifications.

[wire-distance]: 01-power-generation/05-wire-distance-reference.md

## Outstanding TBD Items

_Auto-derived from this page's section (`area/power-systems`) — open GitHub issues only._

{{ tbds() }}
