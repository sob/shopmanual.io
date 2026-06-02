---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - safety
---

# 2.11 Diesel Runaway Protection {#runaway-protection}

## Overview

Layered, fully mechanical defense against diesel runaway on the Cummins R2.8. The strategy has two independent layers:

1. **Prevention** - Mishimoto baffled catch can in the crankcase ventilation path blocks the most common runaway initiator (oil ingestion via PCV).
2. **Termination** - AMOT 4261M intake air shutoff valve in the pre-turbo intake tract, manually actuated by a dash-mounted push-pull cable with locking T-handle.

This is a deliberate departure from Cummins' Repower default (no air shutoff) because the ECM kill path documented in [Keyless Ignition][keyless] (normal shutdown drops the PBS-I PINK IGN output, cutting ECM power — the PMU is not in this path) cannot stop a runaway that is sustained by oil or hydrocarbon vapor — the ECM can be cutting injector commands and the engine will still run. The AMOT cable is the only kill path that works under all failure modes, including total electrical/ECM failure.

## Components

| Component                              | Part Number             | Manufacturer    | Notes                                              |
| :------------------------------------- | :---------------------- | :-------------- | :------------------------------------------------- |
| Baffled oil catch can                  | MMOCC-CBT               | Mishimoto       | Compact, 13 oz capacity, petcock drain             |
| Catch can mounting bracket             | MMOCC-UB                | Mishimoto       | Universal aluminum bracket                         |
| Intake air shutoff valve (2.8")        | 4261M02A027-AA          | AMOT            | Manual/pneumatic cylinder, NPT, manual trip        |
| Push-pull cable + locking T-handle     | 30-144-TTL-BH-3         | Midwest Control | 144" cable, turn-to-lock T-handle, 3" travel, bulkhead mount |
| Catch can hose                         | 5/8" oil-resistant      | User-supplied   | 2 ft typical; worm clamps both ends                |
| AMOT-to-intake adapters                | NPT-to-hose, 2.8"       | User-supplied   | Match turbo inlet tube size (verify on R2.8)       |

## Catch Can: Crankcase Ventilation

### Plumbing

```text
R2.8 valve cover breather
    ↓
5/8" oil-resistant hose (engine-side)
    ↓
Catch can INLET (top)
    │  Baffled separation
    ▼
Catch can OUTLET (top)
    ↓
5/8" hose to turbo inlet
    ↓
Turbo inlet (pre-compressor)
```

### Mounting

- Engine bay, intake side, away from exhaust manifold heat
- Vertical orientation; petcock at bottom for draining
- Within easy reach for visual inspection at every oil change

### Function

The R2.8 routes crankcase blow-by vapor back to the pre-turbo intake (factory closed PCV). The baffled can sits in this line. Oil mist condenses on the internal baffles and collects in the reservoir; clean vapor continues to the intake. This blocks the most common runaway initiator on small modern diesels: oil carryover from a worn turbo shaft seal or overfilled crankcase being burned as supplemental fuel.

## AMOT 4261M: Manual Air Shutoff

### Valve Specifications

| Parameter                | Value                          |
| :----------------------- | :----------------------------- |
| Valve body size          | 2.8" (71 mm) - smallest 4261M  |
| Bore size                | 2.4" (61 mm)                   |
| Weight                   | 3.1–4.0 lb                     |
| Body material            | Anodized aluminum              |
| Shaft material           | Stainless steel                |
| Seals                    | Nitrile (200°F max intake temp)|
| Mechanical pull-to-release | 67 N (15 lb)                 |
| Operating mode           | Manually cocked open; spring-loaded; trips closed on cable pull or air-pressure loss |

### Cable + Handle Specifications

| Parameter                | Value                          |
| :----------------------- | :----------------------------- |
| Part                     | Midwest Control 30-144-TTL-BH-3 |
| Length                   | 144" (12 ft) - more than adequate for dash-to-engine-bay |
| Travel                   | 3" working stroke              |
| Handle                   | Turn-to-lock T-handle, bulkhead mount |
| Conduit                  | Steel-armored Bowden           |

### Mounting

- **Valve location:** Pre-turbo intake tract, between air filter outlet and turbo inlet. **Must be pre-turbo** — post-turbo placement does not work because the line is pressurized during normal operation and the turbo itself stores enough air to sustain runaway briefly.
- **Handle location:** Dash, driver-accessible without leaving belted position. Label: `EMERGENCY ENGINE SHUTOFF — PULL TO STOP`.
- **Cable routing:** Through firewall via a dedicated grommet (not shared with other cables), secured every 12" with adel clamps to prevent chafing or sag. Avoid sharp bends (≥6" radius).

### Function

In normal operation the valve is cocked open and held by an internal latch. The cable handle sits flush against the dash bezel. When the driver pulls the T-handle:

1. Cable pulls the AMOT trip lever ≥15 lb of force
2. Internal latch releases
3. Return spring snaps butterfly closed within ~100 ms
4. Engine starves of intake air and stops within 1–2 seconds

The handle's turn-to-lock feature prevents accidental actuation (turn quarter-turn to unlock before pulling) and holds the cable in the tripped position after pulling (turn to lock-pulled).

### Reset Procedure

The 4261M does **not** auto-reset. After actuation:

1. Determine and resolve the cause (oil ingestion, fuel leak, etc.)
2. Open the hood
3. Manually re-cock the AMOT butterfly using the lever on the valve body
4. Push the dash T-handle back to flush, turn to lock-closed
5. Restart engine via normal keyless sequence

This is intentional — it forces a diagnosis step and prevents an unattended restart into the same fault.

## Failure Modes Covered

| Scenario                                  | Covered By               |
| :---------------------------------------- | :----------------------- |
| Oil ingestion via crankcase blow-by       | Catch can (prevention)   |
| Worn turbo shaft seal feeding oil to intake | Catch can (prevention) |
| External fuel/oil/propane vapor inhaled by intake | AMOT cable          |
| ECM stuck commanding injector duty cycle  | AMOT cable               |
| PBS-I/ECM fails to cut injection (PINK IGN stuck, ECM keeps running) | AMOT cable     |
| Total electrical failure                  | AMOT cable (mechanical)  |
| Driver incapacitated                      | Not covered (no auto-trip in this design) |

The last row is the conscious limitation of the manual-only design. Adding speed-sensed auto-trip would require AMOT 4261M with electric solenoid actuator (`4261M02A071-AA`) plus an 8210K speed switch — see [Future Enhancements](#future-enhancements).

## Maintenance

| Interval        | Task                                                   |
| :-------------- | :----------------------------------------------------- |
| Every oil change | Drain catch can via petcock; visually inspect hose condition |
| Every oil change | Verify AMOT lever returns freely (do NOT trip — verify by inspection only) |
| Annually        | Function-test AMOT: engine off, pull T-handle, verify butterfly closes positively. Reset and confirm engine restarts. |
| Annually        | Inspect cable conduit for chafing at firewall grommet and adel clamp points |

## Standards Context

| Reference          | Position                                                  |
| :----------------- | :-------------------------------------------------------- |
| Cummins R2.8 Repower Installation Guide (5504137) | Does not require an air shutoff valve for the consumer crate program |
| Cummins commercial/industrial R2.8 application sheets | Air shutoff standard on oil-field, marine, hazardous-area deployments |
| AMOT 4261M datasheet | "An air intake shut-off valve is recommended for diesel engines which have a possibility of encountering hydrocarbon vapors" |

The off-road LJ build sits between consumer and industrial use cases. Fuel handling during recovery, dust/oil exposure, and modified intake plumbing all push the risk profile toward the industrial side, justifying the additional protection.

## Future Enhancements

Two upgrade paths from this baseline, neither required:

1. **Add electric solenoid auto-trip** — replace AMOT actuator option `27` with option `71` (electric solenoid, 12 VDC) and feed it from a speed switch driven by the alternator W terminal or a magnetic crank pickup. Auto-closes on overspeed condition.
2. **Add overspeed sensing** — AMOT 8210K electronic speed switch + magnetic pickup wired to drive the solenoid above. Provides automatic protection independent of driver action.

Both upgrades preserve the manual cable as the always-available backup.

## Outstanding Items

- [ ] Verify R2.8 turbo inlet tube outside diameter (2.5" suspected; 2.8" AMOT body is closest available)
- [ ] Source NPT-to-hose adapter fittings sized to match turbo inlet
- [ ] Select dash T-handle mounting location (within reach belted, away from accidental contact)
- [ ] Assign firewall grommet for AMOT cable pass-through (dedicated grommet required)
- [ ] Determine catch can mounting bracket attachment point on engine bracketry

## Related Documentation

- [Keyless Ignition][keyless] - Why ECM-only kill is insufficient; this doc supersedes the prior "no protection" note
- [Engine Systems Checklist][checklist] - Phase 11 install steps
- [TBD Tracker][tbd] - Open items for parts selection
- [Purchase Tracker][purchase] - BOM line items

[keyless]: ../05-control-interfaces/06-keyless-ignition.md
[checklist]: ../09-installation/02-engine-systems-checklist.md
[tbd]: ../09-installation/00-tbd-tracker.md
[purchase]: ../09-installation/03-purchase-tracker.md
