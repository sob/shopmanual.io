---
hide:
  - toc
tags:
  - wire-routing
  - harness
---

# 1.7.3 Harness Inventory {#harness-inventory}

## Purpose

Catalogs each fabricatable wire harness in the build. A "harness" here = a discrete bundle of wires with a defined start connector, end connector(s), routing path, and BOM — something you'd lay out on a workbench and tape together as a unit.

This page is the **index and system-wide view**. The detailed, build-it-from-this specs (conductor tables, gauges, colors, lengths, protection, connectors) live on the three **build sheets** below — each pairs the harnesses with the [LJ Tub Map][lj-tub-map] diagram that shows their physical routing.

**Use these docs to:**

- Order connectors and lugs in correct quantities
- Plan fabrication order (build harnesses bench-side, install in vehicle)
- Identify reuse / consolidation opportunities
- Define service-replaceable units (one harness fails → replace just that segment)

**Bundling philosophy:** Each harness terminates at a connector at every transition point (firewall, body penetration, distribution box). This makes harnesses individually serviceable and lets you lay them out flat for fabrication. The cost is more connectors; the benefit is much easier R&R.

**Numbering note:** Two prior bundles (the old H1+H4 power trunk and the old H6+H7 rear cabin bundle) were merged in May 2026. The catalog was renumbered to a single sequence H1–H9 — there are no compound names (no "H1/4", no "H6/7"). See the [interference assessment](#bundle-interference-assessment) for why the merged bundles are safe.

---

## Harness Build Sheets

Each build sheet embeds the matching tub-map diagram and the workbench specs for the harnesses it shows.

| Build sheet | Tub-map page | Harnesses |
|:------------|:-------------|:----------|
| [Power Distribution][power-build] | Power Distribution | **H1** Passenger Rear Power Trunk · **H2** START Engine Bay Trunk · **H3** BCDC Cross-Cab |
| [Lighting & SwitchPros][lighting-build] | Lighting & SwitchPros | **H4** SwitchPros Front Bundle · **H5** Rear Cabin Trunk Bundle |
| [Controls, Recovery & Drivetrain][controls-build] | Controls, Recovery & Drivetrain | **H6** ARB Compressor · **H7** Winch Trigger · **H8** Kilduff Shifter · **H9** TCU to Engine Bay |

## Harness Summary

| # | Harness | Build sheet | Conductors | Largest gauge | Length |
|:--|:--------|:------------|:----------:|:-------------:|:-------|
| H1 | Passenger Rear Power Trunk (AUX fwd + winch) | [Power][power-build] | 3 | 2/0 AWG | ~13 ft (+13 ft winch to bumper) |
| H2 | START Engine Bay Trunk (alt + starter + PMU feed + START+ fwd-bus feed) | [Power][power-build] | 4 | 2/0 AWG | 6–8 ft |
| H3 | BCDC Cross-Cab | [Power][power-build] | 2 | 1/0 AWG | ~5–6 ft |
| H4 | SwitchPros Front Bundle | [Lighting][lighting-build] | 3 outputs | 14 AWG | 4–8 ft |
| H5 | Rear Cabin Trunk Bundle (SP rear + PMU rear) | [Lighting][lighting-build] | ~10 | 14 AWG | 8–14 ft |
| H6 | ARB Compressor | [Controls][controls-build] | 4 | 6 AWG | ~10 ft |
| H7 | Winch Trigger | [Controls][controls-build] | 5 | 18 AWG | ~3 ft + ~13 ft |
| H8 | Kilduff Shifter → TCU | [Controls][controls-build] | 1 (multi) | Proprietary | ~3–5 ft |
| H9 | TCU → Engine Bay | [Controls][controls-build] | 6 | 14 AWG | 3–4 ft |

!!! note "Engine-bay distribution nodes (not cabin harnesses)"
    Two busbars fan power out to local loads and so are **not** catalogued as fabricatable cabin harnesses — like the Firewall CONSTANT bus, they are distribution points, and their short local feeds are built in place:

    - **START+ Forward Distribution Bus** (Blue Sea 2105 MaxiBus, engine bay) — fed by H2's 2 AWG forward-bus master feed; fans out on short engine-bay local feeds to the radiator fan (4 AWG), iBooster main (8 AWG), and TCU (12 AWG). The TCU's leg is carried by [H9][controls-build]; the fan and iBooster legs are short engine-bay runs. See [START+ Forward Distribution Bus][start-fwd-bus].
    - **Firewall CONSTANT bus** (cabin side) — fed by H1's 2/0 AWG forward feed; fans out to SwitchPros, BODY PDU, and Fusion. See [AUX Battery Distribution][aux-battery].

## Wire Color Convention {#wire-color-convention}

Colors on the build sheets follow this convention. Power and ground colors are universal automotive practice; signal colors are the builder's choice — pick a consistent scheme and keep it the same across every harness.

| Wire role | Color | Notes |
|:----------|:------|:------|
| Power / positive feed (+) | **Red** | All constant/switched +12V distribution, feeds, and high-current power |
| Ground / negative (−) | **Black** | All returns and battery negatives |
| CAN bus | **Twisted pair** | Keep the pair twisted; do not split. Color per controller (e.g., J1939) |
| Vendor-supplied harness | **Per vendor pigtail** | SwitchPros (Delphi), ARB, CH4X4, Kilduff/ZF ship their own colors — match the supplied pigtail |
| Signal / trigger / output (non-vendor) | **Builder's choice** | Choose a consistent scheme and record it |

For protective wrap/loom, heat sleeve, abrasion sleeve, and P-clamp standards by location, see [Wire Protection Standards][wire-routing]. This build wraps power runs in braided sleeve with per-harness tracers — see [Protective Sleeve & Tracers](#sleeve-convention).

## Protective Sleeve & Tracers {#sleeve-convention}

Wrap preference for this build:

- **Default is black braided expandable sleeve** (PET, e.g. Techflex Flexo PET) over the full length of power runs, sized to the bundle OD. Black is the base color; a contrasting **tracer stripe** woven into the sleeve identifies each power trunk where several run together (e.g. in the cabin trunk). Braided sleeve is abrasion-resistant, flexes around the sill / trans-tunnel path, and lets you fan branches out without cutting the wrap.

| Harness | Sleeve | Carries |
|:--------|:-------|:--------|
| **H1** Passenger Rear Power Trunk | Black braided, red tracer | AUX forward feed + winch power/ground |
| **H2** START Engine Bay Trunk | Black braided, yellow tracer | Alternator, starter, PMU feed, START+ forward-bus feed |
| **H3** BCDC Cross-Cab | Black braided, green tracer | BCDC input + cross-ground reference |
| **H6** ARB Compressor (motor pair) | Black braided, blue tracer | 2× 6 AWG compressor motor cables |

- **Heat sleeve still applies** where any run enters the engine bay within ~12" of exhaust — over the braided sleeve as needed.
- **Split loom** remains fine for the small-wire signal/lighting bundles (H4, H5, H7, H9) and for short, branchy, or frequently-accessed runs where braided sleeve is awkward; use a braided sleeve with a tracer instead if you prefer to color-code those too. H8 ships as a factory harness (no added wrap needed beyond loom through the tunnel).

---

## Harness Map

```text
                  ┌──────────────────────────────────────────────────┐
                  │                  ENGINE BAY                       │
                  │                                                   │
  H2 START trunk ─►──┐                                                │
                     │ alt, starter, PMU feed, START+ fwd-bus feed    │
                     │                                                │
                     ▼                                                │
                  ┌─────┐                                             │
                  │ PMU │◄────── H4 SP front ◄──┐                     │
                  └──┬──┘                       │                     │
                     │                          │                     │
  ═════════════════════════════════ FIREWALL ═════════════════════════│
                     │                          │                     │
                     ▼ HDP24                    │                     │
                  ┌──────────────────────────────────┐                │
                  │  FIREWALL CLUSTER (cabin side):  │                │
                  │  SwitchPros + GND bus + BODY PDU │                │
                  │  + Firewall CONSTANT bus + CBs   │                │
                  │  (audio amp on direct AUX feed)  │                │
                  └────┬──────────────┬──────────────┘                │
                       │              │                               │
                       │      H5 Rear Cabin Trunk Bundle              │
                       │      (SwitchPros rear + PMU rear, ~10 cond)  │
                       │              │                               │
                       ▼              ▼                               │
                  ┌─────────────────────────────────────────┐         │
                  │  CABIN TRUNK                            │         │
                  │  Forward (passenger side): H1           │         │
                  │  Forward (driver side): H2              │         │
                  │  Rearward: H5 + CT4 turn + H6 signal    │         │
                  │  Cross-cab: H3 (under rear bench)       │         │
                  └────┬──────────────────────────┬─────────┘         │
                       │                          │                   │
                       ▼                          ▼                   │
       ┌─────────────────────┐         ┌────────────────────┐         │
       │ DRIVER REAR WELL    │         │ PASSENGER REAR WELL│         │
       │ • START battery     │◄────────│ • AUX battery      │         │
       │ • 250A + 80A CBs    │  H3     │ • 300A + 150A CBs  │         │
       │                     │ BCDC    │ • SafetyHub        │         │
       │                     │ cross   │ • BCDC             │         │
       │  H2 ↑ (4 cables)    │ (under  │  H1 ↑ (3 cables)   │         │
       │  driver floor/wall  │  rear   │  passenger         │         │
       │  to engine bay      │  bench) │  floor/wall to     │         │
       │                     │         │  3× bulkhead studs │         │
       └─────────────────────┘         │  at firewall;      │         │
                                       │  winch portion     │         │
                                       │  continues to      │         │
                                       │  front bumper      │         │
                                       │  H6 ARB compressor │         │
                                       │  → under pass seat │         │
                                       └──────┬─────────────┘         │
                                              │                       │
                                              ▼                       │
       ┌─────────────────────────────────────────────────────────────┐
       │  FRONT BUMPER (H1 winch portion terminates)                 │
       │  REAR CARGO BULKHEAD (H5 multi-pin breakout)                │
       └─────────────────────────────────────────────────────────────┘
```

---

## Bundle Interference Assessment {#bundle-interference-assessment}

Two harnesses (H1 and H5) bundle multiple originally-separate runs into a single sleeve. EMI/crosstalk evaluation:

**H1 (Passenger Rear Power Trunk) — 1× 2/0 AWG forward feed + 2× 1/0 AWG winch power/ground:**

- All three conductors carry power only — no sense lines, no signal returns, no CAN/audio/analog.
- Inductive coupling between adjacent power conductors is irrelevant for distribution (the coupled noise has no signal path to corrupt; loads see CB-protected DC).
- Winch peak current (~400A, seconds) raises a strong transient B-field but does not couple to the parallel forward-feed cable in any way that matters at the firewall CONSTANT bus.
- **Verdict: no interference risk. Safe to bundle.**

**H5 (Rear Cabin Trunk Bundle) — SP lighting outputs + PMU OUT-21/22/23 + 1 SP trigger return:**

- SP OUT-6/7/10/12/13 are switched DC for lighting loads (14 AWG), not PWM.
- PMU OUT-21/22/23 are switched DC for brake / reverse / parking tail signals (16 AWG), not PWM in this build (no dimming required; tail circuits run at full output when commanded).
- TRIGGER-2 (18 AWG) is a switch return from the rear cargo rocker. SP triggers require sustained 12V to register; brief inductive transients from adjacent switched outputs are filtered by the SP input.
- No CAN bus, no audio signal, no analog sensor wiring shares this bundle. (CT4 rear turn signals were considered for inclusion — they would also be switched DC and remain safe to add later.)
- **Verdict: no interference risk under current load profile. Safe to bundle.** If a future change introduces PWM dimming on any PMU rear output, re-evaluate — twisted pair or shielding may be warranted for the TRIGGER-2 line in that case.

**Other bundles (H2, H3, H4, H6, H7, H8, H9):** Each is single-purpose with homogeneous content (H2 = power only; H3 = power + ground reference; H4 = SP outputs; H6 = ARB power + signal already noted as physically separable; H7 = trigger logic only; H8 = factory shifter harness; H9 = TCU connections, includes twisted CAN pair). No new bundling concerns.

---

## Cabin Trunk Bundle Summary

The **cabin trunk** (trans tunnel / sill, firewall ↔ rear wheel wells) carries multiple harnesses in parallel. Total bundle inventory:

| Direction | Harness | Cable count | Largest gauge | Path side |
|:----------|:--------|:-----------:|:-------------:|:---------:|
| Forward (rear → firewall) | **H1** Passenger Rear Power Trunk (AUX fwd + winch power+gnd) | 3 | 2/0 AWG | Passenger sill/floor |
| Cross-cab | H3 (BCDC inter-battery + cross-gnd) | 2 | 1/0 AWG | Under rear bench |
| Forward (driver rear → engine bay) | H2 (alt, starter, PMU feed, START+ fwd-bus feed) | 4 | 2/0 AWG | Driver sill/floor |
| Rearward (firewall → rear) | **H5** Rear Cabin Trunk Bundle (SP rear outputs + PMU rear lighting) | ~10 | 14 AWG | Trans tunnel |
| Rearward (firewall → rear) | CT4 rear turn signals | 2 | 14 AWG | Trans tunnel (could merge into H5) |
| Rearward (firewall → under pass seat) | SwitchPros control + pressure (ARB) | 2 | 14–18 AWG | Trans tunnel (per H6 optimization) |

**Passenger sill/floor (H1):** ~3 cables, ~1.5" OD bundle, terminates at 3× bulkhead studs at firewall

**Driver sill/floor (H2):** ~4 cables (3× 2/0 AWG + 1× 2 AWG), ~1.6" OD bundle, terminates at heavy power grommet at firewall

**Trans tunnel rearward (H5 + CT4 + ARB signal):** ~14 conductors of small wire (14–18 AWG)

**Suggested trunk wrap:** 1.5"–2" braided expandable sleeve (preferred for the power runs) or split loom per side, tracer-coded per harness so the bundles stay identifiable — see [Protective Sleeve & Tracers](#sleeve-convention). P-clamp every 12–18".

---

## Bundle Optimization Opportunities (Summary)

These were noted inline on the build sheets; consolidated here for review:

1. ~~Old H4 + old H1 share rear-well → firewall path~~ **Resolved (2026-05-30):** Merged into single **H1 Passenger Rear Power Trunk**. Firewall transition uses a **single sealed 2-piece rubber grommet** (e.g., Steele Rubber) — cables run continuously, no service break. Bulkhead studs (Blue Sea 2203/2204) max at 250A and were underrated for the winch peaks (400A); Anderson SB175 was also undersized. Continuous-cable + grommet is WARN's documented standard for high-current firewall pass-through.
2. ~~Old H6 + old H7 + CT4 rear turn + old H8 SP signal wires share cabin trunk → rear~~ **Partially resolved (2026-05-30):** Old H6 + old H7 merged into **H5 Rear Cabin Trunk Bundle** with single multi-pin breakout (Deutsch DT15 or AMP CPC ~15-pin) at rear cargo bulkhead. CT4 rear turn signals and ARB control wires *could* still join — pending decision.
3. **H5 sub-harness (firewall → rear breakout) is a single straight pull;** R&R of any individual rear light becomes a pigtail swap.
4. **H6 motor cables only.** Move control/pressure wires into H5 since they originate at SwitchPros.
5. **Front lockers + rock lights + fog in one bundle** through SwitchPros firewall bulkhead to engine bay → grille area. Splice/breakout at front for fan-out.
6. ~~HDP20 firewall connector pin budget~~ **Resolved (2026-05-30):** Split into two dedicated bulkheads — HDP24-24-29 for non-SP traffic (18/29 used, 11 spare) + HDP24-18-14 for SwitchPros forward outputs (6/14 used, 8 spare). SP harness stays Delphi-native end-to-end. See [Pin Budget Audit][firewall-ingress].

---

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Decide front bumper breakout connector style (Deutsch DT, AMP CPC, etc.)
- [ ] Decide rear cargo bulkhead breakout connector style and pin count
- [ ] Confirm SwitchPros front locker wire routing (front axle access)
- [ ] Decide if ARB control wires merge into H5 (recommended) or run as H6 signal pair
- [ ] Source connector + lug + heat shrink BOM totals
- [ ] Confirm braided-sleeve sizes and per-harness tracer colors for the power runs (see [Protective Sleeve & Tracers](#sleeve-convention)); decide split loom vs braided for the small-wire bundles per zone
- [ ] Define and record the signal-wire color scheme for non-vendor signal/trigger wires (power = red, ground = black are fixed; see [Wire Color Convention](#wire-color-convention))

## Related Documentation

- [Power Distribution Build Sheet][power-build] - H1, H2, H3 with tub-map diagram
- [Lighting & SwitchPros Build Sheet][lighting-build] - H4, H5 with tub-map diagram
- [Controls, Recovery & Drivetrain Build Sheet][controls-build] - H6–H9 with tub-map diagram
- [Wire Routing][wire-routing] - Zone-based routing reference and protection standards
- [Firewall Ingress][firewall-ingress] - HDP24 pinout and penetrations
- [AUX Battery Distribution][aux-battery] - H1 source
- [START Battery Distribution][start-battery] - H2 and H3 source
- [SwitchPros SP-1200][switchpros] - H4, H5 source controller
- [PMU24 Outputs][pmu-outputs] - H5 source
- [SafetyHub 150][safetyhub] - H6, H7 source
- [Recovery Systems / Winch][recovery] - H1 (winch portion) destination
- [Air Compressor][air-compressor] - H6 destination

[power-build]: 04-harness-power-distribution.md
[lighting-build]: 05-harness-lighting-switchpros.md
[controls-build]: 06-harness-controls-recovery-drivetrain.md
[lj-tub-map]: 04-harness-power-distribution.md
[wire-routing]: index.md
[firewall-ingress]: 02-firewall-ingress.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[start-battery]: ../02-starter-battery-distribution/index.md
[start-fwd-bus]: ../02-starter-battery-distribution/index.md#start-forward-bus
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[safetyhub]: ../03-aux-battery-distribution/04-safetyhub.md
[recovery]: ../../08-exterior-systems/01-winch.md
[air-compressor]: ../../08-exterior-systems/02-air-compressor.md
