---
hide:
  - toc
tags:
  - product-details
  - control-interface
  - controller
  - turn-signals
---

# Command Touch CT4 {#command-touch-ct4}

/// html | div.product-info

**Model:** SwitchPros Command-Touch CT4

**Manual:** <https://www.switchpros.com/wp-content/uploads/CT4-Rev-1.0.pdf>

**Type:** Programmable steering column-mounted turn signal and accessory controller

**Function:** Turn signals (left/right), headlight control, and auxiliary accessories

**Power Source:** PMU Out 13 (15A, programmed CONSTANT for hazards when ignition off)

**Mounting Location:** Steering column

**Ground:** Chassis ground (via ignition/ground harness)

**IP Rating:** IP67

**GPS Module:** Included (enables automatic turn signal cancellation based on speed and steering angle)

///

## Overview

**Specifications:**

- **Total Capacity:** 10A per switch output (~9A max actual load)
- **Four Outputs:**
  - SW1 (UP): Right Turn Signal (configured in turn signal mode)
  - SW2 (DOWN): Left Turn Signal (configured in turn signal mode)
  - SW3 (PULL): Headlights (low beam, latching on/off)
  - SW4 (PUSH): High Beams (momentary or toggle)
- **Built-in Hazard Switch:** Flashes all outputs in sync when pressed
- **Built-in Audio Module:** Audible sound when turn signal is active
- **Lane Change Feature:** Lever press <0.5 sec flashes turn signal 3 times

## Turn Signal and Lighting System Integration

The CT4 provides complete turn signal and headlight control:

### Turn Signals {#ct4-turn-signals}

- **Front Turn Signals:** Amber LED turn signal lights (dedicated turn signal only)
  - Wired to CT4 SW1 (right) and SW2 (left) outputs
  - Wire gauge: 14 AWG from CT4 to junction, 16 AWG to each light
  - **Note:** These are dedicated turn signals, not dual-function with parking lights

- **Rear Turn Signals:** Maxbilt Trail Tail lights (integrated brake/turn/marker/reverse)
  - **Brake/Turn wire (Yellow):** Combined brake and turn signal function
  - Wired to CT4 SW1 (right) and SW2 (left) outputs (parallel with front signals)
  - Wire gauge: 14 AWG from CT4 to rear junction

### Headlight Control

- **Headlights (SW3 - PULL):** Baja Designs LP6 headlights (low beam)
  - **Pull lever** → Activates headlights (low beam)
  - Power: PMU Out 13 (CONSTANT) → CT4 internal switching → SW3 output
  - CT4 SW3 output → LP6 Pin 1 (low beam, both lights in parallel)
  - CT4 handles switching internally (10A output capacity, 3.6A actual load)
  - Disabled when ignition off (via ignition signal from ignition switch RUN)
  - Latching on/off control (pull once to turn on, pull again to turn off)
  - Wire gauge: 14 AWG from CT4 SW3 output to LP6 headlights
  - When active: Also triggers DRL cutoff relay to disable DRL circuit (SW3 output tapped to relay coil)

- **High Beams (SW4 - PUSH):** Switches to high beams
  - **Push lever** (while headlights on) → Activates high beams
  - Power: PMU Out 13 (CONSTANT) → CT4 internal switching → SW4 output
  - CT4 SW4 output → LP6 Pin 4 (high beam, both lights in parallel)
  - CT4 handles switching internally (10A output capacity, 5.6A actual load)
  - Disabled when ignition off (via ignition signal from ignition switch RUN)
  - CT4 provides mutual exclusivity (high beam disables low beam automatically)
  - Momentary or latching toggle (programmable)
  - Wire gauge: 14 AWG from CT4 SW4 output to LP6 headlights

### DRL/Parking Lights

Automatic ignition-controlled circuit that powers:

- License plate lights
- LP6 Headlight DRL function (Pin 3) - **via cutoff relay**
- Front 2" LED side markers (parking function)
- Maxbilt tail light RED wire (marker/parking function)

**Power Source:** PMU Out 23 (7A capacity, ~2.6A load, auto with ignition)

**DRL Auto-Off:** PMU programming logic disables when CT4 SW3 activates (headlights on = DRL off)

Wire gauge: 14 AWG from PMU to junction, 16 AWG to each light

See [PMU DRL Auto-Off Logic](#pmu-drl-auto-off-logic) section below for complete wiring.

## Wiring Pinout

**12-pin Connector on CT4:**

| Wire Color  | Label      | Function                | Connection Point                                                         | Notes                                                    |
| :---------- | :--------- | :---------------------- | :----------------------------------------------------------------------- | :------------------------------------------------------- |
| Brown       | SW1, UP    | Right Turn (CT4 output) | Front/rear right turn signals                                            | 10A max per output                                       |
| Red         | SW2, DOWN  | Left Turn (CT4 output)  | Front/rear left turn signals                                             | 10A max per output                                       |
| Orange      | SW3, PULL  | Headlights (low beam)   | LP6 Pin 1 (low beam, both lights) + DRL cutoff relay coil                | 10A output, 3.6A load, disabled when ignition off        |
| Yellow      | SW4, PUSH  | High Beams              | LP6 Pin 4 (high beam, both lights)                                       | 10A output, 5.6A load, disabled when ignition off        |
| Red (thick) | 12V Supply | Main power input        | PMU Out 13 (15A CONSTANT)                                                | Powers all SW outputs, allows hazards when ignition off  |
| Black       | Ground     | Ground return           | Chassis ground or firewall ground stud                                   | Via ignition/ground harness                              |
| White/Gray  | Ignition   | Ignition signal input   | Ignition switch RUN output (18 AWG, splits to PMU Pin 7, SwitchPros, CT4) | Disables SW3/SW4 when ignition off, keeps SW1/SW2 active |

## Programming Configuration

The CT4 is highly programmable. Recommended configuration for this build:

1. **Turn Signal Mode:** GPS turn signal mode (automatic cancellation based on speed and steering angle)
   - SW1 (UP) = Right Turn
   - SW2 (DOWN) = Left Turn
   - GPS module monitors vehicle speed and steering to detect turn completion

2. **Ignition Control:** Ignition-aware mode
   - SW1/SW2 (turn signals/hazards) work anytime, even when ignition is off (critical for safety)
   - SW3/SW4 (headlights) disabled when ignition off (via ignition signal from ignition switch RUN)
   - Prevents battery drain from headlights left on

3. **ON-OFF/Momentary:**
   - SW1/SW2: ON-OFF (latching turn signals with GPS auto-cancel)
   - SW3 (Headlights): ON-OFF latching (pull to turn on/off)
   - SW4 (High Beams): Momentary or ON-OFF (choose preferred behavior)

4. **Low Voltage Disconnect:** Enabled for all switches (protects battery from over-discharge)

5. **Flash/Strobe:** Disabled (turn signals use built-in flash pattern)

6. **Switch Memory:** Disabled (turn signals don't remember state after ignition cycle)

## GPS Module Configuration

- **Manual Override:** Can still manually cancel by moving lever to center or opposite direction
- **Mounting:** GPS antenna must have clear view of sky (mount on dash or near windshield)
- **Calibration:** May require initial calibration drive for optimal performance

### PMU DRL Auto-Off Logic

**Purpose:** Automatically turns off DRL when headlights are activated via CT4 SW3

**Implementation:** PMU programming logic (no external relay needed)

**PMU Configuration:**

```text
PMU Input 7 (In 7): CT4 SW3 headlight status signal (tapped from low beam circuit)
PMU Pin 7: Ignition RUN signal (12V switched input)
PMU Output 23 (Out 23): DRL/Parking lights circuit

Programming Logic:
IF (Pin7_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out23_DRL = ON
ELSE
  Out23_DRL = OFF
END
```

**How It Works:**

1. **Ignition ON, Headlights OFF (CT4 SW3 off):**
   - PMU Pin 7 = ON (ignition RUN)
   - PMU In 7 = OFF (CT4 SW3 not active)
   - PMU Out 23 = ON
   - All DRL/parking lights illuminated

2. **Ignition ON, Headlights ON (CT4 SW3 on):**
   - PMU Pin 7 = ON (ignition RUN)
   - PMU In 7 = ON (CT4 SW3 active)
   - PMU Out 23 = OFF
   - Headlights (low or high beam) active instead

3. **Ignition OFF:**
   - PMU Pin 7 = OFF
   - PMU Out 23 = OFF (regardless of headlight status)
   - All DRL/parking lights off

**Installation Notes:**

- Tap CT4 SW3 output (low beam circuit) to PMU In 7 for headlight status monitoring
- Run wire from PMU Out 23 to DRL junction
- Total DRL/parking circuit load: ~2.6A — see [DRL & Parking][drl-parking] for the itemized load breakdown and wiring
- PMU Out 23 capacity: 7A (sufficient for the ~2.6A load)

## Installation Checklist

Check-off items only. Wire gauges, pin assignments, and tail-light color codes
live in the [Wiring](#wiring) section above and the linked light pages.
Controller power feed (PMU Out 13) and ignition-signal distribution are tracked
in the [Power Systems Checklist][power-checklist].

### Power, Ground & Ignition

- [ ] Confirm CT4 12V supply (PMU Out 13) landed at steering column
- [ ] Confirm CT4 ground connected
- [ ] Confirm CT4 ignition signal connected (shared Y-split with PMU Pin 7, SwitchPros)
- [ ] Verify SW3/SW4 (headlights) disabled when ignition off
- [ ] Verify SW1/SW2 (turn signals/hazards) work with ignition off (safety feature)

### Lighting Wiring

- [ ] Confirm CT4 SW1 (right turn) → front right marker + rear right tail light
- [ ] Confirm CT4 SW2 (left turn) → front left marker + rear left tail light
- [ ] Confirm Maxbilt tail lights wired per page wiring table
- [ ] Confirm CT4 SW3 → LP6 low beam (both lights)
- [ ] Confirm CT4 SW4 → LP6 high beam (both lights)
- [ ] Confirm CT4 SW3 tapped to DRL cutoff relay coil
- [ ] Confirm CT4 SW3 tapped to PMU In 7 (headlight status)
- [ ] Confirm PMU Out 23 → DRL/parking junction (license plate, LP6 DRL, markers, tail markers)

### GPS Module

- [ ] Determine GPS antenna mounting location (clear sky view)
- [ ] Confirm GPS antenna connected to CT4 GPS input
- [ ] Perform GPS calibration drive per CT4 manual

### Programming

- [ ] Program all switches to battery control mode
- [ ] Program GPS turn signal mode (auto-cancel)
- [ ] Program SW3 (Headlights) to ON-OFF latching
- [ ] Program SW4 (High Beams) to preferred behavior
- [ ] Enable low voltage disconnect for all switches
- [ ] Disable flash/strobe and switch memory

### Testing

- [ ] Verify turn signals flash front and rear in sync, at correct rate
- [ ] Verify hazards work with ignition off
- [ ] Verify lane-change mode (short press = 3 flashes, auto-cancel)
- [ ] Verify GPS auto-cancel and manual cancel
- [ ] Verify headlight control (SW3 low beam, SW4 high beam mutual exclusivity)
- [ ] Verify DRL auto-off when headlights active, back on when off
- [ ] Verify brake lights work independently of turn signals

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [Vehicle Lighting][vehicle-lighting-overview] - Complete wiring details for all lighting circuits controlled by CT4
- [Engine Systems][pmu-power-distribution] - PMU specifications and programming

[control-interfaces-overview]: 01-overview.md
[vehicle-lighting-overview]: ../03-lighting-systems/01-lighting-overview.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[drl-parking]: ../03-lighting-systems/05-drl-parking.md
[power-checklist]: ../09-installation/01-power-systems-checklist.md
