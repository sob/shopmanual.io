---
hide:
  - toc
tags:
  - product-details
  - lighting
  - tail-lights
  - led
---

# Tail, Brake & Reverse Lights {#tail-brake-reverse-lights}

/// html | div.product-info
![Maxbilt Round Trail Tail](../images/maxbilt-trail-tail.png){ loading=lazy }

**Type:** LED Tail Light (4-function: Brake, Turn, Marker, Reverse)

**Model:** Round Trail Tail

**Manufacturer:** Maxbilt

**Product Page:** [Maxbilt Round LED Tail Lights][product-link]

**Quantity:** 2

**Mounting:** Rear quarter panels

**Power Source:** CT4 (turn), PMU Out 21 (brake), PMU Out 22 (reverse), PMU Out 23 (marker)

///

## Wire Functions

| Color  | Function       | Connection       | Wire Gauge | Notes                                |
| :----- | :------------- | :--------------- | :--------- | :----------------------------------- |
| BLACK  | Ground         | Chassis ground   | 16 AWG     | Clean metal-to-metal                 |
| WHITE  | Reverse        | [Reverse splice][reverse-lights] | 16 AWG | Parallel with Squadron Sport reverse |
| YELLOW | Brake/Turn     | [Turn splice][turn-signals] + [Brake splice][brake-lights] | 16 AWG | Combined function, internal diodes   |
| RED    | Marker/Parking | [Running splice][drl-parking-lights] | 16 AWG | DRL/parking circuit                  |

## Reverse Lights

**Power:** PMU Out 22 (~5A load, 16 AWG)
**Trigger:** Transmission reverse switch → PMU In 3
**Circuits:** Maxbilt WHITE + Squadron Sport reverse + WolfBox camera trigger (parallel)

**Wiring:**

1. Transmission reverse signal → PMU In 3
2. PMU Out 22 → Maxbilt WHITE + [Squadron Sport reverse lights][reverse-lights] + WolfBox trigger (parallel)
3. Chassis ground

**Load Breakdown:**

- Maxbilt WHITE: ~2A (LED, 130 red + 18 white LEDs total)
- Squadron Sport pair (557805): 2.8A (1.4A × 2)
- WolfBox trigger: negligible
- **Total: ~5A** (PMU Out 22 capacity: 7A, 71% utilization)

## Brake Lights {#brake-lights}

**Power:** PMU Out 21 (7A capacity)
**Trigger:** Brake pedal switch → PMU In 2

### Brake Light Distribution

PMU Out 21 splices to all brake lights:

| Destination | Load | Wire | Notes |
| :---------- | :--- | :--- | :---- |
| Maxbilt Round Trail Tail (YELLOW) | ~3A | 16 AWG | Both tail lights |
| RTL-S Brake (Yellow) | 1.45A | Per RTL-S harness | Chase light brake function |
| **Total** | **~4.5A** | | PMU Out 21 capacity: 7A (64%) |

**Splice Location:** Rear of vehicle (accessible for service)

## Brake/Turn Signal Integration

Maxbilt Round Trail Tail lights have **internal diode isolation** for combined brake/turn function. No external diodes required.

**Operation:**

- Right turn active → right tail light flashes
- Brake pressed → both tail lights solid
- Right turn + brake → right flashes, left stays solid

## Marker/Parking Lights

**Power:** PMU Out 23 (DRL/parking circuit)
**Maxbilt Connection:** RED wire
**Control:** Automatic with ignition
**Shared Circuit:** LP6 DRL

See [DRL/Parking Lights][drl-parking-lights] for circuit details.

## Outstanding Items

- [ ] Plan wire routing from CT4 to rear tail lights
- [ ] Plan wire routing from PMU Out 21/22 to rear tail lights

## Related Documentation

- [PMU Power Distribution][pmu-power-distribution] - PMU Out 21, Out 22 circuits
- [Command Touch CT4][command-touch-ct4] - Turn signal control
- [DRL/Parking Lights][drl-parking-lights] - Marker/parking circuit (RED wire)
- [Communication & Camera][communication-systems] - WolfBox camera reverse trigger

[product-link]: https://shop.maxbilt.com/collections/trail-tail-lighting/products/jeep-wrangler-round-led-tail-lights-jeep-cj-yj-tj
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[drl-parking-lights]: 05-drl-parking.md
[communication-systems]: ../07-communication-systems/index.md
[reverse-lights]: ../04-offroad-lighting/10-reverse-lights.md
[turn-signals]: 03-turn-signals.md
[brake-lights]: #brake-lights
