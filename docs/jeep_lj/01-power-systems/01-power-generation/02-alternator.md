---
hide:
  - toc
tags:
  - product-details
  - power-generation
  - alternator
---

# 1.1.2 Alternator {#alternator}

/// html | div.product-info
![Premier Power Welder HO-C28 Alternator](../../images/premier-power-welder-ho-c28-alternator.jpg){ loading=lazy }

**Type:** High-Output Welding Alternator

**Model:** Premier Power Welder HO-C28

**Manufacturer:** Premier Power Welder

**Product Page:** [Cummins R2.8 270A Alternator][premier-alternator]

**Rating:** 270 amps

**Application:** Cummins R2.8 Turbo Diesel

**Price:** $899.95

///

## Specifications

- **Output:** 270A continuous
- **Voltage:** 12V (standard automotive)
- **Application:** Cummins R2.8 engines
- **Type:** High-output welding alternator
- **SKU:** HO-C28

## System Configuration

**Primary Function:** Charges START battery and powers vehicle electrical systems

**Output Capacity:** 270A continuous (exceeds system maximum draw of ~326A with margin)

**Mounting:** Direct bolt-on replacement for Cummins R2.8

## Wiring

| Connection      | Destination                        | Notes                                                            |
| :-------------- | :--------------------------------- | :--------------------------------------------------------------- |
| Positive Output | START battery+ (driver rear wheel well) | See [START Battery Distribution][starter-battery] for wire specs |
| Ground          | Engine block                       | Bonded via alternator mounting bolts                             |

**Ground Path:** Alternator case → Engine block → Engine bay ground bus → START battery- (driver rear wheel well)

See [START Battery Distribution][starter-battery] for complete wire specifications (gauge, distance, voltage drop calculations).

[starter-battery]: ../02-starter-battery-distribution/index.md

## Load Analysis

**Alternator Capacity:** 270A continuous

**Worst Realistic Load:** 218A (offroad scenario) = 52A margin (19% headroom)

The alternator supplies START battery loads plus BCDC charging. AUX battery loads (SwitchPros, ARB compressor, winch) do NOT draw from alternator.

See [START Battery Load Analysis][start-load-analysis] for complete scenario details.

## Outstanding Items

- [ ] Determine alternator positive output terminal size (for 1/0 AWG lug selection) — see [Vendor Inquiry](#vendor-inquiry) below
- [ ] Verify alternator voltage regulator set point (14.2–14.4V is the correct AGM target;[^agm-target] confirm the HO-C28 actually regulates there) — see [Vendor Inquiry](#vendor-inquiry) below

## Vendor Inquiry — Premier Power Welder (draft) {#vendor-inquiry}

Both open items above are answered by one email to Premier Power Welder:

```text
Subject: HO-C28 (Cummins R2.8 270A) — output stud size & regulator set point

Hi Premier Power Welder,

I'm wiring the HO-C28 270A alternator (Cummins R2.8) into a dual-battery
truck and need two specs to finish the install:

1. Output terminal: what is the thread/stud size of the positive output
   post? I'm sizing a ring lug for 1/0 AWG cable and want the correct
   stud diameter (e.g. 1/4"-20, 5/16"-18, M8, etc.).

2. Voltage regulation: what is the regulator set point, and is it
   suitable for AGM batteries (target ~14.2-14.4V at the battery)? Is the
   regulator internal and fixed, or adjustable? My START battery is AGM.

Application: HO-C28 on a Cummins R2.8 Repower, charging an AGM start
battery (~850 CCA).

Thanks,
[name]
```

## Related Documentation

- [Batteries][batteries] - START battery specifications (850 CCA)
- [START battery Distribution][starter-battery] - Alternator charging destination
- [Grounding Architecture][grounding] - Alternator ground path
- [Wire Distance Reference][wire-distance] - Alternator to battery routing distance

[premier-alternator]: https://premierpowerwelder.com/shop/high-output-welding-alternators/cummins-alternators/cummins-r2-8-270-amps-high-output-welding-alternator/
[batteries]: 01-batteries.md
[start-load-analysis]: ../08-load-analysis/02-start-battery.md
[grounding]: ../05-grounding/index.md
[wire-distance]: 05-wire-distance-reference.md

[^agm-target]: AGM batteries take an absorption/charge voltage of ~14.2–14.7V at the terminals (mfr range 14.0–14.7V), so the 14.2–14.4V target is correct; many stock regulators sit lower (13.8–14.0V) and undercharge AGM. The target is validated — what remains is confirming the HO-C28's actual set point (vendor or field measurement). General AGM charging references (Victron / battery-mfr guidance), accessed 2026-06-03.
