---
tags:
  - product-details
  - drivetrain
  - axle
---

# 10.5 - Rear Axle {#rear-axle}

/// html | div.product-info

**Type:** Sterling 10.5, full float

**Source:** 2005-2010 Ford F-350 Super Duty, SRW

**Locker:** ARB RD140 Air Locker

**Axle Shafts:** Factory 35 spline

///

## Specifications

| Specification | Value |
| :------------ | :---- |
| Type | Sterling 10.5, full float |
| Source | 2005-2010 Ford F-350 Super Duty (SRW)[^owner-notes] |
| Width (WMS) | 68.87"[^owner-notes] |
| Bolt Pattern | 8x170[^owner-notes] |
| Spline Count | 35 (shafts), 31 (pinion)[^owner-notes] |
| Locker | ARB RD140[^rd140] |

!!! info "Housing Identification"
    Corporate Sterling is identified by the absence of a filler hole in the OE
    inspection cover. Housing must be 2010 or earlier; 2011+ went to a
    different pinion spline and 5.13 gears do not exist for it. A 2008-2010
    housing also needs an extra pinion spacer with the gear install kit (see
    Ring & Pinion).

## Ring & Pinion

| Specification | Value |
| :------------ | :---- |
| Ratio | 5.13 |
| Manufacturer | Revolution Gear |
| Part | F10.25-513L (long spline)[^gearset] — sourcing {{ tbd(297) }} |
| Install Kit | Revolution 35-2046[^install-kit] |
| 2008-2010 Housing | Add Revolution SK F10.5-Conv pinion spacer (sold separately)[^install-kit] |

!!! warning "Gear and Housing Mismatch"
    There is no 10.5-native 5.13. This is a 10.25" ring gear run in the 10.5
    housing. Revolution supports the combination: the F10.25 long-pinion set
    fits both housings, and 35-2046 is the kit for a 10.5 housing running it
    (not 35-2046A, which is for a factory 10.5 gear).[^gearset] Add
    approximately 0.120" to the pinion depth stack as a starting point, then
    adjust. A solid crush sleeve spacer works without modification despite not
    being listed for the 10.5.[^owner-notes] RD140 fitment with this gear:
    {{ tbd(300) }}.

## Differential

| Specification | Value |
| :------------ | :---- |
| Locker | ARB RD140 Air Locker[^rd140] |
| Spline | 35 |
| Ratio Coverage | All ratios (no carrier break)[^rd140] |
| Solenoid Draw | ~2A |
| Control | SwitchPros Button 10, OUTPUT-10 |
| Air Source | [ARB Twin Compressor][air-compressor] via manifold |

Air locker selected over the Ford factory electric locker (BC3Z-4026-B). The
air system already exists for the front locker, so the marginal cost is one
solenoid and a 6 ft line. The e-locker has no published current draw, requires
a housing pass-through and bulkhead connector, and its 12V-engage / 5V-hold
profile is not reproducible on a SwitchPros output.[^locker-choice]

See [Air Lockers][air-lockers] for wiring, air line routing, and operation.

## Axle Shafts

| Specification | Value |
| :------------ | :---- |
| Manufacturer | Factory |
| Type | Full float |
| Spline Count | 35 |

## Brakes

| Specification | Value |
| :------------ | :---- |
| Type | Factory Super Duty disc |
| Pads and Rotors | PowerStop Z36 Truck & Tow |
| Park Brake | 8.1" drum-in-hat, mechanical[^owner-notes] |

Factory disc with integrated park brake. No conversion required. Master
cylinder sizing, flex hoses, proportioning, and bias are on the
[Brakes][brakes] page.

## Housing Preparation

| Item | Part |
| :--- | :--- |
| Truss | Motobilt |
| Differential Cover | Motobilt |
| Pinion Yoke | 1350, 31 spline, strap style |
| Brackets | TJ/LJ suspension brackets |
| Breather | Relocated; braided line routed high into the engine bay |

Pumpkin is offset to the passenger side with a longer driver-side tube. Lay
out ORI lower mounts and link brackets before the truss goes on. Pinion
pointed at the transfer case for the CV driveshaft (see
[Driveshafts][driveshafts]).

All welding completed before internals installed.

!!! info "ABS and Tone Ring"
    No ABS on this build; speed is GPS-sourced via the Dakota Digital
    [GPS-50-2][bim-gps]. Factory tone ring omitted, sensor port blocked off.

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Verify no filler hole in OE inspection cover
- [ ] Confirm donor housing year; a 2008-2010 housing needs the Revolution SK F10.5-Conv spacer in addition to kit 35-2046
- [ ] Confirm park brake hardware complete
- [ ] Cite an OEM or vendor source for WMS width, 8x170 bolt pattern, and spline counts before bracket layout or wheel order
- [ ] Locate and plumb the axle breather before the truss is welded
- [ ] Confirm the Motobilt cover fill plug clears the truss, and whether it includes a drain plug
- [ ] Adjust and verify park brake shoes before the axle goes under the vehicle

## Related Documentation

- [Front Axle][front-axle]
- [Air Lockers][air-lockers] - Locker control, air lines, operation
- [Air Compressor][air-compressor] - ARB Twin Compressor and tank
- [Driveshafts][driveshafts] - Rear shaft yoke and CV
- [Brakes][brakes] - Master cylinder sizing, flex hoses, proportioning valve, park brake
- [Suspension][suspension] - ORI strut and link bracket layout
- [Purchase Tracker][purchase-tracker] - Axle swap parts

[front-axle]: 04-front-axle.md
[air-lockers]: ../08-exterior-systems/03-air-lockers.md
[air-compressor]: ../08-exterior-systems/02-air-compressor.md
[driveshafts]: 03-driveshafts.md
[brakes]: 08-brakes.md
[bim-gps]: ../02-engine-systems/09-gauge-cluster/04-bim-gps.md
[suspension]: 06-suspension.md
[purchase-tracker]: ../09-installation/03-purchase-tracker.md

[^owner-notes]: Owner build notes, 2026-09-16 — donor range, housing identification, WMS width, bolt pattern, spline counts, park brake size, pinion depth offset, and the solid spacer note. Not yet backed by an OEM or vendor citation; see Build Tasks.
[^rd140]: ARB **RD140** — Air Locker, "Ford 10.25/10.5 Inch", 35 spline, all gear ratios; $1,399.95. [Revolution Gear listing](https://revolutiongear.com/arb-air-locker-rd140-for-ford-10-25-10-5-with-35-spline-axles-all-gear-ratios/), accessed 2026-09-16. Supersedes the RD116 (30-spline Dana 44) previously specified for the rear.
[^gearset]: Revolution Gear **F10.25-513L** — Ford 10.25" long-pinion 5.13 ring & pinion. Revolution: "Ford 10.25 Inch (Long Pinion) Gear sets can be used in 10.25 Inch and 10.5 Inch Ford Differentials. Master Overhaul Kit P/N 35-2046 is required to use gears in a 10.5 Inch Differential." Revolution Gear dealer listings, accessed 2026-09-16.
[^install-kit]: Revolution **35-2046** — "Fits 1993-99 Ford 10.25 Inch and 1999-2007 10.5 Inch housing with Revolution Gear F10.25 ring and pinion. 2008-10 10.5 Inch housings require spacer for install, sold separately, part number SK F10.5-Conv." [revolutiongear.com](https://revolutiongear.com/revolution-gear-ford-10-25-master-install-kit-use-in-10-5-w-aftmkt-10-25-gear/), accessed 2026-09-16. Do not order **35-2046A**, which is the kit for a factory 10.5" gear.
[^locker-choice]: Owner decision, 2026-09-16 — ARB RD140 over the Ford factory e-locker (BC3Z-4026-B): the air infrastructure already exists for the front locker, and the e-locker's 12V-engage / 5V-hold drive is not reproducible on a SwitchPros output.
