---
hide:
  - toc
---

# 1.7.3 Harness Inventory {#harness-inventory}

## Purpose

Catalogs each fabricatable wire harness in the build. A "harness" here = a discrete bundle of wires with a defined start connector, end connector(s), routing path, and BOM — something you'd lay out on a workbench and tape together as a unit.

**Use this doc to:**

- Order connectors and lugs in correct quantities
- Plan fabrication order (build harnesses bench-side, install in vehicle)
- Identify reuse / consolidation opportunities
- Define service-replaceable units (one harness fails → replace just that segment)

**Bundling philosophy:** Each harness terminates at a connector at every transition point (firewall, body penetration, distribution box). This makes harnesses individually serviceable and lets you lay them out flat for fabrication. The cost is more connectors; the benefit is much easier R&R.

---

## Harness Map

```text
                  ┌──────────────────────────────────────────────────┐
                  │                  ENGINE BAY                       │
                  │                                                   │
  H2 START trunk ─►──┐                                                │
                     │ alt, starter, PMU feed, BCDC input             │
                     │                                                │
                     ▼                                                │
                  ┌─────┐                                             │
                  │ PMU │◄────── H5 SP front ◄──┐                     │
                  └──┬──┘                       │                     │
                     │                          │                     │
  ═════════════════════════════════ FIREWALL ═════════════════════════│
                     │                          │                     │
                     ▼ HDP20                    │                     │
                  ┌──────────────────────────────────┐                │
                  │  FIREWALL CLUSTER (cabin side):  │                │
                  │  SwitchPros + GND bus + BODY PDU │                │
                  │  + Firewall CONSTANT bus + CBs   │                │
                  │  (audio amp on direct AUX feed)  │                │
                  └────┬──────────────┬──────────────┘                │
                       │              │                               │
                       │      H6/7 Rear Cabin Trunk Bundle              │
                       │      (SwitchPros rear + PMU rear, ~10 cond)    │
                       │              │                                  │
                       ▼              ▼                                  │
                  ┌─────────────────────────────────────────┐         │
                  │  CABIN TRUNK                            │         │
                  │  Forward (passenger side): H1/4         │         │
                  │  Forward (driver side): H2              │         │
                  │  Rearward: H6/7 + CT4 turn + H8 signal  │         │
                  │  Cross-cab: H3 (under rear bench)       │         │
                  └────┬──────────────────────────┬─────────┘         │
                       │                          │                   │
                       ▼                          ▼                   │
       ┌─────────────────────┐         ┌────────────────────┐         │
       │ DRIVER REAR WELL    │         │ PASSENGER REAR WELL │         │
       │ • START battery     │◄────────│ • AUX battery       │         │
       │ • 250A + 80A CBs    │  H3     │ • 300A + 150A CBs   │         │
       │                     │ BCDC    │ • SafetyHub         │         │
       │                     │ cross   │ • BCDC              │         │
       │  H2 ↑ (3× 2/0 AWG)  │ (under  │  H1/4 ↑ (3 cables)  │         │
       │  driver floor/wall  │  rear   │  passenger          │         │
       │  to engine bay      │  bench) │  floor/wall to      │         │
       │                     │         │  3× bulkhead studs  │         │
       └─────────────────────┘         │  at firewall;       │         │
                                       │  winch portion      │         │
                                       │  continues to       │         │
                                       │  front bumper       │         │
                                       │  H8 ARB compressor  │         │
                                       │  → under pass seat  │         │
                                       └──────┬──────────────┘         │
                                              │                       │
                                              ▼                       │
       ┌─────────────────────────────────────────────────────────────┐
       │  FRONT BUMPER (H1/4 winch portion terminates)               │
       │  REAR CARGO BULKHEAD (H6/7 multi-pin breakout)              │
       └─────────────────────────────────────────────────────────────┘
```

---

## Harness Catalog

### H1/4 — Passenger Rear Power Trunk (AUX Forward Feed + Winch)

*Formerly two harnesses (H1 + H4) — merged 2026-05-30 since they share the entire passenger-side path. Fabricated and installed as a single bundled assembly.*

**Route:** Passenger rear wheel well (AUX battery) → up inside passenger rear quarter sill → forward along **inside floor board / side wall** (passenger side) → A-pillar area → **3× bulkhead studs through firewall** → engine bay → forward along passenger inner fender → through grille area → front bumper (winch portion only)

**Length:** ~13 ft to firewall (all 3 cables); ~13 ft additional for winch cables continuing to bumper

**Contains:**

| Wire | Gauge | Function | Termination at battery | Termination at firewall | Continues to |
|:-----|:-----:|:---------|:----------------------|:------------------------|:-------------|
| Forward feed (+) | 2/0 AWG | Powers SwitchPros + BODY PDU + Fusion via Firewall CONSTANT bus | Ring lug to 300A CB output stud | Ring lug to bulkhead stud | (terminates at firewall — bus input stud on engine bay side via short jumper) |
| Winch power (+) | 1/0 AWG | AUX battery+ → winch contactor B+ | Ring lug to AUX battery+ stud | Ring lug to bulkhead stud | Lug to winch contactor B+ |
| Winch ground (−) | 1/0 AWG | AUX battery- → winch contactor B− | Ring lug to AUX battery- stud | Ring lug to bulkhead stud | Lug to winch motor / chassis at front |

**Firewall pass-through:** **Single sealed 2-piece rubber grommet** sized for the ~1.5" OD bundle (~1.75" firewall hole). Cables run continuously from rear wheel well to their respective destinations — no service break at the firewall. The grommet seals the firewall penetration only; the cables themselves are uninterrupted.

**Why continuous cables + grommet (not inline connectors or bulkhead studs):**

- WARN install documentation references this approach as standard for winch firewall pass-through
- No amperage limit at the pass-through (the cable is the conductor; grommet just seals the hole)
- Common feed-through marine bulkhead studs (Blue Sea 2203/2204, Cole Hersee 46211) max at 250A continuous — borderline for H1 (232A) and underrated for H4 winch peaks (400A)
- Anderson SB175 is undersized for the winch leg (175A continuous); SBE320/SB350 would work but adds complexity
- Service is rare in practice — when needed, pulling the entire cable end-to-end is acceptable
- Steele Rubber or similar 2-piece grommet, ~$5–15

**Protection:** Split loom + wrapped harness sleeve along entire cabin path. Heat sleeve where the winch cables enter engine bay. P-clamps every 12–18".

**Notes:**

- 3-cable bundle: ~1.5" OD final wrapped harness
- Path is fully inside the body until firewall transition (no exposed frame rail)
- Cables terminate as ring lugs at destinations (lug-to-stud at battery / CB / bus / contactor on each end). If a service break is ever desired, do it as a lug-to-lug junction inside the rear wheel well, not at the firewall.

---

### H2 — START Engine Bay Trunk

**Route:** Driver rear wheel well (START battery) → up inside driver rear quarter sill → forward along **inside floor board / side wall** (driver side) → A-pillar area → driver firewall penetration → engine bay

**Length:** 6–8 ft per cable

**Contains:**

| Wire | Gauge | Function | Termination at battery | Termination at engine bay |
|:-----|:-----:|:---------|:----------------------|:--------------------------|
| Alternator charging input | 2/0 AWG | Alternator → START battery+ | Lug to battery+ stud | Lug to alternator output stud |
| Starter motor power | 2/0 AWG | START battery+ → starter | Lug to battery+ stud | Lug to starter B+ stud |
| PMU24 main feed | 2/0 AWG | START battery+ → 250A CB → PMU24 | Lug to 250A CB output | Lug to PMU power stud |

(BCDC input feed (4 AWG via 80A CB) takes the H3 cross-cab path instead — see H3.)

**Connectors:** Lug terminations at both ends. Heat sleeve required where bundle enters engine bay (>12" from exhaust). Bundle 3 cables with looms; expect ~1.5" OD final bundle.

**Protection:** Split loom + wrapped harness sleeve in cabin / sill. Heat sleeve in engine bay. P-clamps every 12–18".

**Firewall penetration:** Driver-side grommet for high-current cables — separate from the HDP24 (HDP24 is passenger-side, signal-only). Three 2/0 AWG cables need a grommet sized for ~1.5" bundle OD.

**Notes:**

- All 3 high-current cables share the same driver-side floor / side wall path
- Path is fully inside the body (no exposed frame rail)
- Driver-side firewall grommet is a new firewall penetration — separate from existing passenger-side HDP24 and SwitchPros bulkheads

---

### H3 — BCDC Cross-Cab

**Route:** Driver rear wheel well (START battery) → **under the rear bench seat cushion** → passenger rear wheel well (BCDC + AUX battery)

**Length:** ~5–6 ft (straight cross-cab run under bench)

**Contains:**

| Wire | Gauge | Function | Termination at driver well | Termination at passenger well |
|:-----|:-----:|:---------|:--------------------------|:------------------------------|
| BCDC input | 4 AWG | START battery+ via 80A CB → BCDC input terminal | Lug to 80A CB output | Lug to BCDC input red terminal (M8) |
| Cross-ground reference | 1/0 AWG | START battery- → AUX battery- (critical for BCDC operation) | Lug to START battery- | Lug to AUX battery- |

**Connectors:** Lug terminations both ends. No inline connectors needed for short run.

**Protection:** Split loom along the run. Bench cushion provides physical shielding from above; floor pan shields from below. P-clamps to body cross-member at 1–2 points.

**Notes:**

- Under-bench routing is short, dry, accessible, and physically protected (bench cushion above, floor pan below)
- No frame rail exposure; no need to share the longer floor / side wall paths used by H1/H2/H4
- BCDC sensor cable (~6 ft, 2-pin) is included with BCDC unit, runs to AUX battery+ terminal at the same wheel well — short, stays passenger-side, not part of this harness
- Path is independent of cabin trunk runs (H1/H4 passenger side, H2 driver side), so no cabin trunk congestion impact

---

### H4 — Winch Feed *(merged into H1/4 — see above)*

**Status:** Merged into **H1/4 Passenger Rear Power Trunk** on 2026-05-30. The two harnesses share the entire passenger-side path from AUX battery to firewall, so they are now fabricated as a single 3-cable bundle. The 2× 1/0 AWG winch cables continue past the firewall to the front bumper. See [H1/4 above](#h14--passenger-rear-power-trunk-aux-forward-feed--winch).

---

### H5 — SwitchPros Front Bundle

**Route:** SwitchPros (firewall, cabin side) → **dedicated SwitchPros HDP24-18-14 firewall bulkhead** → engine bay → grille / front bumper / front axle

**Length:** 4–8 ft (depending on destination)

**Contains:**

| SwitchPros output | Gauge | Function | Destination | SP bulkhead pins |
|:-----------------:|:-----:|:---------|:------------|:----------------:|
| OUT-3 (35A circuit) | 14 AWG | Fog light | Front bumper (BD S8 amber) | 1 (+) / 2 (−) |
| OUT-6 (front rocks subset, 15A circuit, shared with rear) | 14 AWG | Front bumper rock light + 2x front wheel well rock lights | Splice at front for 3 lights | 3 (+) / 4 (−) |
| OUT-17 (low-side 2A) | 18 AWG | Front ARB locker solenoid | Front axle (~12 ft from SP) | 5 (+) / 6 (−) |

**Connectors:** Custom 2-pin Delphi at SwitchPros output side (per SP harness convention); harness terminates at HDP24-18-14 cabin-side plug at firewall. Engine-bay side picks up at HDP24-18-14 receptacle and re-terminates as 2-pin Delphi at each light/solenoid.

**Ground strategy:** Each output's load ground returns through the SP bulkhead (pins 2, 4, 6) to the SwitchPros Ground Bus on cabin side. Clean SP-native architecture; no reliance on chassis ground at forward loads.

**Notes:**

- 3 forward-going SwitchPros circuits in this bundle, 6 pins through dedicated SP bulkhead (HDP24-18-14)
- Front locker wire (18 AWG) is the longest run — passes through front fender well and along front axle
- Front rock lights (4 in front wheel wells + 1 front bumper) all share OUT-6 with rear rocks
- Could be split into "front bumper sub-harness" (fog + front rock + front bumper) and "front axle sub-harness" (front locker) if those routings diverge
- **8 spare pins** on SP bulkhead accommodate future ditch/roof additions if A-pillar routing becomes impractical

See [SwitchPros Firewall Bulkhead][firewall-ingress] for connector spec and pinout.

---

### H6/7 — Rear Cabin Trunk Bundle (SwitchPros Rear + PMU Rear)

*Formerly two harnesses (H6 + H7) — merged 2026-05-30 since they share the firewall-to-rear cabin trunk path. Fabricated as a single multi-conductor bundle with a rear cargo bulkhead breakout connector.*

**Route:** SwitchPros (firewall, cabin side) + PMU24 outputs (via HDP24 pins 4/5/6 from engine bay) → converge at firewall → cabin trunk (trans tunnel) → rear cargo bulkhead breakout → fans out to rear destinations

**Length:** 8–14 ft (depending on destination; PMU portion is ~11–16 ft total including engine bay leg)

**Contains:**

| Source | Output / Function | Gauge | Destination |
|:-------|:------------------|:-----:|:------------|
| **SwitchPros** OUT-6 (shared with front) | Rear rocks (rear bumper + 2× rear wheel well) | 14 AWG | Splice at rear for 3 lights |
| **SwitchPros** OUT-7 | Chase light (BD RTL-S 30") | 14 AWG | Rear bumper |
| **SwitchPros** OUT-10 | Rear ARB locker solenoid | 14 AWG | Rear axle |
| **SwitchPros** OUT-12 | Rear work lights (2× BD S1) | 14 AWG | Above license plate |
| **SwitchPros** OUT-13 | Cargo lights (2× flush in rear wheel wells) | 14 AWG | Triggered by rear cargo rocker |
| **SwitchPros** TRIGGER-2 | Cargo rocker switch return | 18 AWG | Rear cargo rocker (rear wheel well top) |
| **PMU** OUT-21 | Brake signal | 16 AWG | Tail clusters (L+R) + 3rd brake |
| **PMU** OUT-22 | Reverse signal | 16 AWG | Tail clusters (L+R) |
| **PMU** OUT-23 | Running/parking signal | 16 AWG | Tail clusters (L+R) + license plate |
| **PMU** ground return | Common tail cluster ground | 16 AWG | SwitchPros GND bus at firewall |

**Connectors:**

- **Firewall (cabin side):** SwitchPros outputs originate as Delphi 2-pin pigtails at SP module; PMU outputs enter the cabin via HDP24 pins 4/5/6. Both join the trunk wrap aft of firewall.
- **Rear cargo bulkhead breakout:** Single multi-pin connector — **Deutsch DT15-XX (15-pin)** or **AMP CPC ~15-pin**. All ~10 conductors mate at this single service point.
- **Rear-side pigtails:** Short individual harnesses from breakout to each destination (chase, work, cargo, rocks, locker, tail clusters).

**Protection:** Split loom + wrapped harness sleeve through cabin trunk. P-clamps every 12–18".

**Notes:**

- ~10 conductors in the cabin trunk bundle (mostly 14 AWG + a few 16/18 AWG)
- **Service model:** R&R any rear light by swapping its pigtail at the rear bulkhead breakout. The cabin trunk pull stays in place.
- Splices needed for the tail clusters: each PMU output feeds both driver and passenger sides + 3rd brake/license — can be done at the breakout or with Y-splices closer to lights
- CT4 rear turn signals could also join this bundle through the cabin trunk; tracked separately because they originate at CT4 (steering column) not firewall

---

### H7 — PMU Rear Lighting *(merged into H6/7 — see above)*

**Status:** Merged into **H6/7 Rear Cabin Trunk Bundle** on 2026-05-30. PMU rear outputs share the cabin trunk path with SwitchPros rear outputs after exiting HDP24, so they are now fabricated as a single multi-conductor bundle with shared rear bulkhead breakout. See [H6/7 above](#h67--rear-cabin-trunk-bundle-switchpros-rear--pmu-rear).

---

### H8 — ARB Compressor Bundle

**Route:** SafetyHub (passenger rear wheel well) → under cargo / under rear bench → under passenger seat (compressor mount)

**Length:** ~10 ft

**Contains:**

| Wire | Gauge | Function | Termination at SafetyHub | Termination at compressor |
|:-----|:-----:|:---------|:-------------------------|:--------------------------|
| Motor 1 power | 6 AWG | SafetyHub MIDI-1 (60A) → compressor motor 1 | Lug to MIDI-1 output | Compressor motor terminal |
| Motor 2 power | 6 AWG | SafetyHub MIDI-2 (60A) → compressor motor 2 | Lug to MIDI-2 output | Compressor motor terminal |
| Control signal | 14 AWG | SwitchPros OUT-11 → compressor control terminal | (Comes from SwitchPros at firewall, not SafetyHub — runs separately or joins this bundle along common path) | Compressor control terminal |
| Pressure switch | 18 AWG | ARB pressure switch (on manifold under passenger seat) → SwitchPros TRIGGER-3 | (At firewall, not SafetyHub) | Pressure switch normally-open contact |

**Connectors:** Lug at SafetyHub side, ring/spade at compressor. ARB compressor manifold typically has a pigtail with its own connector.

**Notes:**

- Motor 1 + motor 2 are 6 AWG (high current, brief peaks) — bundle as a pair
- Control + pressure switch wires originate at SwitchPros at firewall, NOT SafetyHub — they run from firewall through cabin to under passenger seat
- Could be merged into H8 if they share routing, or kept separate as "H8b ARB signal"

**Optimization opportunity:** Run the SwitchPros control + pressure switch wires through the cabin trunk to under passenger seat as part of H6 SwitchPros rear bundle (they're SP wires anyway), and split off at the compressor. Saves a separate harness — the only ARB-specific harness is the 2x 6 AWG motor cables from SafetyHub.

---

### H9 — Winch Trigger Control (small wire)

**Route:** BODY PDU (firewall, cabin side) → dash switch ([CH4X4 dual-momentary push][ch4x4-winch]) → HDP24 firewall pins 16/17 → winch contactor at front bumper

**Length:** ~3 ft (BODY PDU → dash) + ~13 ft (dash → contactor via engine bay)

**Contains:**

| Wire | Gauge | Function | Termination |
|:-----|:-----:|:---------|:------------|
| Switch +12V supply | 18 AWG | BODY PDU CB43 (10A) → CH4X4 switch common | Spade at BODY PDU, included pigtail at switch |
| IN trigger | 18 AWG | CH4X4 IN button → HDP24 pin 16 → contactor IN trigger | Included pigtail at switch, HDP24 socket, ring/spade at contactor |
| OUT trigger | 18 AWG | CH4X4 OUT button → HDP24 pin 17 → contactor OUT trigger | Included pigtail at switch, HDP24 socket, ring/spade at contactor |
| Illumination supply | 18 AWG | Dash illumination circuit | Included pigtail at switch |
| Switch ground | 18 AWG | Switch common ground | Chassis ground at dash |

**Connectors:** CH4X4 includes its own connector + cable kit. HDP24-24-29 at firewall penetration. Ring/spade terminals at contactor.

**Notes:**

- BODY PDU CB43 (10A, ~3 ft to dash) replaces the previously-planned SafetyHub ATC-1 (15A, ~13 ft from rear wheel well). The 18 AWG wire is properly sized for the ~3A trigger current; the prior 14 AWG / 15A spec was over-built and routed wastefully.
- Switch is dual-momentary push (not a polarity-reversing rocker) — the WARN ZEON 10-S contactor handles polarity internally
- Warn handheld remote wires in parallel at the contactor trigger terminals
- SafetyHub ATC-1 slot freed for future use (recovery accessories etc.)

[ch4x4-winch]: https://ch4x4.com/product/ch4x4-momentary-dual-push-switch-for-toyota-winch-in-out-symbol/

---

### H10 — Kilduff Shifter to TCU

**Route:** Kilduff shifter in **center console** → straight down through trans tunnel → Turbolamik TCU **mounted on 8HP70 mechatronic** (transmission valve body)

**Length:** ~3–5 ft

**Contains:**

| Wire | Gauge | Function | Termination at shifter | Termination at TCU |
|:-----|:-----:|:---------|:----------------------|:-------------------|
| Shifter harness | Proprietary multi-conductor (factory 8HP70 connector) | All shifter signals (P/R/N/D, manual +/−, button states, illumination) | Kilduff-supplied connector at shifter base | Factory 8HP70 connector at TCU |

**Connectors:**

- Kilduff supplies the shifter end of the harness with their shifter kit
- TCU end uses the factory 8HP70 mechatronic connector (Turbolamik TCU 2.0 mates to this)

**Protection:** Split loom through trans tunnel. The trans tunnel keeps the cable away from cabin contents and provides a clean straight run.

**Notes:**

- TCU is **mounted on the 8HP70 mechatronic** (the trans valve body), not in cabin or engine bay — so this is a very short pull
- No firewall penetration
- No other H-series harnesses share this path — it's a single-purpose, self-contained run
- Kilduff includes the wiring harness with the shifter kit — no separate fabrication required

See [Transmission][transmission] for shifter and TCU specs.

---

### H11 — TCU to Engine Bay

**Route:** Turbolamik TCU on 8HP70 mechatronic → up through trans tunnel forward → engine bay (PMU + J1939 tap + starter P/N relay)

**Length:** 3–4 ft

**Contains:**

| Wire | Gauge | Function | Source | Destination |
|:-----|:-----:|:---------|:-------|:------------|
| TCU power feed | 14 AWG | PMU OUT16 (CONSTANT, 15A) → TCU power input | PMU OUT16 (engine bay) | TCU power terminal |
| J1939 CAN High | Twisted pair | Shared J1939 bus tap (same tap as PMU, Dakota Digital BIM-01-2) | CAN bus tap point | TCU CAN-H |
| J1939 CAN Low | Twisted pair (paired with CAN High) | Shared J1939 bus tap | CAN bus tap point | TCU CAN-L |
| Aux out (Reverse) | 18 AWG | TCU aux output: 12V when shifter in R → PMU In 3 (drives PMU OUT22 reverse lights) | TCU aux Reverse pin | PMU In 3 |
| Aux out (P/N) | 18 AWG | TCU aux output: 12V when shifter in P or N → starter P/N interlock relay coil | TCU aux P/N pin | Starter P/N interlock relay coil+ |
| TCU ground | 14 AWG | TCU ground return | TCU ground terminal | Engine bay ground bus |

**Connectors:**

- TCU end: Turbolamik TCU's connector (depends on TCU model — 2.0 typically uses a small Deutsch DT or similar)
- Engine bay ends: Each wire terminates at its destination (PMU spade/screw terminal, J1939 splice, relay coil terminal, ground bus stud)

**Protection:** Split loom from TCU through trans tunnel up to engine bay. Heat sleeve where it enters engine bay zone (>12" from exhaust).

**Notes:**

- All endpoints are in engine bay — no firewall penetration needed
- J1939 CAN tap is shared with PMU and Dakota Digital BIM-01-2 — the TCU is a third node on the same bus (just adds a splice at the existing tap point)
- The brake switch input to TCU (for unlock-from-Park) is sourced from the cabin brake pedal switch (which already feeds PMU In 2 via HDP24 pin 13) — could share routing or take a separate tap; routing TBD
- TCU is one of three controllers tightly coupled to the engine bay: PMU24 (mounted on firewall), Dakota Digital BIM modules (on HDPE panel cabin side), and TCU (mounted on transmission). All share the J1939 CAN bus.

See [Transmission][transmission] and [PMU Outputs][pmu-outputs] for related details.

[transmission]: ../../10-drivetrain/01-transmission.md

---

## Cabin Trunk Bundle Summary

The **cabin trunk** (trans tunnel / sill, firewall ↔ rear wheel wells) carries multiple harnesses in parallel. Total bundle inventory:

| Direction | Harness | Cable count | Largest gauge | Path side |
|:----------|:--------|:-----------:|:-------------:|:---------:|
| Forward (rear → firewall) | **H1/4** Passenger Rear Power Trunk (AUX fwd + winch power+gnd) | 3 | 2/0 AWG | Passenger sill/floor |
| Cross-cab | H3 (BCDC inter-battery + cross-gnd) | 2 | 1/0 AWG | Under rear bench |
| Forward (driver rear → engine bay) | H2 (alt, starter, PMU feed) | 3 | 2/0 AWG | Driver sill/floor |
| Rearward (firewall → rear) | **H6/7** Rear Cabin Trunk Bundle (SP rear outputs + PMU rear lighting) | ~10 | 14 AWG | Trans tunnel |
| Rearward (firewall → rear) | CT4 rear turn signals | 2 | 14 AWG | Trans tunnel (could merge into H6/7) |
| Rearward (firewall → under pass seat) | SwitchPros control + pressure (ARB) | 2 | 14–18 AWG | Trans tunnel (per H8 optimization) |

**Passenger sill/floor (H1/4):** ~3 cables, ~1.5" OD bundle, terminates at 3× bulkhead studs at firewall

**Driver sill/floor (H2):** ~3 cables, ~1.5" OD bundle, terminates at heavy power grommet at firewall

**Trans tunnel rearward (H6/7 + CT4 + ARB signal):** ~14 conductors of small wire (14–18 AWG)

**Suggested trunk wrap:** 1.5"–2" split loom or wrapped harness sleeve per side. P-clamp every 12–18".

---

## Bundle Optimization Opportunities (Summary)

These were noted inline above; consolidated here for review:

1. ~~H4 + H1 share rear-well → firewall path~~ **Resolved (2026-05-30):** Merged into single **H1/4 Passenger Rear Power Trunk**. Firewall transition uses a **single sealed 2-piece rubber grommet** (e.g., Steele Rubber) — cables run continuously, no service break. Bulkhead studs (Blue Sea 2203/2204) max at 250A and were underrated for the H4 winch peaks (400A); Anderson SB175 was also undersized. Continuous-cable + grommet is WARN's documented standard for high-current firewall pass-through.
2. ~~H6 + H7 + CT4 rear turn + H8 SP signal wires share cabin trunk → rear~~ **Partially resolved (2026-05-30):** H6 + H7 merged into **H6/7 Rear Cabin Trunk Bundle** with single multi-pin breakout (Deutsch DT15 or AMP CPC ~15-pin) at rear cargo bulkhead. CT4 rear turn signals and ARB control wires *could* still join — pending decision.
3. **H6/7 sub-harness (firewall → rear breakout) is a single straight pull;** R&R of any individual rear light becomes a pigtail swap.
4. **H8 motor cables only.** Move control/pressure wires into H6/7 since they originate at SwitchPros.
5. **Front lockers + rock lights + fog in one bundle** through SwitchPros firewall bulkhead to engine bay → grille area. Splice/breakout at front for fan-out.
6. ~~HDP20 firewall connector pin budget~~ **Resolved (2026-05-30):** Split into two dedicated bulkheads — HDP24-24-29 for non-SP traffic (18/29 used, 11 spare) + HDP24-18-14 for SwitchPros forward outputs (6/14 used, 8 spare). SP harness stays Delphi-native end-to-end. See [Pin Budget Audit][firewall-ingress].

---

## Outstanding Items

- [ ] Decide front bumper breakout connector style (Deutsch DT, AMP CPC, etc.)
- [ ] Decide rear cargo bulkhead breakout connector style and pin count
- [x] ~~Calculate HDP20 firewall pin budget — fits or needs upsize?~~ → **Resolved:** Upsized to HDP24-24-29 (29 size-16 contacts, 21 used + 8 future headroom). See [Pin Budget Audit][firewall-ingress] for full pin assignment. Forward-going SP loads use chassis ground locally (1 pin per output instead of 2).
- [ ] Confirm SwitchPros front locker wire routing (front axle access)
- [ ] Decide if ARB control wires merge into H6 (recommended) or run as H8 signal pair
- [ ] Source connector + lug + heat shrink BOM totals
- [ ] Determine harness sleeve / wrap material (split loom vs braided sleeving) per zone

## Related Documentation

- [Wire Routing][wire-routing] - Zone-based routing reference
- [Firewall Ingress][firewall-ingress] - HDP20 pinout and penetrations
- [AUX Battery Distribution][aux-battery] - H1 and H4 source
- [START Battery Distribution][start-battery] - H2 and H3 source
- [SwitchPros SP-1200][switchpros] - H5, H6 source controller
- [PMU24 Outputs][pmu-outputs] - H7 source
- [SafetyHub 150][safetyhub] - H8, H9 source
- [Recovery Systems / Winch][recovery] - H4 destination
- [Air Compressor][air-compressor] - H8 destination

[wire-routing]: index.md
[firewall-ingress]: 02-firewall-ingress.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[start-battery]: ../02-starter-battery-distribution/index.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[safetyhub]: ../03-aux-battery-distribution/04-safetyhub.md
[recovery]: ../../08-exterior-systems/01-winch.md
[air-compressor]: ../../08-exterior-systems/02-air-compressor.md
