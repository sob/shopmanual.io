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

Accessory loads are split across four [Garmin PowerSwitch][garmin-spec] boxes.
Each is a 6-circuit digital switch box rated **30 A max per output, 100 A max
system**, at 12-16 V. There are no separate breakers on the branch circuits -
the PowerSwitch output rating is the protection, so branch conductors are sized
to the output rating rather than to expected load.

| Panel | Location | Feeds |
| :---- | :------- | :---- |
| **Rear Powerswitch (A)** | Rear seat | 3x Alpine PKG-RES3HDMI headrest screens (5 A each), 3x Nvidia Shield. **Circuit 6 as built:** Starlink Advanced Power Supply + 12 V USB-C outlet (rear driver's door) → UXG Lite |
| **Rear Powerswitch (B)** | Rear | Starlink Advanced Power Supply, USB power outlets, Twinkle Lights, and two 5 V USB-C buck converters feeding the UniFi USW-Flex-Mini and UXG Lite (3 A) |
| **Front Powerswitch** | Front seat | Midland MXTX575 (15 A), rearview mirror, radar detector (2 A) |
| **Engine Bay Powerswitch** | Engine bay | KC 50" light bar (45 A), KC reverse lights (8 A), KC bumper lights, KC rock lights (2.5 A), KC fog lights |

Both rear panels sit downstream of the **Rear Powerswitch (A) & (B) cutoff**.

!!! warning "The table above is the redesign drawing, not the as-built"
    The Devices drawing puts Starlink and the UniFi gear on Rear Powerswitch (B)
    behind two 5 V buck converters, with a USW-Flex-Mini switch. That is not how
    it is wired today: **Starlink and the UXG Lite are both on Rear Powerswitch
    (A) circuit 6**, the UXG Lite runs off a 12 V USB-C outlet in the rear
    driver's door, and the USW-Flex-Mini is not in use. See
    [Starlink Power](01-starlink-power.md). The drawing needs reconciling - see
    Outstanding Items.

---

## Sub-sections

- **[1.1 - Starlink Power](01-starlink-power.md)** - Starlink Advanced Power Supply fed directly from 12 V DC, replacing the 1000 W inverter

---

## Outstanding Items

- [ ] Document wire gauges and run lengths for each panel feed
- [ ] Document circuit-by-circuit conductor sizing on all four PowerSwitch panels against the 30 A output rating
- [ ] Confirm AUX battery capacity against measured house load (see [#4][issue-4] discussion - a single 100 Ah bank was judged undersized with a fridge on it)
- [ ] Decide whether the Genesis Offroad dual-battery tray (see [Diagrams](../02-diagrams/index.md)) is being used or dropped
- [ ] Document the grounding scheme - the drawings show no ground returns
- [ ] Reconcile the Devices redesign drawing with the as-built wiring: Starlink + UXG Lite moved to Rear Powerswitch (A) circuit 6, USW-Flex-Mini dropped
- [ ] Decide where the 3x Nvidia Shield network connections land now that the USW-Flex-Mini is out

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
[garmin-spec]: https://www8.garmin.com/manuals/webhelp/GUID-16B1D74D-857B-4FFB-8DE2-A0960FE0D090/EN-US/GUID-E9A53DAE-B84A-4E4F-9488-5536604B1779.html
