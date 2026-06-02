---
tags:
  - communication-systems
hide:
  - toc
---

# Section 7: Communication Systems {#communication-systems-index}

Radio communication and camera systems for vehicle-to-vehicle coordination and situational awareness.

## System Components

| Component                  | Model               |  Power | Control              |
| :------------------------- | :------------------ | -----: | :------------------- |
| [GMRS Radio][gmrs-radio]   | Rugged Radio G1     | 15A TX | PMU OUT6             |
| [Intercom][intercom]       | Rugged Radio STX    |     2A | PMU OUT20            |
| [Dash Camera][dash-camera] | WolfBox G900 TriPro |     5A | BODY PDU CB39        |
| [Navigation][navigation]   | Garmin Tread 2 Overland |     2A | SwitchPros OUT-8     |

**Total System Power:** ~24A peak (radio transmitting + intercom + camera + navigation)

## Signal Flow

```text
Rugged Radio G1 GMRS
    │
    └─► RADIO port ──► STX Intercom RADIO port
                            │
                            ├─► Headset Port 1 ──► Driver headset
                            ├─► Headset Port 2 ──► Front passenger headset
                            ├─► Headset Port 3 ──► Rear left headset
                            ├─► Headset Port 4 ──► Rear right headset
                            │
                            └─► AUX port ◄── Fusion MS-RA670 audio

WolfBox Mirror Camera
    │
    ├─► Front camera (integrated) ──► SD card recording
    └─► Rear camera ──► Display on reverse
```

## Outstanding Items

None - see individual component pages for specific items.

## Related Documentation

- [PMU Outputs][pmu-outputs] - Radio and intercom power circuits
- [BODY PDU][body-pdu] - Camera power circuit
- [Audio Systems][audio-systems] - Fusion head unit for intercom AUX input
- [Command Touch CT4][ct4] - Turn signal and horn controller

[gmrs-radio]: 01-gmrs-radio.md
[intercom]: 02-intercom.md
[dash-camera]: 04-dash-camera.md
[navigation]: 05-navigation.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[audio-systems]: ../06-audio-systems/index.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
