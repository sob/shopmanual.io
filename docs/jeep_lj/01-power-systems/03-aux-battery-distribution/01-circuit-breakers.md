---
hide:
  - toc
---

# 1.3.1 Circuit Protection {#aux-battery-circuit-breakers}

## Overview

AUX-side circuit protection splits into **two banks**:

1. **Battery-post bank** (3 Blue Sea MRBF terminal fuses on the AUX battery+ post in the passenger rear wheel well)
2. **Firewall-side bank** (2 Mechanical Products Series 17 CBs at the [Firewall CONSTANT Bus][constant-bus] in the cabin)

## Battery-Post Terminal Fuses (MRBF)

Blue Sea Systems MRBF terminal fuses (30–300 A, 10,000 A AIC @ 14 V DC, ignition protected) mount directly on the AUX+ post in a terminal fuse block — dual block 2151 for the forward feed + SafetyHub, single block 5191 for the amp.[^mrbf] Part numbers to confirm at order: {{ tbd(331) }}. They replace the former inline Mechanical Products 174-S2-250-2 / 174-S2-150-2 CBs and the Blue Sea 187 80A CB (2026-10-17): one joint per circuit instead of three (lug→CB in, CB out→lug), no stacked ring lugs beyond the block, and the within-7"-of-post rule is satisfied on the post. Fuses are not resettable — carry spares.

| Circuit                              | Fuse       | Wire    | Power Path                                                              | Max Load              | Sizing                         |
| :----------------------------------- | :--------: | :------ | :---------------------------------------------------------------------- | :-------------------- | :----------------------------- |
| **Forward Feed (to Firewall Bus)**   | 250A MRBF  | 2/0 AWG | AUX battery+<br/>└→ 250A MRBF<br/>&nbsp;&nbsp;&nbsp;└→ Firewall CONSTANT Bus | ~154A combined max (SP + BODY PDU) | 162% of combined load; matches the 250A rating of the Blue Sea 2105 bus and the 2/0 AWG ampacity (~265A @ 60°C) — downsized from 300A on 2026-09-22 (Fusion head unit rides the forward feed through the BODY PDU on CB30; the JL Audio amp is the direct-AUX-feed device) |
| **SafetyHub 150 (Recovery)**         | 150A MRBF  | 2 AWG   | AUX battery+<br/>└→ 150A MRBF<br/>&nbsp;&nbsp;&nbsp;└→ SafetyHub 150        | ~90A (ARB only — winch control on BODY PDU CB43) | 167% of max load (future-proofed) |
| **JL Audio MV800/8i Amp**            | 80A MRBF   | 4 AWG   | AUX battery+<br/>└→ 80A MRBF<br/>&nbsp;&nbsp;&nbsp;└→ JL Audio MV800/8i (under rear seat) | 80A max (fuse-limited) | Matches the amp's recommended 80A fuse value and protects the 4 AWG run (95A @ 20°C) — downsized from 100A on 2026-09-22, keeping 4 AWG ({{ tbd(149) }}) |

## Firewall-Side CBs (Co-located with Firewall CONSTANT Bus)

Mounted within 7" of [Firewall CONSTANT Bus][constant-bus]. Protect each downstream controller.

| Circuit                      | Model                                            | Rating | Reset Type | Power Path                                                                         | Max Load                                                  | Sizing                              |
| :--------------------------- | :----------------------------------------------- | :----: | :--------- | :--------------------------------------------------------------------------------- | :-------------------------------------------------------- | :---------------------------------- |
| **SwitchPros RCR-Force 12**  | Mechanical Products<br/>([174-S2-150-2][mp-150]) |  150A  | Manual     | Firewall CONSTANT Bus<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ SwitchPros           | ~100A (all lighting outputs on)                           | 150% of max load                    |
| **BODY PDU**                 | Mechanical Products<br/>([174-S2-100-2][mp-100]) |  100A  | Manual     | Firewall CONSTANT Bus<br/>└→ 100A CB<br/>&nbsp;&nbsp;&nbsp;└→ BODY PDU             | ~54A max (radio 15A, USB 13A, camera 10A, seats 10A peak, winch control 2A, cargo 4A) | 185% of max load (future expansion) |

!!! info "Wire Sizing for Protection"
Forward feed uses 2/0 AWG protected by the 250A MRBF for the 13-ft run to the firewall bus (now carries only SP+BODY, ~154A max; 2/0 retained for upgrade headroom). 2/0 AWG copper is rated ~265A @ 60°C (project wire-ampacity reference), so the 250A fuse is at or below the wire's ampacity and equal to the 2105 bus rating. Project rule (2026-09-22): when protection exceeds its wire, drop the rating rather than upsize the wire. Firewall-side outputs use 2 AWG (130A @ 20°C) for SwitchPros and BODY PDU. Audio amp uses 4 AWG (95A @ 20°C, JL Audio minimum spec) for the short ~3-4 ft run from AUX battery to under-seat amp location.

**Mechanical Products Series 17 (2 units, firewall side):**

- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Dimensions: 3.39" L × 1.9" W (per unit)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: 2 at firewall (bus side: 150A SP + 100A BODY)

**Space Requirements:**

- **Battery post:** MRBF blocks mount on the AUX+ post — no wheel-well CB bracket needed
- **Firewall-side cluster:** 2 CBs in a row with wiring clearance — ~7" × 4" (~28 sq in) near bus

## Related Documentation

- [AUX battery Distribution Overview][rear-battery]
- [Firewall CONSTANT Bus][constant-bus] - Downstream distribution
- [SwitchPros][switchpros] - Load details for SwitchPros circuit
- [SafetyHub 150][safetyhub] - Load details for SafetyHub circuit (ARB compressor)
- [BODY PDU][body-rtmr] - Load details for BODY PDU circuit
- [JL Audio MV800/8i Amp][audio] - Load details for amplifier circuit

[^mrbf]: Blue Sea Systems MRBF terminal fuse: 30–300 A, interrupt 10,000 A @ 14 V DC, ignition protected; requires terminal fuse block 5191 (single) or 2151 (dual). https://bluesea.com/products/5184 and https://defender.com/en_us/blue-sea-systems-dual-mrbf-terminal-fuse-block-2151 (accessed 2026-10-17). Part numbers to confirm at order ({{ tbd(331) }}).

[mp-150]: https://www.waytekwire.com/item/49079/
[mp-100]: https://www.waytekwire.com/item/49077/
[rear-battery]: index.md
[constant-bus]: 02-constant-bus.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[safetyhub]: 04-safetyhub.md
[body-rtmr]: 03-body-pdu.md
[audio]: ../../06-audio-systems/02-amplifier.md
