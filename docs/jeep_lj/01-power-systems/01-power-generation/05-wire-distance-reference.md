---
hide:
  - toc
---

# 1.1.5 Wire Distance Reference {#wire-distance-reference}

Measured wire routing distances between major electrical components for voltage drop calculations and wire sizing.

!!! note "Measurement Method"
These distances represent actual measured cable routing paths (not straight-line distances) following frame rails, firewall passages, and avoiding obstacles. All measurements are one-way cable length.

!!! info "Dual Rear Wheel Well Battery Configuration"
Both batteries located in rear wheel wells for optimal wire routing:

    - **Driver Rear Wheel Well** = START battery (critical systems)
    - **Passenger Rear Wheel Well** = AUX battery (accessories)

## Component Distance Matrix

| From                         | To                                     | Distance | Notes                                                 |
|:-----------------------------|:---------------------------------------|:---------|:------------------------------------------------------|
| **Alternator**               | **START battery** (driver rear wheel well)  | 8 ft     | Primary charging path                                 |
| **Starter**                  | **START battery** (driver rear wheel well)  | 6 ft     | Cranking power                                        |
| **PMU24**                    | **START battery** (driver rear wheel well)  | 7 ft     | Critical systems power                                |
| **BCDC Alpha 50**            | START battery → AUX battery            | 5-6 ft   | Inter-battery charging (BCDC in passenger rear wheel well) |
| **Winch** (front bumper)     | **AUX battery** (passenger rear wheel well) | 13 ft    | Recovery system power                                 |
| **OEM Battery** (engine bay) | **Starter**                            | 4 ft     | Reference: original configuration                     |
| **OEM Battery** (engine bay) | **Winch** (front bumper)               | 5 ft     | Reference: original configuration                     |
| **OEM Battery** (engine bay) | **Alternator**                         | 4 ft     | Reference: original configuration                     |
| **Firewall** (driver side)   | **Tail lights**                        | 13 ft    | Rear wiring runs                                      |
| **Steering column**          | **Driver headlight**                   | 6 ft     | CT4 lighting control                                  |
| **Steering column**          | **Passenger headlight**                | 9 ft     | CT4 lighting control                                  |
| **Steering column**          | **Driver tail light**                  | 11 ft    | CT4 lighting control                                  |
| **Steering column**          | **Passenger tail light**               | 16 ft    | CT4 lighting control                                  |
| **PMU** (engine bay)         | **Steering column**                    | 3 ft     | PMU to CT4/controls                                   |
| **Passenger rear wheel well**| **A-pillar**                           | 7 ft     | AUX battery to front accessories                      |
| **Passenger rear wheel well**| **Roof**                               | 6 ft     | AUX battery to roof-mounted equipment                 |

## Optimized Wire Gauge Specifications

Wire gauges optimized for performance at measured routing distances:

| Circuit                        | Distance                      | Wire Gauge | Max Current             | Voltage Drop @ Temp              | Notes                                                     |
| :----------------------------- | :---------------------------- | :--------- | :---------------------- | :------------------------------- | :-------------------------------------------------------- |
| **Alternator → START battery** | 8 ft                          | 2/0 AWG    | 270A                    | 2.81% @ 60°C                     | Charging system - temp derating applied                   |
| **PMU24 Power Feed**           | 7 ft                          | 2/0 AWG    | 220A                    | 2.40% @ 60°C                     | Direct connection via 250A CB - upgraded from 1/0 AWG     |
| **Starter Motor**              | 6 ft                          | 2/0 AWG    | 400-600A                | <3% @ 20°C                       | Brief cranking load - minimal temp effect                 |
| **BCDC Inter-Battery**         | 5-6 ft                        | 4 AWG      | 50A                     | 0.94% @ 20°C                     | Rear wheel well to rear wheel well (cross-cab routing TBD - see [Wire Routing][wire-routing]) |
| **Winch → AUX battery**        | 13 ft one-way (26 ft circuit) | 1/0 AWG    | 250A typical, 400A peak | 6.3% @ 250A, 10.1% @ 400A @ 20°C | Passenger rear wheel well to front bumper routing (path TBD - see [Wire Routing][wire-routing]) |

**Temperature Derating Notes:**

- Engine bay circuits (alternator, PMU) calculated @ 60°C ambient
- Wheel well circuits (starter, winch) calculated @ 20°C ambient
- Voltage drop percentages shown at maximum rated current

## Measurements Needed

Distances required for voltage drop calculations and wire purchases. Measure actual routing paths, not straight-line.

### Lighting Circuits (Priority: High)

| From                    | To                       | Wire   | Distance | Purpose                             |
|:------------------------|:-------------------------|:-------|:---------|:------------------------------------|
| CT4 (steering column)   | Driver headlight         | 14 AWG | 6 ft ✓   | Low/high beam voltage drop          |
| CT4 (steering column)   | Passenger headlight      | 14 AWG | 9 ft ✓   | Low/high beam voltage drop          |
| CT4 (steering column)   | Left fender turn signal  | 14 AWG | 6 ft ✓   | Same as driver headlight            |
| CT4 (steering column)   | Right fender turn signal | 14 AWG | 9 ft ✓   | Same as passenger headlight         |
| CT4 (steering column)   | Driver tail light        | 14 AWG | 11 ft ✓  | Turn signal rear                    |
| CT4 (steering column)   | Passenger tail light     | 14 AWG | 16 ft ✓  | Turn signal rear                    |
| PMU (engine bay)        | Rear tail lights         | 16 AWG | 13 ft ✓  | Brake/reverse/marker (Out 21/22/23) |
| SwitchPros (firewall) | Roll bar dome lights     | 16 AWG | ~8 ft    | Low current, estimated              |
| PBS-I PURPLE START      | Cole Hersee 24213 coil   | 16 AWG | ~10 ft ✓ | Via WAIT-gate relay + firewall Pin 15  |
| CT4 SW3 output          | PMU In 7                 | 18 AWG | 3 ft ✓   | Same as steering column → PMU       |

### Offroad Lighting (Priority: Medium)

| From                    | To                           | Distance | Notes                                  |
|:------------------------|:-----------------------------|:---------|:---------------------------------------|
| SwitchPros (firewall) | A-pillar ditch lights        | 7 ft ✓   | Via Baja harness                       |
| SwitchPros (firewall) | Roof                         | 6 ft ✓   | Roof-mounted lights                    |
| SwitchPros (firewall) | Rear rock lights (2)         | 2-3 ft   | Low current, voltage drop negligible   |
| SwitchPros (firewall) | Front rock lights (4)        | ~10 ft   | Estimated via frame rail               |

### Air System (Priority: High)

| From                      | To                          | Wire      | Distance | Purpose           |
|:--------------------------|:----------------------------|:----------|:---------|:------------------|
| SafetyHub (engine bay)    | ARB compressor (under seat) | 6 AWG × 2 | ~8 ft    | Compressor power (through firewall) |
| ARB compressor            | Chassis ground              | 6 AWG     | ~2 ft    | Local ground      |
| SwitchPros (firewall)   | Compressor control terminal | 14 AWG    | ~6 ft    | Control signal    |
| Air manifold (under seat) | Front axle locker           | Air line  | ~6 ft    | Custom air line   |
| Air manifold (under seat) | Rear axle locker            | Air line  | ~6 ft    | Custom air line   |

### Communication (Priority: Low)

| Location/Route             | Purpose                      |
|:---------------------------|:-----------------------------|
| STX intercom mounting      | ✓ Dash/behind dash           |
| GMRS radio mounting        | ✓ Dash (~6 ft to A-pillar antenna) |
| Ham antenna position       | ✓ Passenger A-pillar (~4 ft to dash) |
| Rear camera cable path     | ~11 ft (windshield → A-pillar → rear center) |

### Mounting Locations (Priority: Medium)

| Component                       | Status                                      |
|:--------------------------------|:--------------------------------------------|
| SwitchPros power module         | ✓ Firewall (cabin side, passenger area, with BODY PDU + Firewall CONSTANT Bus) |
| SwitchPros control panel        | ✓ Dash mounted                              |
| SwitchPros control cable length | 5 ft (firewall to dash, short run)          |
| Firewall CONSTANT Bus           | ✓ Firewall (cabin side, passenger area)     |
| Firewall CONSTANT Bus feed      | 2/0 AWG, ~13 ft from AUX battery+, 300A CB at battery |
| CT4 GPS antenna                 | ✓ Integrated in CT4 unit                    |
| Rear cargo rocker switch        | ✓ Blue Sea 4160 on rear wheel well top      |
| Rear seat dome override switch  | ✓ Blue Sea 4160, rear passenger accessible  |

## Related Documentation

- [Batteries][batteries] - Battery specifications and mounting locations
- [BCDC Alpha 50][bcdc] - Inter-battery charging system
- [Alternator][alternator] - Charging system specifications
- [PMU24][pmu] - Power management unit
- [Starter System][starter] - Starter power requirements
- [Recovery Systems][recovery] - Winch specifications
- [START battery Distribution][starter-battery] - Driver rear wheel well battery terminal connections
- [AUX battery Distribution][aux-battery] - Passenger rear wheel well battery terminal connections

[batteries]: 01-batteries.md
[bcdc]: 03-bcdc.md
[alternator]: 02-alternator.md
[pmu]: ../04-pmu/index.md
[starter]: ../../02-engine-systems/01-starter.md
[recovery]: ../../08-exterior-systems/01-winch.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[wire-routing]: ../07-wire-routing/index.md
