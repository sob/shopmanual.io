---
hide:
  - toc
---

# Vehicle Lighting Overview {#vehicle-lighting-overview}

This section covers all street-legal DOT-required lighting circuits controlled by the Command Touch CT4 and PMU.

## System Components

**Controller:** [Command Touch CT4][command-touch-ct4] - Steering column-mounted multifunction controller

- Turn signal control (left/right) with GPS auto-cancel
- Headlight control (low/high beam)
- Powered by PMU Out 13 (15A CONSTANT) + ignition signal (cabin bus bar Terminal 1)

**Power Distribution:** [PMU][pmu-power-distribution] - Programmable power management

- DRL (Out 23)
- Parking/tail markers (Out 12) — work with ignition off
- Brake lights (Out 21)
- Reverse lights (Out 22)

## Lighting Systems

### Headlights {#headlights-overview}

- **Type:** Baja Designs LP6 DOT LED (complete replacement)
- **Low Beam:** CT4 SW3 (3.6A total) - latching on/off
- **High Beam:** CT4 SW4 (5.6A total) - momentary or latching
- **DRL:** PMU Out 23 (0.8A total) - automatic with ignition, auto-off when headlights on (dedicated output; tail markers are on Out 12)
- **See:** [Headlights][headlights] for complete specifications

### Turn Signals {#turn-signals-overview}

- **Front:** Dedicated amber LED turn signals (CT4 SW1/SW2)
- **Rear:** Integrated into Maxbilt Round Trail Tail lights (YELLOW wire)
- **Features:** GPS auto-cancel, lane change mode, hazard function
- **See:** [Turn Signals][turn-signals] for complete specifications

### Tail, Brake & Reverse Lights {#tail-brake-reverse-overview}

- **Type:** Maxbilt Round Trail Tail LED (4-function)
- **Brake:** PMU Out 21 (3A) - trigger via brake pedal switch
- **Reverse:** PMU Out 22 (5A) - trigger via transmission switch, also activates WolfBox camera
- **Turn:** CT4 SW1/SW2 (internal diode isolation in Maxbilt)
- **Marker/Parking:** PMU Out 12 (parking circuit — dash switch or headlights, works with ignition off)
- **See:** [Tail, Brake & Reverse][tail-brake-reverse-lights] for complete specifications

### DRL & Parking Lights {#drl-parking-overview}

- **DRL circuit:** PMU Out 23 (7A capacity, 0.8A load) — LP6 DRL only; on with ignition, off when headlights on
- **Parking/tail circuit:** PMU Out 12 (15A capacity, ~2A load) — Maxbilt tail markers + RTL-S running; dash parking-light switch OR headlights, **ignition-independent** (lit while parked, like a production car)
- **No external relay needed** - both handled by PMU programming (CT4 SW3 status on PMU In 7)
- **See:** [DRL & Parking Lights][drl-parking-lights] for complete specifications

## Power Sources

| Circuit             | Power Source           | Capacity | Load    |
| :------------------ | :--------------------- | :------- | :------ |
| CT4 Controller      | PMU Out 13 (CONSTANT)  | 15A      | ~9A     |
| Headlights Low/High | CT4 SW3/SW4            | 10A each | 3.6/5.6A|
| DRL                 | PMU Out 23             | 7A       | 0.8A    |
| Parking/Tail Markers| PMU Out 12             | 15A      | ~2A     |
| Brake Lights        | PMU Out 21             | 7A       | ~3A     |
| Reverse Lights      | PMU Out 22             | 7A       | ~5A     |

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller specifications and programming
- [PMU Power Distribution][pmu-power-distribution] - Power management and programming
- [Offroad Lighting][offroad-auxiliary-lighting] - Auxiliary and offroad lighting circuits
- [Control Interfaces Overview][control-interfaces-overview] - All control interfaces

[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[headlights]: 02-headlights.md
[turn-signals]: 03-turn-signals.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
[drl-parking-lights]: 05-drl-parking.md
[offroad-auxiliary-lighting]: ../04-offroad-lighting/index.md
[control-interfaces-overview]: ../05-control-interfaces/index.md
