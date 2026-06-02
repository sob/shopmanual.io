---
hide:
  - toc
tags:
  - product-details
  - communication-systems
  - rugged-radio
---

# 7.2 Intercom {#intercom}

4-place intercom system for driver and passenger communication with radio and audio integration.

/// html | div.product-info
![Rugged Radio STX](../images/rugged-radio-stx.jpg){ loading=lazy }

**Type:** 4-Place Intercom

**Model:** STX

**Manufacturer:** Rugged Radios

**Product Page:** [Rugged Radio STX][product-link]

**Manual:** [Quick Start Guide][manual-link]

**Mounting:** Behind dash

**Power Source:** PMU OUT20 (5A capacity, CONSTANT)

///

## Specifications

| Spec          |                            Value |
| :------------ | -------------------------------: |
| Headset Ports | 4 (expandable to 8 via EXT port) |
| Input Voltage |                         9-16V DC |
| Current Draw  |                      <2A typical |
| Dimensions    |               5.5" × 3.5" × 1.5" |

## Features

- VOX or PTT mode per headset
- Individual volume controls per headset
- RADIO port for G1 GMRS integration
- AUX port for Fusion head unit audio
- EXT port for expansion modules
- Music auto-mute when radio transmits

## Ports

| Port        | Function                  | Connection                     |
| :---------- | :------------------------ | :----------------------------- |
| RADIO       | Two-way radio integration | G1 GMRS via integration cable  |
| AUX         | External audio input      | Fusion MS-RA670 (3.5mm or RCA) |
| EXT         | Expansion modules         | Optional 4-place expansion     |
| Headset 1-4 | Headset connections       | Push-to-connect jacks          |

## Headset Configuration

| Port   | Position        | Jack Location          | Cable Length    |
| :----- | :-------------- | :--------------------- | :-------------- |
| Port 1 | Driver          | STX unit (behind dash) | 6 ft (included) |
| Port 2 | Front passenger | STX unit (behind dash) | 6 ft (included) |
| Port 3 | Rear left       | Driver rear wheel well      | Extended        |
| Port 4 | Rear right      | Passenger rear wheel well   | Extended        |

## Wiring

| Connection | Wire              | Source            | Notes                    |
| :--------- | :---------------- | :---------------- | :----------------------- |
| Power (+)  | 14 AWG            | PMU OUT20         | Via firewall grommet     |
| Ground (−) | 14 AWG            | START battery neg | Direct for audio quality |
| G1 Radio   | Integration cable | G1 RADIO port     | Audio/PTT/mute           |
| Aux Audio  | 3.5mm or RCA      | Fusion MS-RA670   | Music to headsets        |

## Installation Notes

- Direct battery ground recommended for best audio quality
- PMU output has integrated 5A protection - no inline fuse needed

## Outstanding Items

None - all specifications determined.

## Related Documentation

- [Communication Systems Overview][comm-overview]
- [GMRS Radio][gmrs-radio]
- [Audio Systems][audio-systems]
- [PMU Outputs][pmu-outputs]

[comm-overview]: index.md
[gmrs-radio]: 01-gmrs-radio.md
[audio-systems]: ../06-audio-systems/index.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[product-link]: https://www.ruggedradios.com/products/stx-stereo-high-fidelity-bluetooth-intercom
[manual-link]: https://cdn.shopify.com/s/files/1/0240/3280/4960/files/STX_-_Quick_Start_Guide.pdf?v=1724339126
