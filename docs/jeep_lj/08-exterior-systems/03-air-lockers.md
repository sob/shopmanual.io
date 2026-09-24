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

**Locker Control:** Two latching dash switches, fed from BODY PDU CB44 through relay K27 (ignition). The front switch is fed from the rear switch, so the front can only lock while the rear is locked. See [Dashboard Controls][dashboard-controls] (moved off SwitchPros buttons 9 and 10, 2026-09-24).

**Solenoids:** Both at the air manifold under the passenger seat, per ARB: "Mount solenoid within close proximity of the air supply"[^arb-solenoid]

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
| Dash Switch       | Front locker (fed from rear switch) | Rear locker    |
| Solenoid Location | Air manifold, under passenger seat  | Air manifold, under passenger seat |

!!! warning "Front Gear Thickness"
    RD166 is the 4.56-and-up carrier. The Revolution 5.13 gear must be standard
    thickness. Do not order D60-513RT (thick) or the REV-F350-513-K package.

Rear RD140 fitment with the 10.25" gear in the 10.5 housing: {{ tbd(300) }}.

## Wiring

### Solenoid Control

| Locker | Control | Wire | Route |
| ------ | ------- | ---- | ----- |
| Rear   | Rear dash switch (BODY PDU CB44 via K27) | 18 AWG | Dash → under passenger seat |
| Front  | Front dash switch, fed from the rear switch output | 18 AWG | Dash → under passenger seat |

Both solenoids sit at the manifold, so the locker wiring is cabin-only and short. No locker wire runs to either axle, and none crosses the firewall; only the air lines run to the axles. The earlier front-axle wire route is no longer needed ({{ tbd(81) }}). Full wiring: [Dashboard Controls: Locker Switches][locker-switches].

## Air Line Routing

!!! info "Air Line Installation"
    Air lines from manifold must be routed to both axles with proper protection
    from heat, abrasion, and road debris.

| Line         | Route                                                        | Length |
| ------------ | ------------------------------------------------------------ | ------ |
| Front Locker | Front solenoid (at manifold, under seat) → along driver frame rail → front axle | ~12 ft |
| Rear Locker  | Rear solenoid (at manifold, under seat) → rear axle                            | ~6 ft  |

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

The switches are latching. Switch a locker ON and its solenoid opens: tank air locks the differential **instantly**, with no wait for the compressor, and it stays locked while the switch is ON. Switch it OFF to release.[^arb-switch]

| Step | Switch | Result |
| ---- | ------ | ------ |
| 1 | Rear ON | Rear locked |
| 2 | Front ON | Front locked (does nothing unless the rear is ON) |
| 3 | Rear OFF | Both release: the front loses its feed with the rear |

Both lockers also release at key-off, because relay K27 opens with the ignition.

Tank refill after locker use is automatic — see [Air Compressor: Automatic Pressure Control][air-compressor-auto] for the pressure switch logic.

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
- [Dashboard Controls][dashboard-controls] - Locker switches and wiring
- [Front Axle][front-axle] - Dana 60 specifications
- [Rear Axle][rear-axle] - Sterling 10.5 specifications

[air-compressor]: 02-air-compressor.md
[air-compressor-auto]: 02-air-compressor.md#automatic-pressure-control
[dashboard-controls]: ../05-control-interfaces/05-dashboard-controls.md
[locker-switches]: ../05-control-interfaces/05-dashboard-controls.md#locker-switches
[front-axle]: ../10-drivetrain/04-front-axle.md
[rear-axle]: ../10-drivetrain/05-rear-axle.md

[^rd166]: ARB **RD166** — Air Locker, Dana 60HD, 35 spline, 4.56 & up (4-series carrier). [Revolution Gear listing](https://revolutiongear.com/arb-air-locker-rd166-for-dana-60hd-with-35-spline-axles-4-56-and-up/), accessed 2026-09-16.
[^rd140]: ARB **RD140** — Air Locker, Ford 10.25/10.5 Inch, 35 spline, all gear ratios. [Revolution Gear listing](https://revolutiongear.com/arb-air-locker-rd140-for-ford-10-25-10-5-with-35-spline-axles-all-gear-ratios/), accessed 2026-09-16.
[^arb-solenoid]: ARB RD166 Installation Guide, §4.1 "Mounting the Solenoid", p. 27. <https://store.arbusa.com/content/RD166.pdf> (accessed 2026-09-24).
[^arb-switch]: ARB RD166 Installation Guide, §5.1 (ON/OFF actuator switch) and §6.3 "Testing the Air Locker Actuation", p. 37: switch ON locks, switch OFF releases. The front-fed-from-rear wiring is ARB's recommended dual-locker layout, §5.2.2.2, p. 35.
