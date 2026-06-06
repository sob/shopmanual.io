---
hide:
  - toc
---

# Jeep LJ Cummins R2.8 Build - Electrical Documentation {#jeep-lj-cummins-r28-build-electrical-documentation}

## Project Overview

This documentation covers the complete electrical system design for a 2006 Jeep LJ (Wrangler Unlimited) with a Cummins R2.8 Turbo Diesel engine swap. The factory wiring and TIPM are replaced with a modular architecture: dual isolated batteries, programmable power management (PMU24), a safety controller (SafetyHub), and split control surfaces for street lighting (Command Touch CT4) and offroad lighting (SwitchPros SP-1200). Brakes are converted to electro-hydraulic (Bosch iBooster + Wilwood master cylinder), and ignition is keyless via PBS-I with a WAIT-gate relay.

<div class="mobile-nav-only" markdown="1">

## System Architecture

The electrical system is organized into zones for logical distribution and maintenance:

### Power Systems

- **[Power Generation][power-generation]** - Batteries, alternator, BCDC, solar, grounding
- **[START battery Distribution][start-battery]** - Driver rear wheel well primary power distribution
- **[AUX battery Distribution][aux-battery]** - Passenger rear wheel well accessory power distribution
- **[Power Management Unit][pmu]** - PMU24 programmable power management
- **[BODY PDU][body-pdu]** - Body relay/fuse panel
- **[SafetyHub][safetyhub]** - Safety control system

### Critical Systems

- **[Starter System][starter]** - Engine starting system
- **[Brake Booster][brake-booster]** - Bosch iBooster Gen 2 + Wilwood master cylinder
- **[HVAC System][hvac]** - Heating, ventilation, and air conditioning
- **[Wiper System][wipers]** - Windshield wipers
- **[Horn System][horn]** - Vehicle horn
- **[Radiator Fan][radiator-fan]** - Engine cooling fan
- **[Grid Heater][grid-heater]** - Diesel grid heater
- **[Fuel System][fuel-system]** - Fuel pump and delivery
- **[Gauge Cluster][gauge-cluster]** - Dakota Digital HDX cluster + BIMs
- **[Runaway Protection][runaway-protection]** - Diesel runaway shutoff

### Lighting Systems

- **[Lighting Overview][lighting-overview]** - Complete lighting system overview
- **[Headlights][headlights]** - Main headlights
- **[Turn Signals][turn-signals]** - Turn signal system
- **[Tail, Brake & Reverse][tail-brake-reverse]** - Rear lighting
- **[DRL & Parking Lights][drl-parking]** - Daytime running and parking lights
- **[Offroad & Aux Lighting][offroad-lighting]** - Auxiliary and offroad lighting

### Control Interfaces

- **[Overview][control-overview]** - Control systems overview
- **[SwitchPros SP-1200][switchpros]** - SwitchPros lighting controller
- **[Command Touch CT4][ct4]** - Command Touch control panel
- **[Dashboard Switches][dashboard-controls]** - Physical dashboard controls
- **[Keyless Ignition][keyless-ignition]** - PBS-I keyless start with WAIT-gate relay

### Stereo Systems

- **[Audio Systems][audio]** - Fusion head unit, JL Audio MV800/8i 8-channel amp, JL Audio speakers and subwoofers

### Communications

- **[Communication Systems][communications]** - GMRS radio, intercom, dash camera

### Auxiliary Systems

- **[Winch][winch]** - Warn Zeon 10-S winch (10,000 lb)
- **[Air Compressor][air-compressor]** - ARB Twin Compressor and tank
- **[Air Lockers][air-lockers]** - ARB RD116 front/rear lockers
- **[Rear Air Chuck][rear-air-chuck]** - External air access

### Drivetrain

- **[Drivetrain Overview][drivetrain]** - Transmission, transfer case, axles, suspension, steering

### Installation

- **[Installation Overview][installation]** - Build sequence, checklists, purchase tracker
- **[Wire Routing & Layout][wire-routing]** - Physical wire routing, grommets, grounds

</div>

## Key Features

### Dual Battery System

- **START battery:** Driver rear wheel well - powers critical engine systems via PMU and SafetyHub
- **AUX battery:** Passenger rear wheel well - powers accessories via inline CBs + Firewall CONSTANT bus (cabin distribution cluster)
- **Battery Isolation:** RedArc BCDC Alpha 50 DC-DC charger with automatic jump-start assist

See [Power Generation][power-generation] for complete battery and charging system details.

### Modular Power Distribution

The factory TIPM is replaced with discrete, serviceable modules:

- **[PMU24][pmu]:** Programmable 24-channel power management unit
- **[BODY PDU][body-pdu]:** Body relay/fuse panel for cabin accessories
- **[SafetyHub][safetyhub]:** 12-channel advanced safety controller
- **[Ron Francis WS-51C][wipers]:** Wiper control module

### Brake & Ignition

- **[Bosch iBooster Gen 2 + Wilwood MC][brake-booster]:** Electro-hydraulic brake booster (Honda Accord Hybrid Gen 2 iBooster, Wilwood Tandem Compact master cylinder, Back Bay Customs adapter)
- **[PBS-I Keyless Ignition][keyless-ignition]:** Pushbutton start, self-contained WAIT-gate relay (no PMU dependency)

### Major Systems

- **[Lighting Control][switchpros]:** SwitchPros SP-1200 for offroad and auxiliary lighting
- **[Command Touch CT4][ct4]:** Street-legal lighting and turn signal control
- **[Audio System][audio]:** JL Audio MV800/8i 8-channel amp w/ DSP, JL Audio marine speakers and 2× 8" subs with RGB LED
- **[Communication][communications]:** Rugged Radio G1 GMRS, STX 4-place intercom, WolfBox dash camera
- **[Recovery & Air][recovery-air]:** Warn 10,000 lb winch, ARB air lockers, ARB Twin Air Compressor

**[TBD Tracker][tbd-tracker]** — Open items and unresolved specs.

## Print / Download

Print page combines all docs into a single binder-ready page (US Letter, duplex, binding margins).

<div class="print-hide" markdown="1">

**[Open Print Page](/print_page/){target="_blank"}**

</div>

[power-generation]: 01-power-systems/01-power-generation/index.md
[start-battery]: 01-power-systems/02-starter-battery-distribution/index.md
[aux-battery]: 01-power-systems/03-aux-battery-distribution/index.md
[pmu]: 01-power-systems/04-pmu/index.md
[body-pdu]: 01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[safetyhub]: 01-power-systems/03-aux-battery-distribution/04-safetyhub.md
[starter]: 02-engine-systems/01-starter.md
[brake-booster]: 02-engine-systems/02-brake-booster.md
[hvac]: 02-engine-systems/03-hvac.md
[wipers]: 02-engine-systems/04-wipers.md
[horn]: 02-engine-systems/05-horn.md
[radiator-fan]: 02-engine-systems/06-radiator-fan.md
[grid-heater]: 02-engine-systems/07-grid-heater.md
[lighting-overview]: 03-lighting-systems/01-lighting-overview.md
[headlights]: 03-lighting-systems/02-headlights.md
[turn-signals]: 03-lighting-systems/03-turn-signals.md
[tail-brake-reverse]: 03-lighting-systems/04-tail-brake-reverse.md
[drl-parking]: 03-lighting-systems/05-drl-parking.md
[offroad-lighting]: 04-offroad-lighting/index.md
[control-overview]: 05-control-interfaces/01-overview.md
[switchpros]: 05-control-interfaces/02-switchpros-sp1200.md
[ct4]: 05-control-interfaces/03-command-touch-ct4.md
[gauge-cluster]: 02-engine-systems/09-gauge-cluster/index.md
[dashboard-controls]: 05-control-interfaces/05-dashboard-controls.md
[audio]: 06-audio-systems/index.md
[communications]: 07-communication-systems/index.md
[winch]: 08-exterior-systems/01-winch.md
[air-compressor]: 08-exterior-systems/02-air-compressor.md
[air-lockers]: 08-exterior-systems/03-air-lockers.md
[rear-air-chuck]: 08-exterior-systems/04-rear-air-chuck.md
[recovery-air]: 08-exterior-systems/index.md
[wire-routing]: 01-power-systems/07-wire-routing/index.md
[fuel-system]: 02-engine-systems/08-fuel-system.md
[runaway-protection]: 02-engine-systems/11-runaway-protection.md
[keyless-ignition]: 05-control-interfaces/06-keyless-ignition.md
[drivetrain]: 10-drivetrain/index.md
[installation]: 09-installation/index.md
[tbd-tracker]: tbd-tracker.md
