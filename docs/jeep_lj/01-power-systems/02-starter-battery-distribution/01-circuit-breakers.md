---
hide:
  - toc
---

# 1.2.1 Circuit Protection {#front-battery-circuit-breakers}

## Overview

START battery positive circuits are protected in two places:

1. **Battery post** — Blue Sea MRBF terminal fuses mounted directly on the START+ post (PMU, Forward Distribution Bus master, BCDC input)
2. **Engine bay** — Mechanical Products Series 17 circuit breakers and inline fuses at the [START+ Forward Distribution Bus][front-battery]

## Battery-Post Terminal Fuses (MRBF)

Blue Sea Systems MRBF terminal fuses (30–300 A, 10,000 A AIC @ 14 V DC, ignition protected) sit on the battery post in a terminal fuse block — dual block 2151 for PMU + forward bus, single block 5191 for BCDC.[^mrbf] Part numbers to confirm at order: {{ tbd(331) }}.

| Circuit        | Fuse            | Wire   | Power Path                                                                 | Max Load                       | Sizing                                                                                                         |
| :------------- | :-------------: | :----- | :------------------------------------------------------------------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------------- |
| **PMU24**      | 150A MRBF       | 1 AWG  | START battery+<br/>└→ 150A MRBF<br/>&nbsp;&nbsp;&nbsp;└→ PMU24 battery stud | 85–115A typical; 150A stud max | Matches the PMU battery stud's 150 A constant limit;[^pmu-pinout] 1 AWG @ 150A, ~7 ft, 60°C-derated ≈ 2.6% drop (2.0% at 115A typical) — downsized from 2/0 + 250A CB (2026-10-17) |
| **Fwd Dist Bus (master)** | 100A MRBF | 2 AWG | START battery+<br/>└→ 100A MRBF<br/>&nbsp;&nbsp;&nbsp;└→ [START+ Forward Distribution Bus][front-battery] | ~62A continuous / ~102A brief peak | At or below the 2 AWG ampacity (110A @ 60°C); the brief ~102A peak is inside the MRBF time-current curve;[^mrbf] selective with the downstream load CBs |
| **BCDC Input** | 80A MRBF        | 4 AWG  | START battery+<br/>└→ 80A MRBF<br/>&nbsp;&nbsp;&nbsp;└→ BCDC Alpha 50      | 50–55A BCDC input              | 145–160% of max load                                                                                           |

**Total battery-post fuses:** 3 (PMU 150A, Forward Dist Bus master 100A, BCDC 80A)

**Why terminal fuses instead of inline CBs:** one joint per circuit instead of three (lug→CB in, CB out→lug), no stacked ring lugs beyond the block, and the within-7"-of-post rule is satisfied by mounting on the post itself. Fuses are not resettable — carry spares. Replaces the three Mechanical Products Series 17 inline CBs (174-S2-250-2, 174-S2-100-2, 174-S2-080-2) at the START battery (2026-10-17).

## Forward Distribution Bus Breakers (engine bay)

Loads on the [START+ Forward Distribution Bus][front-battery] (engine bay) are each protected at the bus, fed from the 100A master MRBF above. The two heavy loads use Mechanical Products Series 17 breakers (SKUs follow the S2 pattern — confirm via {{ tbd(135) }}); the two light loads use ATO/ATC inline fuse holders at the bus.

| Circuit | Model | Rating | Power Path | Max Load | Sizing |
| :------ | :---- | :----: | :--------- | :------- | :----- |
| **Radiator Fan** | Mechanical Products (174-S2-060-2) | 60A CB | Fwd Bus → 60A CB → fan | 53A continuous | 113% of max load (protects 4 AWG) |
| **iBooster main** | Mechanical Products (174-S2-050-2) | 50A CB | Fwd Bus → 50A CB → iBooster | 40A brief peak / 0.25A idle | 125% of brief peak (protects 8 AWG) |
| **CT4 12V supply** | ATO/ATC inline fuse holder | 15A fuse | Fwd Bus → 15A fuse → HDP24 pin 2 → CT4 | ~9A | Protects 14 AWG; size-16 contact 13A |
| **PBS-I battery +12V** | ATO/ATC inline fuse holder | 5A fuse | Fwd Bus → 5A fuse → HDP24 pin 22 → PBS-I RED | Standby {{ tbd(84) }} | Protects 14 AWG |

**Total Forward Bus protection:** 2 CBs (fan 60A, iBooster 50A) + 2 inline fuses (CT4 15A, PBS-I 5A). The TCU moved back to PMU OUT15 (2026-10-17); its 25A bus CB is deleted.

**Series 17 Circuit Breakers (engine bay, 2 units):**

- Manufacturer: Mechanical Products Series 17
- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Dimensions: 3.39" L × 1.9" W (per unit)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: Engine bay, on a bracket beside the [Forward Distribution Bus][front-battery]

**Space Requirements:** The MRBF blocks mount on the START+ post (no wheel-well bracket needed). The 2 forward-bus load CBs plus 2 fuse holders mount in the engine bay beside the Forward Distribution Bus, not in the wheel well.

## Related Documentation

- [START battery Distribution Overview][front-battery]
- [PMU Outputs][pmu-outputs] - Load details for PMU circuit (Dakota Digital, TCU, communication systems, etc.)
- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [Communication Systems][comms] - Radio and intercom specifications (now PMU powered)

[^mrbf]: Blue Sea Systems MRBF terminal fuse: 30–300 A, interrupt 10,000 A @ 14 V DC, ignition protected; requires terminal fuse block 5191 (single) or 2151 (dual). https://bluesea.com/products/5184 and https://defender.com/en_us/blue-sea-systems-dual-mrbf-terminal-fuse-block-2151 (accessed 2026-10-17). Part numbers to confirm at order ({{ tbd(331) }}).
[^pmu-pinout]: ECUMaster, *PMU-24 DL Pinout v1.1* (2023-10-06): battery stud "Maximum constant current: 150 A"; O1–O5, O12–O16 25 A; O6–O11 15 A; O17–O24 7 A; terminals 211CC2S2160P 13–17 AWG, 211CC3S2120 14–16 AWG, 211CC3S3120 10–12 AWG. https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf (accessed 2026-10-17).

[front-battery]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[bcdc]: ../01-power-generation/03-bcdc.md
[comms]: ../../07-communication-systems/index.md
