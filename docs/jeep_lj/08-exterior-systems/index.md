---
hide:
  - toc
---

# Section 8: Exterior Systems {#exterior-systems}

Recovery equipment and air systems for offroad capability.

## Contents

| Section | Component | Description |
| :------ | :-------- | :---------- |
| [8.1][winch] | Warn Zeon 10-S Winch | 10,000 lb winch, 409A peak |
| [8.2][air-compressor] | ARB Twin Compressor | Brushless 90A compressor, 1-gallon tank, auto pressure control |
| [8.3][air-lockers] | ARB Air Lockers | RD116 front/rear Dana 44 lockers |
| [8.4][rear-air-chuck] | Rear Air Chuck | External air access in tailgate area |

## System Overview

**Recovery:**

- Warn Zeon 10-S winch (10,000 lb capacity, 409A peak)
- Direct AUX battery connection (1/0 AWG, no external breaker)
- Dash rocker switch + factory wired remote

**Air System:**

- ARB Twin Compressor (brushless, 90A draw)
- 1-gallon air tank (135-150 PSI automatic pressure)
- ARB front/rear air lockers (RD116)
- Rear air chuck plate for tire inflation

## Power Distribution

| Component      | Power Source            | Protection      | Control            |
| -------------- | ----------------------- | --------------- | ------------------ |
| Winch Motor    | AUX battery direct      | None (internal) | Dash rocker/remote |
| Winch Control  | SafetyHub ATC-1         | 15A ATC         | Dash rocker        |
| Compressor     | SafetyHub MIDI-1/MIDI-2 | 2× 60A MIDI     | SwitchPros OUT-11  |
| Front Locker   | SwitchPros OUTPUT-17    | Low-side driver | Button 9           |
| Rear Locker    | SwitchPros OUTPUT-10    | 15A             | Button 10          |

## Outstanding Items

See individual component pages for specific items.

## Related Documentation

- [AUX Battery Distribution][aux-battery] - Winch and compressor power
- [SafetyHub][safetyhub] - Winch trigger and compressor fuses
- [SwitchPros][switchpros] - Compressor and locker control

[winch]: 01-winch.md
[air-compressor]: 02-air-compressor.md
[air-lockers]: 03-air-lockers.md
[rear-air-chuck]: 04-rear-air-chuck.md
[aux-battery]: ../01-power-systems/03-aux-battery-distribution/index.md
[safetyhub]: ../01-power-systems/03-aux-battery-distribution/04-safetyhub.md
[switchpros]: ../05-control-interfaces/02-switchpros-sp1200.md
