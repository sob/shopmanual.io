---
hide:
  - toc
tags:
  - diagrams
---

# Section 2: Diagrams {#diagrams}

Every drawing on this page is a page of **`Van Electrical.drawio`** at the
repository root. The draw.io file is the source of truth - these PNGs are
regenerated from it by the `drawio-export` workflow, so edit the drawing, never
the image.

**As Built** is the reference for what is in the van. The pages below it are
design history: the original wiring, the Genesis variant, and the redesign.
Where they disagree with As Built, As Built wins.

---

## As Built {#as-built}

What is in the van today. Two Odyssey AGM Group 34 batteries sit in a Genesis
Offroad dual tray with the BCDC Alpha 50. AUX feeds Rear Powerswitch (A) and
(B) through the SGP32 relay on ignition. The AUX isolator, the Engine Bay
Powerswitch, and power for the Nvidia Shields are shown dashed as planned or
TBD. Written up in [Batteries & Charging](../01-power-systems/02-batteries-charging.md)
and [Switch Panels](../01-power-systems/03-switch-panels.md).

![Nissan NV 3500 as built](../images/van-as-built.png)

---

## Starlink Power (v3) {#starlink-v3}

The Starlink feed as built: Rear Powerswitch (A) circuit 6 → Starlink Advanced
Power Supply → High Performance dish, on 12 V DC with no inverter. The same
circuit triggers the 12 V USB-C outlet that runs the UXG Lite, and the supply's
LAN port feeds the UXG Lite WAN input. Written up in
[Starlink Power](../01-power-systems/01-starlink-power.md).

![Starlink power v3 - Advanced Power Supply on 12 V DC](../images/van-starlink-power.png)

---

## Devices {#devices}

Device-level view of the power redesign: all four Powerswitch panels and
everything hanging off them, with the legend counting how each load is
controlled.

!!! info "This is the plan, not the as-built"
    The redesign groups Starlink and the UniFi gear on Rear Powerswitch (B),
    includes a USW-Flex-Mini switch, and adds a Front Powerswitch. As built,
    Starlink and the UXG Lite are on **Rear Powerswitch (A) circuit 6**, there
    is no Ethernet switch, and there is no Front Powerswitch - see
    [As Built](#as-built).

![Nissan NV 3500 power redesign, device level](../images/van-devices.png)

---

## Current State {#current-state}

The system as originally drawn, with the 1000 W inverter that Starlink and the
Nvidia Shields were powered through. Kept as the before picture. The inverter
is gone, the batteries are in the Genesis tray, and the SGP32 relay now feeds
the rear panels - see [As Built](#as-built). Its Rear Powerswitch (A) circuits
1-5 still match the van.

![Nissan NV 3500 current state wiring](../images/van-current-state.png)

---

## Genesis {#genesis}

The same system with the batteries in a Genesis Offroad Group 34 dual battery
tray. The van uses the Genesis tray (with the BCDC Alpha 50), so this is closer
to reality than Current State, but it still shows the inverter on the SGP32
relay - see [As Built](#as-built).

![Nissan NV 3500 with Genesis Offroad dual battery](../images/van-genesis.png)

---

## Superseded pages {#superseded}

`Van Electrical.drawio` also carries a **Starlink v2** page - the Yaosheng PoE
injector approach that preceded the Advanced Power Supply. It is kept in the
drawing for history but is not rendered here.
