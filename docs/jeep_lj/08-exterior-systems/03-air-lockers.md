---
hide:
  - toc
tags:
  - product-details
  - exterior-systems
  - air-lockers
  - arb
---

# 8.3 Air Lockers {#air-lockers}

ARB air-operated locking differentials for the front Dana 60 and rear Sterling
10.5 axles.

/// html | div.product-info

**Front Model:** ARB RD166 (Dana 60, 35 spline, 4.56 & up)

**Rear Model:** ARB RD140 (Ford 10.25/10.5 Corporate Sterling, 35 spline)

**Front Locker Control:** SwitchPros OUTPUT-17 (low-side driver, 2A)

**Rear Locker Control:** SwitchPros OUTPUT-10 (15A output, 2A draw)

**Air Source:** [ARB Twin Compressor][air-compressor] via manifold

///

## Specifications

| Spec              | Front Locker         | Rear Locker           |
| ----------------- | -------------------- | --------------------- |
| Model             | ARB RD166[^rd166]    | ARB RD140[^rd140]     |
| Axle              | Dana 60              | Sterling 10.5         |
| Spline Count      | 35                   | 35                    |
| Gear Ratio        | 5.13                 | 5.13                  |
| Carrier Series    | 4-series (4.56 & up) | All ratios            |
| Solenoid Draw     | ~2A                  | ~2A                   |
| SwitchPros Output | OUTPUT-17 (low-side) | OUTPUT-10 (15A)       |
| SwitchPros Button | Button 9             | Button 10             |

!!! warning "Front Gear Thickness"
    RD166 is the 4.56-and-up carrier. The Revolution 5.13 gear must be standard
    thickness. Do not order D60-513RT (thick) or the REV-F350-513-K package.

Rear RD140 fitment with the 10.25" gear in the 10.5 housing: {{ tbd(300) }}.

## Wiring

### Solenoid Control

| Locker | SwitchPros Output | Wire   | Route                                     |
| ------ | ----------------- | ------ | ----------------------------------------- |
| Front  | OUTPUT-17         | 18 AWG | Firewall → driver frame rail → front axle |
| Rear   | OUTPUT-10         | 18 AWG | Firewall → cabin trunk → rear axle        |

### Wire Routing

- **Front Locker (OUTPUT-17):** SwitchPros (firewall, cabin side) → along driver frame rail → front axle solenoid; path and length {{ tbd(81) }}
  - Wire: 18 AWG (2A load, low-side driver output)
  - Protection: Split loom, P-clamps every 18", secure to frame rail
- **Rear Locker (OUTPUT-10):** SwitchPros (firewall, cabin side) → [H5 rear bundle][lighting-build] through the cabin trunk → rear axle solenoid; length {{ tbd(63) }}
  - Wire: 18 AWG (2A load)
  - Protection: Split loom where exposed, secure to axle housing

## Air Line Routing

!!! info "Air Line Installation"
    Air lines from manifold must be routed to both axles with proper protection
    from heat, abrasion, and road debris.

| Line         | Route                                                        | Length |
| ------------ | ------------------------------------------------------------ | ------ |
| Front Locker | Manifold (under seat) → along driver frame rail → front axle | ~12 ft |
| Rear Locker  | Manifold (under seat) → rear axle                            | ~6 ft  |

**Air Line Specifications:**

- **Type:** ARB air line kit (1/4" OD nylon tubing, 200 PSI rated)
- **Fittings:** Push-to-connect fittings at manifold and locker ends

**Protection:**

- Split loom over entire run where exposed to road debris
- P-clamps every 12" along frame rail
- High-temp silicone sleeve where crossing near exhaust (6" minimum clearance)
- Rubber grommets at body/frame penetrations

!!! warning "Axle Travel Slack"
    Leave service loops at both axles sized for full droop on the ORI struts.
    Measure at full droop, not at ride height. Loop length: {{ tbd(303) }}.

## Operation

### Engagement Sequence

Press and hold Button 9 (front, OUTPUT-17) or Button 10 (rear, OUTPUT-10): solenoid opens, pressurized air from tank locks the differential **instantly** — no waiting for the compressor. Release to disengage. Behavior is identical on both axles.

**Automatic Refill:**

- After multiple locker uses, tank pressure drops below 135 PSI
- Pressure switch automatically activates compressor to refill tank
- No user action required

## Safety Considerations

!!! warning "Locker Operation"
    - Only engage lockers at low speeds (typically <5 mph)
    - Disengage lockers before returning to normal speeds
    - Never engage lockers on dry pavement
    - Ensure adequate air pressure before engaging lockers

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Verify RD166 against the Revolution D60 reverse 5.13 standard thickness gear
- [ ] Order ARB air line installation kit with 1/4" fittings for front/rear

## Related Documentation

- [Air Compressor][air-compressor] - ARB Twin Compressor and air tank
- [SwitchPros][switchpros] - Locker control (OUTPUT-10, OUTPUT-17)
- [Lighting & SwitchPros Build Sheet][lighting-build] - H5 rear bundle carrying OUT-10
- [Front Axle][front-axle] - Dana 60 specifications
- [Rear Axle][rear-axle] - Sterling 10.5 specifications

[air-compressor]: 02-air-compressor.md
[switchpros]: ../05-control-interfaces/02-switchpros-sp1200.md
[lighting-build]: ../01-power-systems/07-wire-routing/05-harness-lighting-switchpros.md
[front-axle]: ../10-drivetrain/04-front-axle.md
[rear-axle]: ../10-drivetrain/05-rear-axle.md

[^rd166]: ARB **RD166** — Air Locker, Dana 60HD, 35 spline, 4.56 & up (4-series carrier). [Revolution Gear listing](https://revolutiongear.com/arb-air-locker-rd166-for-dana-60hd-with-35-spline-axles-4-56-and-up/), accessed 2026-09-16.
[^rd140]: ARB **RD140** — Air Locker, Ford 10.25/10.5 Inch, 35 spline, all gear ratios. [Revolution Gear listing](https://revolutiongear.com/arb-air-locker-rd140-for-ford-10-25-10-5-with-35-spline-axles-all-gear-ratios/), accessed 2026-09-16.
