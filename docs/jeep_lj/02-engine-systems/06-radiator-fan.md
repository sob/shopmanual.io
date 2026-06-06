---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - radiator-fan
---

# 2.6 Radiator Fan {#radiator-fan-system}

/// html | div.product-info
![GM 84100128 Camaro Electric Fan](../images/gm-84100128-camaro-fan.jpg){ loading=lazy }

**Type:** Electric radiator fan

**Model:** GM 84100128

**Manufacturer:** General Motors

**Product Page:** [GM Parts Direct 84100128][gm-fan]

**Mounting:** Radiator shroud

**Power Source:** [START+ Forward Distribution Bus][start-fwd-bus] (60A CB) — relocated off the PMU

**Speed Control:** Dedicated brushless-fan controller + own coolant sensor ({{ tbd(134) }}) — independent of PMU/J1939

///

## Overview

Brushless PWM electric fan. Power is START-direct (off the PMU); variable speed is set by a dedicated brushless-fan controller reading its own coolant temperature sensor — independent of the PMU and the J1939 bus. The controller commands **full speed on lost/invalid sensor signal**, so a CAN or PMU fault can no longer leave the engine without cooling.

## Specifications

- **Current:** 53A @ full speed, 32A @ 60%, 16A @ 30% — ⚠️ unverified[^fan-specs]
- **Airflow:** 4188 CFM installed, 5690 CFM free air — ⚠️ unverified[^fan-specs]

[^fan-specs]: ⚠️ UNVERIFIED. Neither GM nor ACDelco publishes a current-draw or CFM figure for fan 84100128 (now superseded by 84790788), so the 53A / 4188 CFM values could not be confirmed against a manufacturer source (checked 2026-05-30). These drive the 60A breaker / 4 AWG wire sizing and fan-controller selection ({{ tbd(134) }}) — confirm by clamp-meter measurement on the actual fan before finalizing, or treat as an engineering estimate.

## Temperature Control

The dedicated fan controller maps coolant temp to fan speed (target curve below; exact setpoints tunable on the chosen controller, {{ tbd(134) }}):

| Coolant Temp | Fan Speed       | PWM Duty Cycle | Current |
| :----------- | :-------------- | :------------- | :------ |
| <185°F       | OFF             | 100%           | 0A      |
| 185-195°F    | Low (30%)       | 70%            | ~16A    |
| 195-205°F    | Medium (60%)    | 40%            | ~32A    |
| ≥205°F       | Full (100%)     | 10%            | 53A     |
| sensor fault | **Full (100%)** | failsafe       | 53A     |

!!! warning "Inverted Duty Cycle"
    GM brushless fans use **inverted duty cycle** — high duty cycle = low fan speed. The controller's PWM output must account for this inversion.

## Wiring

| Circuit             | Wire Gauge     | Source                                   | Destination         | Notes                                |
| :------------------ | :------------- | :--------------------------------------- | :------------------ | :----------------------------------- |
| Fan Power           | 4 AWG          | [START+ Forward Dist Bus][start-fwd-bus] (60A CB) → relay | Fan motor (+)       | Relay enabled by the fan controller  |
| Fan PWM Signal      | 18 AWG         | Fan controller PWM output                | Fan control input   | Low-current speed signal (inverted)  |
| Fan Ground          | 4 AWG          | Fan motor (−)                            | Engine Bay Bus      | Short run                            |
| Controller / sensor | per controller | {{ tbd(134) }}                           | Coolant temp sensor | Sensor + sender-port location {{ tbd(134) }} |

Power is switched by a relay (or the controller's integral power stage) at the engine-bay Forward Distribution Bus; the controller sets fan speed via the PWM signal. No PMU outputs are involved.

See [START Battery Distribution][start-fwd-bus] for the forward-bus feed and breaker.

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [START+ Forward Distribution Bus][start-fwd-bus] - Power feed + 60A breaker
- [Engine Bay Ground Bus][ground-bus] - Fan ground connection

[gm-fan]: https://www.gmpartsdirect.com/oem-parts/gm-fan-84100128
[install-checklist]: ../09-installation/02-engine-systems-checklist.md
[start-fwd-bus]: ../01-power-systems/02-starter-battery-distribution/index.md#start-forward-bus
[ground-bus]: ../01-power-systems/05-grounding/01-engine-bay-ground-bus.md
