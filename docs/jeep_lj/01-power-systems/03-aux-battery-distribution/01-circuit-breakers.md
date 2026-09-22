---
hide:
  - toc
---

# 1.3.1 Circuit Breakers {#aux-battery-circuit-breakers}

## Overview

AUX-side circuit breakers split into **two banks**:

1. **Battery-side bank** (3 CBs at AUX battery+ in passenger rear wheel well, within 7" per code)
2. **Firewall-side bank** (2 CBs at [Firewall CONSTANT Bus][constant-bus] in cabin)

All Mechanical Products Series 17 (except audio amp on Blue Sea 187).

## Battery-Side CBs (Passenger Rear Wheel Well)

Mounted inline on a bracket within 7" of AUX battery+ terminal. Protect the three protected feeds leaving the battery.

| Circuit                              | Model                                            | Rating | Reset Type | Power Path                                                              | Max Load              | Sizing                         |
| :----------------------------------- | :----------------------------------------------- | :----: | :--------- | :---------------------------------------------------------------------- | :-------------------- | :----------------------------- |
| **Forward Feed (to Firewall Bus)**   | Mechanical Products<br/>([174-S2-250-2][mp-250]) |  250A  | Manual     | AUX battery+<br/>└→ 250A CB<br/>&nbsp;&nbsp;&nbsp;└→ Firewall CONSTANT Bus | ~154A combined max (SP + BODY PDU) | 162% of combined load; matches the 250A rating of the Blue Sea 2105 bus and the 2/0 AWG ampacity (~265A @ 60°C) — downsized from 300A on 2026-09-22 (Fusion head unit rides the forward feed through the BODY PDU on CB30; the JL Audio amp is the direct-AUX-feed device) |
| **SafetyHub 150 (Recovery)**         | Mechanical Products<br/>([174-S2-150-2][mp-150]) |  150A  | Manual     | AUX battery+<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SafetyHub 150        | ~90A (ARB only — winch control on BODY PDU CB43) | 167% of max load (future-proofed) |
| **JL Audio MV800/8i Amp**            | Blue Sea<br/>187-series, 80A (P/N to confirm at order) |  80A  | Manual     | AUX battery+<br/>└→ 80A CB<br/>&nbsp;&nbsp;&nbsp;└→ JL Audio MV800/8i (under rear seat) | 80A max (fuse-limited) | Matches the amp's recommended 80A fuse value and protects the 4 AWG run (95A @ 20°C) — downsized from 100A on 2026-09-22, keeping 4 AWG ({{ tbd(149) }}) |

## Firewall-Side CBs (Co-located with Firewall CONSTANT Bus)

Mounted within 7" of [Firewall CONSTANT Bus][constant-bus]. Protect each downstream controller.

| Circuit                      | Model                                            | Rating | Reset Type | Power Path                                                                         | Max Load                                                  | Sizing                              |
| :--------------------------- | :----------------------------------------------- | :----: | :--------- | :--------------------------------------------------------------------------------- | :-------------------------------------------------------- | :---------------------------------- |
| **SwitchPros RCR-Force 12**  | Mechanical Products<br/>([174-S2-150-2][mp-150]) |  150A  | Manual     | Firewall CONSTANT Bus<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SwitchPros           | ~100A (all lighting outputs on)                           | 150% of max load                    |
| **BODY PDU**                 | Mechanical Products<br/>([174-S2-100-2][mp-100]) |  100A  | Manual     | Firewall CONSTANT Bus<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ BODY PDU             | ~54A max (radio 15A, USB 13A, camera 10A, seats 10A peak, winch control 2A, cargo 4A) | 185% of max load (future expansion) |

!!! info "Wire Sizing for CB Protection"
Forward feed uses 2/0 AWG protected by the 250A CB for the 13-ft run to the firewall bus (now carries only SP+BODY, ~154A max; 2/0 retained for upgrade headroom). 2/0 AWG copper is rated ~265A @ 60°C (project wire-ampacity reference), so the 250A breaker is at or below the wire's ampacity and equal to the 2105 bus rating. Project rule (2026-09-22): when a breaker exceeds its wire, drop the breaker rather than upsize the wire. Firewall-side outputs use 2 AWG (130A @ 20°C) for SwitchPros and BODY PDU. Audio amp uses 4 AWG (95A @ 20°C, JL Audio minimum spec) for the short ~3-4 ft run from AUX battery to under-seat amp location.

**Mechanical Products Series 17 (4 units):**

- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Dimensions: 3.39" L × 1.9" W (per unit)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: 2 at passenger rear wheel well (battery side: 250A + 150A), 2 at firewall (bus side: 150A SP + 100A BODY)

**Blue Sea 187-Series (1 unit - Audio Amp):**

- Type: Surface mount
- Reset: Manual
- Terminals: 5/16" (M8) studs
- Dimensions: 3.44" H × 2.32" W × 1.8" D
- Rating: 5000A interrupt @ 12V DC
- Standards: Ignition protected, waterproof
- Mounting: Passenger rear wheel well (battery side, stacked with MP CBs on bracket)

**Space Requirements:**

- **Battery-side bracket:** 3 CBs stacked (250A + 150A + 80A audio amp) — ~10" × 2" (~20 sq in) on wheel well bracket
- **Firewall-side cluster:** 2 CBs in a row with wiring clearance — ~7" × 4" (~28 sq in) near bus

## Related Documentation

- [AUX battery Distribution Overview][rear-battery]
- [Firewall CONSTANT Bus][constant-bus] - Downstream distribution
- [SwitchPros][switchpros] - Load details for SwitchPros circuit
- [SafetyHub 150][safetyhub] - Load details for SafetyHub circuit (ARB compressor)
- [BODY PDU][body-rtmr] - Load details for BODY PDU circuit
- [JL Audio MV800/8i Amp][audio] - Load details for amplifier circuit

[mp-250]: https://www.waytekwire.com/item/49082/
[mp-150]: https://www.waytekwire.com/item/49079/
[mp-100]: https://www.waytekwire.com/item/49077/
[rear-battery]: index.md
[constant-bus]: 02-constant-bus.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
[audio]: ../../06-audio-systems/02-amplifier.md
