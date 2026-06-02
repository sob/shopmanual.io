---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - signal-distribution
---

# 1.6 Ignition Signal Distribution {#ignition-signal-distribution}

/// html | div.product-info
![Blue Sea MaxiBus 2105](../../images/blue-sea-2105-maxibus.jpg){ loading=lazy }

**Type:** Common BusBar

**Model:** Blue Sea 2105 MaxiBus

**Manufacturer:** Blue Sea Systems

**Product Page:** [MaxiBus 250A BusBar][bluesea-2105]

///

## Overview

Distributes low-current 12V ignition sense signal to non-critical convenience devices. With the keyswitch removed (see [Keyless Ignition][keyless-ignition]), the bus bar input is now sourced from the **PBS-I PINK IGN output** (60A onboard relay inside the cabin-mounted PBS-I module). The PBS-I energizes PINK IGN whenever the system is in ACC (after 2 presses) or START mode; PINK does not drop during cranking.

**Location:** Cabin side of firewall

**Function:** Signal distribution only (not a power bus)

!!! info "Engine-Bay Consumers Tap Through Firewall"
The bus bar's outbound feed to engine-bay consumers (ECM 12V supply, PMU Pin 7) crosses the firewall on HDP24 Pin 12 — see [Firewall Ingress][firewall-ingress].

    - **PMU 12V Switched Input (Physical Pin 7):** Wire tapped from the bus bar engine-bay distribution stud - see [PMU Inputs][pmu-inputs]
    - **Cummins ECM 12V Supply:** Wire tapped from the same engine-bay distribution stud
    - **Starter Control:** PBS-I PURPLE START output (separate firewall Pin 15) gates through WAIT-gate relay → Cole Hersee 24213 - see [Starter System][starter-system] and [Keyless Ignition][keyless-ignition]

    **Note:** PMU "Pin 7" (physical connector pin for 12V switched power) is different from PMU "In 7" (digital input channel #7 used for CT4 headlight status).

## Specifications

- **Rating:** 250A AC/DC continuous, 300V AC / 48V DC max
- **Terminals:** 12x #10-24 screws, 2x 5/16"-18 studs
- **Dimensions:** 7.93" L x 1.50" W
- **Accessories:** Insulating cover (Part 2718)
- **Full Specs:** [Blue Sea 2105][bluesea-2105]

## Stud/Terminal Assignment

| Stud/Terminal           | Connection                | Wire Gauge   | Distance              | Max Current     | Notes                                              |
| :---------------------- | :------------------------ | :----------- | :-------------------- | :-------------- | :------------------------------------------------- |
| **Stud 1 (5/16")**      | **PBS-I PINK IGN (INPUT)** | **14 AWG ✓** | **~2 ft (cabin local)** | **~5A total**   | No firewall crossing; PBS-I onboard 60A relay protects |
| Stud 2 (5/16")          | **Engine-bay outbound (OUTPUT)** | 14 AWG ✓     | Through firewall (HDP24 Pin 12) | ~5A peak     | **5A inline fuse required at this stud** per Cummins R2.8 install manual; feeds ECM Pin 41 (black, keyswitch) + PMU Pin 7 |
| Terminal 1 (#10-24)     | Command Touch CT4         | 18 AWG ✓     | ~3 ft                 | ~20mA           | Ignition sense for turn signal auto-cancel         |
| Terminal 2 (#10-24)     | SwitchPros SP-1200        | 18 AWG ✓     | ~4 ft                 | ~20mA           | Pin 3 (Lt Blue) - ignition sense                   |
| Terminal 3 (#10-24)     | Fusion MS-RA670 Radio     | 18 AWG ✓     | ~2 ft                 | ~20mA           | Yellow wire - ignition sense                       |
| Terminal 4 (#10-24)     | BCDC Alpha 50             | 18 AWG ✓     | ~12 ft                | ~20mA           | Blue wire - activates charging when engine running |
| Terminal 5 (#10-24)     | **\[Available\]**           | -            | -                     | -               | Future ignition-switched device                    |
| Terminals 6-12 (#10-24) | **\[Available\]**           | -            | -                     | -               | Future expansion (7 terminals)                     |

**Utilization:** 6 of 14 used (2 studs + 4 terminals used, 0 studs + 8 terminals available)

## Mounting

**Location:** Cabin side of firewall, behind dash (former keyswitch location now repurposed)

**Benefits:** PBS-I source is local (cabin), most consumers are cabin-side; single outbound firewall feed (Pin 12) serves engine-bay loads

## Related Documentation

- [Power Systems Overview][power-overview]
- [PMU Inputs][pmu-inputs] - Pin 7 ignition sense and signal distribution diagram
- [Firewall Ingress][firewall-ingress] - Grommet 2 specifications
- [BCDC Alpha 50][bcdc] - Charging activation

[bluesea-2105]: https://www.bluesea.com/products/2105/MaxiBus_250A_BusBar_-_Two_5_16in-18_Studs_and_Twelve_10-24_Screws
[power-overview]: ../index.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
[firewall-ingress]: ../07-wire-routing/02-firewall-ingress.md
[bcdc]: ../01-power-generation/03-bcdc.md
[keyless-ignition]: ../../05-control-interfaces/06-keyless-ignition.md
[starter-system]: ../../02-engine-systems/01-starter.md
