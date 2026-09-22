---
hide:
  - toc
---

# DRL & Parking Lights {#drl-parking-lights}

Two circuits on two PMU outputs:

| Circuit | PMU Output | Loads | Control |
| :------ | :--------- | :---- | :------ |
| **DRL** | Out 23 (7A) | LP6 headlight DRL (Pin 3, both lights) | Automatic: on with ignition, off when headlights are on |
| **Parking / tail markers** | Out 12 (15A) | Maxbilt Round Trail Tail RED (both), RTL-S running (red) | Dash parking-light switch **or** headlights; works with the ignition off |

Parking lights are independent of the ignition so the vehicle can be lit while parked, like any production car (owner decision, 2026-09-22). That is why the two functions cannot share one output: the DRL auto-off logic would otherwise switch the tail markers off whenever the headlights are on.

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

**Parking-light switch:** Dash-mounted Toyota-style ON/OFF switch (1.54" × 0.83" cutout, see [Dashboard Controls][dashboard-controls]), wired switch-to-ground to [PMU In 4][pmu-inputs] via [HDP24 pin 21][firewall-ingress]. The PMU is CONSTANT-powered, so both the input and Out 12 work with the ignition off.

## PMU Logic

```text
PMU In 4  (In4_ParkSwitch):     dash parking-light switch (switch-to-ground)
PMU In 7  (In7_CT4_Headlights): CT4 SW3 headlight status (12V when low beam on)
PMU Pin 7 (Pin7_IgnitionRUN):   ignition signal (12V switched input)

Parking / tail markers — ignition-independent:
IF (In4_ParkSwitch == ON) OR (In7_CT4_Headlights == ON)
  THEN Out12_Parking = ON
ELSE
  Out12_Parking = OFF
END

DRL — ignition only, off with headlights:
IF (Pin7_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out23_DRL = ON
ELSE
  Out23_DRL = OFF
END
```

## Operation States

| State | Ignition | Park switch | Headlights (In 7) | Out 23 DRL | Out 12 Parking |
| :---- | :------: | :---------: | :---------------: | :--------: | :------------: |
| Daytime driving | ON | OFF | OFF | ON | OFF |
| Night driving | ON | any | ON | OFF | ON |
| Parked, lit | OFF | ON | OFF | OFF | ON |
| Parked, dark | OFF | OFF | OFF | OFF | OFF |

Headlights (CT4 SW3/SW4) are disabled with the ignition off, so In 7 cannot hold the parking circuit on when parked; only the switch does.

## Wiring

**PMU Input Wiring:**

- **Pin 7:** Ignition signal from the engine-bay distribution off HDP24 Pin 12 (PBS-I PINK IGN) — see [PMU Inputs][pmu-inputs]
- **In 7:** CT4 SW3 output, tapped in the engine bay after HDP24 pin 9 — see [Firewall Ingress][firewall-ingress]
- **In 4:** Dash parking-light switch, switch-to-ground, via HDP24 pin 21

**PMU Output Wiring:**

- **Out 23:** 16 AWG from PMU (engine bay) to LP6 Pin 3 (DRL) on each headlight (0.8A total)
- **Out 12:** 16 AWG from PMU (engine bay) → HDP24 pin 6 → H5 cabin trunk → rear splice: Maxbilt RED (each tail light) + RTL-S running; SwitchPros LIGHTS input tapped at the firewall

**Wiring Method:** Simple inline splices; no junction box required at these loads.

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Source the parking-light dash switch (Toyota-style ON/OFF) and add it to the [dash cutout layout][dashboard-controls]
- [ ] Create PMU programming: Out 12 parking logic (In 4 OR In 7, no ignition term) and Out 23 DRL auto-off
- [ ] Verify at test: parking lights on with ignition off; tail markers stay on with headlights on; DRL off with headlights on

## Related Documentation

- [Headlights][headlights] - LP6 DRL function (Pin 3)
- [Tail, Brake & Reverse][tail-brake-reverse-lights] - Maxbilt RED marker wire
- [Chase Light][chase-lights] - RTL-S running function
- [Command Touch CT4][ct4] - SW3 headlight status tap to PMU In 7
- [Dashboard Controls][dashboard-controls] - Parking-light switch
- [PMU Power Distribution][pmu-power-distribution] - PMU Out 12 / Out 23 circuits and programming
- [PMU Inputs][pmu-inputs] - In 4 / In 7 / Pin 7
- [Firewall Ingress][firewall-ingress] - HDP24 pins 6 and 21

[headlights]: 02-headlights.md
[tail-brake-reverse-lights]: 04-tail-brake-reverse.md
[chase-lights]: ../04-offroad-lighting/04-chase-lights.md
[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[dashboard-controls]: ../05-control-interfaces/05-dashboard-controls.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[harness-h5]: ../01-power-systems/07-wire-routing/05-harness-lighting-switchpros.md#h5
