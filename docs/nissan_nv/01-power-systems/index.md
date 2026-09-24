---
hide:
  - toc
---

# Section 1: Power Systems {#power-systems}

## System Overview

The van is a **12 V** system. Two Odyssey AGM Group 34 batteries, one START and
one AUX, sit in a Genesis Offroad dual battery tray with a Redarc BCDC Alpha 50
DC-DC charger between them. The AUX battery feeds the rear switch panels
through a 200 A SGP32 relay on ignition.

![Nissan NV 3500 as built - batteries, SGP32 relay, and both rear switch panels](../images/van-as-built.png)

*As-built view. Diagram source: `Van Electrical.drawio` (page "As Built"); the image is regenerated from the draw.io file on each export.*

---

## Distribution

Accessory loads are split across [Garmin PowerSwitch][garmin-spec] boxes, each
a 6-circuit digital switch box rated **30 A max per output, 100 A max per box**,
at 12-16 V. There are no branch breakers: the PowerSwitch output is the
protection, so branch conductors are sized to the output rating rather than to
the expected load.

| Panel | State | Location | Feeds |
| :---- | :---- | :------- | :---- |
| **Rear Powerswitch (A)** | Installed | Rear | 1-3 Alpine PKG-RES3HDMI headrest screens, 4 USB power outlets, 5 rearview mirror, 6 Starlink Advanced Power Supply + 12 V USB-C outlet (UXG Lite) |
| **Rear Powerswitch (B)** | Installed | Rear | 1 radar detector; 2-6 spare |
| **Engine Bay Powerswitch** | Planned | Engine bay | KC 50" light bar, reverse, bumper (x2), rock, and fog lights |

Both rear panels are fed from AUX through the ignition-switched SGP32 relay.
The **Front Powerswitch** on the *Devices* drawing does not exist. The
circuit-by-circuit detail is in [Switch Panels](03-switch-panels.md).

---

## Sub-sections

- **[1.1 - Starlink Power](01-starlink-power.md)** - Starlink Advanced Power Supply fed directly from 12 V DC, replacing the 1000 W inverter
- **[1.2 - Batteries & Charging](02-batteries-charging.md)** - Genesis dual battery tray, BCDC Alpha 50, SGP32 relay rear feed, planned AUX isolator
- **[1.3 - Switch Panels](03-switch-panels.md)** - Circuit assignments for Rear Powerswitch (A) and (B), and the planned Engine Bay panel

---

## Outstanding Items

Section-specific items live on each sub-page. Items that span the whole system:

- [ ] Document wire gauges and run lengths for each panel feed
- [ ] Confirm AUX battery capacity against measured house load (see [#4][issue-4] discussion - a single 100 Ah bank was judged undersized with a fridge on it)
- [ ] Document the grounding scheme - the drawings show no ground returns

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
[garmin-spec]: https://www8.garmin.com/manuals/webhelp/GUID-16B1D74D-857B-4FFB-8DE2-A0960FE0D090/EN-US/GUID-E9A53DAE-B84A-4E4F-9488-5536604B1779.html
