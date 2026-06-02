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
  - **Note:** Yellow wire handles both brake and turn signal (combined function)

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

**Power Source:** PMU Out 9 (8A capacity, SWITCHED)

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
| White/Gray  | Ignition   | Ignition signal input   | Ignition switch RUN output (18 AWG, splits to PMU In 6, SwitchPros, CT4) | Disables SW3/SW4 when ignition off, keeps SW1/SW2 active |

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
PMU Input 6 (In 6): Ignition RUN signal
PMU Output 9 (Out 9): DRL/Parking lights circuit

Programming Logic:
IF (In6_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out9_DRL = ON
ELSE
  Out9_DRL = OFF
END
```

**How It Works:**

1. **Ignition ON, Headlights OFF (CT4 SW3 off):**
   - PMU In 6 = ON (ignition RUN)
   - PMU In 7 = OFF (CT4 SW3 not active)
   - PMU Out 9 = ON
   - All DRL/parking lights illuminated

2. **Ignition ON, Headlights ON (CT4 SW3 on):**
   - PMU In 6 = ON (ignition RUN)
   - PMU In 7 = ON (CT4 SW3 active)
   - PMU Out 9 = OFF
   - Headlights (low or high beam) active instead

3. **Ignition OFF:**
   - PMU In 6 = OFF
   - PMU Out 9 = OFF (regardless of headlight status)
   - All DRL/parking lights off

**Installation Notes:**

- Tap CT4 SW3 output (low beam circuit) to PMU In 7 for headlight status monitoring
- Use 14 AWG wire from PMU Out 9 to DRL junction
- PMU Out 9 distributes to:
  - LP6 Pin 3 (DRL) - both lights
  - License plate lights
  - Front LED side markers
  - Maxbilt tail RED wire (marker/parking)
- Total DRL circuit load: ~8A (4 circuits: license plate, LP6 DRL, front markers, rear markers)
- PMU Out 9 capacity: 15A (sufficient for 8A load)

## Installation Checklist

### Power & Ground

- [ ] Route PMU Out 13 wire to steering column location (CT4 12V supply)
- [ ] Connect CT4 ground to chassis ground or firewall ground stud

### Ignition Signal

- [ ] Connect CT4 ignition signal to ignition switch RUN output (Y-split shared with PMU In 6, SwitchPros)
- [ ] Route ignition signal wire from ignition switch to steering column (18 AWG)
- [ ] Verify SW3/SW4 (headlights) are disabled when ignition is off
- [ ] Verify SW1/SW2 (turn signals/hazards) work with ignition off (safety feature)

### Turn Signal Wiring

- [ ] Route CT4 SW1 (right turn) wire from steering column to:
  - Front right 2" LED side marker
  - Rear right Maxbilt tail light (YELLOW wire - brake/turn)
- [ ] Route CT4 SW2 (left turn) wire from steering column to:
  - Front left 2" LED side marker
  - Rear left Maxbilt tail light (YELLOW wire - brake/turn)
- [ ] Use 14 AWG wire from CT4 to junction points
- [ ] Use 16 AWG wire from junction to each individual light
- [ ] Wire Maxbilt tail lights per wiring table:
  - BLACK wire → Ground (chassis ground)
  - WHITE wire → Reverse lights (PMU Out 18)
  - YELLOW wire → Brake/Turn (CT4 turn signal output + PMU Out 17 via diodes)
  - RED wire → Marker/parking lights (PMU Out 9)
- [ ] Verify turn signals flash front and rear simultaneously
- [ ] Test lane change feature (< 0.5 sec press = 3 flashes)
- [ ] Verify brake lights work independently of turn signals

### Headlight Wiring

- [ ] Route ignition signal from ignition switch RUN output (18 AWG) to CT4 ignition input (splits to PMU In 6, SwitchPros, CT4)
- [ ] Route CT4 main power from PMU Out 13 to CT4 12V supply
- [ ] Route CT4 SW3 output wire to LP6 Pin 1 (low beam, both lights in parallel, 14 AWG)
- [ ] Route CT4 SW4 output wire to LP6 Pin 4 (high beam, both lights in parallel, 14 AWG)
- [ ] Tap CT4 SW3 output wire to DRL cutoff relay coil (to disable DRL when headlights on)
- [ ] Verify headlight control (SW3 pull to turn on/off low beams)
- [ ] Test high beam control (SW4 push to switch between low and high beams)
- [ ] Verify CT4 provides mutual exclusivity (high beam disables low beam automatically)
- [ ] Verify headlights disabled when ignition off (ignition signal working correctly)
- [ ] Verify turn signals/hazards work with ignition off (hazard safety feature)

### DRL/Parking Light Wiring

- [ ] Tap CT4 SW3 output (low beam circuit) to PMU In 7 for headlight status monitoring
- [ ] Configure PMU Out 9 DRL auto-off logic (see PMU programming section)
- [ ] Route 14 AWG wire from PMU Out 9 to DRL junction
- [ ] Route 16 AWG wire from junction to each light:
  - License plate lights
  - LP6 Headlight Pin 3 (DRL input) - both left and right
  - Front 2" LED side markers (parking function) - both left and right
  - Maxbilt tail light RED wire (marker/parking) - both left and right
- [ ] Verify all DRL/parking lights illuminate when ignition is turned on
- [ ] Verify DRL automatically turns off when headlights are activated (CT4 SW3)
- [ ] Verify DRL turns back on when headlights are turned off
- [ ] Test total current draw on DRL circuit via PMU diagnostics (should be ~8A)

### GPS Module Installation

- [ ] Mount GPS antenna on dash top or near windshield for clear sky view
- [ ] Route GPS antenna cable to CT4 controller at steering column
- [ ] Connect GPS antenna to CT4 GPS input port
- [ ] Secure GPS antenna cable to prevent interference with controls
- [ ] Verify GPS antenna has unobstructed view of sky

### Programming

- [ ] Program CT4 to battery control mode (not ignition control) for all switches
- [ ] Program CT4 to GPS turn signal mode (automatic cancellation based on speed/steering)
- [ ] Program SW3 (Headlights) to ON-OFF latching mode
- [ ] Program SW4 (High Beams) to momentary or ON-OFF (choose preferred behavior)
- [ ] Enable low voltage disconnect for all switches
- [ ] Disable flash/strobe (turn signals use built-in pattern, headlights should be solid)
- [ ] Disable switch memory
- [ ] Perform GPS calibration drive per CT4 manual instructions

### Testing

- [ ] Test hazard function works with ignition off (verify battery power configuration)
- [ ] Verify turn signals flash at correct rate (front and rear synchronized)
- [ ] Test built-in audio module sounds when turn signals are active
- [ ] Test GPS auto-cancel by making several turns at various speeds
- [ ] Verify manual cancel still works (move lever to center or opposite direction)
- [ ] Test lane change mode (quick press <0.5 sec flashes 3 times, then auto-cancels)
- [ ] Test headlight control (SW3 pull to turn on/off low beams)
- [ ] Test high beam control (SW4 push to switch between low and high beams)
- [ ] Verify DRL automatically turns off when headlights are activated
- [ ] Verify DRL turns back on when headlights are turned off
- [ ] Test low voltage disconnect prevents over-discharge

## Outstanding Items

- [ ] Determine GPS antenna mounting location (dash top or near windshield for best sky view)

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [Vehicle Lighting][vehicle-lighting-overview] - Complete wiring details for all lighting circuits controlled by CT4
- [Engine Systems][pmu-power-distribution] - PMU specifications and programming

[control-interfaces-overview]: 01-overview.md
[vehicle-lighting-overview]: ../03-lighting-systems/01-lighting-overview.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
