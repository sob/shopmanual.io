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

**Model:** SwitchPros Command-Touch CT4 — Turn Signal & Accessory Kit (with GPS)

**Status:** Purchased (kit, plus an Axia Alloys 1.125" clamp)

**Manual:** <https://www.switchpros.com/wp-content/uploads/CT4-Rev-1.0.pdf>

**Type:** Programmable steering column-mounted turn signal and accessory controller

**Function:** Turn signals (left/right), headlight control, and auxiliary accessories

**Power Source:** PMU Out 13 (15A, programmed CONSTANT for hazards when ignition off)

**Mounting Location:** Steering column, on the Axia Alloys 1.125" clamp (the kit's 1.5" clamp is sized for UTV columns)[^ct4-clamp]

**Ground:** Chassis ground (via ignition/ground harness)

**IP Rating:** IP67

**GPS Module:** Included (enables automatic turn signal cancellation based on speed and steering angle)

///

## Overview

**Additional Features:**

- **Built-in Hazard Switch:** Flashes all outputs in sync when pressed
- **Built-in Audio Module:** Audible sound when turn signal is active
- **Lane Change Feature:** Lever press <0.5 sec flashes turn signal 3 times

## Output Allocation

The CT4 has four 10A outputs (40A module total). In turn-signal mode SW1/SW2 are locked to the turns, so **SW3 and SW4 are the only accessory outputs**. The kit ships wired for UTV use; this build reprograms both for headlights:[^ct4-manual]

| Output | Lever | Kit default | This build |
| :----- | :---- | :---------- | :--------- |
| SW1 (Brown) | Push up | Right turn | Right turn |
| SW2 (Red) | Push down | Left turn | Left turn |
| SW3 (Orange) | Pull | Horn | Low beam |
| SW4 (Yellow) | Push | Aux | High beam |

- The kit horn is **not** on SW3. It is driven by PMU Out 18 from the steering-wheel horn button — see [Horn System][horn].
- No CT4 accessory output is left for anything else.
- The manual says the Hazard switch "flashes all outputs in sync." Whether that includes SW3/SW4 (the headlights) is unconfirmed: {{ tbd(327) }}.

## Kit Contents

| Kit item | Use in this build |
| :------- | :---------------- |
| CT4 module + lever, main harness, 4-pin output harness, universal IGN/GND harness | Used |
| GPS module | Used — automatic turn-signal cancel |
| Horn | Used — on PMU Out 18, not CT4 SW3 ([Horn System][horn]) |
| 2× front amber turn-signal LEDs (400 lm, ¾" grommet mount) | Used — front turn signals ([Turn Signals][turn-signals]) |
| 2× rear amber turn-signal LEDs | Spare — rear turns are the Maxbilt tail lights |
| License-plate frame with lamp | Used — lamp spliced into PMU Out 12 instead of the CT4 harness ([DRL & Parking][drl-parking]) |
| Front/rear light harnesses (3' / 15') | Optional — SW1/SW2 are spliced to the build's own turn/tail wiring |
| 1.5" Axia Alloys clamp | Spare — UTV size; the 1.125" clamp is used |
| 2× 6mm Axia Alloys universal mounts, universal SwitchPros bracket | Optional mounting hardware |
| 2 sheets of legends | Switch labels |

Kit contents per the SwitchPros product page.[^ct4-kit]

## Turn Signal and Lighting System Integration

### Turn Signals {#ct4-turn-signals}

- **Front Turn Signals:** The kit's amber LED turn signals (dedicated turn signal only) — see [Turn Signals][turn-signals]
  - Wired to CT4 SW1 (right) and SW2 (left) outputs
  - Wire gauge: 14 AWG from CT4 to junction, 16 AWG to each light
  - **Note:** These are dedicated turn signals, not dual-function with parking lights

- **Rear Turn Signals:** Maxbilt Trail Tail lights (integrated brake/turn/marker/reverse)
  - **Brake/Turn wire (Yellow):** Combined brake and turn signal function
  - Wired to CT4 SW1 (right) and SW2 (left) outputs (parallel with front signals)
  - Wire gauge: 14 AWG from CT4 to rear junction

### Headlight Control

Pin/gauge/load detail is in the [Wiring Pinout](#wiring-pinout) table below.

- **Headlights (SW3 - PULL):** Latching on/off (pull once for on, again for off). SW3 is tapped in the engine bay to PMU In 7 (headlight status): DRL off, parking/tail markers on.
- **High Beams (SW4 - PUSH):** Push while headlights on. CT4 enforces mutual exclusivity — high beam disables low beam automatically. Momentary or latching toggle (programmable).

Both stay active with the ignition off — the CT4 is CONSTANT-powered from PMU Out 13 — so the headlights, and the parking/tail markers that follow them, can be lit while parked.

### DRL/Parking Lights

Two PMU circuits, neither switched by the CT4 directly — the CT4 only reports headlight status (SW3 → PMU In 7):

- **DRL — PMU Out 23 (0.8A):** LP6 headlight DRL function (Pin 3). On with ignition, off when SW3 headlights are on.
- **Parking/tail markers — PMU Out 12 (~2A):** Maxbilt tail light RED wire, RTL-S running section. On whenever the headlights are on (SW3 low **or** SW4 high, sensed on PMU In 7 / In 5); no separate switch; works with the ignition off. Also feeds the kit license-plate lamp (spliced here rather than into the CT4 harness).

Wire gauge: 16 AWG from PMU to each splice.

See [DRL & Parking][drl-parking] for the PMU logic, operation states, and load breakdown.

## Wiring Pinout

**12-pin Connector on CT4:**

| Wire Color  | Label      | Function                | Connection Point                                                         | Notes                                                    |
| :---------- | :--------- | :---------------------- | :----------------------------------------------------------------------- | :------------------------------------------------------- |
| Brown       | SW1, UP    | Right Turn (CT4 output) | Front/rear right turn signals                                            | 10A max per output                                       |
| Red         | SW2, DOWN  | Left Turn (CT4 output)  | Front/rear left turn signals                                             | 10A max per output                                       |
| Orange      | SW3, PULL  | Headlights (low beam)   | LP6 Pin 1 (low beam, both lights); tapped to PMU In 7 in the engine bay  | 10A output, 3.6A load, active with ignition off          |
| Yellow      | SW4, PUSH  | High Beams              | LP6 Pin 4 (high beam, both lights); tapped to PMU In 5 in the engine bay | 10A output, 5.6A load, active with ignition off          |
| Red (thick) | 12V Supply | Main power input        | PMU Out 13 (15A CONSTANT)                                                | Powers all SW outputs, allows hazards when ignition off  |
| Black       | Ground     | Ground return           | Chassis ground or firewall ground stud                                   | Via ignition/ground harness                              |
| White/Gray  | Ignition   | Ignition signal input   | Cabin ignition bus bar Terminal 1 (18 AWG, ~20 mA, fused per bus doc)     | Ignition status only — no switch is ignition-disabled (see Programming Configuration) |

## Programming Configuration

Recommended configuration for this build:

1. **Turn Signal Mode:** GPS turn signal mode (automatic cancellation based on speed and steering angle)

2. **Ignition Control:** Set **all four switches to Battery** control. This is a per-switch setting and the factory default is Ignition, so it must be changed.[^ct4-manual] SW3/SW4 must work while parked because the parking/tail markers follow the headlights (there is no separate parking switch); the low-voltage disconnect below is the battery protection.

3. **ON-OFF/Momentary:**
   - SW1/SW2: ON-OFF (latching turn signals with GPS auto-cancel)
   - SW3 (Headlights): ON-OFF latching (pull to turn on/off)
   - SW4 (High Beams): Momentary or ON-OFF (choose preferred behavior)

4. **Low Voltage Disconnect:** Enabled for all switches (protects battery from over-discharge)

5. **Flash/Strobe:** Disabled (turn signals use built-in flash pattern)

6. **Switch Memory:** Disabled (turn signals don't remember state after ignition cycle)

## GPS Module Configuration

- **Manual Override:** Can still manually cancel by moving lever to center or opposite direction
- **Mounting:** Level surface, label facing up, not obstructed by any metal, kept dry (no pressure washing); orientation otherwise doesn't matter.[^ct4-manual] The manual's UTV location ("under the plastic hood") doesn't fit the LJ's steel hood — the dash top under the windshield meets every condition.
- **Calibration:** May require initial calibration drive for optimal performance

### PMU DRL Auto-Off Logic

CT4 SW3 (low beam) taps to PMU In 7 and SW4 (high beam) to PMU In 5; the PMU turns Out 23 (DRL) off and Out 12 (parking/tail markers) on whenever either is active. See [DRL & Parking][drl-parking] for the full PMU logic, operation-state table, and load breakdown.

## Installation Checklist

Check-off items only. Wire gauges, pin assignments, and tail-light color codes
live in the [Wiring Pinout](#wiring-pinout) section above and the linked light pages.
Controller power feed (PMU Out 13) and ignition-signal distribution are tracked
in the [Power Systems Checklist][power-checklist].

### Power, Ground & Ignition

- [ ] Confirm CT4 12V supply (PMU Out 13) landed at steering column
- [ ] Confirm CT4 ground connected
- [ ] Confirm CT4 ignition signal connected (cabin ignition bus bar Terminal 1)
- [ ] Verify SW3/SW4 (headlights) work with the ignition off (parking/tail markers follow them)
- [ ] Verify SW1/SW2 (turn signals/hazards) work with ignition off (safety feature)

### Lighting Wiring

- [ ] Confirm CT4 SW1 (right turn) → front right marker + rear right tail light
- [ ] Confirm CT4 SW2 (left turn) → front left marker + rear left tail light
- [ ] Confirm Maxbilt tail lights wired per page wiring table
- [ ] Confirm CT4 SW3 → LP6 low beam (both lights)
- [ ] Confirm CT4 SW4 → LP6 high beam (both lights)
- [ ] Confirm CT4 SW3 tapped to PMU In 7 (headlight status)
- [ ] Confirm PMU Out 23 → LP6 DRL (Pin 3) and PMU Out 12 → parking/tail splice (Maxbilt RED, RTL-S running, kit plate lamp)

### GPS Module

- [ ] Mount GPS module on the dash top: level, label up, no metal overhead, dry
- [ ] Confirm GPS antenna connected to CT4 GPS input
- [ ] Perform GPS calibration drive per CT4 manual

### Programming

- [ ] Program all four switches to Battery control (factory default is Ignition)
- [ ] Program GPS turn signal mode (auto-cancel)
- [ ] Program SW3 (Headlights) to ON-OFF latching
- [ ] Program SW4 (High Beams) to preferred behavior
- [ ] Enable low voltage disconnect for all switches
- [ ] Disable flash/strobe and switch memory

### Testing

- [ ] Verify turn signals flash front and rear in sync, at correct rate
- [ ] Verify hazards work with ignition off
- [ ] Verify hazards do not flash the headlights (SW3/SW4)
- [ ] Verify lane-change mode (short press = 3 flashes, auto-cancel)
- [ ] Verify GPS auto-cancel and manual cancel
- [ ] Verify headlight control (SW3 low beam, SW4 high beam mutual exclusivity)
- [ ] Verify DRL auto-off when headlights active, back on when off
- [ ] Verify tail markers stay on with headlights on, and parking lights work with the ignition off
- [ ] Verify brake lights work independently of turn signals

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [Vehicle Lighting][vehicle-lighting-overview] - Complete wiring details for all lighting circuits controlled by CT4
- [Turn Signals][turn-signals] - Kit front LEDs and Maxbilt rear turns on SW1/SW2
- [Horn System][horn] - Kit horn on PMU Out 18
- [Engine Systems][pmu-power-distribution] - PMU specifications and programming

[control-interfaces-overview]: 01-overview.md
[vehicle-lighting-overview]: ../03-lighting-systems/01-lighting-overview.md
[turn-signals]: ../03-lighting-systems/03-turn-signals.md
[horn]: ../02-engine-systems/05-horn.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[drl-parking]: ../03-lighting-systems/05-drl-parking.md
[power-checklist]: ../09-installation/01-power-systems-checklist.md

[^ct4-manual]: SwitchPros *Command-Touch CT4* manual, Rev. 1.0091524 — p.1 (overview: 10A per switch, 40A module, hazard "flashes all outputs in sync"); p.2–3 (programming table and step 2: Ignition/Battery set per switch, default Ignition); p.5 (GPS mounting: level, label up, no metal obstruction, keep dry); p.6 (wiring diagram: Brown SW1 right turn, Red SW2 left turn, Orange SW3 horn, Yellow SW4 aux). <https://www.switchpros.com/wp-content/uploads/CT4-Rev-1.0.pdf>
[^ct4-kit]: SwitchPros store, "Command-Touch CT4 Accessory Controller GPS Turn Signal Kit for 1.5 Steering Column" product page, accessed 2026-09-27. <https://store.switchpros.com/command-touch-ct4-accessory-controller-gps-turn-signal-kit-for-1-5-steering-column/>
[^ct4-clamp]: Owner purchase, 2026-09 — Axia Alloys 1.125" clamp bought separately for the LJ column. The kit's 1.5" clamp is listed for Polaris RZR Turbo S / Ranger / Speed UTV columns on the SwitchPros product page (accessed 2026-09-27).
