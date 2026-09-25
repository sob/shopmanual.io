---
tags:
  - communication-systems
hide:
  - toc
---

# Section 7: Communication Systems {#communication-systems-index}

Radio communication and camera systems for vehicle-to-vehicle coordination and situational awareness.

## System Components

| Component                  | Model                                                   |  Power | Control              |
| :------------------------- | :------------------------------------------------------ | -----: | :------------------- |
| [GMRS Radio][gmrs-radio]   | Rugged Radio G1, overhead on the roll cage              | 15A TX | PMU OUT6             |
| [Intercom][intercom]       | Rugged Radio STX Remote Head (STX-RS), knob on the dash |     2A | PMU OUT20            |
| [Dash Camera][dash-camera] | WolfBox G900 TriPro                                     |     5A | BODY PDU CB39        |
| [Navigation][navigation]   | Garmin Tread 2 Overland                                 |     2A | PMU OUT14 (ignition) |

**Total System Power:** ~24A peak (radio transmitting + intercom + camera + navigation)

## Signal Flow

```text
Rugged Radio G1 GMRS (overhead, roll cage)
    │
    └─► Radio cable ──► STX-RS intercom box RADIO port (behind dash)
                            │
                            ├─► Remote head (dash knob) ── 39 in cable
                            ├─► Driver headset + PTT
                            ├─► Co-driver headset + PTT ──► Front passenger
                            ├─► CREW 1 ──► Rear left headset
                            ├─► CREW 2 ──► Rear right headset
                            ├─► CREW 3 ──► Spare
                            │
                            └─◄ Bluetooth ── phone (music and calls)

WolfBox Mirror Camera
    │
    ├─► Front camera (integrated) ──► SD card recording
    └─► Rear camera ──► Display on reverse
```

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [PMU Outputs][pmu-outputs] - Radio and intercom power circuits
- [BODY PDU][body-pdu] - Camera power circuit
- [Audio Systems][audio-systems] - Fusion head unit and speakers
- [Command Touch CT4][ct4] - Turn signal and horn controller

[gmrs-radio]: 01-gmrs-radio.md
[intercom]: 02-intercom.md
[dash-camera]: 04-dash-camera.md
[navigation]: 05-navigation.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[audio-systems]: ../06-audio-systems/index.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
