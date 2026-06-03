---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - wipers
---

# 2.4 Wiper System {#windshield-wiper-control-system}

/// html | div.product-info

**Type:** Electronic Wiper Controller

**Model:** WS-51C

**Manufacturer:** Ron Francis Wiring

**Product Page:** [Ron Francis WS-51C][ws-51c-product]

**Installation Manual:** [WS-51C Instructions][ws-51c-manual]

**Mounting:** Dash-mounted (integrated switch/controller)

**Power Source:** PMU OUT11 (15A capacity)

///

## Overview

Ron Francis WS-51C replaces TIPM wiper functions. Provides delay/intermittent control for factory TJ wiper motor with integrated washer pump control and auto-wipe.

## Wiring

| Circuit       | Wire       | Source               | Destination               | Notes                   |
| :------------ | :--------- | :------------------- | :------------------------ | :---------------------- |
| Module Power  | 14 AWG     | PMU OUT11            | WS-51C power input        | Auto (ignition ON)      |
| Module Ground | 14 AWG     | WS-51C ground        | Firewall ground           |                         |
| Low Speed     | Per WS-51C | WS-51C output        | Wiper motor low terminal  |                         |
| High Speed    | Per WS-51C | WS-51C output        | Wiper motor high terminal |                         |
| Park Switch   | Per WS-51C | Wiper motor park     | WS-51C park input         | Auto-park detection     |
| Washer Pump   | Per WS-51C | WS-51C washer output | Factory washer pump       | 3-5A, auto-wipe feature |

See [PMU Outputs][pmu-outputs] for PMU configuration.

## Features

- Off / Mist / Delay / Low / High speeds
- Variable delay (1-20 seconds)
- Park position control
- Auto-wipe after washer spray

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [PMU Outputs][pmu-outputs] - OUT11 configuration

[install-checklist]: ../09-installation/02-engine-systems-checklist.md
[ws-51c-product]: https://www.ronfrancis.com/product/173
[ws-51c-manual]: https://s3.amazonaws.com/cdn.ronfrancis.com/downloads/INSTRUCTIONS/WS51C-INST.pdf
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
