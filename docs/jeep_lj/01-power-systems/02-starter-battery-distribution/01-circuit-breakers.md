---
hide:
  - toc
---

# 1.2.1 Circuit Breakers {#front-battery-circuit-breakers}

## Overview

All START battery positive circuits protected by Mechanical Products Series 17 circuit breakers with direct battery connections.

**Location:** Driver rear wheel well, within 7" of START battery positive terminal (ABYC/NEC code compliant)

## Circuit Breaker Specifications

| Circuit        | Model                                            | Rating | Reset Type | Power Path                                                          | Max Load                                  | Sizing                                                             |
| :------------- | :----------------------------------------------- | :----: | :--------- | :------------------------------------------------------------------ | :---------------------------------------- | :----------------------------------------------------------------- |
| **PMU24**      | Mechanical Products<br/>([174-S2-250-2][mp-250]) |  250A  | Manual     | START battery+<br/>└→ 250A CB<br/>&nbsp;&nbsp;&nbsp;└→ PMU24        | 140-170A typical (radiator fan, iBooster + TCU no longer on PMU) | Protects 2/0 AWG (265A @ 60°C); now generously oversized after relocation |
| **Fwd Dist Bus (master)** | Mechanical Products<br/>(174-S2-150-2, {{ tbd(135) }}) | 150A | Manual | START battery+<br/>└→ 150A CB<br/>&nbsp;&nbsp;&nbsp;└→ [START+ Forward Distribution Bus][front-battery] | ~108A peak (~68A continuous) | Protects 2 AWG forward feed; selective with downstream load CBs |
| **BCDC Input** | Mechanical Products<br/>([174-S2-080-2][mp-80])  |  80A   | Manual     | START battery+<br/>└→ 80A CB<br/>&nbsp;&nbsp;&nbsp;└→ BCDC Alpha 50 | 50-55A BCDC input                         | 145-160% of max load                                               |

**Total battery-side Circuit Breakers:** 3 (PMU 250A, Forward Dist Bus master 150A, BCDC 80A)

!!! info "PMU Circuit Breaker Sizing"
250A CB sized to protect 2/0 AWG wire (265A @ 60°C). With the radiator fan, iBooster, and TCU relocated to the [Forward Distribution Bus][front-battery], typical PMU load drops to ~85-115A (well under half the CB rating). The CB is left at 250A (no benefit to downsizing).

## Forward Distribution Bus Breakers (engine bay)

The three loads relocated off the PMU each get a breaker at the [START+ Forward Distribution Bus][front-battery] (engine bay), fed from the 150A master above. SKUs follow the Mechanical Products Series 17 S2 pattern — confirm via {{ tbd(135) }}.

| Circuit | Model | Rating | Power Path | Max Load | Sizing |
| :------ | :---- | :----: | :--------- | :------- | :----- |
| **Radiator Fan** | Mechanical Products (174-S2-060-2) | 60A | Fwd Bus → 60A CB → fan | 53A continuous | 113% of max load (protects 4 AWG) |
| **iBooster main** | Mechanical Products (174-S2-050-2) | 50A | Fwd Bus → 50A CB → iBooster | 40A brief peak / 0.25A idle | 125% of brief peak (protects 8 AWG) |
| **Turbolamik TCU** | Mechanical Products (174-S2-025-2) | 25A | Fwd Bus → 25A CB → TCU | 15A continuous | 167% of max load (protects 12 AWG) |

**Total Forward Bus Circuit Breakers:** 3 (fan 60A, iBooster 50A, TCU 25A)

**All Circuit Breakers:**

- Manufacturer: Mechanical Products Series 17
- Type: Surface mount
- Reset: Manual (Type III - push to reset)
- Terminals: 3/8"-16 studs (S2 configuration)
- Dimensions: 3.39" L × 1.9" W (per unit)
- Ratings: 48V DC (20-150A), 30V DC (175-200A), 14V DC (225-300A)
- Standards: Marine-rated (SAE J1171, ABYC E-11, UL1500, IP67, MIL-STD-202)
- Mounting: Driver rear wheel well within 7" of battery positive terminal

**Space Requirements:** 3 battery-side CBs (PMU 250A, Forward Bus master 150A, BCDC 80A) side-by-side with wiring clearance: ~10" × 4" (~40 sq in). The 3 forward-bus load CBs (fan/iBooster/TCU) mount in the engine bay on a bracket beside the [Forward Distribution Bus][front-battery], not in the wheel well.

## Related Documentation

- [START battery Distribution Overview][front-battery]
- [PMU Outputs][pmu-outputs] - Load details for PMU circuit (radiator fan, Dakota Digital, communication systems, etc.)
- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [Communication Systems][comms] - Radio and intercom specifications (now PMU powered)

[mp-250]: https://www.waytekwire.com/item/49082/
[mp-80]: https://www.waytekwire.com/item/49015/
[front-battery]: index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[bcdc]: ../01-power-generation/03-bcdc.md
[comms]: ../../07-communication-systems/index.md
