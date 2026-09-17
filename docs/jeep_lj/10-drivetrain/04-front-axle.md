---
tags:
  - product-details
  - drivetrain
  - axle
---

# 10.4 - Front Axle {#front-axle}

/// html | div.product-info

**Type:** Dana 60, high pinion (reverse rotation)

**Source:** 2005-2010 Ford F-350 Super Duty, SRW

**Locker:** ARB RD166 Air Locker

**Axle Shafts:** Factory Dana/Spicer 35 spline

///

## Specifications

| Specification | Value |
| :------------ | :---- |
| Type | Dana 60, high pinion reverse rotation |
| Source | 2005-2010 Ford F-350 Super Duty (SRW)[^owner-notes] |
| Width (WMS) | 69.25"[^owner-notes] |
| Bolt Pattern | 8x170[^owner-notes] |
| Spline Count | 35 inner, 35 outer[^owner-notes] |
| Tube | 3.5" x 0.500" wall[^owner-notes] |
| Knuckles | Factory cast steel |
| Locker | ARB RD166[^rd166] |

## Ring & Pinion

| Specification | Value |
| :------------ | :---- |
| Ratio | 5.13 |
| Manufacturer | Revolution Gear |
| Part | D60 reverse, **standard thickness** |
| Install Kit | D60 reverse master install kit |

!!! warning "Gear Thickness"
    ARB RD166 is the 4.56-and-up carrier. Gear must be standard thickness.
    Do **not** order D60-513RT (thick) or the REV-F350-513-K package.

## Differential

| Specification | Value |
| :------------ | :---- |
| Locker | ARB RD166 Air Locker[^rd166] |
| Spline | 35 |
| Carrier Series | 4-series (4.56 & up)[^rd166] |
| Control | SwitchPros Button 9, OUTPUT-17 |

See [Air Lockers][air-lockers] for wiring, air line routing, and operation.

## Axle Shafts

| Specification | Value |
| :------------ | :---- |
| Manufacturer | Dana/Spicer (factory) |
| Spline Count | 35 |
| U-Joint | Spicer SPL55-3X[^owner-notes] |
| Quantity | 4 (2 installed, 2 spare) |

Stock shafts retained. Chromoly and 1550-series joints deferred: the 8" ram
caps steering at 40 degrees, which is where factory 1480-series joints bind,
so larger joints buy no usable angle. Bolt-in upgrade if shafts prove
marginal.[^shafts]

## Hubs

| Specification | Value |
| :------------ | :---- |
| Type | Yukon Hardcore manual locking |
| Part | YHC70011[^owner-notes] |
| Spline | 35 |
| Engagement | 1/3 turn |

Factory wheel end retained. Yukon hubs replace factory lockouts. No free-spin
conversion required.

## Ball Joints

| Specification | Value |
| :------------ | :---- |
| Type | American Iron ball joint delete |
| Style | Press-fit, welded per AI instructions |
| Bushing Offset | {{ tbd(298) }} (0, 1.5, or 3 degree) |
| Hardware | AI-1900 trail hardware kit |

Upper and lower both required. Lower addresses shaft push-out on breakage.[^bje]

!!! info "Caster Adjustment"
    Bushing offset sets caster and camber together, summing to the bushing
    rating. Every 15 degrees of bushing rotation gives 0.5 degrees of change on
    a 3-degree set. Buying caster at the knuckle avoids rotating the inner Cs,
    which would also rotate the pinion.

## Inner Cs

Factory inner Cs retained, no gussets. Accepted deviation from the
weld-once-for-future-power principle. Revisit only with an engine change.[^bje]

## Housing Preparation

| Item | Part |
| :--- | :--- |
| Truss | Motobilt |
| Differential Cover | Motobilt |
| Pinion Yoke | 1350, 29 spline, strap style[^owner-notes] |
| Breather | Relocated; braided line routed high into the engine bay |

All welding completed before internals installed.

!!! info "ABS and Tone Ring"
    No ABS on this build; speed is GPS-sourced via the Dakota Digital
    [GPS-50-2][bim-gps]. Factory tone ring omitted, sensor port blocked off.

## Steering

| Specification | Value |
| :------------ | :---- |
| High Steer Arms | Offroad Anonymous 05-16 SD60 full hydro weld-on[^ora] |
| Ram | PSC 8" double ended (see [Steering][steering]) |
| Ram Mount | Barnes 4WD universal DIY |
| Target Angle | 40 degrees[^ora] |

ORA published travel-to-angle: 8" travel gives 40 degrees, 9" gives 45, 10"
gives 50, measured at the innermost mounting hole. Multiple mounting holes
allow trading angle for mechanical advantage.[^ora]

!!! warning "Steering Stops"
    Stops must satisfy both the u-joint bind angle and ram stroke. Set with
    paint inside the joints, run stops in until paint rubs off, back out one
    turn. Leave 1/8" at each end of ram travel so the cylinder never bottoms
    internally. Verify under load, not by hand.

Ball joint delete clearance against the high steer arms: {{ tbd(299) }}.

## Brakes

Factory Super Duty calipers and rotors. See [Brakes][brakes].

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Confirm factory hub type before ordering (auto vs manual lockout)
- [ ] Set and verify steering stops under load
- [ ] Preheat knuckles before welding high steer arms
- [ ] Cite an OEM or vendor source for WMS width, tube size, and spline counts before bracket layout or wheel order
- [ ] Locate and plumb the axle breather before the truss is welded
- [ ] Confirm the Motobilt cover fill plug clears the truss, and whether it includes a drain plug
- [ ] Lay out link brackets and the ram mount before the truss is welded
- [ ] Verify beadlock clearance to the ram and links at full lock and full droop

## Related Documentation

- [Air Lockers][air-lockers] - Front locker control and air system
- [Driveshafts][driveshafts] - Front shaft yoke and CV
- [Steering][steering] - PSC full hydro system
- [Rear Axle][rear-axle]
- [Brakes][brakes]

[air-lockers]: ../08-exterior-systems/03-air-lockers.md
[driveshafts]: 03-driveshafts.md
[steering]: 07-steering.md
[rear-axle]: 05-rear-axle.md
[brakes]: 08-brakes.md
[bim-gps]: ../02-engine-systems/09-gauge-cluster/04-bim-gps.md

[^owner-notes]: Owner build notes, 2026-09-16 — donor range, WMS width, bolt pattern, spline counts, tube size, u-joint series, hub part number, and pinion yoke spline. Not yet backed by an OEM or vendor citation; see Build Tasks.
[^rd166]: ARB **RD166** — Air Locker, Dana 60HD, 35 spline, 4.56 & up (4-series carrier); $1,399.95 list. [Revolution Gear listing](https://revolutiongear.com/arb-air-locker-rd166-for-dana-60hd-with-35-spline-axles-4-56-and-up/), accessed 2026-09-16. Supersedes the RD116 (30-spline Dana 44) previously specified for the front.
[^ora]: Offroad Anonymous **05-16 Super Duty Dana 60 Weld-On High Steer Kit** (full hydro option) — ORA publishes "8″ steering travel provides 40° steering angle" for the 05-10 knuckle version. [offroadanonymous.com](https://offroadanonymous.com/product/05-16-super-duty-dana-60-weld-on-high-steer-kit/), accessed 2026-09-16. The 9"/45° and 10"/50° figures are owner notes from the same listing.
[^shafts]: Owner decision, 2026-09-16 — factory Dana/Spicer 35-spline shafts retained; chromoly shafts and 1550-series joints deferred because the 40° steering cap set by the 8" ram is where the factory joints bind.
[^bje]: Owner decision, 2026-09-16 — American Iron ball joint delete (upper and lower, welded per AI instructions); factory inner Cs retained without gussets.
