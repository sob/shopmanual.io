---
hide:
  - toc
---

# DRL & Parking Lights {#drl-parking-lights}

Two circuits on two PMU outputs, both driven from the CT4 headlight status — no separate parking-light switch:

| Circuit | PMU Output | Loads | Control |
| :------ | :--------- | :---- | :------ |
| **DRL** | Out 23 (7A) | LP6 headlight DRL (Pin 3, both lights) | On with ignition, off when either beam is on |
| **Parking / tail markers** | Out 12 (15A) | Maxbilt Round Trail Tail RED (both), RTL-S running (red) | On whenever the headlights are on (low or high beam); works with the ignition off |

Parking lights follow the headlights and are independent of the ignition, so pulling the headlights on while parked lights the vehicle like any production car (owner decisions, 2026-09-22). That is why the two functions cannot share one output: the DRL auto-off logic would otherwise switch the tail markers off whenever the headlights are on.

## DRL Circuit (Out 23)

| Destination | Load | Wire | Notes |
| :---------- | :--- | :--- | :---- |
| LP6 Headlight DRL (Pin 3) | 0.8A | 16 AWG | Both lights, engine bay — does not cross the firewall |
| **Total** | **0.8A** | | PMU Out 23 capacity: 7A (11%) |

## Parking / Tail Marker Circuit (Out 12)

PMU Out 12 crosses the firewall on [HDP24 pin 6][firewall-ingress] and runs to the rear in the [H5 cabin trunk][harness-h5]:

| Destination | Load | Wire | Notes |
| :---------- | :--- | :--- | :---- |
| Maxbilt Round Trail Tail (RED) | ~1A | 16 AWG | Both tail lights |
| RTL-S Running (Red) | 0.8A | Per RTL-S harness | Chase light running function |
| SwitchPros LIGHTS input (Pin 4) | ~0A | 18 AWG | Parking-light sense for SwitchPros auto-off / DRL integration — tap at the firewall |
| **Total** | **~2A** | | PMU Out 12 capacity: 15A (13%) |

**Splice Location:** Rear of vehicle (accessible for service). The RTL-S white work section is currently drawn on this same splice (+1.3A) — see [Chase Light][chase-lights]; whether it stays on the parking circuit is an open question.

## Headlight Status Inputs

The PMU senses both CT4 headlight outputs, tapped on the engine-bay side of the firewall connector (no extra pins):

| PMU Input | Source | Tap | Why |
| :-------- | :----- | :-- | :-- |
| **In 7** | CT4 SW3 (low beam) | After [HDP24 pin 9][firewall-ingress], 18 AWG | Headlights on |
| **In 5** | CT4 SW4 (high beam) | After [HDP24 pin 10][firewall-ingress], 18 AWG | The CT4 drops SW3 while SW4 is active, so without In 5 the tail markers would go dark on high beam |

**CT4 programming:** SW3/SW4 must remain active with the ignition off (the CT4 is CONSTANT-powered from PMU Out 13); see [Command Touch CT4][ct4]. The PMU is CONSTANT-powered too, so Out 12 works with the ignition off.

## PMU Logic

```text
PMU In 7  (In7_CT4_LowBeam):   CT4 SW3 status (12V when low beam on)
PMU In 5  (In5_CT4_HighBeam):  CT4 SW4 status (12V when high beam on)
PMU Pin 7 (Pin7_IgnitionRUN):  ignition signal (12V switched input)

Parking / tail markers — follow the headlights, ignition-independent:
IF (In7_CT4_LowBeam == ON) OR (In5_CT4_HighBeam == ON)
  THEN Out12_Parking = ON
ELSE
  Out12_Parking = OFF
END

DRL — ignition only, off with either beam:
IF (Pin7_IgnitionRUN == ON) AND (In7_CT4_LowBeam == OFF) AND (In5_CT4_HighBeam == OFF)
  THEN Out23_DRL = ON
ELSE
  Out23_DRL = OFF
END
```

## Operation States

| State | Ignition | Low beam (In 7) | High beam (In 5) | Out 23 DRL | Out 12 Parking |
| :---- | :------: | :-------------: | :--------------: | :--------: | :------------: |
| Daytime driving | ON | OFF | OFF | ON | OFF |
| Night driving, low beam | ON | ON | OFF | OFF | ON |
| Night driving, high beam | ON | OFF | ON | OFF | ON |
| Parked, headlights pulled on | OFF | ON | OFF | OFF | ON |
| Parked, dark | OFF | OFF | OFF | OFF | OFF |

## Wiring

**PMU Input Wiring:**

- **Pin 7:** Ignition signal from the engine-bay distribution off HDP24 Pin 12 (PBS-I PINK IGN) — see [PMU Inputs][pmu-inputs]
- **In 7:** CT4 SW3 output, tapped in the engine bay after HDP24 pin 9 — see [Firewall Ingress][firewall-ingress]
- **In 5:** CT4 SW4 output, tapped in the engine bay after HDP24 pin 10

**PMU Output Wiring:**

- **Out 23:** 16 AWG from PMU (engine bay) to LP6 Pin 3 (DRL) on each headlight (0.8A total)
- **Out 12:** 16 AWG from PMU (engine bay) → HDP24 pin 6 → H5 cabin trunk → rear splice: Maxbilt RED (each tail light) + RTL-S running; SwitchPros LIGHTS input tapped at the firewall

**Wiring Method:** Simple inline splices; no junction box required at these loads.

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Create PMU programming: Out 12 parking logic (In 7 OR In 5, no ignition term) and Out 23 DRL auto-off (off with either beam)
- [ ] Program the CT4 so SW3/SW4 are not ignition-disabled (see [CT4 Programming Configuration][ct4])
- [ ] Verify at test: parking/tail markers on with low beams, stay on with high beams, work with the ignition off; DRL off with either beam

## Related Documentation

- [Headlights][headlights] - LP6 DRL function (Pin 3)
- [Tail, Brake & Reverse][tail-brake-reverse-lights] - Maxbilt RED marker wire
- [Chase Light][chase-lights] - RTL-S running function
- [Command Touch CT4][ct4] - SW3/SW4 status taps to PMU In 7 / In 5; ignition-control programming
- [PMU Power Distribution][pmu-power-distribution] - PMU Out 12 / Out 23 circuits and programming
- [PMU Inputs][pmu-inputs] - In 5 / In 7 / Pin 7
- [Firewall Ingress][firewall-ingress] - HDP24 pin 6 and the engine-bay taps after pins 9/10

[headlights]: 02-headlights.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
[chase-lights]: ../04-offroad-lighting/04-chase-lights.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[harness-h5]: ../01-power-systems/07-wire-routing/05-harness-lighting-switchpros.md#h5
