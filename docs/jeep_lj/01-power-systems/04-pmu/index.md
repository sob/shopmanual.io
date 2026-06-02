---
hide:
  - toc
---

# 1.4 PMU Power Distribution {#pmu-power-distribution}

Engine bay power distribution handled by ECUMaster PMU24, a programmable power management unit with 24 outputs replacing traditional relay/fuse panels.

**Location:** Engine bay

## Power Connections

| Connection         | Source            | Wire Gauge             | Protection | Notes                                                                                                            |
| :----------------- | :---------------- | :--------------------- | :--------- | :--------------------------------------------------------------------------------------------------------------- |
| **Main Power**     | START battery+    | 2/0 AWG                | 250A CB    | Optimized for 220A max load with proper protection coordination - See [Circuit Breakers][front-circuit-breakers] |
| **Ground**         | START battery-    | 2/0 AWG                | N/A        | Matches power wire gauge for 220A max load - See [Grounding Architecture][grounding]                             |
| **Ignition Sense** | Ignition signal bus bar (engine bay distribution off HDP24 Pin 12) | 18 AWG         | N/A        | Sourced from PBS-I PINK IGN via the cabin ignition bus bar - see [PMU Inputs][pmu-inputs] and [Keyless Ignition][keyless-ignition] |
| **CAN Bus**        | Cummins ECM J1939 | 18-20 AWG twisted pair | N/A        | Stub tap - see [PMU Inputs][pmu-inputs]                                                                          |

## System Components

- **[1.4.1 - Overview][pmu-overview]** - Product specifications, capacity analysis, features, mounting
- **[1.4.2 - Inputs][pmu-inputs]** - Digital/analog inputs, CAN bus integration, ignition distribution
- **[1.4.3 - Outputs][pmu-outputs]** - 24-output configuration, load analysis, combined outputs
- **[1.4.4 - Programming][pmu-programming]** - Logic examples, sequential startup, configuration, outstanding items

## Related Documentation

- [START battery Distribution][starter-battery-distribution] - PMU power source and circuit breaker
- [Grounding Architecture][grounding] - PMU ground connection
- [Firewall Ingress][firewall-ingress] - Wire routing through firewall

[pmu-overview]: 01-pmu-overview.md
[pmu-inputs]: 02-pmu-inputs.md
[pmu-outputs]: 03-pmu-outputs.md
[pmu-programming]: 04-pmu-programming.md
[front-circuit-breakers]: ../02-starter-battery-distribution/01-circuit-breakers.md
[grounding]: ../05-grounding/index.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[firewall-ingress]: ../07-wire-routing/02-firewall-ingress.md
[keyless-ignition]: ../../05-control-interfaces/06-keyless-ignition.md
