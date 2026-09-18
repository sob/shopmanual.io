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
- **Native to the chassis:** the NP241OR is the factory TJ/LJ Rubicon case, so crossmember mounting and the floor shifter/linkage arrangement are the factory ones for this vehicle rather than adapted from a JK case. Note this does **not** extend to the driveshafts — both are custom Tom Woods units measured at the stretched 110.5" wheelbase regardless of which case is fitted (see [Driveshafts][driveshafts]).
- **Front output side matches the axle:** the NP241OR's front output is on the **driver's side**,[^output] and the Super Duty Dana 60 front axle is a **driver's-side differential drop**.[^axle-drop] The front driveshaft therefore runs down the driver's side without crossing the vehicle — no clearance conflict with the R2.8's oil pan to design around.
- **Strength:** the Rock-Trac's reinforced 4:1 planetary is the heavier-duty variant of the NP241 family. The R2.8's torque is well within either case.

## Adapter (8HP70 → NP241OR)

**An adapter is required — there is no native bolt-up.** The 8HP70 is not the case's factory transmission, so it mates through a transmission-to-transfer-case adapter.[^why-adapter]

**DomiWorks publishes both sides of this exact pairing:** the adapter's fitment list is "NP231, NP241, NP242, NP243, NP246, NP249" from an **8HP70/75 Dodge RAM EcoDiesel** — and the donor here is an 8HP70 EcoDiesel out of a RAM 1500.[^adapter] The NP241OR is an NP241; its 4:1 planetary is internal and does not change the input face the adapter bolts to, so fitment is expected. Confirm in one line with the vendor anyway, since the listing does not spell out the OR variant ({{ tbd(313) }}).

**Specifications:** 115 mm overall, anodized aluminum, case tilt adjustable in 5° increments through a full 360° rotation, with an integrated support bracket for the crossmember and cushions.[^adapter]

- **DomiWorks 24004001** — **$1,005.90** from DriftHQ (US stock), versus ≈8,495 SEK direct from DomiWorks plus import.[^adapter]
- **Alternative — Advance Adapters:** no off-the-shelf 8HP70 → stock NP241OR kit. Their 8HP70 tooling (output assembly 50-9905, housing 51-9905) is built to mate to an Atlas. Their previously noted NP241 input gears are **JK-specific and no longer relevant** to this case. Call to spec a 23-spline build, or go Atlas.

### Parts list (DomiWorks path)

| Part | Source | Notes |
| :--- | :----- | :---- |
| Adapter 24004001 | DriftHQ / DomiWorks | $1,005.90; adapter + integral crossmember bracket |
| 23-spline input gear (ZTNP22390 or equiv.) | Transmission parts supplier | **Required** — DomiWorks specifies a 23-spline input gear and names ZTNP22390. Whether the OR's factory 23-spline gear qualifies as "equivalent" is the open question ({{ tbd(313) }}) |
| NP241OR input bearing + front seal | Rebuild parts | Replace if the input gear is swapped |
| Grade-10.9 mounting hardware | — | Adapter-to-trans / adapter-to-case bolts; inclusion in the kit unconfirmed ({{ tbd(313) }}) |
| Spacer plate | DomiWorks | **Only if** output protrusion exceeds the standard 96 mm — see below |

!!! note "Input gear — the one item that can still force a teardown"
    Both sides being 23-spline is necessary but not sufficient: the gear also has to be dimensionally right for the adapter's 115 mm length and the 8HP70's output. The OR's factory gear was cut for the 42RLE/NSG370, not this adapter. Budget for the ZTNP22390 unless DomiWorks confirms the factory gear works — and note that swapping it means opening the case, which is also when the input bearing and front seal get replaced.

**On the 8HP70 (transmission) side**, the only DomiWorks part is the conditional spacer plate. The 8HP70's factory output shaft is used as-is — it is already a 4WD/transfer-case output (this is a 4x4 Ram donor); no coupler or output adapter is needed from DomiWorks.

**Critical measurement:** DomiWorks' standard fit is **96 mm** from the rear plane to the axle tip. The longer outputs that need the spacer plate are called out as *some Jeep Grand Cherokee EcoDiesel* units, so a RAM 1500 donor is expected to be standard — measure before ordering rather than assume.[^adapter]

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

- [x] Acquire the NP241OR — **in hand**; the JK NV241 is also on hand and is kept as a spare/fallback[^both-cases]
- [ ] Verify the unit is an OR (4:1) and not a Command-Trac — red and silver tag on the rear identifies it[^model]
- [ ] Re-confirm the adapter path for the OR case with DomiWorks before ordering ({{ tbd(313) }})
- [ ] Measure 8HP70 output-shaft protrusion (≤~96 mm, else order DomiWorks spacer plate or shorten)
- [ ] Confirm the donor case's input spline and stickout against the DomiWorks requirement
- [ ] Confirm the 5-position switch is fitted; record its connector/pinout ({{ tbd(145) }})
- [ ] Measure switch resistance at each detent (2H / 4H / N / 4L) and record the table ({{ tbd(145) }}) — the switch is external, on top of the case, so this is done at its connector while moving the lever through the detents. **Not blocked:** the case is on hand, no teardown and no parts needed[^both-cases]
- [ ] Size the An 1 divider from the measured resistances; set PMU thresholds; verify 2H reads "no 4x4"
- [ ] Cap and label the unused tailhousing VSS connector

## Vendor Inquiry — DomiWorks (draft)

Draft email to confirm fitment and parts before ordering:

Your listing already answers fitment, price, tilt, the crossmember bracket, and the 96 mm protrusion standard. These are the four questions it does not:

```text
Subject: NP241OR (Rubicon 4:1) fitment — Ram 1500 EcoDiesel 8HP70 adapter

Hi DomiWorks,

I'm mating a Ram 1500 EcoDiesel 8HP70 (4x4) to a Jeep TJ Rubicon
NP241OR "Rock-Trac" transfer case (4.0:1 low range, 2003-2006). Your
adapter lists NP241 fitment from the 8HP70/75 EcoDiesel, which is
exactly my pairing, but I want to confirm four things before ordering.

1. The listing says NP241 — does that cover the Rubicon NP241OR
   specifically? I understand the 4:1 planetary is internal and the
   input face is common to the family, but I'd like that confirmed.

2. Input gear: you specify a 23-spline gear, ZTNP22390 or equivalent.
   The NP241OR's factory input is already 23-spline short (1-1/8"
   stickout). Does the factory gear work as-is, or does it have to be
   replaced with the ZTNP22390? This decides whether I need to open the
   case at all.

3. Bearing / seal / hardware: are the input bearing, front seal, and
   adapter mounting bolts included, or separate?

4. Clearance: does the adapter clear the OR case's 5-position position
   switch on top of the case, and the short tailhousing VSS boss?

Donor details:
- Transmission: ZF 8HP70 (Chrysler 845RE), Ram 1500 EcoDiesel, 4x4
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
[front-axle]: 04-front-axle.md
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
[^adapter]: DomiWorks Engineering NP231/241/242/243/246/249 → Dodge 8HP70/75 EcoDiesel adapter. Published fitment: "NP231, NP241, NP242, NP243, NP246, NP249" from 8HP70/75 Dodge RAM EcoDiesel, RAM 1500, Jeep Grand Cherokee EcoDiesel, and JGC Hemi 5.7/6.0. Specs: 115 mm overall, anodized aluminum, tilt adjustable "in 5 degrees increment, 360 full rotation," "integrated support bracket for easy integration of crossmember and cushions." Requires a 23-spline transfer case input gear, "ZTNP22390 or equivalent." Standard output protrusion 96 mm from rear plane to axle tip; longer units (some Jeep Grand Cherokee EcoDiesel) need the spacer plate. **$1,005.90 USD** — [DriftHQ listing](https://drifthq.com/products/domiworks-engineering-np231-241-242-243-246-249-transfer-case-adapter-to-dodge-8hp70-75-ecodiesel-ram-1500), accessed 2026-09-18; ≈8,495 SEK direct from DomiWorks, accessed 2026-05-31. Prices subject to change. The listing does not name the NP241**OR** variant specifically — see {{ tbd(313) }}. Advance Adapters 8HP70 tooling (output assembly 50-9905 $642.51, housing 51-9905 $371.11), accessed 2026-05-31.
[^both-cases]: Owner confirmation, 2026-09-18 — both the NP241OR and the previously spec'd JK NV241 GenII are on hand. No transfer case needs sourcing, and the position-switch measurement for {{ tbd(145) }} can be done on the bench now.
[^axle-drop]: Ford front Dana 60 axles are **driver's-side differential drop** with reverse-cut (high pinion) gears: "Ford versions are driver's side differential drop, reverse-cut gears" (Wikipedia, Dana 60); "All these Ford front axles were drivers side differential, reverse-cut (high pinion) gears, and kingpin knuckles to 1991.5 and balljoints thereafter" (Blue Oval Trucks, "Ford Super Duty Dana 50 vs Dana 60"). Both accessed 2026-09-18. Matches the NP241OR's driver's-side front output — see [Front Axle][front-axle].
[^tc-switch]: 5-position transfer case switch, OE **5083138AA** (Omix-Ada 18676.52, Crown 5083138AA), mounted on top of the case. Listed applications include **2003-2006 Wrangler TJ with the NV241OR**, 2007-2018 JK, WJ Grand Cherokee with NV242/NV247, and KJ Liberty with NV231/NV242. Omix-Ada / Quadratec / Crown Automotive product listings, accessed 2026-09-18. **Per-detent resistance values are not published for this application — measure at teardown** ({{ tbd(145) }}). Values circulating on forums (2WD ≈1.1-1.2 kΩ … 4L ≈60 Ω) are for a Liberty/Selec-Trac application and are NOT applicable here.
[^hdx-inputs]: Dakota Digital HDX manual MAN 650542H, p.13: "**4x4 (−)** — The 4x4 input is activated by a ground signal from a switch on the transfer case… Whenever the 4x4 input is grounded a green 4x4 indicator will be shown on the Home Screen"; "**EXTRA (+)** — This is an extra indicator input that is activated by +12V. When activated, a custom label is displayed on the TFT" (8 characters max, p.31). PMU high-side-only switching per [PMU Overview][pmu-overview].
[^why-adapter]: The 8HP70 is not the NP241OR's factory transmission (the TJ Rubicon paired it with the 42RLE automatic or NV3550/NSG370 manual), so an adapter is required. The 8HP *family* does pair with an NV241 from the factory — the JL Wrangler automatic bolts an 850RE/8HP75 to one — but the Ram EcoDiesel 8HP70's bolt pattern only *resembles* the Jeep 850RE and is not interchangeable, and no direct Ram-8HP70-to-Jeep-case kit is on the market. The transmission is fixed (Turbolamik TCU + Kilduff shifter are spec'd to the 8HP70). jlwranglerforums.com 8-speed swap PSA / Advance Adapters 5054 (JL 850RE / Dodge 8HP70 → Atlas), accessed 2026-05-31.
