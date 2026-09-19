---
hide:
  - toc
---

# Section 1: Power Systems {#power-systems}

## System Overview

The van is a **12 V** system built around two Odyssey AGM Group 34 batteries -
one START, one AUX - with a RedArc BCDC Alpha 50 DC-DC charger between them.
A 200 A SGP32 relay and 600 A manual cutoffs isolate the AUX side.

![Nissan NV 3500 power redesign - all four switch panels and their loads](../images/van-devices.png)

*Device-level view of the redesign. Diagram source: `Van Electrical.drawio` (page "Devices"); the image is regenerated from the draw.io file on each export.*

---

## Distribution

Accessory loads are split across four switch panels, each a 6-circuit
Powerswitch:

| Panel | Location | Feeds |
| :---- | :------- | :---- |
| **Rear Powerswitch (A)** | Rear seat | 3x Alpine PKG-RES3HDMI headrest screens (5 A each), 3x Nvidia Shield |
| **Rear Powerswitch (B)** | Rear | Starlink Advanced Power Supply, USB power outlets, Twinkle Lights, and two 5 V USB-C buck converters feeding the UniFi USW-Flex-Mini and UXG Lite (3 A) |
| **Front Powerswitch** | Front seat | Midland MXTX575 (15 A), rearview mirror, radar detector (2 A) |
| **Engine Bay Powerswitch** | Engine bay | KC 50" light bar (45 A), KC reverse lights (8 A), KC bumper lights, KC rock lights (2.5 A), KC fog lights |

Both rear panels sit downstream of the **Rear Powerswitch (A) & (B) cutoff**.

---

## Sub-sections

- **[1.1 - Starlink Power](01-starlink-power.md)** - Starlink Advanced Power Supply fed directly from 12 V DC, replacing the 1000 W inverter

---

## Outstanding Items

- [ ] Document wire gauges and run lengths for each panel feed
- [ ] Document circuit-by-circuit breaker sizing on all four Powerswitch panels
- [ ] Confirm AUX battery capacity against measured house load (see [#4][issue-4] discussion - a single 100 Ah bank was judged undersized with a fridge on it)
- [ ] Decide whether the Genesis Offroad dual-battery tray (see [Diagrams](../02-diagrams/index.md)) is being used or dropped
- [ ] Document the grounding scheme - the drawings show no ground returns

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
