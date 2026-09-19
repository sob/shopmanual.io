---
hide:
  - toc
tags:
  - starlink
  - power-distribution
---

# 1.1 Starlink Power {#starlink-power}

Starlink runs off a **Starlink Advanced Power Supply** fed directly from the
van's 12 V DC system. This replaces the 1000 W AC inverter the dish was
originally powered through, and closes [#4][issue-4].

![Nissan NV 3500 Starlink power - Rear Powerswitch (B) feeding the Starlink Advanced Power Supply, which feeds the dish over the Starlink cable](../images/van-starlink-power.png)

*Diagram source: `Van Electrical.drawio` (page "Starlink v3"); the image is regenerated from the draw.io file on each export.*

---

## Why this replaced the inverter {#why}

The original install ran 12 V → 1000 W inverter → 120 V AC → the Starlink AC
brick → PoE to the dish. Two DC/AC/DC conversions in series, with the inverter
sitting idle-drawing whenever Starlink was on.

The alternatives worked through in [#4][issue-4] were all worse:

| Option | Why it was dropped |
| :----- | :----------------- |
| Keep the inverter | Conversion losses and inverter idle draw; the thing it was there for is now solved upstream |
| 24 V or 48 V sub-bank for the dish | Needs a second battery chemistry/voltage in the van, its own DC-DC charger, and re-plumbing everything else to 24 V |
| Generic step-up PoE injector | The PoE injector documentation calls for a high-quality supply; unbranded 12→48 V buck/boost injectors were not trusted at 320 W |
| **Starlink Advanced Power Supply** | **Takes 12 V DC natively, is the vendor's own part, and drops both the inverter and the third-party injector out of the path** |

---

## Advanced Power Supply {#advanced-power-supply}

| Spec | Value | Source |
| :--- | :---- | :----- |
| Input | 100-240 V AC **or** 12-56 V DC | [Starlink Performance spec sheet][spec-sheet] |
| DC certified range | 10.5-57 V DC | [Starlink support][dc-support] |
| Recommended DC input | Above 20 V where available | [Starlink support][dc-support] |
| DC current limit | Self-limits to under 20 A; output power is reduced at low input voltage to stay there | [Starlink support][dc-support] |
| Ports | High-power PoE (to the dish) + LAN | [Starlink Performance spec sheet][spec-sheet] |
| Dimensions | 310 x 180 x 40 mm (12.2 x 7.1 x 1.6 in) | [Starlink Performance spec sheet][spec-sheet] |
| Weight | 2.1 kg (4.6 lb) | [Starlink Performance spec sheet][spec-sheet] |
| Environmental | IP68 with cables installed, -40 °C to 60 °C | [Starlink Performance spec sheet][spec-sheet] |
| DC cable supplied | Starlink DC Power Cable, 1.5 m, 2-pin (red +, black −) | [Starlink Performance spec sheet][spec-sheet] |

!!! warning "12 V is the bottom of the useful range"
    Starlink certifies the supply down to 10.5 V but **recommends staying above
    20 V**. On a 12 V bank the supply caps itself at under 20 A, so peak
    delivery is roughly 240 W before conversion losses. That covers a dish
    averaging 75-100 W, but snow-melt and high-throughput peaks are exactly the
    conditions where the supply will throttle. An AGM bank sagging toward
    11.5 V under load gives away more headroom still.

    If Starlink performance turns out to be capped in cold weather, the fix is
    a higher input voltage (a 24 V sub-bank on a DC-DC charger), not a bigger
    12 V feed.

---

## Circuit {#circuit}

The supply is switched from **Rear Powerswitch (B)**, alongside the Twinkle
Lights and the two 5 V USB-C buck converters that run the UniFi gear.

| Item | Value |
| :--- | :---- |
| Source | Rear Powerswitch (B), AUX battery side |
| Nominal system voltage | 12 V DC |
| Design current | Size the feed and breaker for **20 A** - the supply's own self-limit |
| Supplied DC cable | 1.5 m, 2-pin (red +, black −) |
| Output to dish | Starlink cable, PoE |

!!! note "Size for 20 A, not for average draw"
    The dish averages 75-100 W, which at 12 V is only 6-9 A. Do not size the
    circuit on that number. The supply will pull up to its own ~20 A limit
    during snow melt and cold-start, so the breaker, the wire, and the
    Powerswitch circuit all need to carry 20 A continuously.

---

## What this removes {#what-this-removes}

Both of these come out of the Starlink path:

- **1000 W inverter** - still shown on the [Current State and Genesis
  diagrams](../02-diagrams/index.md), which document the system as it was
  before this change. It may still be wanted for other AC loads; that is a
  separate decision.
- **Third-party PoE injector** - the Yaosheng 8 A injector and its modified
  PoE cable, shown on the superseded "Starlink v2" page.

---

## Outstanding Items

- [ ] Confirm which dish is in the van (High Performance / Flat High Performance vs. Performance) and that the Advanced Power Supply is the supported supply for it
- [ ] Confirm the dish-side cable - whether the existing run reuses the modified PoE cable or is replaced by a stock Starlink cable
- [ ] Measure real-world draw at 12 V (idle, streaming, snow melt) and record it here
- [ ] Pick the breaker size and wire gauge for the Rear Powerswitch (B) circuit and record the run length
- [ ] Decide where the LAN port lands - UXG Lite WAN, or the USW-Flex-Mini
- [ ] Record the mounting location and orientation of the supply

[issue-4]: https://github.com/sob/shopmanual.io/issues/4
[spec-sheet]: https://starlink.com/public-files/specification_sheet_performance.pdf
[dc-support]: https://starlink.com/support/article/d92539dd-f4f6-df83-284a-33cc48fe35b5
