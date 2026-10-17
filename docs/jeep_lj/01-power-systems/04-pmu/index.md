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
| **Main Power**     | START battery+    | 1 AWG, ~7 ft           | 150A MRBF terminal fuse at the START post | PMU battery stud is 150 A max constant[^pmu-pinout]; ≈2.6% drop at 150A (60°C-derated), ≈2.0% at 115A typical. Downsized from 2/0 + 250A CB (2026-10-17) - See [Circuit Breakers][front-circuit-breakers] |
| **Ground**         | Engine Bay Ground Bus stud 5 | 12 AWG (connector pin 25) | N/A | Logic reference only, as short as possible; load current returns through each load's own ground - See [Grounding Architecture][grounding] |
| **Ignition Sense** | Ignition signal bus bar (engine bay distribution off HDP24 Pin 12) | 18 AWG (16 AWG pigtail at PMU) | N/A        | Sourced from PBS-I PINK IGN via the cabin ignition bus bar; PMU switches off when it drops, except for the Delayed turn off window that keeps the TCU (OUT15) alive - see [PMU Inputs][pmu-inputs], [PMU Programming][pmu-programming] and [Keyless Ignition][keyless-ignition] |
| **CAN Bus**        | Cummins ECM J1939 | 18-20 AWG twisted pair (16 AWG pigtail at PMU) | N/A        | Stub tap - see [PMU Inputs][pmu-inputs]                                                                          |

## System Components

- **[1.4.1 - Overview][pmu-overview]** - Product specifications, capacity analysis, features, mounting
- **[1.4.2 - Inputs][pmu-inputs]** - Digital/analog inputs, CAN bus integration, ignition distribution
- **[1.4.3 - Outputs][pmu-outputs]** - 24-output configuration, load analysis, combined outputs
- **[1.4.4 - Programming][pmu-programming]** - Logic examples, sequential startup, configuration, outstanding items

## Related Documentation

- [START battery Distribution][starter-battery-distribution] - PMU power source and MRBF terminal fuse
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

[^pmu-pinout]: ECUMaster, *PMU-24 DL Pinout v1.1* (2023-10-06): battery stud "Maximum constant current: 150 A"; O1–O5, O12–O16 25 A; O6–O11 15 A; O17–O24 7 A; terminals 211CC2S2160P 13–17 AWG, 211CC3S2120 14–16 AWG, 211CC3S3120 10–12 AWG. https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf (accessed 2026-10-17).
