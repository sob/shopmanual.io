---
hide:
  - toc
tags:
  - product-details
  - drivetrain
  - transmission
  - 8hp70
---

# 10.1 Transmission - ZF 8HP70 (845RE) {#transmission}

/// html | div.product-info

**Type:** 8-speed automatic transmission

**Model:** ZF 8HP70 (Chrysler 845RE)

**Donor Vehicle:** 2015-2019 RAM 1500 EcoDiesel 4x4

**Torque Capacity:** 520 lb-ft (factory), 700+ lb-ft (built)

**Controller:** Turbolamik TCU 2.0 with basic wiring harness

**Adapter Kit:** Custom (in progress)

///

## Specifications

| Specification    | Value                          |
| :--------------- | :----------------------------- |
| Manufacturer     | ZF Friedrichshafen             |
| Model            | 8HP70 (Chrysler 845RE)         |
| Donor            | 2015-2019 RAM 1500 EcoDiesel 4x4 |
| Type             | 8-speed automatic, 4WD         |
| Torque Capacity  | 520 lb-ft (stock)              |
| Weight           | ~225 lbs (dry)                 |
| Length           | ~27.5"                         |
| Fluid Capacity   | ~9 quarts (pan drop service)   |
| Fluid Type       | ZF Lifeguard 8 (or equivalent) |

## Gear Ratios

| Gear    | Ratio  |
| :------ | :----- |
| 1st     | 4.714  |
| 2nd     | 3.143  |
| 3rd     | 2.106  |
| 4th     | 1.667  |
| 5th     | 1.285  |
| 6th     | 1.000  |
| 7th     | 0.839  |
| 8th     | 0.667  |
| Reverse | 3.295  |

## Controller - Turbolamik TCU 2.0

/// html | div.product-info

**Model:** Turbolamik TCU 2.0

**Variant:** Basic Wiring Harness (CAN)

**Product Page:** [Turbolamik TCU 2.0][turbolamik]

**Manual:** [Turbolamik Manual][turbolamik-manual]

///

| Specification      | Value                                    |
| :----------------- | :--------------------------------------- |
| Supported Trans    | 8HP45, 8HP50, 8HP55, 8HP70, 8HP75, 8HP90, 8HP95 (Gen1/Gen2/Gen3) |
| Shift Speed        | 50-150ms                                 |
| Drive Modes        | 8 configurable (Street, Race, Offroad, etc.) |
| CAN Protocols      | ECUMaster, Haltech, AEM, Motec, MaxxECU, etc. |
| Transbrake         | Yes                                      |
| Virtual Clutch     | Yes                                      |
| Price              | ~€1,880 (~$2,000) with basic harness     |

**Why Turbolamik over MaxxECU:**

- Supports all 8HP generations (MaxxECU is Gen1 only)
- Works standalone with Cummins ECM (no torque reduction dependency)
- Proven ECUMaster CAN integration (compatible with PMU24)
- 10+ years development, not beta

## Electrical Requirements

### Power

| Circuit            | Wire Gauge | Source   | Destination                  | Notes                           |
| :----------------- | :--------- | :------- | :--------------------------- | :------------------------------ |
| TCU Power          | 14 AWG     | PMU OUT16 | Turbolamik harness (1.8m)   | 15A, CONSTANT (must stay on)    |
| TCU Ignition       | 18 AWG     | Ignition bus | Turbolamik harness        | Wake-up signal                  |
| TCU Ground         | 14 AWG     | Engine bay ground bus | Turbolamik harness | 700mm lead from harness         |

**Note:** TCU power must remain active at all times - if power is cut before TCU goes to sleep, adaptations won't save.

### CAN Bus Integration

| Connection         | Wire Gauge | Source              | Destination         | Notes                    |
| :----------------- | :--------- | :------------------ | :------------------ | :----------------------- |
| CAN H              | 20 AWG     | Turbolamik harness  | Cummins J1939 tap   | Twisted pair with CAN L  |
| CAN L              | 20 AWG     | Turbolamik harness  | Cummins J1939 tap   | Twisted pair with CAN H  |

The Turbolamik communicates with the Cummins R2.8 ECM via J1939 CAN for:

- Engine RPM
- Throttle position
- Vehicle speed

**CAN Tap Location:** Same tap point as PMU24 and Dakota Digital (Cummins body harness)

### Sensors & Inputs

| Sensor/Input          | Type                  | Notes                         |
| :-------------------- | :-------------------- | :---------------------------- |
| Input Speed Sensor    | Internal to trans     | Hall effect                   |
| Output Speed Sensor   | Internal to trans     | Hall effect                   |
| Transmission Temp     | Internal to trans     | NTC thermistor                |
| Range Sensor (BTSI)   | Internal to trans     | Gear position                 |
| Shifter Input         | Electronic shifter    | Kilduff (factory 8HP70 connector) |
| Brake Switch          | Digital input         | Unlock from Park              |

### Aux Outputs (TCU → Vehicle)

| Output            | Function                          | Destination                              | Notes                                              |
| :---------------- | :-------------------------------- | :--------------------------------------- | :------------------------------------------------- |
| Aux Out (Reverse) | 12V when shifter in R             | [PMU In 3][pmu-inputs]                   | Drives PMU OUT22 (Reverse Lights)                  |
| Aux Out (P/N)     | 12V when shifter in P or N        | **\[Reserve\]**                          | Not currently consumed; PBS-I handles brake interlock for cranking. Available for future P/N gating if needed. |
| J1939 broadcast   | Gear position, trans temp, mode   | [BIM-01-2 J1939][bim-j1939] → HDX GEAR   | Shares Cummins J1939 bus                           |

### Shifter

/// html | div.product-info

**Model:** Kilduff 8HP70 / 8 Speed ZF Shifter for Swaps

**Finish:** Red with Skulls

**Product Page:** [Kilduff 8HP70 Shifter][kilduff-shifter]

///

| Specification | Value                     |
| :------------ | :------------------------ |
| Dimensions    | 10" L × 4.5" W × 5" H     |
| Handle Height | 11" (tallest)             |
| Type          | Electronic (no cables)    |
| Positions     | P-R-N-D, +/- manual       |
| Connection    | Factory 8HP70 connector   |
| Mounting      | Center console            |

**Manual Mode (+/-):** Allows manual gear selection for rock crawling, engine braking on descents, and technical terrain.

**Wiring:** Electronic shifter connects directly to transmission controller. No shift cables required.

### Drive Mode Switch

| Specification | Value                              |
| :------------ | :--------------------------------- |
| Type          | Rocker switch (SPDT or 3-position) |
| Location      | Dash rocker switch panel           |
| Connection    | Transmission controller mode input |

| Position | Mode     | Use Case                          |
| :------- | :------- | :-------------------------------- |
| Up       | Sport    | Higher shift points, firmer shifts |
| Center   | Normal   | Daily driving, highway            |
| Down     | Tow/Haul | Engine braking, grades, towing    |

**Wiring:** Low-current signal wires from rocker switch to transmission controller mode input pins. Exact pinout depends on controller selection (Compushift vs US Shift).

## Cooling

| Component          | Notes                                   |
| :----------------- | :-------------------------------------- |
| Trans Cooler       | External cooler recommended             |
| Cooler Lines       | -6 AN or factory hard lines             |
| Thermostat         | 180°F bypass thermostat recommended     |

## Adapter & Bellhousing

| Component          | Source/Part Number | Notes                            |
| :----------------- | :----------------- | :------------------------------- |
| Adapter Kit        | Custom             | R2.8 to 8HP70 (in progress)      |
| Flexplate          | Adapted from AX15 kit | R2.8 to 8HP70 (custom adapter) |
| Pilot Bearing      | TBD                | If required                      |

## Outstanding Items

- [ ] Order Turbolamik TCU 2.0 with basic wiring harness
- [ ] Install Turbolamik TCU on 8HP70 mechatronic (soldering required)
- [ ] Route TCU power from PMU OUT16 (14 AWG, CONSTANT)
- [ ] Connect TCU CAN to J1939 bus (same tap as PMU/Dakota Digital)
- [ ] Install Kilduff shifter in center console
- [ ] Wire drive mode rocker switch (dash panel) to TCU mode inputs
- [ ] Complete custom adapter kit for R2.8 to 8HP70
- [ ] Complete flexplate adaptation from AX15 kit
- [ ] Determine transmission cooler size and routing

## Related Documentation

- [Transfer Case][transfer-case] - NV241 GenII connection
- [PMU Inputs][pmu-inputs] - J1939 CAN bus tap
- [Cummins R2.8][engine] - Engine CAN integration

[transfer-case]: 02-transfer-case.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[engine]: ../02-engine-systems/index.md
[starter]: ../02-engine-systems/01-starter.md
[bim-j1939]: ../02-engine-systems/09-gauge-cluster/03-bim-j1939.md
[kilduff-shifter]: https://www.kilduffmachine.com/store/p168/Kilduff_8PH70_%2F_8_speed_ZF_Shifter_for_swaps_%23KIL8HP70.html
[turbolamik]: https://www.turbolamik.us/tcu-2-0-turbolamik/
[turbolamik-manual]: https://manual.turbolamik.eu/
