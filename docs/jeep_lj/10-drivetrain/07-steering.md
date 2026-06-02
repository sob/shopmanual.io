---
tags:
  - product-details
  - drivetrain
  - steering
---

# 10.7 - Steering {#steering}

/// html | div.product-info

**Type:** Full hydraulic steering

**Manufacturer:** PSC Motorsports

///

Full hydraulic steering with no mechanical linkage: a PSC pump feeds a PSC orbital steering control valve, which drives a double-ended ram. Ram stroke is limited to Dana 44 spec by Busted Knuckle Off-Road steering stops, and the ram mounts via an Artec Industries Dana 60 ram mount cut down to fit the Dana 44. A Mishimoto fluid cooler with fan (gated by a 180 °F inline thermostat) cools the circuit.[^steering-config]

Component part numbers below come from the PSC **FHK400TJ** kit — the 1997-2006 TJ/LJ Extreme Series full hydraulic kit with a 2.75" double-ended cylinder (PSC's 40"+ tire kit).[^psc-kit] The orbital valve and cylinder carry over directly; the kit **pump is the exception** — its PK40JP2-FH bracket is Jeep 4.0L-specific and does not fit this build's Cummins R2.8.

## Specifications

| Component | Specification |
| :-------- | :------------ |
| Type | Full hydraulic (no mechanical linkage) |
| Kit | PSC FHK400TJ (TJ/LJ Extreme Series, 2.75" double-ended) |
| Steering Control Valve | PSC 160cc orbital (in FHA160-S accessory kit) |
| Ram | PSC SC2227K1 (2.75" × 8.0" double-ended) |
| Pump | Cummins-specific PSC pump TBD (kit PK40JP2-FH is 4.0L-only) |
| Reservoir | Remote (included with pump kit) — model TBD |
| Cooler | Mishimoto fluid cooler + fan (180 °F inline thermostat) |
| Fluid | PSC 715 (SWEPCO 715) |

## System Components

### Hydraulic Pump

> **Pump is engine-specific — the kit pump does not fit.** The FHK400TJ kit ships a **PK40JP2-FH** pump kit built for the Jeep **4.0L** accessory drive. This build runs a **Cummins R2.8**, so the kit pump/bracket does not bolt up — a Cummins-compatible PSC pump must be sourced. The kit's orbital valve and cylinder are engine-agnostic and carry over unchanged.

| Specification | Value |
| :------------ | :---- |
| Manufacturer | PSC Motorsports |
| Model | TBD — Cummins R2.8 pump + bracket (NOT the kit's PK40JP2-FH) |
| Flow Rate | TBD |
| Pressure | TBD |
| Drive | TBD (belt vs. Cummins gear-drive) |

### Steering Control Valve

| Specification | Value |
| :------------ | :---- |
| Type | Orbital (PSC) |
| Model | 160cc — supplied in PSC FHA160-S accessory kit |

### Steering Ram

| Specification | Value |
| :------------ | :---- |
| Type | Double-ended (PSC) |
| Model | SC2227K1 |
| Bore | 2.75" |
| Stroke | 8.0" native; effective stroke limited to Dana 44 spec via Busted Knuckle Off-Road steering stops |
| Mount | Artec Industries Dana 60 ram mount, cut down to fit the Dana 44 |

### Reservoir

| Specification | Value |
| :------------ | :---- |
| Type | Remote (included with PSC pump kit) |
| Capacity | TBD |
| Location | TBD |

### Cooler

| Specification | Value |
| :------------ | :---- |
| Unit | Mishimoto fluid cooler |
| Fan | Mishimoto (matched to cooler) |
| Control | 180 °F inline thermostat |
| Fan Current Draw | TBD (confirm fits PMU Out 8 ~15A budget) |
| Fan Power Source | PMU Out 8 (~15A, thermostat-switched) — see [PMU Outputs][pmu-outputs] |

## Fluid Specifications

| Specification | Value |
| :------------ | :---- |
| Fluid Type | PSC 715 (SWEPCO 715) |
| Capacity | TBD (kit ships ~4 qt; confirm system fill) |

## Outstanding Items

- [ ] Source a Cummins R2.8-compatible PSC pump + bracket (kit PK40JP2-FH is 4.0L-only)
- [ ] Confirm pump drive type (belt vs Cummins gear-drive), flow rate, and pressure
- [ ] Confirm the Dana 44 stroke length set by the Busted Knuckle stops
- [ ] Document Artec Industries ram mount part number and the Dana 44 cut dimensions
- [ ] Confirm remote reservoir model and mounting location
- [ ] Confirm fluid system fill quantity
- [ ] Confirm Mishimoto cooler fan current draw fits the PMU Out 8 (~15A) budget
- [ ] Document hydraulic line routing

[^steering-config]: Owner decision, 2026-05-30 — full-hydro kit is PSC pump + PSC orbital valve + PSC double-ended ram; Busted Knuckle Off-Road steering stops limit ram stroke to Dana 44 spec; Artec Industries Dana 60 ram mount cut down to the Dana 44; Mishimoto fluid cooler + fan on a 180 °F inline thermostat. Model numbers, bore/stroke values, flow/pressure, and fluid specs remain pending.

[^psc-kit]: PSC Motorsports **FHK400TJ** — 1997-2006 Jeep TJ/LJ Extreme Series full hydraulic kit, 2.75" double-ended cylinder (PSC Motorsports / pscsteering.com, accessed 2026-05-31). Kit boxes: **FHA160-S** (160cc full-hydraulic accessory kit w/ orbital valve), **PK40JP2-FH** (high-flow pump kit — **Jeep 4.0L bracket**, not used here), **SC2227K1** (2.75" × 8.0" double-ended cylinder); fluid PSC/SWEPCO 715. Smaller-tire variant is **FHK100TJ** (2.5" bore / 125cc valve, 35-42"). Pump bracket is 4.0L-specific, so it does not fit this build's Cummins R2.8 — valve and cylinder carry over.

## Related Documentation

- [Front Axle][front-axle]
- [Suspension][suspension]

[front-axle]: 04-front-axle.md
[suspension]: 06-suspension.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
