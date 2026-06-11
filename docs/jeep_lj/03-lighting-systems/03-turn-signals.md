---
hide:
  - toc
tags:
  - product-details
  - lighting
  - turn-signals
---

# Turn Signals {#turn-signals}

**Controller:** [Command Touch CT4][command-touch-ct4] (SW1 = right turn, SW2 = left turn)

**Power Source:** PMU Out 13 (CONSTANT, via CT4)

**Features:** GPS auto-cancel, lane change mode, hazard function

## Turn Signal Distribution

Each CT4 output (SW1 right, SW2 left) splices to three destinations:

| Destination | Load | Wire | Notes |
| :---------- | :--- | :--- | :---- |
| Front turn signal | ~0.2A | 14 AWG | Fender-mounted LED |
| Maxbilt rear turn | ~0.3A | 16 AWG | Integrated tail light |
| RTL-S amber | 0.36A | Per RTL-S harness | Chase light turn function |
| **Total per side** | **~0.9A** | | Well under 10A CT4 output capacity |

**Splice Location:** Behind dash (accessible for service)

## Front Turn Signals

![LED Side Marker](../images/led-side-marker.jpg){ loading=lazy width=200 }

**Type:** Amber LED turn signals
**Quantity:** 2 (left and right fenders)
**Function:** Turn signal only (CT4 controlled)
**Part #:** {{ tbd(153) }}
**Size:** 0.8" × 0.8" × 1.1"
**Draw:** ~0.2A each (~0.4A total, estimated)

### Wiring

| Function   | Source  | Wire          | Current | Ampacity @60°C | Utilization |
| :--------- | :------ | :------------ | :------ | :------------- | :---------- |
| Right Turn | CT4 SW1 | BROWN, 14 AWG | ~0.2A   | 20A            | 1%          |
| Left Turn  | CT4 SW2 | RED, 14 AWG   | ~0.2A   | 20A            | 1%          |

**Routing:** CT4 (steering column) → firewall grommet → engine bay → fenders

**Connections:** Soldered with marine heat shrink (waterproof)

## Rear Turn Signals

Rear turn signals are fed from the CT4 splice (see distribution table above):

- **Maxbilt Round Trail Tail** - YELLOW wire, see [Tail/Brake/Reverse Lights][tail-brake-reverse-lights]
- **RTL-S Chase Light** - Yellow/Blue wires, see [Chase Lights][chase-lights]

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Measure wire distance: CT4 → firewall → fenders (see [Wire Distance Reference][wire-distance])

[wire-distance]: ../01-power-systems/01-power-generation/05-wire-distance-reference.md

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller programming and wiring
- [Tail/Brake/Reverse Lights][tail-brake-reverse-lights] - Rear turn signal integration

[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
[chase-lights]: ../04-offroad-lighting/04-chase-lights.md
