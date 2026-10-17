---
hide:
  - toc
---

# 1.2 START battery Distribution (Driver Rear Wheel Well) {#starter-battery-distribution}

/// html | div.product-info
![Odyssey PC1500 Battery Terminals](../../images/odyssey-pc1500.jpg){ loading=lazy }
///

## Overview

The START battery (driver rear wheel well) provides power for critical engine and safety systems:

1. **Direct high-current** → Starter (no CB), alternator charging input (no CB)
2. **MRBF terminal fuse protected** → PMU (150A MRBF), BCDC (80A MRBF)
3. **[START+ Forward Distribution Bus](#start-forward-bus)** (100A master MRBF → single feed → engine-bay busbar) → radiator fan (60A CB), iBooster main (50A CB), CT4 (15A fuse), PBS-I (5A fuse)
4. **Direct low-current** → ECM, grid heater (fusible link protection)

See [Circuit Protection][circuit-breakers] for complete fuse and CB specifications. Battery-side protection is Blue Sea MRBF terminal fuses mounted on the START+ post (within-7" rule satisfied on the post);[^mrbf] engine-bay load protection is at the forward bus.

!!! info "Single Source of Truth"
This page is the authoritative source for all START battery wire specs (gauge, distance, voltage drop). Component pages reference here. For battery specs see [Section 1.1][batteries]. For ground bus bars see [Section 1.5][grounding].

## START battery Positive Terminal (7 circuits, 6 lugs)

| Circuit                    | Destination          | Wire Gauge  | Distance | Current  | Voltage Drop    | Protection   |
| :------------------------- | :------------------- | :---------- | :------- | :------- | :-------------- | :----------- |
| [Alternator][alternator]   | Engine bay           | 2/0 AWG     | 8 ft     | 270A     | 2.81% @ 60°C    | None         |
| [Starter][starter]         | Engine bay           | 2/0 AWG     | 6 ft     | 400-600A | 1.9-3.9% @ 20°C | None         |
| [PMU24][pmu]               | Engine bay           | 1 AWG       | ~7 ft    | 150A max (stud limit)[^pmu-pinout] | 2.6% @ 60°C (2.0% @ 115A typical) | 150A MRBF |
| [START+ Forward Dist Bus](#start-forward-bus) | Engine bay | 2 AWG | ~8 ft | ~102A brief peak | 1.2% @ 60°C | 100A MRBF |
| ECM                        | Engine bay           | Per Cummins | Short    | <5A      | Negligible      | Fusible link |
| [Grid Heater][grid-heater] | Engine bay           | Per Cummins | Short    | ~80A     | Negligible      | Fusible link |
| [BCDC Alpha 50][bcdc]      | Passenger rear wheel well | 4 AWG       | ~6 ft    | 50A      | 0.94% @ 20°C    | 80A MRBF     |

**Post lugs (6):** alternator, starter, dual MRBF block (PMU + forward bus), single MRBF block (BCDC), ECM, grid heater. The MRBF blocks mount on the post, so the fused circuits add no stacked ring lugs beyond the block.[^mrbf] PMU feed downsized from 2/0 AWG + 250A CB to 1 AWG + 150A MRBF (2026-10-17) to match the PMU battery stud's 150 A constant limit; ECUMaster's minimum is 25 mm² (3 AWG).[^pmu-pinout] See [Circuit Protection][circuit-breakers].

## START+ Forward Distribution Bus {#start-forward-bus}

The radiator fan and iBooster were relocated off the PMU onto START-direct power, and the CT4 and PBS-I — the only loads that must stay live at key-off — join them here. All sit forward (engine bay / dash) while the START battery is in the rear wheel well, so — mirroring the [AUX forward-feed architecture][constant-bus] — a **single master-protected feed** runs forward to an engine-bay busbar that fans out to the loads on short local feeds. This keeps the long rear-to-front run to one heavy cable instead of several, and places each load's protection near its load.

**Busbar:** Blue Sea 2105 MaxiBus (250A), engine bay, insulated cover — recommended; confirm with {{ tbd(135) }}
**Master feed:** 2 AWG, ~8 ft, 100A MRBF terminal fuse at the START post — the fuse sits at or below the 2 AWG ampacity (110A @ 60°C)

| Load | Feed (from bus) | Wire Gauge | Distance | Current | Voltage Drop | Protection |
| :--- | :-------------- | :--------- | :------- | :------ | :----------- | :--------- |
| [Radiator Fan][radiator-fan] | Radiator shroud | 4 AWG | short | 53A continuous | <1% @ 60°C[^fwd-bus-vdrop] | 60A CB |
| [iBooster][brake-booster] main | Firewall | 8 AWG | short | 40A peak / 0.25A idle | <0.5%[^fwd-bus-vdrop] | 50A CB |
| [Command Touch CT4][ct4] 12V supply | HDP24 pin 2 → steering column | 14 AWG | — | ~9A | — | 15A inline fuse |
| [PBS-I][keyless-ignition] RED +12V battery | HDP24 pin 22 → PBS-I | 14 AWG | — | Standby {{ tbd(84) }} | — | 5A inline fuse |

The master feed carries the combined load (~62A continuous: fan 53A + CT4 9A; ~102A brief peak: fan 53A + iBooster 40A + CT4 9A); voltage drop and fuse sizing are set on that single cable.[^fwd-bus-vdrop] The iBooster's separate ignition **enable** (~5A) is sourced from the [Ignition Signal bus][ignition-signal], not this bus. Fan speed is set by a dedicated fan controller ({{ tbd(134) }}) with its own coolant sensor, independent of the PMU and J1939. The Turbolamik TCU returned to [PMU OUT15][pmu-outputs] (2026-10-17), kept alive after key-off by the PMU "Delayed turn off" window.

!!! info "Shared forward feed — intentional tradeoff"
    This is the same shared-feed tradeoff the [AUX side][constant-bus] accepts, and is more robust than the loads' former shared dependency on the PMU module. Each load keeps its own fuse or breaker. See [Standards Exceptions][standards-exceptions] for the full "no bus bar between battery and loads" exception rationale.

[^fwd-bus-vdrop]: Master feed 2 AWG @ ~102A brief peak (~62A continuous), ~8 ft, 60°C-derated (×1.2) ≈ 1.2% — sized on the combined load. The brief peak is inside the 100A MRBF time-current curve (MRBF holds ≥135% for more than 60 s class).[^mrbf] Load feeds are short from the engine-bay bus, so per-load drop is negligible: fan 4 AWG @ 53A, iBooster 8 AWG @ 40A brief, CT4 14 AWG @ 9A. Final master-feed length and selective coordination with the downstream load CBs pending {{ tbd(136) }} and {{ tbd(135) }}.

## START battery Negative Terminal (6 connections)

| Circuit                                    | Destination          | Wire Gauge  | Distance | Current    | Voltage Drop  |
| :----------------------------------------- | :------------------- | :---------- | :------- | :--------- | :------------ |
| Engine block ground stud (starter return)  | Engine bay           | 2/0 AWG     | ~8 ft    | 600A+ peak | <0.1V @ 60°C — short 2/0 jumper from the block to the [Engine Bay Ground Bus][engine-ground-bus] |
| ECM                                        | Engine bay           | 12 AWG      | Short    | <5A        | Negligible    |
| [Grid Heater][grid-heater]                 | Engine bay           | Per Cummins | Short    | ~80A       | Negligible    |
| [AUX Battery][aux-battery]                 | Passenger rear wheel well | 1/0 AWG     | 5-6 ft   | 75A max    | <0.05V @ 20°C |
| [G1 GMRS Radio][radios]                    | Roll cage, overhead  | 10 AWG      | Measure  | 15A TX     | Recheck       |
| [STX Intercom][radios]                     | Dashboard            | 10 AWG      | ~8 ft    | 5A         | 0.4% @ 20°C   |

Radio grounds direct to battery for RF noise isolation. ECM/grid heater via Cummins harness to isolate from starter spikes.

START− intentionally has no local chassis bond — its chassis reference is the 2/0 AWG run forward, which lands at the engine block ground stud (the starter return point) and reaches the [Engine Bay Ground Bus][engine-ground-bus] through a short (~3 ft) 2/0 jumper (re-landed 2026-10-17 to shorten the cranking loop — see [Starter][starter]). The rear frame chassis bond lives on the AUX− side. The 6 connections above are the complete, final set; an earlier "7 connections" count was an error.

## Related Documentation

- [Power Generation][power-gen] - Battery and alternator specifications
- [Circuit Protection][circuit-breakers] - MRBF terminal fuse and CB specifications
- [Grounding Architecture][grounding] - Ground bus bars
- [PMU24][pmu] - Power management unit
- [BCDC Alpha 50][bcdc] - DC-DC charger to AUX battery
- [Starter System][starter] - Starter specifications
- [Alternator][alternator] - Charging system
- [AUX battery Distribution][aux-battery] - Aux/accessory battery system

[^mrbf]: Blue Sea Systems MRBF terminal fuse: 30–300 A, interrupt 10,000 A @ 14 V DC, ignition protected; requires terminal fuse block 5191 (single) or 2151 (dual). https://bluesea.com/products/5184 and https://defender.com/en_us/blue-sea-systems-dual-mrbf-terminal-fuse-block-2151 (accessed 2026-10-17). Part numbers to confirm at order ({{ tbd(331) }}).
[^pmu-pinout]: ECUMaster, *PMU-24 DL Pinout v1.1* (2023-10-06): battery stud "Maximum constant current: 150 A"; O1–O5, O12–O16 25 A; O6–O11 15 A; O17–O24 7 A; terminals 211CC2S2160P 13–17 AWG, 211CC3S2120 14–16 AWG, 211CC3S3120 10–12 AWG. https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf (accessed 2026-10-17).

[pmu]: ../04-pmu/index.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[ct4]: ../../05-control-interfaces/03-command-touch-ct4.md
[keyless-ignition]: ../../05-control-interfaces/06-keyless-ignition.md
[bcdc]: ../01-power-generation/03-bcdc.md
[batteries]: ../01-power-generation/01-batteries.md
[grid-heater]: ../../02-engine-systems/07-grid-heater.md
[grounding]: ../05-grounding/index.md
[engine-ground-bus]: ../05-grounding/01-engine-bay-ground-bus.md
[power-gen]: ../01-power-generation/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[starter]: ../../02-engine-systems/01-starter.md
[alternator]: ../01-power-generation/02-alternator.md
[radios]: ../../07-communication-systems/index.md
[circuit-breakers]: 01-circuit-breakers.md
[radiator-fan]: ../../02-engine-systems/06-radiator-fan.md
[brake-booster]: ../../02-engine-systems/02-brake-booster.md
[ignition-signal]: ../06-ignition-signal/index.md
[constant-bus]: ../03-aux-battery-distribution/02-constant-bus.md
[standards-exceptions]: ../STANDARDS-EXCEPTIONS.md
