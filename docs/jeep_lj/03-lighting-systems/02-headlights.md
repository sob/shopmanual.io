---
hide:
  - toc
tags:
  - product-details
  - lighting
  - headlights
  - led
---

# Headlights {#headlights}

/// html | div.product-info
![Baja Designs LP6](../images/baja-designs-lp6.jpg){ loading=lazy }

**Type:** DOT LED Headlight (complete replacement)

**Model:** LP6 DOT

**Manufacturer:** Baja Designs

**Product Page:** [LP6 Pair Driving/Combo LED][product-link]

**Installation Guide:** [Baja Designs LP6 DOT Wiring][install-link]

**Quantity:** 2 (left and right)

**Mounting:** Factory headlight buckets

**Power Source:** [Command Touch CT4][command-touch-ct4] SW3/SW4

///

## Pin Configuration (Deutsch DT06-4S connector, IP68)

| Pin | Function  | Connection | Wire Gauge | Current | Ampacity @60°C | Utilization |
| :-: | :-------- | :--------- | :--------- | :------ | :------------- | :---------- |
|  1  | Low Beam  | CT4 SW3    | 14 AWG     | 3.6A    | 20A            | 18%         |
|  2  | Ground    | Chassis    | 14 AWG     | -       | -              | -           |
|  3  | DRL       | PMU Out 23 | 16 AWG     | 0.8A    | 13A            | 6%          |
|  4  | High Beam | CT4 SW4    | 14 AWG     | 5.6A    | 20A            | 28%         |

## Low Beam

- **Control:** Pull CT4 lever (latching on/off)
- **Power:** START battery (40A) → CT4 → SW3 output (10A internal fusing)

## High Beam

- **Control:** Push CT4 lever (momentary or latching - programmable)
- **Power:** START battery (40A) → CT4 → SW4 output (10A internal fusing)
- **Mutual Exclusivity:** CT4 automatically disables low beam when high beam activates

Both beams disable when ignition is off (via ignition signal); current draw is per the pin table above.

## DRL (Daytime Running Light)

- **Power:** PMU Out 23 (shared with Maxbilt tail markers)
- **Auto-Off Logic:** PMU disables DRL when CT4 SW3 activates headlights
- **Control:** Automatic with ignition (on when ignition on, off when headlights or ignition off)
- **Load:** 0.8A total
- See [DRL/Parking Lights][drl-parking-lights] for complete circuit details

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Plan wire routing from CT4 to headlight buckets (engine bay, 14 AWG)
- [ ] Verify headlight aim after installation (LP6 DOT is compliant, just needs aiming)

## Related Documentation

- [Command Touch CT4][command-touch-ct4] - Controller programming and wiring
- [DRL/Parking Lights][drl-parking-lights] - DRL circuit and auto-off logic
- [PMU24 Power Distribution][pmu-power-distribution] - PMU Out 23 DRL circuit

[product-link]: https://www.bajadesigns.com/products/lp6-pair-driving-combo-led.html
[install-link]: https://www.bajadesigns.com/wp-content/uploads/Installation%20Instructions/FGXX_18-7801-INS_001.pdf
[command-touch-ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[drl-parking-lights]: 05-drl-parking.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
