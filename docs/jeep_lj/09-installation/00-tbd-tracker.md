---
hide:
  - toc
---

# 8.1 TBD Tracker - Outstanding Items {#tbd-tracker}

**Purpose:** Central tracking for all To-Be-Determined items across the Jeep LJ electrical system documentation.

**Last Updated:** 2025-11-28

**Total Open Items:** 22

---

## ⚡ Live from GitHub Issues (prototype)

_Generated at build time from open issues labeled `tbd`. Grouped by priority for this vehicle._

{{ tbds(scope='project', group_by='priority') }}

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

---

## 📋 MEDIUM PRIORITY (Design Optimization)

Items that improve the design but don't block installation.

| Item                                   | Description                                                                      | File                                 | Priority |
| :------------------------------------- | :------------------------------------------------------------------------------- | :----------------------------------- | :------- |
| Firewall Grommet Circuits              | Complete wire bundle lists                                                       | [Wire Routing][wire-routing]         | Medium   |
| Passenger Wheel Well Routing           | SwitchPros outputs path                                                          | [Wire Routing][wire-routing]         | Medium   |
| Dash to Console Routing                | Switch panels, USB, radio                                                        | [Wire Routing][wire-routing]         | Medium   |
| Cab to Cargo Routing                   | Rear lights, compressor, lockers                                                 | [Wire Routing][wire-routing]         | Medium   |
| Roof/Roll Bar Routing                  | Light bars, dome lights                                                          | [Wire Routing][wire-routing]         | Medium   |
| 3-Position Selector Switch Assignment  | Which SwitchPros output controls                                                 | [Dashboard Controls][dash-controls]  | Medium   |
| Speaker Mounting Locations             | Dash end caps or kick panels                                                     | [Audio Systems][audio-systems]       | Medium   |
| Horn Relay Specs                       | Contact rating, coil voltage                                                     | [CT4][ct4]                           | Medium   |
| Horn Load                              | Factory Jeep horn amperage (3-6A)                                                | [CT4][ct4]                           | Medium   |
| Horn Circuit Protection                | Inline fuse/breaker (10A typical)                                                | [CT4][ct4]                           | Medium   |
| Winch 3-Position Switch Assignment     | Which SwitchPros output controls                                                 | [Recovery Systems][recovery-systems] | Medium   |
| Cummins Harness Wire Count             | Wire bundle specification for engine harness                                     | [Wire Routing][wire-routing]         | Medium   |
| RF Power Grommet Location              | Grommet 6 location near battery for radio power                                  | [Wire Routing][wire-routing]         | Medium   |
| Solar Panel Wire Gauge                 | Wire sizing for Cascadia 4x4 80W panel connection                                | [BCDC][bcdc]                         | Medium   |
| Alternator Output Terminal Size        | Terminal size for 1/0 AWG lug selection                                          | [Alternator][alternator]             | Medium   |
| Alternator Voltage Regulator Set Point | Verify 14.2-14.4V for AGM batteries                                              | [Alternator][alternator]             | Medium   |
| BODY PDU Metri-Pack Pinout             | J301-J306 connector pinout (military TM or reverse engineering)                  | [BODY PDU][body-rtmr]                | Medium   |
| BODY PDU 12V Relay Part Numbers        | Replacement part numbers for K40, K42, K53 (currently 24V coils)                 | [BODY PDU][body-rtmr]                | Medium   |
| Winch Control Wire Routing             | Routing path from dash to bumper (~15-20 ft through multiple zones)              | [Dashboard Controls][dash-controls]  | Medium   |

---

## 📝 LOW PRIORITY (Optional/Aesthetic)

Items that can be determined during build.

| Item                              | Description                                                                     | File                                 | Priority |
| :-------------------------------- | :------------------------------------------------------------------------------ | :----------------------------------- | :------- |
| Horn Button Type                  | Momentary or latching                                                           | [CT4][ct4]                           | Low      |
| WolfBox License Plate Integration | With existing license plate lights                                              | [Communication][communication]       | Low      |
| BIM Module Current Draw           | Current draw for BIM-17-2, BIM-11-2, BIM-12-2, BIM-13-2 (powered via BIM cable) | [Gauge Cluster][gauge-cluster]       | Low      |
| LED4Life Wire Colors              | Confirm pod wire colors match MLC-RW pinout before install                      | [Footwell Lights][footwell-lights]   | Low      |

---

## 🔍 VERIFICATION NEEDED

Items that are estimated and need actual product specs to confirm.

| Item                | Description                                                                                     | File                       | Action Needed      |
| :------------------ | :---------------------------------------------------------------------------------------------- | :------------------------- | :----------------- |
| Grid Heater Current | Design value 80A - verify via element resistance measurement during installation (~0.15Ω @ 12V) | [Grid Heater][grid-heater] | Measure resistance |

---

## RECENTLY RESOLVED

Items completed since last update.

| Item                          | Resolution                                                                                                                    | Date       |
| :---------------------------- | :---------------------------------------------------------------------------------------------------------------------------- | :--------- |
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
| SwitchPros Control Cable      | 10.5 ft standard cable (wheel well to dash)                                                                                   | 2025-11-28 |
| CT4 Power Source              | PMU Out 13 (15A CONSTANT) - ~9A actual load, allows hazards when ignition off                                                | 2025-11-26 |
| SwitchPros Power Module Location | Passenger rear wheel well (with AUX battery), 1/0 AWG power wire ~2 ft                                                     | 2025-11-26 |
| Rear Seat Switch              | Blue Sea 4160 (10A latching), 16 AWG, parallel with SwitchPros OUTPUT-4                                                      | 2025-11-26 |
| Door Switch Routing           | Factory plunger switches retained, 18 AWG to SwitchPros TRIGGER-1                                                            | 2025-11-26 |
| Turn Signal Distribution      | CT4 splice to front turn, Maxbilt rear, RTL-S amber (~0.9A per side)                                                         | 2025-11-26 |
| Brake Light Distribution      | PMU Out 21 splice to Maxbilt, RTL-S brake (~4.5A total)                                                                      | 2025-11-26 |
| Running Light Distribution    | PMU Out 23 splice to LP6 DRL, Maxbilt marker, RTL-S running (~2.6A total)                                                    | 2025-11-26 |
| RTL-S Wiring Configuration    | 4-wire: black ground, red running (PMU Out 23), yellow brake (OEM), blue work (PMU Out 23); 2-wire: yellow/blue turn (SwitchPros OUTPUT-7) | 2025-11-25 |
| Cargo Light Power Source      | BODY PDU CB20 (10A) with SPST switch on wheel well top; lights flush mounted in wheel well                                                   | 2025-11-26 |
| Rear Work Lights Position     | Above license plate, verified clear of WolfBox rear camera                                                                                   | 2025-11-26 |
| Reverse Lights Mount          | Rear armor brackets                                                                                                                          | 2025-11-26 |
| Cargo Light Switch            | Blue Sea 4160 (10A latching, 3/4" mount) on wheel well top                                                                                   | 2025-11-26 |
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

| Priority    | Count  |
| :---------- | :----- |
| 🔴 Critical | 0      |
| High        | 1      |
| 📋 Medium   | 17     |
| 📝 Low      | 4      |
| 🔍 Verify   | 1      |
| **TOTAL**   | **23** |

## Related Documentation

- [Section 1 Installation Checklist][section-1-install] - Power systems installation guide
- [Section 1.7 Wire Routing][wire-routing] - Wire routing organized by location

[bcdc]: ../01-power-systems/01-power-generation/03-bcdc.md
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
[rock-lights]: ../04-offroad-lighting/06-rock-lights.md
[transmission]: ../10-drivetrain/01-transmission.md
