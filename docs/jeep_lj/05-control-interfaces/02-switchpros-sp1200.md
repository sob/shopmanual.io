---
hide:
  - toc
tags:
  - product-details
  - control-interface
  - controller
  - switchpros
---

# SwitchPros SP-1200 (RCR-Force 12) {#switchpros-sp-1200-rcr-force-12}

/// html | div.product-info

**Model:** RCR-Force 12

**Manual:** <https://www.switchpros.com/wp-content/uploads/RCR-force-12-installation-guide-REV-1.9.pdf>

**Power Source:** 150A breaker from [Firewall CONSTANT Bus][firewall-bus] (fed from AUX battery via 300A master CB + 2/0 AWG forward feed)

**Power Wire:** 2 AWG, ~2 ft (Firewall CONSTANT Bus to power module — both at firewall cluster)

**Power Module Location:** Firewall (cabin side, passenger area) — co-located with BODY PDU and Firewall CONSTANT Bus. Module is IP67 / 125°C-rated so wheel well placement is also valid, but firewall mounting minimizes total output wire length since most loads are forward/upper (~58% of outputs).

**Control Panel Location:** Dash mount (4" L x 3" W x 0.375" H)

**Control Cable:** Standard 5 ft cable (was 10.5 ft when module was rear-mounted — moving to firewall shortens this significantly)

**Ground:** 4 AWG to chassis (per manufacturer spec - reference ground only, not load return)

!!! note "Load Ground Path"
    The 4 AWG controller ground is for logic/reference only. Load return current flows through individual output grounds to the [SwitchPros Ground Bus][switchpros-ground-bus] (1/0 AWG to chassis).

**IP Rating:** IP67 (both power module and control panel)

///

## Overview

The SwitchPros SP-1200 is the main lighting and accessory controller for the Jeep LJ build. It provides 17 total outputs controlled via a 12-button control panel with Bluetooth app integration.

**Specifications:**

- 150A total capacity on CONSTANT bus
- 17 outputs total:
  - 4 outputs @ 35A (high in-rush circuits)
  - 1 output @ 30A (high in-rush)
  - 11 outputs @ 15A (can be combined for larger loads)
  - 1 low-side driver @ 2A

## Control Panel Layout

| Button |       Circuit       | Draw |                                  Details                                  |    Output Pin(s)     |
| :----: | :-----------------: | :--: | :-----------------------------------------------------------------------: | :------------------: |
|   1    |    Roof Lights      | 18A  |                  8x BD XL Sport (Linkable, single circuit)                |       OUTPUT-1       |
|   2    |    Ditch Lights     |  8A  |                   2x BD LP4 Pro (Driving/Combo Pattern)                   |       OUTPUT-2       |
|   3    |      Fog Light      |  6A  |                   1x BD S8 10" (Amber, Wide Cornering)                    |       OUTPUT-3       |
|   4    |     Dome Lights     |  2A  |                4x KC Cyclone V2 (manual + door-triggered)                 |       OUTPUT-4       |
|   5    |   Interior LEDs     |  5A  |                   MLC-RW controller (speaker + footwell RGB)              |       OUTPUT-5       |
|   6    |     Rock Lights     |  3A  |                          6x KC Cyclone V2 Lights                          |       OUTPUT-6       |
|   7    |     Chase Light     |  1A  |                      BD RTL-S 30" (Amber chase mode)                      |       OUTPUT-7       |
|   8    |     Navigation      |  2A  |                        Garmin Tread XL GPS                                |       OUTPUT-8       |
|   9    |    Front Locker     |  2A  |     ARB Locker (see [Air System][air-system-arb-compressor-lockers])      | OUTPUT-17 (low-side) |
|   10   |     Rear Locker     |  2A  |     ARB Locker (see [Air System][air-system-arb-compressor-lockers])      |      OUTPUT-10       |
|   11   |     Compressor      | 15A  | ARB Twin Compressor (see [Air System][air-system-arb-compressor-lockers]) |      OUTPUT-11       |
|   12   |  Rear Work Lights   |  5A  |                   2x BD S1 Black (Above License Plate)                    |      OUTPUT-12       |

**Notes:**

- **Button 4:** Dome lights have dual control - manual button OR door-triggered via TRIGGER-1
  - Driver door switch + Passenger door switch (wired in parallel) → TRIGGER-1 → OUTPUT-4
  - Either door opening or Button 4 press activates dome lights
- **Button 7:** RTL-S amber chase function only - brake/running/work functions powered separately
- **Buttons 5, 8:** Available for future use
- **Button 11:** OUTPUT-11 provides control signal to ARB compressor (main power is separate: CONSTANT bus → dual 60A fuses → compressor)
- **Cargo Light:** Not assigned to button - controlled by rear rocker switch via TRIGGER-2 → OUTPUT-13
- Total lighting draw if all on simultaneously: 44A (within 150A capacity)

## Wiring Pinout

### 20-Pin Harness Connector

| Pin |   Label   |    Color    | Gauge  |  Max Load   | Assigned Circuit                   | Load |                      Notes                      |
| :-: | :-------: | :---------: | :----: | :---------: | ---------------------------------- | :--: | :---------------------------------------------: |
|  1  | OUTPUT-5  |    GREEN    | 14 AWG |     15A     | _AVAILABLE_                        |  —   |                                                 |
|  2  | OUTPUT-6  |    BLUE     | 14 AWG |     15A     | Rock Lights                        |  3A  |                                                 |
|  3  | IGNITION  |   LT BLUE   |   -    |      -      | Connect to ignition signal         |  -   |              For auto-off features              |
|  4  |  LIGHTS   |    WHITE    |   -    |      -      | Connect to parking lights          |  -   |               For DRL integration               |
|  5  | OUTPUT-7  |   PURPLE    | 14 AWG |     15A     | Chase Light (amber)                |  1A  |         RTL-S amber chase function only         |
|  6  | OUTPUT-8  |    GREY     | 14 AWG |     15A     | _AVAILABLE_                        |  —   |                                                 |
|  7  | TRIGGER-1 |    PINK     |   -    |      -      | Door switches (driver + passenger) |  -   | Triggers OUTPUT-4 (dome lights) when doors open |
|  8  | TRIGGER-2 |    PINK     |   -    |      -      | Rear cargo rocker switch           |  -   |        Triggers OUTPUT-13 (cargo light)         |
|  9  | OUTPUT-9  |    WHITE    | 14 AWG | 30A (2x15A) | SPARE (can combine 9+10)           |  -   |                                                 |
| 10  | OUTPUT-9B |    WHITE    | 14 AWG |      -      | SPARE (fused with 9)               |  -   |                                                 |
| 11  | OUTPUT-10 |     TAN     | 14 AWG |     15A     | Rear Locker                        |  2A  |                                                 |
| 12  | OUTPUT-11 |    BROWN    | 14 AWG |     15A     | Compressor control                 | 15A  |          Control signal to compressor           |
| 13  | OUTPUT-12 |     RED     | 14 AWG |     15A     | Rear Work Lights                   |  5A  |                                                 |
| 14  |  GROUND   |    BLACK    |   -    |      -      | Direct to battery negative         |  -   |          Critical - direct connection           |
| 15  | OUTPUT-13 |   ORANGE    | 14 AWG |     15A     | Cargo Light                        |  5A  |   Triggered by rear rocker switch (TRIGGER-2)   |
| 16  | OUTPUT-14 |   YELLOW    | 14 AWG |     15A     | SPARE                              |  -   |                                                 |
| 17  | TRIGGER-3 |    PINK     |   -    |      -      | ARB pressure switch                |  -   |             Auto compressor control             |
| 18  | OUTPUT-17 |  LT GREEN   |   -    |     2A      | Front Locker (low-side)            |  2A  |              Low-side switch only               |
| 19  | OUTPUT-15 | GREEN/BLACK | 14 AWG |     15A     | SPARE                              |  -   |                                                 |
| 20  | OUTPUT-16 | BLUE/BLACK  | 14 AWG |     15A     | SPARE                              |  -   |                                                 |

### 4-Pin Harness (High Current Outputs)

| Pin |  Label   | Color  | Gauge | Max Load | Assigned Circuit | Load |    Notes    |
| :-: | :------: | :----: | :---: | :------: | ---------------- | :--: | :---------: |
|  1  | OUTPUT-1 | BROWN  | 10AWG |   35A    | Roof Lights (8x) | 18A  |             |
|  2  | OUTPUT-2 |  RED   | 10AWG |   35A    | Ditch Lights     |  8A  |             |
|  3  | OUTPUT-3 | ORANGE | 10AWG |   35A    | Fog Light        |  6A  |             |
|  4  | OUTPUT-4 | YELLOW | 10AWG |   35A    | Dome Lights      |  2A  |             |

## Power and Ground Connections

See [AUX Battery Distribution][aux-battery] for source battery and [Firewall CONSTANT Bus][firewall-bus] for downstream distribution.

- **Power:** AUX battery+ → 300A master CB → 2/0 AWG forward (~13 ft) → Firewall CONSTANT Bus → 150A CB → SwitchPros power module
- **Ground (logic reference):** 4 AWG wire from SwitchPros power module → chassis ground at firewall (short run, per manufacturer spec)
- **Load returns:** Each output's ground wire returns to the [SwitchPros Ground Bus][switchpros-ground-bus] (Blue Sea 2105 MaxiBus), co-located with the power module at the firewall

## Trigger Input Assignments

### TRIGGER-1: Door Switches → Dome Lights

Factory door plunger switches retained and wired in parallel to activate dome lights when either door opens.

**Switch Type:** Factory Jeep TJ/LJ door jamb plunger switch (normally open, closes to ground when door opens)

**Wiring:**

```text
Factory Driver Door Plunger (NO) ──┬──→ TRIGGER-1 (Pin 7, PINK)
Factory Passenger Door Plunger (NO)─┘
```

**Wire Routing:**
- Driver door: Door jamb → under dash → firewall SwitchPros (short run)
- Passenger door: Door jamb → under dash → firewall SwitchPros (short run)
- Wire gauge: 18 AWG (trigger signal only, no current load)

**Configuration:**

- Program Button 4 to control OUTPUT-4 OR TRIGGER-1 → OUTPUT-4
- Manual control: Press Button 4
- Automatic control: Open driver or passenger door

**Note:** Rear tailgate replaced factory rear door - no rear door switch needed

### TRIGGER-2: Rear Rocker Switch → Cargo Light

Physical rocker switch mounted in rear cargo area for convenient access when loading/unloading.

**Wiring:**

```text
Rear Cargo Rocker Switch (SPST) → TRIGGER-2 (Pin 8, PINK)
```

**Configuration:**

- Program TRIGGER-2 → OUTPUT-13 (cargo light)
- No button assignment needed
- Physical switch location: Rear cargo area (easily accessible from tailgate)
- Switch type: SPST rocker or toggle switch

### TRIGGER-3: Air Pressure Switch → Auto Compressor Control

ARB air tank pressure switch automatically activates compressor to maintain tank pressure between 135-150 PSI.

**Wiring:**

```text
ARB Pressure Switch (180901) → TRIGGER-3 (Pin 17, PINK)
```

**Configuration:**

Program TRIGGER-3 to activate compressor when tank pressure drops below 135 PSI:

**SwitchPros Logic:**

- **TRIGGER-3 OR Button 11 → OUTPUT-11 (compressor)**
- When tank pressure < 135 PSI: TRIGGER-3 closes → OUTPUT-11 activates → compressor runs
- When tank pressure = 150 PSI: TRIGGER-3 opens → OUTPUT-11 deactivates → compressor stops
- Manual override: Button 11 can force compressor on regardless of tank pressure

**Signal Source:**

- ARB Pressure Switch model 180901 (cut-in: 135 PSI, cut-out: 150 PSI)
- Mounted on air manifold under passenger seat
- Low current signal wire (18 AWG from manifold under passenger seat to SwitchPros TRIGGER-3 at firewall — short run)

**Related Documentation:**

- See [Air System][air-system-arb-compressor-lockers] for complete ARB compressor, tank, and pressure switch specifications

## Outstanding Items

- [ ] Determine exact SwitchPros power module mounting location at firewall (passenger cabin side, near BODY PDU)
- [ ] Determine SwitchPros control panel mounting location on dash
- [ ] Route 4 AWG logic ground wire from SwitchPros power module to chassis ground at firewall (short run, per manufacturer spec)
- [ ] Mount [SwitchPros Ground Bus][switchpros-ground-bus] (Blue Sea 2105 MaxiBus) at firewall near SwitchPros power module for output load returns
- [ ] Connect ignition signal from ignition switch RUN terminal to SwitchPros Pin 3 (IGNITION - LT BLUE)
  - 18 AWG wire, splits from main ignition signal distribution (see [PMU24][pmu-inputs])
- [ ] Determine parking lights signal source for SwitchPros Pin 4 (LIGHTS - WHITE) for DRL integration
- [ ] Order 5 ft control panel cable (firewall power module to dash panel - short run)
- [ ] Wire driver door switch + passenger door switch in parallel to TRIGGER-1 (Pin 7, PINK)
- [ ] Configure Button 4 programming: OUTPUT-4 OR TRIGGER-1 activates dome lights
- [ ] Install rear cargo rocker switch and wire to TRIGGER-2 (Pin 8, PINK)
- [ ] Determine rear cargo rocker switch mounting location (accessible from tailgate)
- [ ] Configure TRIGGER-2 programming: TRIGGER-2 → OUTPUT-13 (cargo light)
- [ ] Route cargo light wiring from SwitchPros OUTPUT-13 to cargo area
- [ ] Route ditch light wiring from SwitchPros OUTPUT-2 to A-pillar/hood mounts
- [ ] Wire ARB pressure switch signal to TRIGGER-3 (Pin 17, PINK)
  - 18 AWG wire from air manifold (under passenger seat) to SwitchPros TRIGGER-3
  - Route through cabin or under vehicle to engine bay SwitchPros power module
- [ ] Configure SwitchPros: TRIGGER-3 OR Button 11 → OUTPUT-11 (compressor auto/manual control)
- [ ] Test automatic pressure control: verify compressor activates at 135 PSI and stops at 150 PSI
- [ ] Assign spare outputs: OUTPUT-9 (30A), OUTPUT-14, OUTPUT-15, OUTPUT-16 (all 15A)

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [Offroad Lighting][offroad-auxiliary-lighting] - Complete wiring details for all lighting circuits controlled by SwitchPros
- [Air System][air-system-arb-compressor-lockers] - ARB locker and compressor wiring details
- [AUX Battery Distribution][aux-battery] - Power feed specifications for SwitchPros

[aux-battery]: ../01-power-systems/03-aux-battery-distribution/index.md
[firewall-bus]: ../01-power-systems/03-aux-battery-distribution/02-constant-bus.md
[air-system-arb-compressor-lockers]: ../08-exterior-systems/02-air-compressor.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[control-interfaces-overview]: 01-overview.md
[offroad-auxiliary-lighting]: ../04-offroad-lighting/index.md
[switchpros-ground-bus]: ../01-power-systems/05-grounding/03-switchpros-ground-bus.md
