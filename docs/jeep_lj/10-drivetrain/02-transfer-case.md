---
tags:
  - product-details
  - drivetrain
  - transfer-case
---

# 10.2 - Transfer Case {#transfer-case}

/// html | div.product-info

**Model:** NV241 GenII (Command-Trac)

**Source:** 2012 Jeep Wrangler JK Unlimited Sport

**Type:** Part-time 4WD with 2.72:1 low range

///

## Specifications

| Specification | Value |
| :------------ | :---- |
| Model | NV241 GenII (Command-Trac)[^model] |
| Source | 2012 Jeep Wrangler JK Unlimited Sport |
| Type | Part-time 4WD, two-speed |
| Low Range Ratio | 2.72:1[^lowrange] |
| High Range Ratio | 1.0:1 |
| Rear Output | 32-spline, fixed yoke[^output] |
| Input | Adapter-dependent — mates to 8HP70 via adapter[^input] |

## Gear Ratios

| Mode | Ratio |
| :--- | :---- |
| 2WD High | 1.00:1 |
| 4WD High | 1.00:1 |
| Neutral | N/A |
| 4WD Low | 2.72:1 |

## Crawl Ratio

With the 8HP70's deep first gear, the shallower Sport low range still yields a usable crawl ratio:

| Component | Ratio |
| :-------- | :---- |
| 8HP70 1st gear | 4.714[^trans] |
| Transfer case low | 2.72 |
| Axle (Revolution) | 5.13 |
| **Crawl ratio** | **≈ 65.8:1** (illustrative) |

The deep 8HP70 first gear largely compensates for the 2.72:1 low range — a 4:1 Rock-Trac with the same gearing would give ≈96.7:1. ≈66:1 is a usable trail crawl ratio for this build.

## Selection Notes

Chosen over the TJ Rubicon NP241OR Rock-Trac (4:1) deliberately:

- **Crawl speed (primary reason):** paired with the 8HP70 (automatic), a 4:1 case gives ≈96.7:1 geared — and the torque converter multiplies torque further at low speed, pushing the effective crawl far deeper. That is too slow to hold momentum on most terrain. An automatic wants a numerically lower geared crawl than a manual because the converter handles creep; ≈66:1 is the better target.
- **Strength:** a wash — both share the NP241 case, 1.25" chain, and 32-spline output, and the R2.8's torque is well within either. The Rock-Trac's reinforced 4:1 planetary is the heavier-duty variant but is not needed here.

## Adapter (8HP70 → NV241)

**An adapter is required — there is no native bolt-up.** The 8HP70 is not the case's factory transmission, so it mates through a transmission-to-transfer-case adapter. The 8HP70 output and the required NV241 input gear are both **23-spline**, so a 23-spline interface is the clean path.[^adapter]

The 8HP *family* does pair with an NV241 from the factory — the JL Wrangler automatic bolts an 850RE/8HP75 to one — **but the Ram EcoDiesel 8HP70's bolt pattern only *resembles* the Jeep 850RE; it is not interchangeable.** So this transmission needs an adapter to **any** NV241 (JK or JL), and the transmission is fixed (Turbolamik TCU + Kilduff shifter are spec'd to the 8HP70).[^why-adapter]

- **Recommended — DomiWorks 24004001:** purpose-built for the 8HP70/75 EcoDiesel Ram 1500 → NP231/241 family; adjustable case tilt. ≈8,495 SEK (~$800–900 USD + import). **Includes only the adapter + integral crossmember bracket** — see the parts list below.[^adapter]
- **Alternative — Advance Adapters:** no off-the-shelf 8HP70 → stock NV241 kit. Their 8HP70 tooling (output assembly 50-9905, housing 51-9905) is built to mate to an Atlas; their NV241-JK input gears (52-9940 32-spline, 52-9945 29-spline) are cut for GM transmissions, not the 8HP70's 23-spline output. Call to spec a 23-spline build, or go Atlas.

### Full parts list (DomiWorks path)

| Part | Source | Notes |
| :--- | :----- | :---- |
| Adapter 24004001 | DomiWorks | Adapter + crossmember bracket only |
| 23-spline NV241 input gear (ZTNP22390 or equiv.) | Transmission parts supplier | Swaps into the case (teardown) |
| NV241 input bearing + front seal | Rebuild parts | Replace during the input-gear swap |
| Grade-10.9 mounting hardware | — | Adapter-to-trans / adapter-to-case bolts |
| Spacer plate | DomiWorks | **Only if** 8HP70 output protrusion exceeds the standard 96 mm |

**On the 8HP70 (transmission) side**, the only DomiWorks part is the conditional spacer plate. The 8HP70's factory output shaft is used as-is — it is already a 4WD/transfer-case output (this is a 4x4 Ram donor) and engages the 23-spline input gear directly through the adapter; no coupler or output adapter is needed from DomiWorks.

**Critical measurement:** check the 8HP70 output-shaft protrusion before ordering — DomiWorks' standard fit is ~96 mm; longer EcoDiesel outputs need the spacer plate (or the axle shortened). Also confirm the donor JK case's input-gear spline before buying the 23-spline replacement.

## Fluid Specifications

| Specification | Value |
| :------------ | :---- |
| Fluid Type | ATF+4[^fluid] |
| Capacity | ≈1.6 L (3.4 pt); fill to overflow[^fluid] |

[^tc-ratio]: The 2012 Jeep Wrangler JK Command-Trac (NVG241 Gen II) low-range ratio is **2.72:1** per Jeep factory specification; the 4.0:1 unit is the Rubicon-only Rock-Trac (NV241OR), which this build no longer uses. Confirm against the JK FSM transfer-case section when finalizing crawl-ratio math.

## Outstanding Items

- [ ] Measure 8HP70 output-shaft protrusion (≤~96 mm, else order DomiWorks spacer plate or shorten)
- [ ] Order: DomiWorks 24004001 adapter; 23-spline NV241 input gear (ZTNP22390 or equiv.); NV241 input bearing + front seal; grade-10.9 hardware
- [ ] Confirm donor JK case input-gear spline before swapping to the 23-spline gear

## Vendor Inquiry — DomiWorks (draft)

Draft email to confirm fitment and parts before ordering:

```text
Subject: Adapter fitment — Ram 1500 EcoDiesel 8HP70 → Jeep JK NP241 (2.72:1)

Hi DomiWorks,

I'm mating a Ram 1500 EcoDiesel 8HP70 (4x4) transmission to a 2012 Jeep
Wrangler JK Sport NP241 transfer case (NV241 GenII Command-Trac, 2.72:1)
and want to confirm the right parts before ordering.

1. Is adapter SKU 24004001 the correct unit for this 8HP70 EcoDiesel →
   NP241 combination?

2. Output protrusion / spacer plate: where exactly do I measure the
   8HP70 output-shaft protrusion from, and what is the cutoff for needing
   the spacer plate? Is the spacer available for the EcoDiesel output,
   and what does it cost?

3. Input gear: do you supply the 23-spline NP241 input gear (ZTNP22390
   or equivalent), or should I source that separately?

4. Bearing / seal / hardware: can you include the NP241 input bearing,
   front seal, and mounting hardware, or are those separate?

5. Lead time and shipping cost to the US (state: ____)?

Donor details:
- Transmission: ZF 8HP70 (Chrysler 845RE), 2015–2019 Ram 1500 EcoDiesel, 4x4
- Transfer case: 2012 Jeep JK Sport NP241 (2.72:1 low range)

Thanks,
[name]
```

## Related Documentation

- [Transmission][transmission]
- [Driveshafts][driveshafts]

[transmission]: 01-transmission.md
[driveshafts]: 03-driveshafts.md

[^model]: 2012 Jeep Wrangler JK Sport uses the NV241 GenII "Command-Trac" part-time, two-speed transfer case (owner-confirmed donor: 2012 JK Unlimited Sport). Manual-trans JK variant is designated NV241J. Quadratec 2012 JK specs / Novak Conversions, accessed 2026-05-31.
[^lowrange]: Low range **2.72:1** — the standard JK Sport (non-Rubicon) Command-Trac ratio; the 4:1 is the Rubicon-only Rock-Trac (NV241OR). Quadratec/ExtremeTerrain 2012 JK Sport drivetrain specs, accessed 2026-05-31. Owner-confirmed stock — not re-geared (2026-05-31).
[^output]: NV241 family rear output: **32-spline**, fixed yoke (no slip-yoke). Novak Conversions / Advance Adapters NVG241 references, accessed 2026-05-31. Confirm on the actual unit.
[^input]: Stock JK NP241 input is 23-spline (manual/NSG370) or 29-spline (auto) depending on donor — moot here, since the case mates to a ZF 8HP70, not its factory transmission. The 8HP70 (Ram) output is **23-spline, ~4" stickout** (Advance Adapters). Mating uses a transmission-to-transfer-case adapter that supplies a new NP241 input gear: Advance Adapters lists JK NP241 (2.72:1) adapter components; DomiWorks Engineering and LOJ Conversions offer 8HP/ZF8 adapter kits as alternatives. Confirm exact output spline/stickout for the EcoDiesel 8HP70 variant when ordering. Accessed 2026-05-31.
[^trans]: ZF 8HP70 (Chrysler 845RE) 1st-gear ratio 4.714 — see [Transmission][transmission].
[^fluid]: NV241 GenII service fluid: **ATF+4**, capacity ≈1.6 L (3.4 pt), filled to the fill-plug overflow. JK NV241 service references (project-jk.com / wranglerjkforum.net), accessed 2026-05-31. Verify against the FSM at service.
[^adapter]: Advance Adapters (8HP70 output 50-9905 $642.51 / housing 51-9905 $371.11; NP241-JK input gears 52-9940 32-spline, 52-9945 29-spline) and DomiWorks 24004001 (≈8,495 SEK), accessed 2026-05-31; prices subject to change. The 8HP70 (Ram) output is 23-spline; Advance Adapters' 6L80→JK NP241 kit (50-9940) confirms the NP241-JK input shaft is 23-spline. DomiWorks specifies a 23-spline input gear (ZTNP22390).
[^why-adapter]: JL Wrangler automatics pair an 8HP-family transmission (850RE Chrysler / 8HP75 ZF) with the NV241, but the Ram EcoDiesel 8HP70 bolt pattern is only *similar* to the Jeep 850RE — and even the 850RE and 8HP75ZF use different connections (Jeep sells a ~$300 adapter between them). A direct Ram-8HP70-to-JL-case kit has been discussed but is not on the market. jlwranglerforums.com 8-speed swap PSA / Advance Adapters 5054 (JL 850RE / Dodge 8HP70 → Atlas), accessed 2026-05-31.
