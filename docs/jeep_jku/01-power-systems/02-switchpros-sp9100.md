---
hide:
  - toc
tags:
  - product-details
  - controller
  - switchpros
---

# 1.2 SwitchPros SP-9100 {#switchpros-sp9100}

/// html | div.product-info

**Model:** SP-9100, an 8-switch programmable switch panel and power system

**State:** Purchased, not installed. It went to the JK instead of the LJ, which uses the [SP-1200][lj-sp1200].

**Manual:** [SP9100 Rev 2.1 (Nov 2024)][manual-rev21]. An older [Rev 1.6][manual-rev16] also exists.

**Power Source:** Direct to the AUX battery positive post of the [Genesis dual battery system][dual-battery], not the bus bar (owner decision, 2026-09-24)

**Power Wire:** Supplied battery cable, 2.5 ft 4 AWG welding cable with a 125 A in-line fuse at the battery end[^m-p5]

**Ground:** Supplied 18 AWG black wire, run directly to the AUX battery negative post[^m-p4]

**Power Module Location:** Not yet chosen. The module must be within 2 ft of the battery, mounted vertically with the connectors facing outward[^m-p3].

**Switch Panel Location:** Center dash or A-pillar, not yet decided. See [Switch Panel Mount](#panel-mount).

**Control Cable:** 10.5 ft, shielded. **Do not cut or splice it**; SwitchPros sells other lengths[^m-p6].

**IP Rating:** IP67, both the power module and the switch panel[^m-p2]

///

## Specifications {#specifications}

| Item | Value | Source |
| :--- | :---- | :----- |
| Total capacity | 125 A max | [^m-p2] |
| Switches 1-4 | 20 A max each, one 14 AWG output wire | [^m-p2] [^m-p3] |
| Switches 5-8 | 35 A max each, two 14 AWG output wires. **Tie both wires together** for 35 A. If split, each wire is limited to 17 A and both loads switch together. | [^m-p2] [^m-p3] |
| Output type | High-side +12 V only. It will not switch ground. | [^m-p3] |
| Per-output current limit | Set in the app in 5 A steps. SwitchPros recommends 15-20% above the load's maximum draw. | [^m-p3] |
| Quiescent draw | 35 mA active; 5.5 mA idle (after 5 min); 3 mA asleep (after 480 min by default) | [^m-p2] [^m-p9] |
| Low-voltage disconnect | On by default at 11.0 V (11.0, 11.5, or 12.0 V selectable) held for 1 min. Up to six outputs can be exempted. | [^m-p8] |
| Input thresholds | Active high > 4.5 V; active low < 0.5 V | [^m-p2] |
| Power module | 6.0 × 3.0 × 0.6 in; 2.8 in deep with the connectors and wires plugged in; -40 to 125 °C | [^m-p2] |
| Switch panel | 4.0 × 2.0 × 0.365 in; -30 to 85 °C; RGB backlight | [^m-p2] |
| Panel cutout (recessed mount) | 3.875 × 1.875 in, 0.237 in corner radius. A surface mount instead needs four 6-32 studs and a 5/8 in harness hole. | [^m-p2] |
| Bluetooth | BLE 4.1, iOS and Android app | [^m-p2] |

---

## Wiring {#wiring}

| Connection | Wire | Source / Destination | Notes |
| :--------- | :--- | :------------------- | :---- |
| Battery cable | 4 AWG, supplied, 125 A fuse | AUX battery positive post → module stud. The fuse holder sits at the battery end. | **Nothing else may land on the module stud**[^m-p1] |
| Ground | Black, 18 AWG | Module → AUX battery negative post | Must go directly to the battery negative to keep the communications bus quiet[^m-p1] |
| Ignition | Light blue | Open: an ignition- or accessory-switched fuse tap | Enables switches programmed as Ignition (the default), and turns on the panel backlight[^m-p4] [^m-p8] |
| Lights / Trigger 2 | White | High-beam signal | Set up as **Trigger 2**, turning on up to 4 outputs, so it no longer dims the backlight[^m-p10]. See [Trigger Inputs](#trigger-inputs). |
| Trigger 1 | Pink | Reverse lamp signal | Turns on up to 4 outputs from an external signal, active high or low[^m-p5]. See [Trigger Inputs](#trigger-inputs). |
| Outputs 1-8 | 14 AWG | Module → loads | Load grounds go to the frame or the battery negative[^m-p3] |

!!! note "Ignition input and Bluetooth"
    While a phone is connected over Bluetooth, **every** switch works with the
    key off, including those programmed as Ignition. Battery-mode outputs that
    are on stay on if the connection drops[^m-p7]. To make a switch always available,
    program it as Battery instead.

!!! note "Output wire gauge"
    The 14 AWG output wires are good for 20 A on runs up to 6 ft. For longer
    runs at full current, SwitchPros recommends 12 or 10 AWG[^m-p3]. Size each
    run to its actual load, and set that output's current limit to protect
    the wire. This matches the owner's minimal-wire preference from the LJ build.

---

## Trigger Inputs {#trigger-inputs}

Both inputs are used as triggers, and backlight dimming is dropped (owner
decision, 2026-09-24). The white wire can either dim the backlight or act as
Trigger 2, not both. SwitchPros says Lights/T2 must stay disabled as a trigger
if it dims the backlight, and the backlight can only be adjusted while the
white wire sees 12 V[^m-p5] [^m-p10]. With white used as a trigger, the
backlight stays at one fixed brightness.

| Input | Wire | Signal | App setup | Outputs it turns on |
| :---- | :--- | :----- | :-------- | :------------------ |
| Trigger 1 | Pink | Reverse lamp | Enable. Active high, to be confirmed with a meter. | Not yet assigned (up to 4) |
| Trigger 2 | White | High beam | Lights/T2 set to Enable, converting it to a trigger. Active high, to be confirmed with a meter. | Not yet assigned (up to 4) |

Outputs that a trigger turns on can still be switched on and off from the
panel[^m-p5].

---

## Switch Panel Mount {#panel-mount}

| Location | Mount | Fitment | Notes |
| :------- | :---- | :------ | :---- |
| Center, top of dash | Motobilt MB8002 Dash Mount | Listed as "Custom Fit for 07-11 Jeep JK/JKU"[^motobilt]. **A 2012 is outside the listed fitment.** | Confirm with Motobilt that it fits a 2012 before buying |
| A-pillar | SwitchPros A-pillar replacement panel | "fits 2011-2017 Jeep Wrangler JK", and works with the SP9100[^sp-apillar] | Replaces the A-pillar trim panel. Comes pre-machined for the switch panel. |

The 10.5 ft control cable cannot be shortened or lengthened[^m-p6]. Check
that it reaches the chosen location from the power module before committing.

---

## Switch Assignments {#switch-assignments}

| Switch | Rating | Load | Draw | Current limit | Mode |
| :----: | :----: | :--- | :--: | :-----------: | :--- |
| 1 | 20 A | Unassigned | - | - | - |
| 2 | 20 A | Unassigned | - | - | - |
| 3 | 20 A | Unassigned | - | - | - |
| 4 | 20 A | Unassigned | - | - | - |
| 5 | 35 A | Unassigned | - | - | - |
| 6 | 35 A | Unassigned | - | - | - |
| 7 | 35 A | Unassigned | - | - | - |
| 8 | 35 A | Unassigned | - | - | - |

Any load over 20 A must go on switches 5-8.

---

## Outstanding Items

- [ ] Assign loads to switches 1-8, recording each load's draw, then set each output's current limit and its Battery or Ignition mode
- [ ] Choose the power module location, within 2 ft of the AUX battery, vertical, connectors facing outward, clear of the exhaust
- [ ] Plan how the 4 AWG cable and the 18 AWG ground reach the AUX posts under the Genesis top lid. The kit includes extra grommets for accessory wires.
- [ ] Choose the switch panel location: center dash (Motobilt MB8002, confirm 2012 fit first) or A-pillar (SwitchPros replacement panel)
- [ ] Pick the ignition-switched fuse in the 2012 JK's TIPM for the light blue wire's add-a-circuit. The wire must read 0 V with the key off.
- [ ] Pick which outputs Trigger 1 (reverse) and Trigger 2 (high beam) each turn on
- [ ] Find the reverse-lamp and high-beam tap points on the 2012 JK, and meter each one to set active high or active low
- [ ] Set the low-voltage disconnect threshold (11.0, 11.5, or 12.0 V) to suit the AUX battery type
- [ ] Choose the firewall pass-through for the 10.5 ft control cable. Removing the black 4-pin connector is allowed; the white connector is not serviceable.

## Related Documentation

- [Dual Battery System][dual-battery] - Genesis kit and the AUX battery that feeds the SP-9100
- [Power Systems][power-systems] - System overview
- [LJ SwitchPros SP-1200][lj-sp1200] - The larger RCR-Force 12 on the LJ build

[manual-rev21]: https://www.switchpros.com/wp-content/uploads/SP9100-Rev-2.1-Oct-2024-Final.pdf
[manual-rev16]: https://www.switchpros.com/wp-content/uploads/SP9100-Rev1.6-Directions-00285489.pdf
[dual-battery]: 01-dual-battery.md
[power-systems]: index.md
[lj-sp1200]: ../../jeep_lj/05-control-interfaces/02-switchpros-sp1200.md

[^m-p1]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 1, "Key Installation Points".
[^m-p2]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 2, "SP9100 Specifications" and §1.1 "Mounting Options".
[^m-p3]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 3, §2.1 "Mounting Guidelines" and §3.1 "Output Wires".
[^m-p4]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 4, §3.2 "Black Ground Wire" and §3.3 "Input Wires".
[^m-p5]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 5, §3.3 (Pink Trigger 1 Wire) and §4.1 "Battery Cable".
[^m-p6]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 6, §5.1 "Communications Cable".
[^m-p7]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 7, §6.2 "How to Connect".
[^m-p8]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 8, §7.1 "Configure Switches" (Low Voltage Disconnect).
[^m-p9]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), p. 9, §7.7 "Set Auto Sleep Settings".
[^m-p10]: SwitchPros SP9100 installation manual, Rev 2.1 (Nov 2024), pp. 9-10, §7.8 "External Trigger Setup".
[^motobilt]: Motobilt, "Dash Mount for Jeep JK/JKU 07-11 for Switch-Pros Unit", MB8002, <https://motobilt.com/products/dash-mount-for-switch-pros-controller-for-jeep-jk-jku> (accessed 2026-09-24). The page lists 2007-2011 fitment only, and Motobilt's switch panel mount collection (<https://motobilt.com/collections/switch-panel-mount>) has no JK mount for 2012 or later.
[^sp-apillar]: Switch-Pros, "A-pillar replacement panel", <https://store.switchpros.com/a-pillar-replacement-panel/> (accessed 2026-09-24). "Black, fits 2011-2017 Jeep Wrangler JK"; "Compatible with SP8100-B and SP9100 systems"; switch panel not included.
