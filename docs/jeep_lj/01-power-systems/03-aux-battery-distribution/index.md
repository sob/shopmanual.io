---
hide:
  - toc
---

# 1.3 AUX battery Distribution (Passenger Rear Wheel Well) {#aux-battery-distribution}

## Overview

The AUX battery ([Dakota Lithium 135Ah LiFePO4][batteries]) in the passenger rear wheel well provides power for high-current accessories and cabin systems via five direct terminal connections:

1. **Direct high-current** → Winch (recovery system, no CB per manufacturer spec)
2. **Direct charging input** → BCDC Alpha 50 output (no CB - charging path)
3. **Inline 300A CB** → 2/0 AWG forward feed → [Firewall CONSTANT Bus][constant-bus] (SwitchPros, BODY PDU)
4. **Inline 150A CB** → 2 AWG short feed → [SafetyHub 150][aux-safetyhub] (local in rear wheel well)
5. **Inline 100A CB** → 4 AWG short feed → [JL Audio MV800/8i Amp][audio] (mounted under rear seat)

!!! info "Two-Stage Distribution Architecture"
The AUX battery has **no local CONSTANT bus** — protected feeds run from inline CBs at the battery to two distribution points: the firewall CONSTANT bus (most loads) and SafetyHub (local). This places distribution near the loads, minimizes the cabin trunk to a single heavy cable, and keeps the rear wheel well compartment uncluttered.

See [Firewall CONSTANT Bus][constant-bus] for downstream distribution, [SafetyHub][aux-safetyhub] for fused recovery circuits, and [Circuit Breakers][circuit-breakers] for full CB list.

!!! info "Single Source of Truth"
This page is the authoritative source for all AUX battery wire specs (gauge, distance, voltage drop). Component pages reference here. For battery specs see [Section 1.1][batteries]. For ground bus bars see [Section 1.5][grounding].

## AUX battery Positive Terminal (5 stacked ring lugs)

| Circuit                              | Destination                       | Wire Gauge | Distance | Current             | Voltage Drop    | Protection               |
| :----------------------------------- | :-------------------------------- | :--------- | :------- | :------------------ | :-------------- | :----------------------- |
| [BCDC Alpha 50 output][bcdc]         | Local (rear wheel well)           | 4 AWG      | Short    | 50A                 | Negligible      | None (charging)          |
| [Firewall CONSTANT Bus][constant-bus] | Firewall (cabin side, passenger) | 2/0 AWG    | ~13 ft   | ~154A max           | 1.3% @ 20°C     | 300A CB at battery (<7") |
| [SafetyHub 150][aux-safetyhub]       | Local (rear wheel well)           | 2 AWG      | ~2 ft    | ~100A max           | <0.5% @ 20°C    | 150A CB at battery (<7") |
| [JL Audio MV800/8i Amp][audio]       | Under rear seat                   | 4 AWG      | ~3-4 ft  | 80A max (fuse)      | <0.5% @ 20°C    | 100A CB at battery (<7") |
| [Winch][recovery]                    | Front bumper                      | 1/0 AWG    | 13 ft    | 250A typ, 409A peak | 4.9% @ 250A / 7.9% @ 409A | [None][winch-protection] |

## AUX battery Negative Terminal (5 connections)

| Circuit                          | Destination            | Wire Gauge | Distance | Current             | Voltage Drop  |
| :------------------------------- | :--------------------- | :--------- | :------- | :------------------ | :------------ |
| Rear Frame Rail (chassis bond)   | Local (chassis)        | 2/0 AWG    | ~3 ft    | {{ tbd(124) }}      | <0.1V @ 20°C  |
| [BCDC Alpha 50][bcdc]            | Local                  | 4 AWG      | Short    | 50A                 | Negligible    |
| [JL Audio MV800/8i Amp][audio]   | Under rear seat        | 4 AWG      | ~3-4 ft  | 80A max (fuse)      | <0.5% @ 30°C  |
| [START Battery][starter-battery] | Driver rear wheel well | 1/0 AWG    | 5-6 ft   | 75A max             | <0.05V @ 20°C |
| [Winch][recovery]                | Front bumper           | 1/0 AWG    | 13 ft    | 250A typ, 409A peak | 4.9% @ 250A / 7.9% @ 409A |

## Related Documentation

- [Firewall CONSTANT Bus][constant-bus] - Forward distribution at firewall
- [SafetyHub 150][aux-safetyhub] - Local recovery distribution (rear wheel well)
- [BODY PDU][body-rtmr] - Cabin convenience circuits (fed from firewall bus)
- [Circuit Breakers][circuit-breakers] - Full CB specs (battery side + firewall side)
- [Grounding Architecture][grounding] - Ground bus bars
- [START battery Distribution][starter-battery] - BCDC input source
- [Recovery Systems][recovery] - Winch specifications

[aux-safetyhub]: 04-safetyhub.md
[constant-bus]: 02-constant-bus.md
[body-rtmr]: 03-body-pdu.md
[batteries]: ../01-power-generation/01-batteries.md
[bcdc]: ../01-power-generation/03-bcdc.md
[circuit-breakers]: 01-circuit-breakers.md
[grounding]: ../05-grounding/index.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[recovery]: ../../08-exterior-systems/01-winch.md
[winch-protection]: ../../08-exterior-systems/01-winch.md#winch-circuit-protection
[audio]: ../../06-audio-systems/index.md
