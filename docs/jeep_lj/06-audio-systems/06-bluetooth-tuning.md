---
hide:
  - toc
tags:
  - product-details
  - audio-systems
  - jl-audio
---

# 6.6 Bluetooth Tuning (VXi-BTC) {#bluetooth-tuning}

JLid Bluetooth communicator for wireless TüN configuration of the MV800/8i — lets DSP tuning be done from a phone or tablet without crawling under the rear seat to plug a laptop into the amp's USB port.

/// html | div.product-info
**Type:** JLid Bluetooth Communicator (control only — no audio streaming)

**Model:** VXi-BTC

**Part Number:** 010-13543-00

**Manufacturer:** JL Audio (Garmin)

**Product Page:** [JL Audio VXi-BTC][product-link]

**Manual:** [JLid Bluetooth Communicator Connection Guide][manual-link]

**Mounting:** Clip-mounted in cabin near amplifier (under rear seat area), non-metallic surface preferred

**Power Source:** JLid bus from MV800/8i (no separate power wiring)

///

## Specifications

All figures from the VXi-BTC Connection Guide.[^vxi-btc-manual]

| Spec                       |                                                Value |
| :------------------------- | ---------------------------------------------------: |
| Bluetooth Topology         |                                            LE (Low Energy) |
| Bluetooth Core Version     |                                              4.2 |
| Connection Range           |                                       Up to 33 ft / 10 m |
| Host Interface             |                                  Proprietary JLid protocol |
| Input Operating Voltage    |                                              5 VDC |
| Current Draw               |                       50 mA max (~0.25 W from JLid bus) |
| Streaming Audio            |                  **No** — control interface only |
| Included Cable             |                              CAT5e, 6.5 ft / 2 m |
| Included Mount             |                       Snap-fit clip + 2 mounting screws |
| Pairing Capacity           |  Multiple devices may be paired; 1 active at a time |

[^vxi-btc-manual]: JL Audio JLid Bluetooth Communicator Connection Guide (`VXi-BTC_MAN_050718`), pp. 1–2. Manual mirror used: customsounds.com.

## Function

The VXi-BTC is a **tuning interface only** — it does not stream music. Use cases on this build:

- Adjust DSP crossover/EQ/delay on the [MV800/8i amp][amplifier] while seated at the driver's seat, with the engine running and music playing
- Save/load TüN project files from a phone or tablet
- Switch between saved DSP presets without a physical preset selector (no [M-DRC-50][m-drc-50-skipped] in this build — see Design Decisions below)

The amp's USB-A/B port remains the fallback for laptop tuning sessions.

## Compatible Apps

| App           |    Platforms                |    Use Case                                       |
| :------------ | :-------------------------- | :------------------------------------------------ |
| TüN Mobile    | iPad, Android tablet         | Full-featured tuning UI (preferred)               |
| TüN Express   | iPhone, iPad, Android phone/tablet | Streamlined — quick adjustments + preset switching |

Both apps are free on the App Store and Google Play.

## Wiring

| Connection | Wire   | Source                        | Notes                                              |
| :--------- | :----- | :---------------------------- | :------------------------------------------------- |
| JLid (data + 5V) | CAT5e  | MV800/8i JLid-COMM (RJ45) | Included 6.5 ft cable; ~3-4 ft used (BTC near amp) |

The VXi-BTC draws its power from the JLid bus — no separate +12 V or ground wiring needed.

!!! warning "Single JLid Port Constraint"
    The MV800/8i has **one JLid-COMM port**. The VXi-BTC occupies it. An M-DRC-50 preset-selector knob cannot coexist on the same amp without manual cable swapping (the MVi-HUB does not add additional accessory ports — it only adds amp-network ports). If a dash preset switch becomes a daily-use need, plan a swap procedure or revisit the architecture.

## Mounting Location

**Clip-mounted under the rear seat near the [MV800/8i amplifier][amplifier]:**

- Cable run: ~3-4 ft from amp's JLid-COMM port to BTC location (included 6.5 ft CAT5e has slack)
- Surface: prefer non-metallic mounting surface — the manual flags **"avoid mounting directly to large metal surfaces or to wire harnesses"** for RF performance. Mount to the trans tunnel cover, a fiberglass surface, or a fabricated standoff bracket above the amp.
- Status LED must remain visible for pairing/troubleshooting
- BT LE 33 ft range covers the driver's seat from a rear-seat mount with margin

## Pairing Procedure (initial setup)

1. Power the amp (key on); BTC LED ring initializes, then flashes blue (Open Visibility)
2. On phone/tablet: launch TüN Mobile or TüN Express, open **Select/Rename Device**
3. Pick `VXi (BT)` from the list, accept Bluetooth Pairing Request
4. BTC LED ring goes solid blue → solid green = active connection
5. Continue through TüN amp configuration prompts

The amp + BTC pair stays remembered; subsequent connects only need step 1-3.

## LED Status Reference

| LED State      | Meaning              |
| :------------- | :------------------- |
| Flashing blue  | Open Visibility (pairable by any device) |
| Solid blue     | Paired but not actively connected |
| Solid green    | Active TüN connection in progress |
| Flashing green | Restricted Visibility (only previously paired devices can connect) |

Press-and-hold the LED button 10 sec → Factory Reset (wipes paired-device list).

## Design Decisions

**M-DRC-50 deferred.** The build started with only the VXi-BTC because:

- The MV800/8i exposes a single JLid port — only one accessory at a time without manual swapping
- The Fusion MS-RA670 head unit already provides volume, source switching, and zone fader/balance from the dash
- DSP tuning sessions are occasional (post-install, after speaker break-in, after seasonal soft-top vs hard-top changes); a Bluetooth link from a phone is the lower-friction tool for that frequency
- DSP preset switching from the dash is not yet a daily-use need. If multi-preset switching (e.g., "Top Up / Top Down / Quiet") becomes valuable, revisit by either (a) swapping in an M-DRC-50 with a swap-cable procedure, or (b) using TüN Express's preset switcher on a phone-as-remote (mounted to the dash via vent clip).

## Outstanding Items

- [ ] Decide BTC mounting surface — trans-tunnel cover vs amp-mounting-plate standoff vs A-pillar/under-dash (whatever balances RF clearance with status-LED visibility)
- [ ] Source VXi-BTC product image (`docs/jeep_lj/images/jl-audio-vxi-btc.jpg`)

## Related Documentation

- [Audio Systems Overview][audio-overview]
- [Amplifier (MV800/8i)][amplifier] — the JLid host
- [Head Unit (MS-RA670)][head-unit] — primary daily control surface (volume, source, fader)

[audio-overview]: index.md
[amplifier]: 02-amplifier.md
[head-unit]: 01-head-unit.md
[m-drc-50-skipped]: #design-decisions
[product-link]: https://www.garmin.com/en-US/p/1706181/
[manual-link]: https://www.customsounds.com/uploads/docs/05d842e4d5097179b506cbd8024db62dbbca16ab.pdf
