---
hide:
  - toc
tags:
  - power-distribution
---

# 1.0 Power Stages {#power-stages}

## Overview

Every circuit in the build belongs to one of three power stages. Each stage is switched by the one before it, and a load goes on the lowest stage that it needs, never lower. This page is the authoritative assignment of loads to stages; wire specs stay on the battery distribution, PMU, and ignition pages linked below.

| Stage | Name | Switched by | Off when |
| :---- | :--- | :---------- | :------- |
| **0** | Battery (permanent) | Nothing: battery post through an MRBF terminal fuse or direct | Never (only by pulling a fuse or the AUX manual disconnect) |
| **1** | Main power (chassis) | PBS-I PINK IGN | Key off |
| **2** | Engine power | PBS-I PINK IGN, via the ECM keyswitch input | Key off, or engine shutdown |

PINK IGN stays on during cranking. PINK/BLK Accessory 1 drops during cranking and is currently unused (see [Keyless Ignition][keyless-ignition]).

## Stage 0 Rules {#stage-0-rules}

A load belongs on stage 0 only if it meets at least one of these:

1. **It must work with the key off.** Hazards (CT4), the keyless module (PBS-I), the ECM battery keep-alive.
2. **It must survive a failure of stage 1 or the PMU while driving.** Brake assist (iBooster), engine cooling (radiator fan).
3. **It is a high-current path that cannot go through a switch.** Starter, alternator output, grid heater element, winch.
4. **It feeds a device that switches its own outputs.** PMU battery stud, SwitchPros, BODY PDU, SafetyHub, amplifier. The device then puts its outputs on stage 1 by reading an ignition signal.

Everything on stage 0 counts against the key-off drain budget, so a load that only needs to run with the key on does not belong here, even if it is important.

**Stage 0 power, staged enable.** A high-current load that must not depend on stage 1 wiring, but should not run with the key off, takes stage 0 *power* and a stage 1 *enable*. The iBooster is the example: main power (40 A) is stage 0 from the [START+ Forward Bus][start-fwd-bus], and its ~5 A ignition enable comes from the [Ignition Signal bus][ignition-signal] on its own fuse and firewall pin. The power path never passes through the PMU or the ignition relay, so only the low-current enable is shared, and that enable drops only when the engine stops too. Assist with the key off isn't needed; the booster's mechanical push-through covers a power loss.

## Stage Assignments {#stage-assignments}

### Stage 0: Battery

| Source | Load | Why stage 0 | Page |
| :----- | :--- | :---------- | :--- |
| START post, direct | Starter | Rule 3 | [Starter][starter] |
| START post, direct | Alternator output | Rule 3 | [Alternator][alternator] |
| START post, fusible link | ECM battery supply | Rule 1 (keep-alive) | [START Distribution][starter-battery] |
| START post, fusible link | Grid heater element (relay switched by ECM) | Rule 3 | [Grid Heater][grid-heater] |
| START post, 150 A MRBF | PMU24 battery stud | Rule 4 (the PMU sleeps when Pin 7 drops) | [PMU][pmu] |
| START post, 80 A MRBF | BCDC Alpha 50 input | Rule 4 (BCDC enables on its ignition sense) | [BCDC][bcdc] |
| START+ Forward Bus | iBooster main power | Rule 2 (enable is stage 1, see above) | [Brake Booster][brake-booster] |
| START+ Forward Bus | Radiator fan (own controller) | Rule 2 | [Radiator Fan][radiator-fan] |
| START+ Forward Bus | CT4 12 V supply | Rule 1 (hazards) | [CT4][ct4] |
| START+ Forward Bus | PBS-I RED +12 V | Rule 1 | [Keyless Ignition][keyless-ignition] |
| AUX post, direct | Winch | Rule 3 | [Winch][winch] |
| AUX post, 250 A MRBF | Firewall CONSTANT bus → SwitchPros, BODY PDU | Rule 4 | [CONSTANT Bus][constant-bus] |
| AUX post, 150 A MRBF | SafetyHub | Rule 4 | [SafetyHub][safetyhub] |
| AUX post, 80 A MRBF | JL Audio amplifier | Rule 4 | [Audio][audio] |

### Stage 1: Main Power (Chassis)

PBS-I PINK IGN feeds the cabin [Ignition Signal bus][ignition-signal], which distributes it in two ways:

| Path | Load |
| :--- | :--- |
| Ignition bus terminals (signal level) | Ignition sense for CT4, SwitchPros, Fusion radio, BCDC; BODY PDU K27 (air lockers); iBooster enable (own 7.5 A fuse, firewall pin 18) |
| Stud 2 → 5 A fuse → firewall pin 12 → PMU Pin 7 | Every PMU output: HVAC blower (OUT5), wipers (OUT11), Dakota HDX (OUT3), GMRS (OUT6), intercom (OUT20), GPS (OUT14), lighting, A/C clutch (OUT17), horn (OUT18). See [PMU Outputs][pmu-outputs]. |

Stage 0 devices that read the ignition signal (SwitchPros, BODY PDU K27, Fusion radio, BCDC) put their own outputs on stage 1 that way.

### Stage 2: Engine Power

| Path | Load | Notes |
| :--- | :--- | :---- |
| Stud 2 → 5 A fuse → firewall pin 12 → ECM pin 41 | Cummins ECM keyswitch input | Dropping PINK IGN is the normal engine stop. Runaway is covered separately by the AMOT air shutoff ([Runaway Protection][runaway]). |
| ECM pins 46/21 | Grid heater relay coil | ECM-switched |
| Same fused feed → TCU wake | Turbolamik TCU ignition | |
| PMU OUT15 | Turbolamik TCU power | **Exception:** engine-stage load on a stage 1 device. Accepted 2026-10-17 to keep the START+ Forward Bus under its 100 A master fuse; the PMU Delayed turn off window covers the TCU sleep ({{ tbd(332) }}). |
| PMU OUT1, OUT16 | Oil cooler fan, PS cooler fan | On the PMU by choice: losing them is a temperature alarm, not a stall. |

The R2.8 fuel pump is gear-driven ([Fuel System][fuel-system]), so there is no fuel pump relay. That is the load most harnesses build stage 2 around; this build doesn't need one.

## Known Gaps {#known-gaps}

These are the places the build doesn't yet match the model. They are proposals, not adopted design.

- **Stages 1 and 2 share one fuse and one firewall pin.** ECM pin 41, PMU Pin 7 and the TCU wake all come off Stud 2 through one 5 A fuse and HDP24 pin 12. A fault there stops the engine, the transmission and every PMU output together. Proposed split: pin 12 → ECM pin 41 only (5 A per Cummins); a spare pin (23–29) on its own fuse → PMU Pin 7 + TCU wake.
- **No load shedding during cranking.** The PMU keeps the HVAC blower and Dakota HDX on while the starter pulls 400–600 A. PINK/BLK Accessory 1 drops during crank; wired to a spare PMU input (In 4, 6 or 8) it could disable comfort outputs while cranking.
- **No key-off drain budget for stage 0.** The [START load analysis][start-load] has no key-off scenario, and the key-off currents of the CT4, fan controller, iBooster and PBS-I ({{ tbd(84) }}) are not documented.
- **No START-side master disconnect.** The only manual disconnect is at the AUX post for the winch ([Standards Exceptions][standards-exceptions]). Optional for this vehicle.

## Outstanding Items

- [ ] Decide on splitting firewall pin 12 into separate stage 1 and stage 2 feeds
- [ ] Decide on crank-time shedding via PBS-I PINK/BLK → PMU input
- [ ] Add a key-off scenario to the START load analysis once key-off currents are measured
- [ ] Decide whether to add a START-side master disconnect

## Related Documentation

- [START Battery Distribution][starter-battery] - Stage 0 feeds from the START post
- [AUX Battery Distribution][aux-battery] - Stage 0 feeds from the AUX post
- [Ignition Signal Distribution][ignition-signal] - Stage 1 and stage 2 source
- [PMU Inputs][pmu-inputs] - Pin 7 and key-off behaviour
- [PMU Outputs][pmu-outputs] - Stage 1 outputs

[starter-battery]: 02-starter-battery-distribution/index.md
[start-fwd-bus]: 02-starter-battery-distribution/index.md#start-forward-bus
[aux-battery]: 03-aux-battery-distribution/index.md
[constant-bus]: 03-aux-battery-distribution/02-constant-bus.md
[safetyhub]: 03-aux-battery-distribution/04-safetyhub.md
[pmu]: 04-pmu/index.md
[pmu-inputs]: 04-pmu/02-pmu-inputs.md
[pmu-outputs]: 04-pmu/03-pmu-outputs.md
[ignition-signal]: 06-ignition-signal/index.md
[start-load]: 08-load-analysis/02-start-battery.md
[standards-exceptions]: STANDARDS-EXCEPTIONS.md
[alternator]: 01-power-generation/02-alternator.md
[bcdc]: 01-power-generation/03-bcdc.md
[starter]: ../02-engine-systems/01-starter.md
[brake-booster]: ../02-engine-systems/02-brake-booster.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
[fuel-system]: ../02-engine-systems/08-fuel-system.md
[runaway]: ../02-engine-systems/11-runaway-protection.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[keyless-ignition]: ../05-control-interfaces/06-keyless-ignition.md
[audio]: ../06-audio-systems/index.md
[winch]: ../08-exterior-systems/01-winch.md
