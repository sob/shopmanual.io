---
hide:
  - toc
tags:
  - product-details
  - audio-systems
  - jl-audio
---

# 6.4 Subwoofers {#subwoofer}

Pair of 8" infinite baffle marine subwoofers with RGB LED lighting, mounted symmetrically in the rear quarter panels.

/// html | div.product-info
**Type:** 8" Infinite Baffle Marine Subwoofer

**Model:** M6-8IB-S-GmTi-i-4

**Manufacturer:** JL Audio

**Product Page:** [M6-8IB-S-GmTi-i-4][product-link]

**Quantity:** 2 (pair)

**Mounting:** Rear quarter panels (one per side, above wheel wells, firing inward)

**Power Source:** Amplifier Channels 1+2 bridged @ 4Ω → Sub A; Ch 3+4 bridged @ 4Ω → Sub B (one dedicated bridged pair per sub)

///

## Specifications (per sub)

| Spec               |                Value |
| :----------------- | -------------------: |
| Power Handling     |        200W RMS @ 4Ω |
| Impedance          |              4Ω SVC |
| Sensitivity        |        ~85 dB @ 1W/1m |
| Voice Coil         |                  2" |
| Overall Diameter   |              ~9.5" |
| Mounting Depth     |              ~4.25" |
| Weight             |             ~7 lbs |
| Warranty           |              3 years |

## Wiring Configuration {#wiring}

Each sub runs on its own dedicated bridged channel pair on the JL Audio MV800/8i — Sub A on Ch 1+2 bridged, Sub B on Ch 3+4 bridged, both at 4Ω. This is an exact RMS match to the sub's 200W @ 4Ω rating, with no series compromise and independent per-sub gain/EQ/delay via the amp's onboard DSP.

| Wiring                    |  Per-Sub Load  | MV800/8i Output | Per Sub  | Safe? |
| :------------------------ | :------------: | :-------------: | :------: | :----: |
| **Bridged @ 4Ω per sub**  |       4Ω       |      200W       | **200W** | ✅ 100% of RMS rating |
| Parallel both on one pair |       2Ω       |  n/a (bridged minimum is 4Ω) |   n/a    | ❌ Below bridged minimum |

**Wiring path (per sub, both pairs identical):**

```
Amp Ch 1+2 (+/−) bridged → Sub A (+/−)
Amp Ch 3+4 (+/−) bridged → Sub B (+/−)
```

Independent gain trim per side is available if the L/R quarter-panel locations end up acoustically asymmetric.

## Infinite Baffle Requirements

- **Minimum air volume:** 0.75 cu ft per sub (1.5 cu ft pair)
- **Installation type:** No dedicated enclosure required
- **Ideal location:** Rear quarter panels above wheel wells, firing inward into cabin
- **IB chamber:** Rear cargo area / behind quarter trim (effectively unlimited volume in an LJ)

## Features

- Transflective RGB LED lighting (via MLC-RW)
- Gunmetal trim ring with titanium sport grille
- Marine-grade construction
- Mica-filled polypropylene cone
- Synthetic rubber surround

## Wiring

| Connection            | Wire   | Notes                                              |
| :-------------------- | :----- | :------------------------------------------------- |
| Sub A (+) / (−)       | 14 AWG | From amp Ch 1+2 bridged to Sub A voice coil        |
| Sub B (+) / (−)       | 14 AWG | From amp Ch 3+4 bridged to Sub B voice coil        |
| LED                   | 20 AWG | RGB from MLC-RW (one tap per sub)                  |

Standard speaker wire (no XM-WHTMFC needed for subwoofer audio). No series jumper between subs — each sub returns directly to its own bridged channel pair.

## Why Two 8" vs Single 12"

The single 12" M7-12IB option (600W RMS, 14" overall diameter, 7.94" mounting depth, requires 3+ cu ft IB chamber) was ruled out for LJ-specific install reasons:

- **Mounting depth:** 7.94" of basket depth makes most LJ panels impractical — cage tubes, wheel wells, and tailgate clearance all conflict.
- **Single-sub asymmetry:** harder to integrate cosmetically vs symmetric L/R 8" pair.
- **No matching 12" M6:** JL doesn't make a 12" M6-IB (M6 IB line tops at 10"), so the pair option doesn't exist at 12".

**Tradeoff accepted:** total sub output is 400W (2× M6-8IB on dedicated bridged pairs of the MV800/8i @ 4Ω each) vs ~580W for a single M7-12IB. About 70% of the single-12" output, but symmetric L/R placement, independent per-sub DSP, and a feasible mounting depth in the LJ quarter panels win out. Acceptable for a soft-top Jeep where wind noise dominates at highway speed anyway.

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Confirm exact mounting locations in rear quarter panels (clear of cage tubes and rear seatbelts)
- [ ] Verify quarter panel material can support sub weight + mounting torque (may need backing plate)
- [ ] Source M6-8IB-S product image (`docs/jeep_lj/images/jl-audio-m6-8ib-s-gmti-i-4.jpg`)

## Related Documentation

- [Audio Systems Overview][audio-overview]
- [Amplifier][amplifier]
- [LED Controller][led-controller]

[audio-overview]: index.md
[amplifier]: 02-amplifier.md
[led-controller]: 05-led-controller.md
[product-link]: https://www.garmin.com/en-US/p/1851253/
