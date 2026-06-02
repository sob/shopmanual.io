---
hide:
  - toc
tags:
  - wire-routing
  - firewall
---

# 1.7.2 Firewall Ingress {#firewall-ingress}

All firewall penetration points for wire routing between engine bay and cabin.

## Cummins Bulkhead Connector

**Size:** 2" diameter hole with factory bulkhead connector (self-sealing)

**Contents:** Factory Cummins interior harness - ECM signals, accelerator pedal, warning lamps, J1939 CAN tap to Dakota Digital

---

## Deutsch HDP20 Bulkhead Connector

Single weatherproof bulkhead connector for all custom wiring through firewall.

### Connector Specification

| Component | Part Number | Description |
|:----------|:------------|:------------|
| **Receptacle** | HDP24-24-29PE-L015 | 29-pin bulkhead receptacle, flange mount (engine side) |
| **Plug** | HDP26-24-29SE | 29-pin plug (cabin side) |

**Insert Arrangement 24-29:** 29× size 16 contacts

- Size 16 contacts: 14-20 AWG, 13A (29 available, ~16 used after PBS-I keyless, ~13 future headroom — exact used-count pending final pin-map recount, see [TBD Tracker][tbd-tracker])

**Mounting:** Single 1.5" diameter hole in firewall (same as previous 24-21 - shell size unchanged)

**Sealing:** IP67/IP68, bayonet quick-connect coupling

**Purpose:** Non-SwitchPros circuits — PMU outputs, CT4 outputs, cabin switches to PMU, winch control, ignition signal, keyless ignition. SwitchPros forward-going outputs use a separate dedicated bulkhead (see [SwitchPros Firewall Bulkhead](#switchpros-firewall-bulkhead)).

!!! info "Upsize from HDP24-24-21 → HDP24-24-29 (2026-05-30)"
The original 24-21 insert (17 size-16 + 4 size-12) was at 16/17 size-16 capacity. Architectural changes (SwitchPros moved to firewall, keyless ignition) added new circuits. Upsized to 24-29 (all size-16) for headroom. SwitchPros forward outputs were split out to a dedicated SP bulkhead for modularity and noise isolation, freeing more pins.

### Why Single Connector

RF interference analysis determined that with ferrite chokes on radio power leads at the radio end, all circuits can share one connector safely. The temp probe routes separately to grille (not through main connector).

---

## Pin Assignment

### Engine Bay → Cabin (6 wires)

| Pin | Circuit | Gauge | Source | Destination | Contact |
|:---:|:--------|:-----:|:-------|:------------|:-------:|
| 1 | GMRS Radio power (+) | 14 AWG | PMU OUT6 | Midland G1 | #16 |
| 2 | **[Available]** | - | - | - | #16 |
| 3 | STX Intercom power | 14 AWG | PMU OUT20 | STX intercom | #16 |
| 4 | Brake lights | 16 AWG | PMU OUT21 | Rear tail lights | #16 |
| 5 | Reverse lights | 16 AWG | PMU OUT22 | Rear tail lights | #16 |
| 6 | DRL/Parking | 16 AWG | PMU OUT23 | Rear tail lights | #16 |
| 12 | PBS-I PINK IGN (ignition signal) | 14 AWG | PBS-I ICM | Ignition bus (cabin) | #16 |

### Cabin → Engine Bay (10 wires)

Pin 12 carries the PBS-I PINK IGN ignition signal; the keyswitch was removed when the PBS-I self-contained keyless system was adopted.

| Pin | Circuit | Gauge | Source | Destination | Contact |
|:---:|:--------|:-----:|:-------|:------------|:-------:|
| 7 | Right turn signal | 14 AWG | CT4 SW1 | Right fender + rear | #16 |
| 8 | Left turn signal | 14 AWG | CT4 SW2 | Left fender + rear | #16 |
| 9 | Low beam headlights | 14 AWG | CT4 SW3 | LP6 Pin 1 (both) | #16 |
| 10 | High beam headlights | 14 AWG | CT4 SW4 | LP6 Pin 4 (both) | #16 |
| 11 | Horn button trigger | 18 AWG | Steering wheel button | PMU In 1 | #16 |
| 13 | Brake switch | 18 AWG | Brake pedal switch | PMU In 2 | #16 |
| 14 | A/C request | 18 AWG | HVAC controls | PMU In 9 | #16 |
| 15 | WAIT-gated PURPLE START | 16 AWG | PBS-I via WAIT-gate relay | Cole Hersee 24213 coil | #16 |
| 16 | Winch control IN | 18 AWG | Dash rocker switch | Winch contactor | #16 |
| 17 | Winch control OUT | 18 AWG | Dash rocker switch | Winch contactor | #16 |

### Available (13 spare pins)

Pins 18-29 + pin 2 (legacy spare) reserved for future non-SwitchPros circuits. The former Boomerang fob-present and gated-start pins were dropped when the PBS-I self-contained keyless system replaced the Boomerang/PMU keyless approach — PBS-I needs no firewall pins beyond PINK IGN (pin 12) and WAIT-gated PURPLE START (pin 15).

---

## SwitchPros Firewall Bulkhead {#switchpros-firewall-bulkhead}

Dedicated bulkhead for SwitchPros forward-going outputs. Separate from main HDP24 for harness modularity, noise isolation (PWM-capable outputs kept away from signal wires), and future expansion headroom.

### Connector Specification

| Component | Part Number | Description |
|:----------|:------------|:------------|
| **Receptacle** | HDP24-18-14PE-L015 | 14-pin bulkhead receptacle, flange mount (engine side) |
| **Plug** | HDP26-18-14SE | 14-pin plug (cabin side) |

**Insert Arrangement 18-14:** 14× size 16 contacts

- Size 16 contacts: 14-20 AWG, 13A (14 available, 6 used today, 8 future headroom)

**Mounting:** Single 1.25" diameter hole in firewall (shell size 18, smaller than main HDP24-24)

**Sealing:** IP67/IP68, bayonet quick-connect coupling

**Location:** Adjacent to main HDP24 on firewall, passenger side cabin/EB transition (near SwitchPros power module)

### Pin Assignment

Each SwitchPros output uses **2 pins** (power out + ground return) — load grounds return to SwitchPros Ground Bus at firewall (cabin side) for clean SP-native architecture.

| Pin | Circuit | Gauge | Direction | Source | Destination |
|:---:|:--------|:-----:|:----------|:-------|:------------|
| 1 | OUT-3 fog light (+) | 14 AWG | Cabin → EB | SP output | BD S8 fog (front bumper) |
| 2 | OUT-3 fog light (−) | 14 AWG | EB → Cabin | Light ground | SP Ground Bus |
| 3 | OUT-6 front rocks (+) | 14 AWG | Cabin → EB | SP output | Front bumper rock + 2× front wheel well rocks (splice in EB) |
| 4 | OUT-6 front rocks (−) | 14 AWG | EB → Cabin | Lights ground | SP Ground Bus |
| 5 | OUT-17 front locker (+) | 18 AWG | Cabin → EB | SP low-side output | Front ARB solenoid |
| 6 | OUT-17 front locker (−) | 18 AWG | EB → Cabin | Solenoid ground | SP Ground Bus |

### Available (8 spare pins)

Pins 7-14 reserved for future SwitchPros forward outputs. Likely candidates:

- OUT-2 ditch lights (2 pins) — if routed through firewall instead of A-pillar
- OUT-1 roof lights (2 pins) — if routed through firewall instead of A-pillar (10 AWG fits size-16)
- Additional front-mounted accessories (2 pins each)

### Why Dedicated SP Bulkhead

| Benefit | Detail |
|:--------|:-------|
| **Modularity** | SwitchPros harness is fully Delphi-native end-to-end; no inline crimps at HDP24. R&R the entire SP harness without touching CT4/PMU wiring. |
| **Noise isolation** | PWM-capable lighting outputs kept on a separate connector from low-level signal wires (PMU inputs, CT4 outputs, switch returns). |
| **Future-proof** | 8 free pins accommodate up to 4 more SP forward outputs if A-pillar routing for ditch/roof lights becomes impractical. |
| **Clean ground architecture** | SP outputs return ground to SP Ground Bus on cabin side via dedicated bulkhead pins, no reliance on chassis ground at forward loads. |

### BOM

| Part Number | Description | Qty | ~Price |
|:------------|:------------|:---:|:------:|
| HDP24-18-14PE-L015 | 14-pin receptacle | 1 | $30 |
| HDP26-18-14SE | 14-pin plug | 1 | $25 |
| 0460-202-16141 | Size 16 pin, solid, nickel | 6 | $0.50 ea |
| 0462-201-16141 | Size 16 socket, solid, nickel | 6 | $0.55 ea |
| 114018 | Sealing plug, size 16 cavity | 8 | $0.25 ea |

**Estimated Total:** ~$65

**Crimping Tool:** HDT-48-00 (shared with main HDP24)

---

## Separate Routing (Not Through Main Connector)

### Cabin → Grille (Small Grommet)

| Circuit | Gauge | Source | Destination | Notes |
|:--------|:-----:|:-------|:------------|:------|
| Outside temp probe (+) | 22 AWG | BIM-17-2 | SEN-15-1 (grille) | Twisted pair |
| Outside temp probe (-) | 22 AWG | BIM-17-2 | SEN-15-1 (grille) | Twisted pair |

**Routing:** Separate small grommet near grille area - keeps analog sensor isolated from power circuits.

### Radio Grounds (Floor/Frame Routing)

Radio grounds do NOT go through firewall - they route through cab floor to START battery:

| Circuit | Gauge | Source | Destination |
|:--------|:-----:|:-------|:------------|
| GMRS Radio ground (-) | 14 AWG | Midland G1 | START battery negative |
| STX Intercom ground (-) | 14 AWG | STX | START battery negative |

**Routing:** Radios (cabin) → under seat/floor → START battery negative (driver rear wheel well) - exact path TBD (avoid exposed frame rail)

---

## Wire Count Summary

### Main HDP24-24-29 (non-SwitchPros)

| Gauge | Count | Circuits |
|:------|:-----:|:---------|
| 14 AWG | 7 | Radio power (2), CT4 outputs (4), PBS-I PINK IGN (1) |
| 16 AWG | 4 | PMU lighting outputs (3), WAIT-gated PURPLE START (1) |
| 18 AWG | 5 | Switch signals (3: horn, brake, A/C), winch control (2) |
| **Main connector** | **16** | HDP24-24-29 (16 of 29 used, 13 spare; exact count pending final recount) |

### SwitchPros HDP24-18-14 (forward SP outputs)

| Gauge | Count | Circuits |
|:------|:-----:|:---------|
| 14 AWG | 4 | OUT-3 fog (power + ground), OUT-6 front rocks (power + ground) |
| 18 AWG | 2 | OUT-17 front locker (power + ground) |
| **SP connector** | **6** | HDP24-18-14 (6 of 14 used, 8 spare for future SP) |

### Separate Routing (Not Through Bulkheads)

| Gauge | Count | Circuits |
|:------|:-----:|:---------|
| 22 AWG | 2 | Temp probe (separate small grommet to grille) |
| 14 AWG | 2 | Radio grounds (cabin floor → START battery, not through firewall) |

---

## Pin Budget Audit (Historical) {#pin-budget-audit}

*This audit drove the decision to upsize to HDP24-24-29 + add dedicated SwitchPros HDP24-18-14. Final architecture documented above.*

### HDP24-24-21 (original)

Architectural changes (SwitchPros relocated to firewall, Firewall CONSTANT bus, keyless ignition) added new circuits that must penetrate the firewall. This section accounts for them against current connector capacity.

### Current usage

| Bank | Capacity | Used | Spare |
|:-----|:--------:|:----:|:-----:|
| Size 16 (14-20 AWG, 13A) | 17 | 16 | 1 (pin 2) |
| Size 12 (12-14 AWG, 25A) | 4 | 0 | 4 (all reserved) |
| **TOTAL** | **21** | **16** | **5** |

### Pending additions

| Circuit | Direction | Gauge | Pins | Source | Destination |
|:--------|:----------|:-----:|:----:|:-------|:------------|
| SwitchPros OUT-3 (fog light) | Cabin → EB → front bumper | 14 AWG | 1 (chassis ground at light) | SP at firewall | BD S8 fog |
| SwitchPros OUT-17 (front locker, low-side) | Cabin → EB → front axle | 18 AWG | 1 (chassis ground at solenoid) | SP at firewall | Front ARB solenoid |
| SwitchPros OUT-6 (front rocks subset) | Cabin → EB → front rocks | 14 AWG | 1 (chassis ground at lights) | SP at firewall | Front bumper rock + front wheel well rocks |
| Boomerang fob present | Cabin → EB | 18 AWG | 1 | Bullet 230 (cabin) | PMU In 4 |
| Gated start return | Cabin → EB | 18 AWG | 1 | Brake switch start tap | EB P/N relay |
| **TOTAL NEW** | | | **5** | | |

!!! note "Ground strategy for forward-going SwitchPros outputs"
Each SwitchPros output normally pairs a power wire (SP → load) with a ground wire (load → SP Ground Bus). For loads forward of the firewall, this doubles the firewall pin count per output.

    **Recommended:** Ground forward-mounted loads to chassis locally. The SwitchPros Ground Bus has a 1/0 AWG bond to chassis at the firewall, so chassis-grounded loads share the same reference. This halves the pin count for forward-going SP outputs (1 pin per output instead of 2).

    Trade-off: relies on chassis ground continuity from front bumper / axle / wheel wells back to the firewall bond. Already required for engine and chassis safety, so no incremental risk.

### Capacity analysis

| Scenario | Size-16 pins used | Spare | Headroom |
|:---------|:-----------------:|:-----:|:--------:|
| **Today (no expansion)** | 16 of 17 | 1 | Minimal |
| **After 5 new circuits (chassis-gnd strategy)** | 21 of 21 (filling pin 2 + 4 size-12 reduced) | 0 | **NONE** |
| **After 8 new circuits (separate-gnd strategy for SP outputs)** | 24 of 21 | -3 | **OVER CAPACITY** |

### Verdict

**Current HDP24-24-21 will work but leaves zero future headroom.**

- The 1 size-16 spare (pin 2) + 4 size-12 reserved cavities can accommodate all 5 new circuits *only* if size-12 cavities accept 18 AWG wires via reducer crimps or 12 AWG dummy wires
- Any future expansion (additional sensors, accessories, telematics) will require a connector change anyway

### Recommendation

**Upsize to Deutsch HDP24-24-29** (same shell size, same firewall hole, 29 size-16 contacts).

| Aspect | HDP24-24-21 (current) | HDP24-24-29 (proposed) |
|:-------|:----------------------|:-----------------------|
| Total contacts | 21 (17 size-16 + 4 size-12) | 29 (all size-16) |
| Used after pending additions | 21 of 21 (full) | 21 of 29 |
| Future headroom | 0 | 8 |
| Firewall hole size | 1.5" diameter | 1.5" diameter (same) |
| Approx connector cost | ~$60 (recpt + plug) | ~$80 (recpt + plug) |
| Crimping tool | HDT-48-00 | HDT-48-00 (same) |

**Net change:** ~$20 extra, same install procedure, same hole, 8 pins of future headroom.

### Alternative: Split into two connectors

Adding a small secondary connector (e.g., HDP20-9-4 with 4 size-20 contacts) for keyless signals only, keeping HDP24-24-21 for current loads. Two penetrations, two sealing surfaces, more work. Not recommended unless HDP24-24-29 is unavailable.

### Implementation order

1. Order HDP24-24-29 receptacle + plug + 12 additional size-16 contacts (8 extra cavities require 8 pins + 8 sockets)
2. Build harness with original 16 circuits + the 5 new circuits
3. Plug-seal remaining 8 cavities for moisture protection
4. Document pin assignments (update the [Pin Assignment](#pin-assignment) section above)

---

## Combined Connector Bill of Materials

### Main HDP24-24-29

| Part Number | Description | Qty | ~Price |
|:------------|:------------|:---:|:------:|
| HDP24-24-29PE-L015 | 29-pin receptacle, flange mount | 1 | $45 |
| HDP26-24-29SE | 29-pin plug | 1 | $35 |
| 0460-202-16141 | Size 16 pin, solid, nickel | 18 | $0.50 ea |
| 0462-201-16141 | Size 16 socket, solid, nickel | 18 | $0.55 ea |
| 114018 | Sealing plug, size 16 cavity | 11 | $0.25 ea |

**Subtotal:** ~$105

### SwitchPros HDP24-18-14

| Part Number | Description | Qty | ~Price |
|:------------|:------------|:---:|:------:|
| HDP24-18-14PE-L015 | 14-pin receptacle, flange mount | 1 | $30 |
| HDP26-18-14SE | 14-pin plug | 1 | $25 |
| 0460-202-16141 | Size 16 pin, solid, nickel | 6 | $0.50 ea |
| 0462-201-16141 | Size 16 socket, solid, nickel | 6 | $0.55 ea |
| 114018 | Sealing plug, size 16 cavity | 8 | $0.25 ea |

**Subtotal:** ~$65

**Grand Total:** ~$170

**Crimping Tool:** HDT-48-00 (size 12-20 solid contacts, used for both connectors)

**Firewall preparation:** Drill **two** 1.5" + 1.25" diameter holes adjacent to each other (passenger side, near SwitchPros mounting location). Allow ~3" minimum spacing between hole centers for sealing clearance.

---

## DRL Auto-Off Signal

**Note:** The DRL cutoff signal does NOT require a separate wire through the firewall. The CT4 SW3 (low beam) wire is tapped on the engine bay side after it passes through the connector:

```text
CT4 SW3 (cabin) → Pin 9 → [ENGINE BAY TAP to PMU In 7] → LP6 headlights
```

PMU In 7 receives the headlight status signal from this tap, enabling DRL auto-off logic.

---

## Related Documentation

- [Wire Routing Overview][wire-routing] - Complete routing by location
- [PMU Outputs][pmu-outputs] - PMU output assignments
- [PMU Inputs][pmu-inputs] - PMU input assignments
- [Command Touch CT4][ct4] - CT4 controller and outputs
- [Dashboard Controls][dash-controls] - Winch rocker switch wiring
- [GMRS Radio][gmrs] - Radio power and ground routing
- [Intercom][intercom] - STX power routing

[wire-routing]: index.md
[tbd-tracker]: ../../09-installation/00-tbd-tracker.md
[keyless-ignition]: ../../05-control-interfaces/06-keyless-ignition.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[pmu-inputs]: ../04-pmu/02-pmu-inputs.md
[ct4]: ../../05-control-interfaces/03-command-touch-ct4.md
[dash-controls]: ../../05-control-interfaces/05-dashboard-controls.md
[gmrs]: ../../07-communication-systems/01-gmrs-radio.md
[intercom]: ../../07-communication-systems/02-intercom.md
