---
hide:
  - toc
tags:
  - engine-systems
---

# Section 2: Engine Systems {#engine-systems}

Engine bay systems and critical vehicle subsystems required for safe vehicle operation.

## Contents

- **[2.1 Starter System][starter]** - Cummins R2.8 starter motor, solenoid, wiring, and control circuit
- **[2.2 Brake Booster][ibooster]** - Bosch iBooster Gen 2 electric brake booster system
- **[2.3 HVAC System][hvac]** - Climate control, blower motor, and heater core circuits
- **[2.4 Wiper System][wipers]** - Ron Francis WS-51C electronic wiper controller
- **[2.5 Horn System][horn]** - PIAA twin-tone horn with relay control
- **[2.6 Radiator Fan][radiator-fan]** - Electric radiator cooling fan system
- **[2.7 Grid Heater][grid-heater]** - Cummins R2.8 cold-start grid heater relay and control
- **[2.8 Fuel System][fuel-system]** - Lift pump control circuit (replaces factory PDC/PCM logic)
- **[2.11 Runaway Protection][runaway-protection]** - Mishimoto catch can + AMOT 4261M manual air shutoff

## System Overview

Engine bay systems are powered primarily from the START battery via PMU24 programmable power distribution (see [PMU][pmu-power-distribution]). The PMU provides intelligent power management with ignition-triggered circuits, overcurrent protection, and diagnostic capabilities.

Critical safety systems (brake booster, starter) have direct battery connections for reliability.

## Related Documentation

- **[PMU Power Distribution][pmu-power-distribution]** - Engine bay power distribution and control
- **[BODY PDU][body-pdu]** - Cabin convenience power distribution
- **[SafetyHub][safetyhub]** - High-current accessory fuse panel

[starter]: 01-starter.md
[ibooster]: 02-brake-booster.md
[hvac]: 03-hvac.md
[wipers]: 04-wipers.md
[horn]: 05-horn.md
[radiator-fan]: 06-radiator-fan.md
[grid-heater]: 07-grid-heater.md
[fuel-system]: 08-fuel-system.md
[runaway-protection]: 11-runaway-protection.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[safetyhub]: ../01-power-systems/03-aux-battery-distribution/04-safetyhub.md
