---
hide:
  - toc
---

# TBD Tracker {#tbd-tracker}

**Purpose:** Central tracking for all To-Be-Determined items across the Jeep LJ electrical system documentation.

**Open items are tracked as GitHub issues** labeled `tbd` and rendered live below. Add or resolve items by opening/closing issues, not by editing this page. Resolved items are archived at the bottom for history.

> The Critical-Spec Verification Audit is a separate validation log (its open on-arrival/on-vehicle checks are tracked via GitHub issue [#29][i29]).

---

## Open Items

_Live from GitHub issues labeled `tbd`, generated at build time. Filter with GitHub syntax (`label:`, `priority:`, `area:`, `project:` or free text), use the dropdowns, click a label to filter by it, or change the sort._

{{ tbds(scope='project', layout='github') }}

---

## Recently Resolved

_Closed `tbd` issues from the last 90 days, rendered live. Full history lives in
[closed GitHub issues](https://github.com/sob/drawings/issues?q=is%3Aissue+is%3Aclosed+label%3Atbd)._

{{ tbds_resolved(scope='project', since='90d') }}

## Historical Archive (pre-migration)

Resolutions captured before TBD tracking moved to GitHub Issues. New
resolutions appear in the table above (rendered live from closed issues).

| Item                          | Resolution                                                                                                                    | Date       |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :--------- |
| ECM Pin 35 WAIT Polarity & Cummins Wiring Doc # | **Confirmed via Cummins Repower R2.8 CM2220 R101B Installation Guide (Bulletin 5504137, Jan 2018), §2 pp. 2-19→2-24.** Circuit Wiring table: Wait-To-Start = Yellow, ECM pin 35; Keyswitch = Pink, pin 41 with 5A inline fuse. Guide states lamps are fed +12V from the keyswitch with the ECM "providing a path to ground via a sink circuit" → Pin 35 is **active-low**, validating the WAIT-gate relay logic (relay taps Pin 35 directly, independent of HDX cluster-input polarity). Full schematic = separate Wiring Diagram Bulletin 5467560 (QSOL). The unverified "document 0042728" reference was removed from the keyless doc. Residual ECM lamp-driver sink-margin check moved to Verification. | 2026-06-01 |
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

## Related Documentation

- [Section 1 Installation Checklist][section-1-install] - Power systems installation guide
- [Section 1.7 Wire Routing][wire-routing] - Wire routing organized by location

[wire-routing]: 01-power-systems/07-wire-routing/index.md
[section-1-install]: 09-installation/01-power-systems-checklist.md
[i29]: https://github.com/sob/drawings/issues/29
