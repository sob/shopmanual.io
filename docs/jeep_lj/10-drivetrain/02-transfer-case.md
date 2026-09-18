---
tags:
  - product-details
  - drivetrain
  - transfer-case
---

# 10.2 - Transfer Case {#transfer-case}

/// html | div.product-info

**Model:** NP241OR (Rock-Trac)

**Source:** 2003-2006 Jeep Wrangler TJ/LJ Rubicon

**Type:** Part-time 4WD with 4.0:1 low range

///

## Specifications

| Specification | Value |
| :------------ | :---- |
| Model | NP241OR "Rock-Trac"[^model] |
| Source | 2003-2006 TJ/LJ Rubicon (Jeep-only application) |
| Type | Part-time 4WD, two-speed |
| Low Range Ratio | 4.0:1[^lowrange] |
| High Range Ratio | 1.0:1 |
| Modes | 2H, 4H, N, 4L[^model] |
| Rear Output | Centerline, fixed yoke[^output] |
| Front Output | Driver's side[^output] |
| Input | 23-spline short, 1-1/8" stickout (most common variant)[^input] |
| Weight | ≈90 lb[^model] |

## Gear Ratios

| Mode | Ratio |
| :--- | :---- |
| 2WD High | 1.00:1 |
| 4WD High | 1.00:1 |
| Neutral | N/A |
| 4WD Low | 4.0:1 |

## Crawl Ratio

| Component | Ratio |
| :-------- | :---- |
| 8HP70 1st gear | 4.714[^trans] |
| Transfer case low | 4.0 |
| Axle (Revolution) | 5.13 |
| **Crawl ratio** | **≈ 96.7:1** (geared) |

Behind an automatic the torque converter multiplies torque further at low speed, so effective crawl is deeper still than the geared figure suggests. That is the accepted tradeoff for the 4:1 — see Selection Notes.

## Selection Notes

The 4:1 Rock-Trac was chosen over the 2.72:1 JK Sport Command-Trac for the deeper low range (owner decision, 2026-09-18).

- **Ratio (primary reason):** 4:1 gives ≈96.7:1 geared versus ≈65.8:1 for the 2.72:1 case. The deeper range is the point — it trades the ability to hold momentum on fast terrain for genuine low-speed control on technical terrain.
- **Converter multiplication — accepted:** paired with the 8HP70 automatic, the converter multiplies torque below stall, pushing effective crawl deeper than 96.7:1. An automatic needs less geared reduction than a manual because the converter handles creep, so this setup will be very slow in 4L-1st. Accepted deliberately.
- **Native to the chassis:** the NP241OR is the factory TJ/LJ Rubicon case, so crossmember, floor shifter, linkage, and driveshaft geometry are native to this vehicle rather than adapted from a JK case. This is a real simplification over the previously spec'd JK unit.
- **Strength:** the Rock-Trac's reinforced 4:1 planetary is the heavier-duty variant of the NP241 family. The R2.8's torque is well within either case.

## Adapter (8HP70 → NP241OR)

!!! warning "Adapter path needs re-spec for the OR case"
    The adapter research below was done against a **JK NV241**. The case selection changed to the TJ/LJ **NP241OR**, and adapter fitment, the required input gear, and the parts list have **not** been re-confirmed for it — see {{ tbd(313) }}. Do not order against this section until DomiWorks confirms the OR application.

**An adapter is required — there is no native bolt-up.** The 8HP70 is not the case's factory transmission, so it mates through a transmission-to-transfer-case adapter.[^why-adapter]

Encouragingly, both sides are **23-spline**: the 8HP70 (Ram) output is 23-spline, and the most common NP241OR input is 23-spline short (1-1/8" stickout).[^input] Whether the OR case's existing input gear can be reused — or still needs the ZTNP22390-style replacement the JK path called for — is exactly what {{ tbd(313) }} must settle.

- **Candidate — DomiWorks 24004001:** built for the 8HP70/75 EcoDiesel Ram 1500 → **NP231/241 family**; adjustable case tilt. ≈8,495 SEK (~$800–900 USD + import). Includes only the adapter + integral crossmember bracket.[^adapter] The OR case is in the NP241 family, but family membership is not fitment confirmation.
- **Alternative — Advance Adapters:** no off-the-shelf 8HP70 → stock NP241OR kit. Their 8HP70 tooling (output assembly 50-9905, housing 51-9905) is built to mate to an Atlas. Their previously noted NP241 input gears are **JK-specific and no longer relevant** to this case. Call to spec a 23-spline build, or go Atlas.

### Provisional parts list (DomiWorks path — pending {{ tbd(313) }})

| Part | Source | Notes |
| :--- | :----- | :---- |
| Adapter 24004001 | DomiWorks | Adapter + crossmember bracket only; OR fitment unconfirmed |
| Input gear (spline/stickout per DomiWorks) | Transmission parts supplier | **May not be needed** if the OR case's 23-spline input is compatible |
| NP241OR input bearing + front seal | Rebuild parts | Replace if the input gear is swapped |
| Grade-10.9 mounting hardware | — | Adapter-to-trans / adapter-to-case bolts |
| Spacer plate | DomiWorks | **Only if** 8HP70 output protrusion exceeds the standard 96 mm |

**On the 8HP70 (transmission) side**, the only DomiWorks part is the conditional spacer plate. The 8HP70's factory output shaft is used as-is — it is already a 4WD/transfer-case output (this is a 4x4 Ram donor); no coupler or output adapter is needed from DomiWorks.

**Critical measurement:** check the 8HP70 output-shaft protrusion before ordering — DomiWorks' standard fit is ~96 mm; longer EcoDiesel outputs need the spacer plate (or the shaft shortened).

## Fluid Specifications

| Specification | Value |
| :------------ | :---- |
| Fluid Type | ATF+4 ({{ tbd(313) }} — confirm against the TJ FSM for the OR case) |
| Capacity | {{ tbd(313) }} — fill to the fill-plug overflow |

## 4WD Position Sensing {#position-sensing}

The dash 4WD and 4LO indicators are driven from the case's OEM position switch, translated by the PMU. The NP241OR is cable/lever-shifted and has no discrete position contact, so nothing on the case can ground the HDX 4x4 input directly.

**Sensor:** 5-position transfer case switch, OE **5083138AA** (Omix-Ada 18676.52) — a two-wire resistive plunger switch mounted **on top of the case**, riding the internal shift rail; each detent presents a different resistance.[^tc-switch] This switch is a **listed application for the 03-06 TJ NV241OR**, so the sensor should already be on the case — confirm on the actual unit and record its per-detent resistances ({{ tbd(145) }}).

### Signal chain

| Stage | Path | Active when |
| :---- | :--- | :---------- |
| Sense | Position switch → 18 AWG pair → [PMU An 1][pmu-inputs] (divider to 0-5V) | always |
| 4x4 indicator | [PMU OUT19][pmu-outputs] → [firewall pin 19][firewall-ingress] → relay coil (cabin) → contacts ground [HDX 4x4 terminal][hdx-control] | 4H **or** 4L |
| 4LO indicator | [PMU OUT24][pmu-outputs] → [firewall pin 20][firewall-ingress] → [HDX EXTRA(+)][hdx-control], label "4LO" | 4L only |

The HDX 4x4 terminal is ground-activated and EXTRA(+) is 12V-activated, so the 4LO leg drives the HDX directly from a PMU high-side output while the 4x4 leg needs a relay to sink it — the PMU switches high-side only.[^hdx-inputs]

!!! warning "Why the resistive sensor is not wired straight to the HDX"
    2H is the **highest**-resistance detent, not an open circuit, so whether the HDX's fixed input threshold falls between 2H and 4H is unknown — a bare-wire connection could light "4x4" in two-wheel drive. The analog path applies measured thresholds instead, and is also what makes a separate 4LO indication possible. See {{ tbd(145) }}.

**If the switch is missing from the donor case,** it is an available service part (≈$50), or fall back to two discrete ground-closing switches on the shift linkage — 4H+4L → HDX 4x4 terminal, 4L only → HDX EXTRA(−) — which removes the PMU, relay, and both firewall pins from the design.

!!! note "The other connector on the case"
    2003-2006 NP241OR units also carry a **3-wire digital square-wave VSS** on the short tailhousing.[^model] It is unused in this build — the speedometer is driven by the [GPS-50-2 BIM module][bim-gps], not a transfer-case sensor. Cap and label it; do not confuse it with the position switch on top of the case.

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Source a 2003-2006 TJ/LJ Rubicon NP241OR (red and silver tag on the rear identifies it)[^model]
- [ ] Re-confirm the adapter path for the OR case with DomiWorks before ordering ({{ tbd(313) }})
- [ ] Measure 8HP70 output-shaft protrusion (≤~96 mm, else order DomiWorks spacer plate or shorten)
- [ ] Confirm the donor case's input spline and stickout against the DomiWorks requirement
- [ ] **At teardown:** confirm the 5-position switch is fitted; record its connector/pinout ({{ tbd(145) }})
- [ ] **At teardown:** measure switch resistance at each detent (2H / 4H / N / 4L) and record the table ({{ tbd(145) }})
- [ ] Size the An 1 divider from the measured resistances; set PMU thresholds; verify 2H reads "no 4x4"
- [ ] Cap and label the unused tailhousing VSS connector

## Vendor Inquiry — DomiWorks (draft)

Draft email to confirm fitment and parts before ordering:

```text
Subject: Adapter fitment — Ram 1500 EcoDiesel 8HP70 → Jeep TJ Rubicon NP241OR (4:1)

Hi DomiWorks,

I'm mating a Ram 1500 EcoDiesel 8HP70 (4x4) transmission to a Jeep TJ
Rubicon NP241OR "Rock-Trac" transfer case (4.0:1 low range, 2003-2006)
and want to confirm the right parts before ordering.

1. Is adapter SKU 24004001 the correct unit for this 8HP70 EcoDiesel →
   NP241OR combination? Your listing covers the NP231/241 family — does
   that include the Rubicon OR case specifically?

2. Input gear: the NP241OR input is commonly 23-spline short (1-1/8"
   stickout) and the 8HP70 output is also 23-spline. Can the case's
   existing input gear be reused, or does your adapter still require a
   specific replacement input gear? If so, which one?

3. Output protrusion / spacer plate: where exactly do I measure the
   8HP70 output-shaft protrusion from, and what is the cutoff for needing
   the spacer plate? Is the spacer available for the EcoDiesel output,
   and what does it cost?

4. Bearing / seal / hardware: can you include the NP241OR input bearing,
   front seal, and mounting hardware, or are those separate?

5. Does the adapter clear the OR case's position switch on top of the
   case and the tailhousing VSS boss?

6. Lead time and shipping cost to the US (state: ____)?

Donor details:
- Transmission: ZF 8HP70 (Chrysler 845RE), 2015–2019 Ram 1500 EcoDiesel, 4x4
- Transfer case: Jeep TJ Rubicon NP241OR Rock-Trac (4:1 low range)

Thanks,
[name]
```

## Related Documentation

- [Transmission][transmission]
- [Driveshafts][driveshafts]
- [HDX Control Module][hdx-control] - 4x4 and EXTRA(+) indicator inputs
- [PMU Inputs][pmu-inputs] - An 1 position sensing
- [PMU Outputs][pmu-outputs] - OUT19 (4x4 relay) and OUT24 (4LO)

[transmission]: 01-transmission.md
[driveshafts]: 03-driveshafts.md
[hdx-control]: ../02-engine-systems/09-gauge-cluster/01-hdx-control.md
[bim-gps]: ../02-engine-systems/09-gauge-cluster/04-bim-gps.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[pmu-overview]: ../01-power-systems/04-pmu/01-pmu-overview.md

[^model]: NP241OR "Rock-Trac" — introduced 2003 in the TJ Wrangler Rubicon package, a Jeep-only application. Three shift modes plus low range (2H, 4H, N, 4L), ≈90 lb, identified by a red and silver tag on the rear. 2003-2006 units carry a three-wire digital square-wave VSS on the short tailhousing; 2007+ (JK) dropped it when speed sensing moved to the ABS module. Novak Conversions, "The Novak Guide to the New Process / NVG 241OR RockTrac Transfer Case," accessed 2026-09-18.
[^lowrange]: Low range **4.0:1** — the Rubicon-only Rock-Trac ratio (the non-Rubicon Command-Trac is 2.72:1). Novak Conversions NP241OR guide, accessed 2026-09-18.
[^output]: NP241OR: driver's-side front output, centerline rear output, fixed yoke output assembly. Novak Conversions NP241OR guide, accessed 2026-09-18. Confirm on the actual unit.
[^input]: NP241OR input shaft: most common variant is **23-spline, short (1-1/8" stickout)**; rarer variants are 23-spline flush, 21-spline short, and 26-spline male. The 8HP70 (Ram) output is 23-spline. Novak Conversions NP241OR guide, accessed 2026-09-18. **Confirm the actual donor unit's variant** — the adapter's input-gear requirement depends on it ({{ tbd(313) }}).
[^trans]: ZF 8HP70 (Chrysler 845RE) 1st-gear ratio 4.714 — see [Transmission][transmission].
[^adapter]: DomiWorks 24004001 (≈8,495 SEK) and Advance Adapters 8HP70 tooling (output assembly 50-9905 $642.51, housing 51-9905 $371.11), accessed 2026-05-31; prices subject to change. **These figures were gathered for a JK NV241 application and have not been re-confirmed for the NP241OR** — see {{ tbd(313) }}.
[^tc-switch]: 5-position transfer case switch, OE **5083138AA** (Omix-Ada 18676.52, Crown 5083138AA), mounted on top of the case. Listed applications include **2003-2006 Wrangler TJ with the NV241OR**, 2007-2018 JK, WJ Grand Cherokee with NV242/NV247, and KJ Liberty with NV231/NV242. Omix-Ada / Quadratec / Crown Automotive product listings, accessed 2026-09-18. **Per-detent resistance values are not published for this application — measure at teardown** ({{ tbd(145) }}). Values circulating on forums (2WD ≈1.1-1.2 kΩ … 4L ≈60 Ω) are for a Liberty/Selec-Trac application and are NOT applicable here.
[^hdx-inputs]: Dakota Digital HDX manual MAN 650542H, p.13: "**4x4 (−)** — The 4x4 input is activated by a ground signal from a switch on the transfer case… Whenever the 4x4 input is grounded a green 4x4 indicator will be shown on the Home Screen"; "**EXTRA (+)** — This is an extra indicator input that is activated by +12V. When activated, a custom label is displayed on the TFT" (8 characters max, p.31). PMU high-side-only switching per [PMU Overview][pmu-overview].
[^why-adapter]: The 8HP70 is not the NP241OR's factory transmission (the TJ Rubicon paired it with the 42RLE automatic or NV3550/NSG370 manual), so an adapter is required. The 8HP *family* does pair with an NV241 from the factory — the JL Wrangler automatic bolts an 850RE/8HP75 to one — but the Ram EcoDiesel 8HP70's bolt pattern only *resembles* the Jeep 850RE and is not interchangeable, and no direct Ram-8HP70-to-Jeep-case kit is on the market. The transmission is fixed (Turbolamik TCU + Kilduff shifter are spec'd to the 8HP70). jlwranglerforums.com 8-speed swap PSA / Advance Adapters 5054 (JL 850RE / Dodge 8HP70 → Atlas), accessed 2026-05-31.
