---
tags:
  - audio-systems
hide:
  - toc
---

# Section 6: Audio Systems {#audio-systems-index}

Marine-grade audio system with multi-zone control and RGB LED lighting integration.

## System Components

| Component                        | Model                          | Power | Control            |
| :------------------------------- | :----------------------------- | ----: | :----------------- |
| [Head Unit][head-unit]           | Fusion MS-RA670                |   15A | BODY PDU F2        |
| [Amplifier][amplifier]           | JL Audio MV800/8i              |   80A internal fuse | AUX battery+ direct (100A inline CB) — mounted under rear seat |
| [Front Speakers][speakers]       | JL Audio M6-650X-S-GmTi-i      |     — | Amp Ch 5+6         |
| [Rear Speakers][speakers]        | JL Audio M6-650VEX-Mb-S-GmTi-i |     — | Amp Ch 7+8         |
| [Subwoofers][subwoofer]          | 2× JL Audio M6-8IB-S-GmTi-i-4  | — | Sub A: Ch 1+2 bridged @ 4Ω; Sub B: Ch 3+4 bridged @ 4Ω |
| [LED Controller][led-controller] | JL Audio MLC-RW                |    5A | SwitchPros OUT-5   |
| [Bluetooth Tuning][bt-tuning]    | JL Audio VXi-BTC               |   50 mA from JLid | MV800/8i JLid-COMM port (no separate power) |

**Total System Power:** ~100A peak worst-case (80A amp fuse-limited + 15A head unit + 5A LED); realistic music playback ~25-40A.

## Signal Flow

```text
MS-RA670 Head Unit
    │
    ├─► Zone 1 RCA ──► MV800/8i Ch 5+6 ──► Front Half-Door Speakers
    ├─► Zone 2 RCA ──► MV800/8i Ch 7+8 ──► Rear Roll Bar Speakers
    ├─► Sub RCA ────► MV800/8i (DSP signal-routed to:)
    │                   ├─► Ch 1+2 bridged @ 4Ω ──► Sub A (200W RMS)
    │                   └─► Ch 3+4 bridged @ 4Ω ──► Sub B (200W RMS)
    └─► Remote Turn-On ──► Amplifier

MLC-RW LED Controller
    │
    └─► RGB outputs ──► All speaker LEDs + Footwell lights
```

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [AUX Battery Distribution][aux-distribution] - Firewall CONSTANT Bus power source (via 300A master CB at AUX battery)
- [BODY PDU][body-pdu] - Head unit and LED controller power
- [Footwell Lights][footwell-lights] - RGB lights controlled by MLC-RW

[head-unit]: 01-head-unit.md
[amplifier]: 02-amplifier.md
[speakers]: 03-speakers.md
[subwoofer]: 04-subwoofer.md
[led-controller]: 05-led-controller.md
[bt-tuning]: 06-bluetooth-tuning.md
[aux-distribution]: ../01-power-systems/03-aux-battery-distribution/index.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[footwell-lights]: ../04-offroad-lighting/09-footwell-lights.md
