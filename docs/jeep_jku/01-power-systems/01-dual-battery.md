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

**Kit:** Genesis Offroad JK Dual Battery Kit, with the Genesis smart combiner (generation to be confirmed)

**Part Number:** 131-JKDBK2AG3 is the current Gen 3 kit[^genesis-gen3]. Confirm this against the installed kit.

**Product Page:** [Gen 3 JK Dual Battery Kit][genesis-gen3]

**Install Video:** [Genesis Offroad installation videos][genesis-install]

**Charging Between Batteries:** Genesis smart combiner only. There is **no DC-DC charger**. The Nissan NV's Genesis tray pairs with a REDARC BCDC Alpha 50 ([NV Batteries & Charging][nv-batteries]), but the JK does not use one.

**Batteries:** Two matching Group 34 (make and model not yet recorded)

///

## How It Works {#how-it-works}

The combiner links the two batteries while charging and separates them when
voltage falls. Genesis says it separates the batteries once voltage stays
below ~12.7 V for about a minute[^genesis-gen3]. With the engine off,
accessories on the power bus bar then draw only from the AUX battery, and the
cranking battery is held in reserve.

The power bus bar is on the **AUX** side. Genesis's solar FAQ says a charger
on the bus bars charges the auxiliary battery first, and reaches the cranking
battery only once the combiner links them[^genesis-gen3].

| Boost switch mode | Behavior[^genesis-gen3] |
| :---------------- | :---------------------- |
| **Auto** | Links the batteries automatically based on their voltage |
| **On** | Links the batteries manually, like jumper cables, to help start the engine |
| **Off** | Separates the batteries manually |

---

## Specifications {#specifications}

| Item | Value | Source |
| :--- | :---- | :----- |
| Combiner rating, current Gen 3 | 300 A continuous; 500 A for 5 min; 2,000 A for 5 s | [^genesis-gen3] |
| Combiner rating, older listing | "200 Amp Isolator" in a reseller listing for the same P/N | [^dales] |
| Inter-battery cable | 2 AWG pure copper welding cable, tin-plated copper lugs | [^genesis-gen3] |
| Bus bars | Positive and negative, each with 3/8", 5/16", and 1/4" studs plus three #10 screws | [^genesis-gen3] |
| Batteries | Matching Group 34 required, not included. Optima is not compatible. | [^genesis-gen3] |
| Battery orientation | Group 34R has its posts in the wrong orientation | [^genesis-diy] |
| Fitment | 2007-2011 and 2012-2018 variants | [^genesis-gen3] |

!!! warning "Two combiner ratings in circulation"
    Genesis's current page rates the combiner at 300 A continuous. A reseller
    listing for the same part number still says 200 A. The power hub has
    changed across revisions, so read the rating off the label on the
    installed unit before relying on either figure (see Outstanding Items).

**Maintenance charging:** Genesis says to connect a charger to the factory
positive cable on the cranking battery and the factory negative cable on the
AUX battery[^genesis-gen3].

---

## Loads on the Bus Bars {#loads}

| Load | Bus bar | State | Notes |
| :--- | :------ | :---- | :---- |
| SwitchPros SP-9100 | Power (AUX), proposed | Planned | 125 A in-line fuse on the SwitchPros battery cable. See [SwitchPros SP-9100][sp9100] |
| Existing accessories | - | Not yet inventoried | See Outstanding Items |

---

## Outstanding Items

- [ ] Confirm the installed kit's generation and part number
- [ ] Read the combiner's continuous rating off the installed unit's label (300 A current Gen 3, or 200 A older listing)
- [ ] Record the JK's model year and engine. The kit ships in 2007-2011 and 2012-2018 variants.
- [ ] Record both batteries' make, model, and Ah rating
- [ ] Record where the boost switch is mounted, and confirm it is wired
- [ ] Inventory everything already landed on the power and ground bus bars, with each wire's gauge and fuse

## Related Documentation

- [Power Systems][power-systems] - System overview
- [SwitchPros SP-9100][sp9100] - Main accessory load on the AUX side
- [Nissan NV Batteries & Charging][nv-batteries] - The same Genesis tray, run with a BCDC Alpha 50

[genesis-gen3]: https://www.genesisoffroad.com/products/gen3-jk-dual-battery-kit
[genesis-install]: https://www.genesisoffroad.com/pages/installation-video
[power-systems]: index.md
[sp9100]: 02-switchpros-sp9100.md
[nv-batteries]: ../../nissan_nv/01-power-systems/02-batteries-charging.md

[^genesis-gen3]: Genesis Offroad, "2007-2018 Jeep Wrangler JK Gen 3 Dual Battery System" product page, SKU 131-JKDBK2AG3, <https://www.genesisoffroad.com/products/gen3-jk-dual-battery-kit> (accessed 2026-09-24). Sources the combiner rating, the ~12.7 V separation behavior, the boost switch modes, cable, bus bar, battery, and fitment details, and the solar and maintenance-charger FAQs.
[^dales]: Dale's Super Store listing, "Genesis Offroad Gen 3 Dual Battery System 200 Amp Isolator 131-JKDBK2AG3" (accessed 2026-09-24): <https://dalessuperstore.com/i-23914212-genesis-offroad-gen-3-dual-battery-system-200-amp-isolator-131-jkdbk2ag3-2012-2018-jeep-wrangler-jk-3-6l.html>. The 200 A figure appears only in the listing title.
[^genesis-diy]: Genesis Offroad, "2007-2018 Jeep Wrangler JK DIY Kit" product page, SKU 131-JKDIY, <https://www.genesisoffroad.com/products/jk-diy-dual-battery-kit> (accessed 2026-09-24).
