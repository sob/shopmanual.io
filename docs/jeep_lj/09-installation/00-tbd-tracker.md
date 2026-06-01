---
hide:
  - toc
---

# 8.1 TBD Tracker - Outstanding Items {#tbd-tracker}

**Purpose:** Central tracking for all To-Be-Determined items across the Jeep LJ electrical system documentation.

**Last Updated:** 2026-06-01

**Total Open Items:** 48

> Count reflects the priority sections below. The Critical-Spec Verification Audit is a separate validation log (its open on-arrival/on-vehicle checks are tracked via GitHub issue [#29][i29]); items already marked ✅ Resolved are not counted.

---

## 🔴 CRITICAL (Installation Blockers)

Items that prevent build completion or system operation.

| Item                                   | Description | File | Priority |
| :------------------------------------- | :---------- | :--- | :------- |
| _(None - all critical items resolved)_ |             |      |          |

---

## HIGH PRIORITY (Needed for Final Design)

Items needed before installation begins but not system-critical.

| Item                              | Description                                                     | File                           | Priority |
| :-------------------------------- | :-------------------------------------------------------------- | :----------------------------- | :------- |
| Dakota Digital Panel Mounting     | HDPE sheet dimensions and location                              | [Wire Routing][wire-routing]   | High     |
| Turbolamik Aux: Reverse           | Confirm aux output channel + pinout configured for Reverse signal → PMU In 3 | [Transmission][transmission]   | High     |
| Turbolamik Aux: P/N               | Confirm aux output channel + pinout configured for P/N (start interlock) | [Transmission][transmission]   | High     |
| PBS-I Kit Order                   | Order Digital Guard Dawg PBS-I kit (ICM, 2 iTag fobs, Start Button + 36" harness, Programming Button, Bypass Card) | [Keyless Ignition][keyless]   | High     |
| WAIT-Gate Relay Part              | Select SPST 30A automotive relay, NC contacts in start path (e.g. Bosch 0332019150 or Hella 4RA 003 510-04) | [Keyless Ignition][keyless]   | High     |
| ECM Pin 41 Inline Fuse            | Add 5A inline fuse on ignition outbound wire to ECM Pin 41 per Cummins R2.8 install manual (confirm doc/page — see "Cummins R2.8 Install Manual Doc #" verification item) | [Keyless Ignition][keyless]   | High     |
| PBS-I Module Mounting Location    | Cabin under-dash position; module ~5.5"×3"×1.25"; away from heat and water (do NOT engine-bay mount) | [Keyless Ignition][keyless]   | High     |
| Start Button Mounting Location    | Dash position within easy reach of driver (button + 36" harness included in PBS-I kit) | [Keyless Ignition][keyless]   | High     |
| R2.8 Turbo Inlet OD               | Measure turbo inlet tube outside diameter to confirm AMOT 4261M-02 (2.8" body) fitment and select intake-side adapter | [Runaway Protection][runaway-protection] | High     |
| AMOT-to-Intake Adapters           | Source NPT-to-hose fittings sized to match measured turbo inlet OD                                | [Runaway Protection][runaway-protection] | High     |
| AMOT T-Handle Mounting Location   | Select dash mounting position for Midwest Control 30-144-TTL-BH-3 (reachable belted, away from accidental contact) | [Runaway Protection][runaway-protection] | High     |
| AMOT Cable Firewall Grommet       | Assign dedicated firewall grommet for AMOT push-pull cable pass-through (must not share with other cables) | [Runaway Protection][runaway-protection] | High     |
| Catch Can Mounting Bracket Point  | Select engine bracketry attachment point for Mishimoto MMOCC-UB universal bracket                  | [Runaway Protection][runaway-protection] | High     |

---

## 📋 MEDIUM PRIORITY (Design Optimization)

Items that improve the design but don't block installation.

| Item                                   | Description                                                                      | File                                 | Priority |
| :------------------------------------- | :------------------------------------------------------------------------------- | :----------------------------------- | :------- |
| Firewall Grommet Circuits              | Complete wire bundle lists                                                       | [Wire Routing][wire-routing]         | Medium   |
| Dash to Console Routing                | Switch panels, USB, radio                                                        | [Wire Routing][wire-routing]         | Medium   |
| Cab to Cargo Routing                   | Rear lights, compressor, lockers                                                 | [Wire Routing][wire-routing]         | Medium   |
| Roof/Roll Bar Routing                  | Light bars, dome lights                                                          | [Wire Routing][wire-routing]         | Medium   |
| Speaker Mounting Locations             | Dash end caps or kick panels                                                     | [Audio Systems][audio-systems]       | Medium   |
| RF Power Grommet Location              | Grommet 6 location near battery for radio power                                  | [Wire Routing][wire-routing]         | Medium   |
| Alternator Output Terminal Size        | Terminal size for 1/0 AWG lug selection                                          | [Alternator][alternator]             | Medium   |
| Alternator Voltage Regulator Set Point | Verify 14.2-14.4V for AGM batteries                                              | [Alternator][alternator]             | Medium   |
| BODY PDU Metri-Pack Pinout             | J301-J306 connector pinout (military TM or reverse engineering)                  | [BODY PDU][body-rtmr]                | Medium   |
| BODY PDU 12V Relay Part Numbers        | Replacement part numbers for K40, K42, K53 (currently 24V coils)                 | [BODY PDU][body-rtmr]                | Medium   |
| Winch Control Wire Routing             | Routing path from dash to bumper via HDP24 (~3 ft BODY PDU→dash + ~13 ft dash→contactor)              | [Dashboard Controls][dash-controls]  | Medium   |
| Drive Mode Switch (transmission)       | Source 3-position Toyota-style switch (1.54"×0.83" cutout) once TCU selected. Verify TCU input requirements (ground-switched vs +12V switched, # of modes). | [Dashboard Controls][dash-controls]  | Medium   |
| Heated Seat Switches                   | Source 2× Toyota-style ON/OFF switches (1.54"×0.83" cutout) for driver + passenger heated seats. Wire to BODY PDU CB45/CB42 via K21/K22 relays. | [Dashboard Controls][dash-controls]  | Medium   |
| Driver-side Firewall Heavy Power Grommet | Source rubber grommet sized for ~1.5" OD bundle (3× 2/0 AWG H2 cables). New firewall penetration on driver side. | [Firewall Ingress][firewall-ingress] | High |
| Passenger-side Firewall Grommet (H1) | Source **single sealed 2-piece rubber grommet** (Steele Rubber or equivalent) sized for ~1.5" OD H1 cable bundle (~1.75" firewall hole). Cables run continuously through — no service break. Standard winch firewall pass-through per WARN install guidance. Bulkhead studs (Blue Sea 2203/2204) and Anderson SB175 were both underrated for the winch peak current. | [Firewall Ingress][firewall-ingress] | High |
| Dash Switch Cutout Layout              | Mark and machine 1.54"×0.83" cutouts directly into Genright dash for winch + future switches. Decide cluster location and spacing (e.g., row of 4 beside HDX cluster). | [Dashboard Controls][dash-controls]  | Medium   |
| Rear Seat Switch Mounting Location     | Physical mounting location for Blue Sea 4160 push button (rear roll bar lights)  | [Dashboard Controls][dash-controls]  | Medium   |
| Subwoofer Mount Locations              | Mark and cut quarter panel openings for 2× JL M6-8IB (8" cutout, 4.25" depth) above wheel wells. Verify clearance from cage tubes and rear seatbelts. May need backing plate. | [Subwoofer][subwoofer]               | Medium   |
| MV800/8i Amp Under-Seat Mounting Plate | Fab mounting plate under driver-side rear seat with airflow gap (no fan — convection-cooled Class-D). Chassis 13.96" × 6.93", but allow **14" × 8-3/8" footprint** including connector clearance (Crutchfield figure). Verify clearance from seat slider rails. | [Amplifier][amplifier]               | Medium   |
| Winch Trigger Control Routing          | Path for 14 AWG control wire (~13 ft) from SafetyHub ATC-1 (passenger rear wheel well) to winch contactor (front bumper) | [Recovery Systems][recovery-systems] | Medium   |
| Front Air Locker Solenoid Routing      | Path for 18 AWG (~12 ft) from SwitchPros OUTPUT-17 (passenger rear wheel well) to front axle solenoid - cross-cab + forward | [Air Lockers][air-lockers] | Medium   |
| Radio Ground Routing                   | Path for 14 AWG ground wires from GMRS / Intercom (dashboard) to START battery negative (driver rear wheel well) - direct grounds required for RF noise isolation | [Firewall Ingress][firewall-ingress] | Medium   |
| Programming Button Storage             | Hidden but accessible location (under dash or in trunk) for PBS-I fob-learn and 4-digit-PIN emergency bypass | [Keyless Ignition][keyless]          | Medium   |
| PBS-I Quiescent Current                | Measure or vendor-confirm standby draw to add to START battery parasitic budget  | [Keyless Ignition][keyless]          | Medium   |
| PBS-I Feature Programming Defaults     | Confirm shipped Feature Programming defaults are acceptable before install (no DIP/jumper menu on PBS-I) | [Keyless Ignition][keyless]          | Medium   |

---

## 📝 LOW PRIORITY (Optional/Aesthetic)

Items that can be determined during build.

| Item                              | Description                                                                     | File                                 | Priority |
| :-------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------- | :------- |
| BIM Module Current Draw           | Current draw for BIM-01-2-J1939, GPS-50-2, BIM-22-3, BIM-17-2 (powered via BIM cable) | [Gauge Cluster][gauge-cluster]       | Low      |
| LED4Life Wire Colors              | Confirm pod wire colors match MLC-RW pinout before install                      | [Footwell Lights][footwell-lights]   | Low      |

---

## 🔍 VERIFICATION NEEDED

Items that are estimated and need actual product specs to confirm.

| Item                | Description                                                                                     | File                       | Action Needed      |
| :------------------ | :---------------------------------------------------------------------------------------------- | :------------------------- | :----------------- |
| Grid Heater Current | Design value 80A - verify via element resistance measurement during installation (~0.15Ω @ 12V) | [Grid Heater][grid-heater] | Measure resistance |
| ECM Pin 35 WAIT Polarity | WAIT-gate relay logic assumes ECM Pin 35 is **active-low** (sinks to ground when WAIT lamp on). HDX doc flags this same signal "active high" pending bench check. Gate logic inverts if wrong. Bench-verify on vehicle before committing gate wiring. | [Keyless Ignition][keyless] | Bench-verify polarity |
| Cummins R2.8 Install Manual Doc # | Keyless doc cited "document 0042728" for WAIT topology + 5A ECM-fuse spec; Runaway/Grid-Heater docs cite Repower Install Guide **5504137** / flyer 5410825. Numbers don't match — confirm the correct document and page for the cited specs. | [Keyless Ignition][keyless] | Confirm source doc/page |

---

## 🚙 DRIVETRAIN (Section 10)

Mechanical drivetrain specifications, tracked separately from the electrical build. Most items need component selection before parts ordering.

| Item                              | Description                                                                                  | File                              | Priority |
| :-------------------------------- | :------------------------------------------------------------------------------------------- | :-------------------------------- | :------- |
| TCU Brake Switch Routing          | Brake pedal switch already feeds PMU In 2 via HDP24 pin 13. Decide: shared signal tap or dedicated wire to TCU? | [Harness Inventory][harness-inventory] | Medium |
| Transmission Pilot Bearing        | If required by flywheel/crank combination                                                    | [Transmission][transmission]      | Medium   |
| Transfer Case Specs               | JK NVG241 (2.72:1) — input spline (per 8HP70 adapter), output type, fluid type & capacity     | [Transfer Case][transfer-case]    | Medium   |
| Front Driveshaft Specs            | Custom (Tom Woods) decided — measure length at final ride height & order                     | [Driveshafts][driveshafts]        | Medium   |
| Rear Driveshaft Specs             | Custom (Tom Woods) decided — measure length at final ride height & order                     | [Driveshafts][driveshafts]        | Medium   |
| Front Axle Gearing & Manufacturer | Ratio and axle housing manufacturer                                                          | [Front Axle][front-axle]          | Medium   |
| Rear Axle Gearing & Locker        | Ratio, manufacturer, and locker type                                                         | [Rear Axle][rear-axle]            | Medium   |
| Front Suspension Components       | Coil rate, bypass valving, control arms, track bar, sway bar                                 | [Suspension][suspension]          | Medium   |
| Rear Suspension Components        | Coil rate, bypass valving, control arms, track bar, sway bar                                 | [Suspension][suspension]          | Medium   |
| Steering Pump Specs               | Kit pump PK40JP2-FH is Jeep 4.0L-only — source Cummins R2.8 PSC pump/bracket; flow/pressure/drive TBD | [Steering][steering]              | Medium   |
| Steering Ram Specs                | PSC SC2227K1 (2.75×8 double-ended, FHK400TJ, 40"+ confirmed) on Artec D60 mount cut to D44 + Busted Knuckle stops; mount P/N + D44 stroke length TBD | [Steering][steering]              | Medium   |
| Steering Cooler Fan (electrical)  | On PMU Out 8 (~15A, 180°F inline thermostat); confirm actual Mishimoto fan draw fits budget   | [Steering][steering]              | Medium   |
| Suspension Geometry               | Departure and breakover angles (calculated from chosen suspension)                           | [Suspension][suspension]          | Low      |
| Steering Reservoir & Fluid        | Fluid = PSC/SWEPCO 715; remote reservoir (in pump kit) model/location + system fill qty TBD  | [Steering][steering]              | Low      |

---

## RECENTLY RESOLVED

Items completed since last update.

| Item                          | Resolution                                                                                                                    | Date       |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :--------- |
| Amplifier Selection (MV800/8i) | **Architecture change:** Swapped Fusion Apollo MS-AP61800 (6-ch, 1800W) → **JL Audio MV800/8i** (8-ch, 800W, integrated DSP, part 010-03339-00). 8 channels allow Sub A on Ch 1+2 bridged @ 4Ω (200W RMS, exact match to M6-8IB rating) and Sub B on Ch 3+4 bridged @ 4Ω (200W RMS), with Ch 5-8 driving the 4 cabin speakers @ 75W RMS each. Eliminates series-wired sub compromise. Onboard DSP (TüN software) replaces external crossover/EQ tuning. 80A internal fuse (vs 125A on Fusion). Power feed unchanged: 4 AWG, direct from AUX battery+ via Blue Sea 187-100A CB. | 2026-06-01 |
| MV800/8i Idle Current & Min Bridged Impedance | Manual (MV800/8i_MAN_071519) confirms: standby current **2.4 mA** (negligible parasitic — no impact on AUX battery budget); minimum impedance **4Ω bridged / 2Ω unbridged**; required cooling clearance **1" (2.5 cm) above shell** when enclosed; manual recommends fuse value of 80A, matching internal fuse. | 2026-06-01 |
| Amp Tuning Interface (VXi-BTC vs M-DRC-50) | Selected **VXi-BTC** (010-13543-00) only — Bluetooth LE 4.2, 33 ft range, JLid-powered (50 mA from amp's bus, no separate wiring). MV800/8i has single JLid-COMM port — only one accessory at a time; MVi-HUB doesn't add ports (it's for multi-amp networking). M-DRC-50 dash preset selector deferred: head unit already handles volume/source, multi-DSP-preset switching isn't a daily-use need yet, and Bluetooth tuning is lower-friction than crawling under the rear seat for the amp's USB port. | 2026-06-01 |
| Subwoofer Wiring (per-sub bridged) | **Architecture change:** Each M6-8IB now runs on its own bridged channel pair on the MV800/8i @ 4Ω (200W RMS exact match), instead of series-wired pair on bridged Ch1+2 @ 8Ω (~145W per sub). Independent per-sub gain/EQ/delay via amp DSP. Total sub output goes from ~290W → 400W. Wiring simplified: no inter-sub series jumper, each sub returns directly to its own bridged pair. | 2026-06-01 |
| Solar Panel Wire Gauge        | 10 AWG minimum (for 2.23A Isc with safety margin) - already specified in solar generation doc                                 | 2026-05-30 |
| SwitchPros Power Module Location | **Architecture change:** Moved from passenger rear wheel well to firewall (cabin side, passenger area). Output fan-out is ~58% forward — placing module near loads minimizes total output wire. SwitchPros Ground Bus moves with controller. Input is 2 AWG, ~2 ft from Firewall CONSTANT Bus. Control cable shortens from 10.5 ft to ~5 ft. | 2026-05-30 |
| AUX Battery CONSTANT Bus #1 (rear) | **Architecture change:** Removed. With SwitchPros, BODY PDU, and Fusion Amp moved to firewall distribution, only 2 CB-protected feeds + 2 direct connections leave the AUX battery. Replaced rear CONSTANT bus with 4 stacked ring lugs on battery + 2 inline CBs (300A master + 150A SafetyHub) on a wheel well bracket. | 2026-05-30 |
| Firewall CONSTANT Bus (new)   | **Architecture change:** Added Blue Sea 2105 MaxiBus (250A) on firewall (passenger cabin side). Fed by 2/0 AWG forward feed from AUX battery via 300A master CB. Feeds SwitchPros (150A CB), BODY PDU (100A CB), Fusion Amp (100A CB). Places distribution near loads; collapses 3 forward feeds into 1 heavy cable through cabin trunk. | 2026-05-30 |
| HDP24 Connector Upsize        | Upsized main firewall connector from HDP24-24-21 to HDP24-24-29 (29 size-16 contacts, 18 used after non-SP additions + 11 future headroom). Same shell size, same firewall hole. | 2026-05-30 |
| Dedicated SwitchPros Firewall Bulkhead | Added second firewall connector (HDP24-18-14, 14 size-16 contacts, 1.25" hole) for SwitchPros forward-going outputs only. Keeps SP harness fully Delphi-native + modular, isolates PWM-capable lighting from signal wires, and reserves 8 spare pins for future SP additions (e.g., ditch/roof if A-pillar gets crowded). | 2026-05-30 |
| SwitchPros Forward-Load Ground Strategy | Each forward SP output uses 2 pins on the dedicated SP bulkhead (power out + ground return). Load grounds return to SwitchPros Ground Bus at firewall cabin side via dedicated bulkhead pins. Clean SP-native architecture; no reliance on chassis ground at forward loads. | 2026-05-30 |
| Winch Trigger Power Source              | Reallocated from SafetyHub ATC-1 (15A, ~13 ft from rear) to BODY PDU CB43 (10A, ~3 ft to dash). Properly sized for 3A trigger current. Saves ~10 ft of 14 AWG wire and frees SafetyHub ATC-1 slot for future use. | 2026-05-30 |
| Winch Dash Switch Part                  | Selected **CH4X4-TOY-D-WINIO** ($24): dual-momentary push switch, Toyota OEM cutout (1.54"×0.83"), dual-color LED. Two independent 3A circuits feed contactor IN/OUT triggers directly — matches WARN ZEON 10-S contactor architecture (contactor handles polarity internally). Safer than single rocker (can't activate both directions simultaneously). | 2026-05-30 |
| Dash Switch Cutout Standard             | All custom dash switches use **Toyota OEM cutout: 1.54"×0.83" (39mm×21mm)**. Wide vendor selection (CH4X4, STEDI, sPOD), pre-cut multi-position fascias available. Replaces ad-hoc Carling Contura cutouts. | 2026-05-30 |
| Dash Switch Mounting Approach           | Cutouts machined directly into existing **Genright aftermarket dash** — no separate fascia panel. Switches snap-lock into their own cutouts. | 2026-05-30 |
| H1 Passenger Rear Power Trunk Routing   | **Path: inside floor board / side wall (passenger side).** Passenger rear wheel well → up rear quarter sill → forward along inside floor/wall → A-pillar → firewall (CONSTANT bus). Fully inside body. Includes forward feed (2/0 AWG) and winch power/ground (2× 1/0 AWG); winch cables continue past firewall to front bumper. (Originally tracked as separate H1 forward feed + H4 winch feed routings.) | 2026-05-30 |
| H2 START → Engine Bay Routing           | **Path: inside floor board / side wall (driver side).** Driver rear wheel well → up rear quarter sill → forward along inside floor/wall → driver A-pillar → driver-side firewall grommet → engine bay. 3× 2/0 AWG bundled (~1.5" OD). New driver-side firewall grommet required. | 2026-05-30 |
| H3 BCDC Cross-Cab Routing               | **Path: under the rear bench seat cushion.** Driver rear wheel well → straight cross-cab under bench → passenger rear wheel well. Short, dry, physically protected by bench above and floor pan below. Independent of cabin trunk runs. | 2026-05-30 |
| Transmission Shifter Type               | Kilduff 8HP70 / 8 Speed ZF Shifter for Swaps — factory 8HP70 connector mates to Turbolamik TCU on mechatronic. Center console mount. Documented as H8 in harness inventory. | 2026-05-30 |
| H8 Kilduff Shifter → TCU Harness        | Documented: shifter (center console) → trans tunnel down → TCU on 8HP70 mechatronic. Kilduff-supplied harness, factory 8HP70 connector, ~3-5 ft. No firewall penetration. (Was H10 prior to 2026-05-31 renumber.) | 2026-05-30 |
| H9 TCU → Engine Bay Harness             | Documented: TCU power (PMU OUT16 14 AWG), J1939 CAN tap, Aux Reverse (PMU In 3), Aux P/N (starter relay coil), TCU ground (engine bay ground bus). All endpoints in engine bay. (Was H11 prior to 2026-05-31 renumber.) | 2026-05-30 |
| H1 Power Trunk Merge (old H1 + old H4)  | Merged old H1 (AUX forward feed) + old H4 (winch feed) into single **H1 Passenger Rear Power Trunk** — share entire passenger-side path. Fabricated as 3-cable bundle (1× 2/0 + 2× 1/0 AWG), ~1.5" OD. | 2026-05-30 |
| Subwoofer Configuration                 | **Architecture change:** Swapped single JL M7-12IB (12", 600W, 14" diameter, 7.94" mounting depth) → 2× JL M6-8IB (8", 200W each, ~9.5" diameter, 4.25" depth), wired **in series (8Ω) bridged to Fusion Ch1+2**. Symmetric L/R mounting in rear quarter panels above wheel wells. Tradeoff: total sub power drops from 580W → ~290W, but 12" depth made LJ panel mounting impractical. Series wiring keeps amp safe (8Ω is above 4Ω bridged minimum; parallel @ 2Ω would damage amp). | 2026-05-31 |
| Fusion Amp Mounting Relocation          | **Architecture change:** Moved Fusion Apollo MS-AP61800 from behind-dash firewall → **under driver-side rear seat**. Power feed now 4 AWG ~3-4 ft direct from AUX battery+ via 100A inline CB (was ~3 ft from Firewall CONSTANT Bus via 100A CB). Ground also ~3-4 ft (was ~8-10 ft). RCAs + remote turn-on grow to ~10-12 ft through trans tunnel — requires high-quality shielded RCA. Removes 100A→Fusion CB from firewall bank (now 2 CBs there: SP + BODY only). Adds 5th stacked lug + 3rd inline CB at AUX battery+ bracket. | 2026-05-31 |
| H5 Rear Cabin Trunk Merge (old H6 + old H7) | Merged old H6 (SwitchPros rear) + old H7 (PMU rear lighting) into single **H5 Rear Cabin Trunk Bundle** — share cabin trunk path. ~10 conductors with multi-pin breakout (Deutsch DT15 or AMP CPC ~15-pin) at rear cargo bulkhead. | 2026-05-30 |
| H1 Firewall Pass-Through Hardware       | **Single sealed 2-piece rubber grommet** (Steele Rubber or equivalent), ~1.75" hole, ~1.5" cable bundle OD. Cables continuous through firewall — no service break. WARN's documented standard for winch firewall pass-through. Bulkhead studs (Blue Sea 2203/2204, Cole Hersee 46211) max at 250A continuous and are underrated for winch peaks (400A). Anderson SB175 also undersized. ~$5-15. | 2026-05-30 |
| Harness Catalog Renumber                | Renumbered the catalog to a single H1–H9 sequence and dropped compound names ("H1/4", "H6/7"). New mapping: H1 (was H1/4), H2 unchanged, H3 unchanged, H4 (was H5 SwitchPros front), H5 (was H6/7 rear cabin trunk), H6 (was H8 ARB compressor), H7 (was H9 winch trigger), H8 (was H10 Kilduff shifter), H9 (was H11 TCU→engine bay). Added bundle interference assessment confirming H1 (power-only) and H5 (switched DC only, no PWM/CAN/audio/analog) are safe to bundle. | 2026-05-31 |
| Horn Relay Specs              | None required - PMU OUT 18 switches PIAA horns directly, no external relay                                                    | 2026-05-25 |
| Horn Load                     | 5.4A (PIAA 2.7A × 2)                                                                                                          | 2026-05-25 |
| Horn Circuit Protection       | None required - PMU OUT 18 has integrated electronic overcurrent/thermal protection                                           | 2026-05-25 |
| Horn Button Type              | Momentary (steering wheel button → PMU In 1)                                                                                  | 2026-05-25 |
| WolfBox License Plate         | Resolved - rear camera mounts above license plate; integration with plate lights not required                                 | 2026-05-25 |
| 3-Position Selector Switch    | Obsolete entry - no such switch in current design (SwitchPros outputs used directly)                                          | 2026-05-25 |
| Winch 3-Position Switch       | Obsolete entry - winch uses BODY PDU-fed center-off momentary rocker, not SwitchPros                                          | 2026-05-25 |
| Cummins Harness Wire Count    | Use factory bulkhead connector as-is; no per-wire enumeration needed                                                          | 2026-05-25 |
| R2.8 ECM A/C Pin (source sync)| Source file `02-engine-systems/03-hvac.md` updated to remove stale TBD; matches 2025-11-28 tracker resolution                 | 2026-05-25 |
| ADU7 Supplemental Display     | Removed from build - PMU OUT14 freed, An 5-8 returned to Available, boost/EGT/AUX-voltage sensors no longer required          | 2026-05-25 |
| Ham Radio                     | Removed from build - PMU OUT12 freed, firewall pin 2 freed, radio ground run eliminated                                       | 2026-05-25 |
| R2.8 ECM A/C Request Input    | CM2220 has no A/C request input - not applicable                                                                             | 2025-11-28 |
| Fusion Amp Mounting           | Back firewall in cab                                                                                                          | 2025-11-28 |
| STX Intercom Mounting         | Dash/behind dash                                                                                                              | 2025-11-28 |
| WolfBox Rear Camera Mount     | Above license plate                                                                                                           | 2025-11-28 |
| WolfBox Cable Length          | ~11 ft (windshield → A-pillar → rear center)                                                                                  | 2025-11-28 |
| GMRS Antenna Location         | Driver A-pillar (~6 ft from dash)                                                                                             | 2025-11-28 |
| Ham Antenna Location          | Passenger A-pillar (~4 ft to dash)                                                                                            | 2025-11-28 |
| Turn Signal Mounting          | Front fenders                                                                                                                 | 2025-11-28 |
| Radiator Fan Wire Length      | 6 ft (PMU to fan)                                                                                                             | 2025-11-28 |
| Speaker IPX Rating            | IP67                                                                                                                          | 2025-11-28 |
| Hi-Lift Jack Mount            | Not needed                                                                                                                    | 2025-11-28 |
| Recovery Board Storage        | Not needed                                                                                                                    | 2025-11-28 |
| SwitchPros Control Cable      | 10.5 ft standard cable (passenger rear wheel well to dash)                                                                    | 2025-11-28 |
| CT4 Power Source              | PMU Out 13 (15A CONSTANT) - ~9A actual load, allows hazards when ignition off                                                | 2025-11-26 |
| Rear Seat Switch              | Blue Sea 4160 (10A latching), 16 AWG, parallel with SwitchPros OUTPUT-4                                                      | 2025-11-26 |
| Door Switch Routing           | Factory plunger switches retained, 18 AWG to SwitchPros TRIGGER-1                                                            | 2025-11-26 |
| Turn Signal Distribution      | CT4 splice to front turn, Maxbilt rear, RTL-S amber (~0.9A per side)                                                         | 2025-11-26 |
| Brake Light Distribution      | PMU Out 21 splice to Maxbilt, RTL-S brake (~4.5A total)                                                                      | 2025-11-26 |
| Running Light Distribution    | PMU Out 23 splice to LP6 DRL, Maxbilt marker, RTL-S running (~2.6A total)                                                    | 2025-11-26 |
| RTL-S Wiring Configuration    | 4-wire: black ground, red running (PMU Out 23), yellow brake (OEM), blue work (PMU Out 23); 2-wire: yellow/blue turn (SwitchPros OUTPUT-7) | 2025-11-25 |
| Cargo Light Power Source      | BODY PDU CB20 (10A) with SPST switch on rear wheel well top; lights flush mounted in rear wheel well                                         | 2025-11-26 |
| Rear Work Lights Position     | Above license plate, verified clear of WolfBox rear camera                                                                                   | 2025-11-26 |
| Reverse Lights Mount          | Rear armor brackets                                                                                                                          | 2025-11-26 |
| Cargo Light Switch            | Blue Sea 4160 (10A latching, 3/4" mount) on rear wheel well top                                                                              | 2025-11-26 |
| Roof Lights OUTPUT-1 Overload | Corrected XL Sport specs (2.2A/pod, not 6A); 8 pods = 18A on single OUTPUT-1 (51% utilization)                               | 2025-11-25 |
| Fusion Amp Current Draw       | 6-ch MS-AP61800: 1.32A idle, 78A max, 125A electronic fuse                                                                    | 2025-11-24 |
| Fusion Amp CB Selection       | Blue Sea 187-100A breaker, 4 AWG power/ground wiring, mount at CONSTANT bus                                                   | 2025-11-24 |
| WolfBox Model                 | G900 TriPro selected                                                                                                          | 2025-11-24 |
| WolfBox Power Source          | BODY PDU F5 (10A, CONSTANT)                                                                                                   | 2025-11-24 |
| WolfBox Mounting              | Windshield mount (replaces factory rearview mirror)                                                                           | 2025-11-24 |
| WolfBox Ground                | Dash ground point                                                                                                             | 2025-11-24 |
| S8 10" Amber Part Number      | 701014 - Baja Designs S8 10" Wide Cornering Amber                                                                             | 2025-11-23 |
| Cargo Area Lighting Type      | BD Squadron Sport Flood (2 pods, 3,000 lumens total)                                                                          | 2025-11-23 |
| Cargo Area Light Quantity     | 2 BD Squadron Sport pods                                                                                                      | 2025-11-23 |
| RGB Controller                | BD RGB Whip has integrated controller                                                                                         | 2025-11-23 |
| iBooster Mounting Bolt Torque | 16.5 Nm (12 ft-lb) - 2x nyloc nuts, 13mm per Tesla Model Y service manual                                                     | 2025-11-23 |
| Grommet Locations             | Determined during installation (general areas documented)                                                                     | 2025-11-22 |
| Firewall Ground Stud Location | Determined during installation                                                                                                | 2025-11-22 |
| Wiper Controller Mounting     | Dash-mounted (WS-51C is integrated switch/controller)                                                                         | 2025-11-22 |
| Radiator Fan Mounting         | Radiator shroud (documented in fan motor specs)                                                                               | 2025-11-22 |
| Heated Seat Load              | Verified with vendor: 5A peak, 2A sustained per seat (not 15A)                                                                | 2025-11-22 |
| SafetyHub Location            | Consolidated to single SafetyHub 150 on AUX battery (ARB compressor, winch trigger); communications moved to PMU              | 2025-11-21 |
| AUX Battery CONSTANT Bus CB   | Resolved by connecting SafetyHub to CONSTANT bus - each load (SwitchPros, SafetyHub, BODY PDU) has individual CB protection   | 2025-11-22 |
| Wire Routing Protection       | Added comprehensive wire protection standards section covering split loom, heat sleeve, p-clamps, grommets by location        | 2025-11-22 |
| BCDC Temperature Sensor       | Documented installation location (side of AUX battery case), sensor specs, and installation procedure                         | 2025-11-22 |
| BCDC Wire Lengths             | Updated to 4 AWG @ 5-6 ft for 50A BCDC (0.94% voltage drop)                                                                   | 2025-11-22 |
| PMU PWM Frequency             | PMU24 supports 4-400 Hz on 25A outputs; GM brushless fan requires 100 Hz - compatible. Note: GM fans use inverted duty cycle. | 2025-11-22 |
| Radiator Fan Distance         | 6 ft estimated (firewall to radiator), 4 AWG wire sizing confirmed (3.2% drop @ 53A full speed)                               | 2025-11-21 |
| Radiator Fan Load             | GM Camaro fan 53A @ 100% PWM (variable speed: 16A @ 30%, 32A @ 60%, 53A @ 100%)                                               | 2025-11-21 |
| Radiator Fan Protection       | PMU OUT2+3+4 has integrated overcurrent/thermal protection, no external CB needed                                             | 2025-11-21 |
| PMU iBooster Thermal          | Resolved via non-adjacent combining: OUT1+10 (46A @ 40°C) vs OUT5+6 adjacent (32A @ 40°C)                                     | 2025-11-21 |
| Grid Heater Current           | Design value 80A (moved to Verification for field measurement)                                                                | 2025-11-21 |
| BCDC Temperature Sensor       | Included with BCDC unit (2-pin reversible, moved to High Priority for install documentation)                                  | 2025-11-21 |
| BODY PDU Model                | Bussmann LR-2 (301-1C-C-R1)                                                                                                   | 2025-11-18 |
| BODY PDU Ground               | Firewall Stud Bus Terminal 3 (14 AWG) - relay coil/logic reference only (~3A); high-side switching means loads ground separately | 2025-11-28 |
| Alternator Part Number        | Premier Power Welder HO-C28                                                                                                   | 2025-11-18 |

---

## Summary by Priority

| Priority         | Count  |
| :--------------- | :----- |
| 🔴 Critical      | 0      |
| High             | 13     |
| 📋 Medium        | 18     |
| 📝 Low           | 2      |
| 🔍 Verify        | 3      |
| 🚙 Drivetrain    | 12     |
| **TOTAL**        | **48** |

## Related Documentation

- [Section 1 Installation Checklist][section-1-install] - Power systems installation guide
- [Section 1.7 Wire Routing][wire-routing] - Wire routing organized by location

[gauge-cluster]: ../02-engine-systems/09-gauge-cluster/index.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan.md
[wire-routing]: ../01-power-systems/07-wire-routing/index.md
[switchpros]: ../05-control-interfaces/02-switchpros-sp1200.md
[dash-controls]: ../05-control-interfaces/05-dashboard-controls.md
[audio-systems]: ../06-audio-systems/index.md
[communication]: ../07-communication-systems/index.md
[turn-signals]: ../03-lighting-systems/03-turn-signals.md
[offroad-lighting]: ../04-offroad-lighting/index.md
[cargo-lights]: ../04-offroad-lighting/07-cargo-lights.md
[chase-light]: ../04-offroad-lighting/04-chase-lights.md
[recovery-systems]: ../08-exterior-systems/01-winch.md
[body-rtmr]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[section-1-install]: 01-power-systems-checklist.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
[alternator]: ../01-power-systems/01-power-generation/02-alternator.md
[hvac]: ../02-engine-systems/03-hvac.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[roof-lights]: ../04-offroad-lighting/03-roof-lights.md
[rear-lights]: ../04-offroad-lighting/08-rear-lights.md
[footwell-lights]: ../04-offroad-lighting/09-footwell-lights.md
[transmission]: ../10-drivetrain/01-transmission.md
[transfer-case]: ../10-drivetrain/02-transfer-case.md
[driveshafts]: ../10-drivetrain/03-driveshafts.md
[front-axle]: ../10-drivetrain/04-front-axle.md
[rear-axle]: ../10-drivetrain/05-rear-axle.md
[suspension]: ../10-drivetrain/06-suspension.md
[steering]: ../10-drivetrain/07-steering.md
[i29]: https://github.com/sob/drawings/issues/29
[constant-bus]: ../01-power-systems/03-aux-battery-distribution/02-constant-bus.md
[starter-doc]: ../02-engine-systems/01-starter.md
[keyless]: ../05-control-interfaces/06-keyless-ignition.md
[pmu-programming]: ../01-power-systems/04-pmu/04-pmu-programming.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
[air-lockers]: ../08-exterior-systems/03-air-lockers.md
[firewall-bus]: ../01-power-systems/03-aux-battery-distribution/02-constant-bus.md
[harness-inventory]: ../01-power-systems/07-wire-routing/03-harness-inventory.md
[subwoofer]: ../06-audio-systems/04-subwoofer.md
[amplifier]: ../06-audio-systems/02-amplifier.md
