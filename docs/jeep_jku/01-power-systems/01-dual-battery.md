---
hide:
  - toc
tags:
  - product-details
  - batteries
  - power-distribution
---

# 1.1 Dual Battery System {#dual-battery}

/// html | div.product-info

**Vehicle:** 2012 Jeep Wrangler JKU, 3.6L

**Kit:** Genesis Offroad JK Dual Battery Kit, an **older generation** (earlier than the current Gen 3), with the Genesis smart isolator

**Part Number:** Not recorded

**Install Video:** [Genesis Offroad installation videos][genesis-install]

**Charging Between Batteries:** Genesis smart isolator only. There is **no DC-DC charger**. The Nissan NV's Genesis tray pairs with a REDARC BCDC Alpha 50 ([NV Batteries & Charging][nv-batteries]), but the JK does not use one.

**Batteries:** Two Odyssey AGM Group 34, the same as the [Nissan NV][nv-batteries]

///

## How It Works {#how-it-works}

The older kit's smart isolator connects the batteries once the cranking
battery reaches 13.2 V, so the alternator charges both batteries. It
separates them when the cranking battery falls to 12.7 V, which keeps enough
charge in the cranking battery to start the engine[^tft].

Accessories on the kit's power and ground bus bars run from the AUX
battery[^tft].

**Start Boost button:** pressing it connects both batteries for 1 minute,
like built-in jumper cables. The system then returns to automatic
mode[^tft].

---

## Specifications {#specifications}

These figures are for the older kit, from a reseller listing[^tft].

| Item | Value |
| :--- | :---- |
| Isolator rating | Sold with either a **standard 85 A** or an **upgraded 200 A** isolator. Which one this JK has is not yet known. |
| Isolator connect / separate | Connects at 13.2 V; separates at 12.7 V (cranking battery) |
| Inter-battery cable | Flexible 2 AWG |
| Bus bars | Power and ground. High-amp loads such as a winch go on the large center post; smaller loads go on the screw terminals. |
| Batteries | Any Group 34 |
| Kit contents | Tray, top lid, smart isolator, boost switch, power and ground bus bars, all wiring, fuse box mount, evap solenoid mount and hoses |

!!! note "Current Gen 3 specs do not apply"
    The current Gen 3 kit (P/N 131-JKDBK2AG3) has a 300 A combiner and an
    Auto/On/Off boost switch[^genesis-gen3]. This JK has the older kit, so
    use the 85 A or 200 A rating printed on the installed isolator instead.

---

## Loads {#loads}

| Load | Connection | State | Notes |
| :--- | :--------- | :---- | :---- |
| SwitchPros SP-9100 | **Direct to the AUX battery posts**, not the bus bars | Planned | Supplied 4 AWG cable with a 125 A in-line fuse. See [SwitchPros SP-9100][sp9100] |
| Power and ground bus bars | - | Nothing connected (2026-09-24) | - |

The SP-9100 connects to the AUX battery, not to the isolator, so its load
never passes through the isolator.

---

## Outstanding Items

- [ ] Read the isolator's rating (85 A or 200 A) off its label, and record the kit's part number if it is marked
- [ ] Record the exact Odyssey model number and Ah rating of both batteries
- [ ] Record where the Start Boost button is mounted, and confirm it works
- [ ] Identify which physical battery in the tray is AUX, so the SP-9100 lands on the correct posts

## Related Documentation

- [Power Systems][power-systems] - System overview
- [SwitchPros SP-9100][sp9100] - Main accessory load, wired directly to the AUX battery
- [Nissan NV Batteries & Charging][nv-batteries] - The same Genesis tray and batteries, run with a BCDC Alpha 50

[genesis-install]: https://www.genesisoffroad.com/pages/installation-video
[power-systems]: index.md
[sp9100]: 02-switchpros-sp9100.md
[nv-batteries]: ../../nissan_nv/01-power-systems/02-batteries-charging.md

[^tft]: Toys For Trucks listing, "JK Dual Battery Kit 200 Amp Isolator 07-11 Wrangler JK Genesis Offroad" (P/N GEN-131-JKDBKE2A-FWMW), <https://www.toysfortrucksofficial.com/product/jk_dual_battery_kit_200_amp_isolator_07_11_wrangler_jk_genesis_offroad> (accessed 2026-09-24). This is the older, pre-Gen 3 kit in its 2007-2011 fitment. It is the source for the 85 A and 200 A isolator options, the 13.2 V and 12.7 V thresholds, the 1-minute Start Boost, the AUX-side bus bars, the 2 AWG inter-battery cable, and the kit contents. The 2012+ version was not checked separately.
[^genesis-gen3]: Genesis Offroad, "2007-2018 Jeep Wrangler JK Gen 3 Dual Battery System" product page, SKU 131-JKDBK2AG3, <https://www.genesisoffroad.com/products/gen3-jk-dual-battery-kit> (accessed 2026-09-24).
