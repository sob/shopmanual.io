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
| **Forward Feed (to Firewall Bus)**   | Mechanical Products<br/>([174-S2-300-2][mp-300]) |  300A  | Manual     | AUX battery+<br/>└→ 300A CB<br/>&nbsp;&nbsp;&nbsp;└→ Firewall CONSTANT Bus | ~152A combined max (SP + BODY PDU) | 197% of combined load (Fusion relocated to direct AUX feed) |
| **SafetyHub 150 (Recovery)**         | Mechanical Products<br/>([174-S2-150-2][mp-150]) |  150A  | Manual     | AUX battery+<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SafetyHub 150        | ~100A (ARB 90A + Winch Trigger 10A) | 150% of max load (future-proofed) |
| **JL Audio MV800/8i Amp**            | Blue Sea<br/>([187-100A][bs-100])                |  100A  | Manual     | AUX battery+<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ JL Audio MV800/8i (under rear seat) | 80A max (fuse-limited) | 125% of fuse rating — wire protection (4 AWG short run); amp's 80A internal fuse is primary trip path |

## Firewall-Side CBs (Co-located with Firewall CONSTANT Bus)

Mounted within 7" of [Firewall CONSTANT Bus][constant-bus]. Protect each downstream controller.

| Circuit                      | Model                                            | Rating | Reset Type | Power Path                                                                         | Max Load                                                  | Sizing                              |
| :--------------------------- | :----------------------------------------------- | :----: | :--------- | :--------------------------------------------------------------------------------- | :-------------------------------------------------------- | :---------------------------------- |
| **SwitchPros RCR-Force 12**  | Mechanical Products<br/>([174-S2-150-2][mp-150]) |  150A  | Manual     | Firewall CONSTANT Bus<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SwitchPros           | ~100A (all lighting outputs on)                           | 150% of max load                    |
| **BODY PDU**                 | Mechanical Products<br/>([174-S2-100-2][mp-100]) |  100A  | Manual     | Firewall CONSTANT Bus<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ BODY PDU             | ~54A max (radio 16A, USB 13A, camera 10A, seats 10A peak) | 185% of max load (future expansion) |

!!! info "Wire Sizing for CB Protection"
Forward feed uses 2/0 AWG (300A @ 20°C) for the 13-ft run to the firewall bus (now carries only SP+BODY, ~152A max; 2/0 retained for upgrade headroom). Firewall-side outputs use 2 AWG (130A @ 20°C) for SwitchPros and BODY PDU. Audio amp uses 4 AWG (95A @ 20°C, JL Audio minimum spec) for the short ~3-4 ft run from AUX battery to under-seat amp location.

**Mechanical Products Series 17 (4 units):**

- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Dimensions: 3.39" L × 1.9" W (per unit)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: 2 at passenger rear wheel well (battery side: 300A + 150A), 2 at firewall (bus side: 150A SP + 100A BODY)

**Blue Sea 187-Series (1 unit - Audio Amp):**

- Type: Surface mount
- Reset: Manual
- Terminals: 5/16" (M8) studs
- Dimensions: 3.44" H × 2.32" W × 1.8" D
- Rating: 5000A interrupt @ 12V DC
- Standards: Ignition protected, waterproof
- Mounting: Passenger rear wheel well (battery side, stacked with MP CBs on bracket)

**Space Requirements:**

- **Battery-side bracket:** 3 CBs stacked (300A + 150A + 100A audio amp) — ~10" × 2" (~20 sq in) on wheel well bracket
- **Firewall-side cluster:** 2 CBs in a row with wiring clearance — ~7" × 4" (~28 sq in) near bus

## Related Documentation

- [AUX battery Distribution Overview][rear-battery]
- [Firewall CONSTANT Bus][constant-bus] - Downstream distribution
- [SwitchPros][switchpros] - Load details for SwitchPros circuit
- [SafetyHub 150][safetyhub] - Load details for SafetyHub circuit (ARB compressor, winch trigger)
- [BODY PDU][body-rtmr] - Load details for BODY PDU circuit
- [JL Audio MV800/8i Amp][audio] - Load details for amplifier circuit

[mp-300]: https://www.waytekwire.com/item/49081/
[mp-150]: https://www.waytekwire.com/item/49079/
[mp-100]: https://www.waytekwire.com/item/49077/
[bs-100]: https://www.bluesea.com/products/187-100A/187_Series_Thermal_Circuit_Breaker_100A
[rear-battery]: index.md
[constant-bus]: 02-constant-bus.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
[audio]: ../../06-audio-systems/02-amplifier.md
