---
hide:
  - toc
tags:
  - product-details
  - communication-systems
  - rugged-radio
  - gmrs
---

# 7.1 GMRS Radio {#gmrs-radio}

40 W GMRS two-way radio for vehicle-to-vehicle communication and group coordination. It connects to the [intercom][intercom] through its own rear-panel intercom port, so everyone on a headset hears the radio and can transmit.[^g1-manual]

/// html | div.product-info
![Rugged Radio G1](../images/rugged-radio-g1.jpg){ loading=lazy }

**Type:** GMRS Mobile Radio

**Model:** G1-GMRS

**Manufacturer:** Rugged Radios

**Product Page:** [Rugged Radio G1][product-link]

**Manual:** [User Manual][manual-link]

**Mounting:** Overhead, centered on the roll cage (owner, 2026-09-25), on the U-bracket that comes with the radio

**Power Source:** PMU OUT6 (25A capacity, CONSTANT)

///

## Specifications

All from the G1 manual (printed page numbers).[^g1-manual]

| Spec            | Value                                                                           |
| :-------------- | :------------------------------------------------------------------------------ |
| Output Power    | 40 W high, 25 W middle, 5 W low (p. 30)                                         |
| Frequency       | TX 462-467 MHz, RX 400-480 MHz (p. 28)                                          |
| Channels        | 15 GMRS (1-7, 15-22) + 8 repeater (p. 7)                                        |
| Current Draw    | 0.16 A standby, 0.4 A receive, 9 A max transmit (pp. 29-30)                     |
| Working Voltage | 13.8 V DC; 15 A fuse in the power cable (pp. 10, 28)                            |
| Size            | 53 x 138 x 153 mm (H x W x D), 2.55 lb (p. 28)                                  |
| Rear Panel      | Intercom port, speaker/programming port (Accessory Hub), power, antenna (p. 16) |
| Waterproof      | IP67 (p. 7)                                                                     |
| FCC License     | Required (family license, no exam)                                              |

## Features

- CTCSS/DCS privacy codes
- VOX (voice-activated transmission)
- Channel scan function

## Antenna

| Spec      | Value                                         |
| :-------- | :-------------------------------------------- |
| Model     | Rugged Radios Stealth UHF-GP (ground plane)   |
| Type      | Low-profile tuned antenna (3.25" tall)        |
| Frequency | 450-480 MHz                                   |
| Gain      | 2.0 dBi                                       |
| Mount     | A-pillar ditch light adapter (MT-ANT-ADPT)    |
| Connector | NMO                                           |
| Cable     | RG58 or LMR-400 (50Ω impedance)               |

## Wiring

| Connection | Wire                             | Source                                         | Notes                                                                                                    |
| :--------- | :------------------------------- | :--------------------------------------------- | :------------------------------------------------------------------------------------------------------- |
| Power (+)  | 14 AWG                           | PMU OUT6                                       | Via firewall grommet, then up to the cage; length not measured                                           |
| Ground (−) | 14 AWG                           | START battery neg                              | Direct connection for RF performance; length not measured                                                |
| Antenna    | RG58 coax                        | Driver A-pillar antenna                        | Route away from power leads                                                                              |
| Intercom   | Intercom cable + 5-pin extension | G1 rear intercom port to the STX-RS RADIO port | Rugged: a 5-pin extension is needed when the radio is more than 1 ft from the intercom body[^rugged-kit] |

## Installation Notes

- Keep coax length <25 ft for minimal signal loss
- The hand mic does not work through the intercom. Rugged recommends keeping it in the Jeep for emergencies and powering off the intercom to use it (see [Intercom][intercom]).

## Build Tasks

- [ ] Choose a roll-cage clamp for the G1's U-bracket, centered on the overhead cage tube
- [ ] Measure the power, ground and coax runs to the overhead mount
- [ ] Measure the run from the G1 to the intercom box and buy a 5-pin intercom extension that long

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [Communication Systems Overview][comm-overview]
- [Intercom][intercom]
- [PMU Outputs][pmu-outputs]
- [START Battery Distribution][starter-battery]

[comm-overview]: index.md
[intercom]: 02-intercom.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[starter-battery]: ../01-power-systems/02-starter-battery-distribution/index.md
[product-link]: https://www.ruggedradios.com/products/rugged-g1-waterproof-gmrs-mobile-radio
[manual-link]: https://cdn.shopify.com/s/files/1/0240/3280/4960/files/G1_Manual.pdf

[^g1-manual]: Rugged Radios, G1 User Manual (31 pp.). Printed p. 7 (features: "Easily connect to an intercom with it's own dedicated port"; 15 GMRS + 8 repeater channels; IP67), p. 10 (15 A transceiver fuse), p. 16 (rear panel: Intercom, Speaker/Programming, Power, Antenna ports), pp. 28-30 (specifications). <https://cdn.shopify.com/s/files/1/0240/3280/4960/files/G1_Manual.pdf> (accessed 2026-09-25).
[^rugged-kit]: Rugged Radios, "STX STEREO Remote Head Complete Master Communication Kit with Intercom and 2-Way Radio": offered with the G1 GMRS radio; "If the radio is not mounted within one foot of the main intercom body, a 5-pin extension is required to link the radio and intercom together." <https://www.ruggedradios.com/products/stx-stereo-remote-head-complete-master-communication-kit-with-intercom-and-2-way-radio> (accessed 2026-09-25).
