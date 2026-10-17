---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - pmu
  - controller
---

# 1.4.1 PMU Overview {#pmu-overview}

/// html | div.product-info
![ECUMaster PMU24 DL](../../images/ecumaster-pmu24.png){ loading=lazy }

**Type:** Programmable Power Management Unit with Data Logging

**Model:** ECUMaster PMU24 DL

**Manufacturer:** ECUMaster

**Product Page:** [ECUMaster PMU24 DL][ecumaster-pmu24]

**Installation Manual:** [PMU User Manual v101.1.5 (PDF)][pmu-manual]

**Pinout Diagram:** [PMU-24 Pinout v1.1 (PDF)][pmu-pinout]

**Wiring Diagram:** See Installation Manual (pinout diagrams for PMU24)

///

## Specifications

**Outputs:**

- 24 programmable high-side outputs: 10×25A (OUT1–5, OUT12–16; 2.8 mm terminals), 6×15A (OUT6–11; 1.5 mm terminals), 8×7A (OUT17–24)[^pmu-pinout]
- **Total capacity:** 150A max constant at the battery stud (power supply limited, not sum of outputs)[^pmu-pinout]
- **Constraint:** Only same-rated outputs can be combined (e.g., 25A + 25A ✓, 25A + 15A ✗)
- **Out 17-24:** Dual-purpose - configurable as 7A outputs OR 0-20V analog inputs

**Key Features:**

- Dedicated 12V switched input (Pin 7), up to 16 analog inputs, 9 digital inputs
- 256MB data logger (500 Hz), real-time clock, IMU, inertia switch
- 2× CAN 2.0 A/B (J1939 compatible), 24× tricolor LED indicators
- PC config via USB ([USB to CAN adapter][usb-to-can] required)

**Physical:** 131×112×33mm, 385g, -40°C to +125°C operating range

**Grounding Note:** PMU is **high-side switching only** - it switches the positive wire to loads. Each load must have its own ground path back to the battery/chassis. The PMU's ground connection (12 AWG from connector pin 25, 2.8 mm terminal 211CC3S3120, to Engine Bay Ground Bus stud 5, as short as possible) is only for internal electronics reference, not load current return. This is why PMU doesn't require a heavy ground wire matching the 1 AWG power feed.

## Connector Terminals

Wire ranges for the PMU connector terminals and ECUMaster's wire table (5A → 18 AWG, 10A → 16, 15A → 14, 25A → 12):[^pmu-manual]

| Terminal | Part          | Wire range  | Rating                                                        | Used on              |
| :------- | :------------ | :---------- | :------------------------------------------------------------ | :------------------- |
| 1.5 mm   | 211CC2S2160P  | 14–17 AWG   | 19 A @ 23°C with 14 AWG                                       | OUT6–11, inputs, CAN, Pin 7 |
| 2.8 mm   | 211CC3S2120   | 14–16 AWG   | -                                                             | 25 A outputs, light loads |
| 2.8 mm   | 211CC3S3120   | 10–12 AWG   | 25 A @ 23°C with 12 AWG, 23 A @ 40°C; two adjacent = 38 A total | 25 A outputs, pin 25 ground |

**Pigtail rule:** any PMU connector wire under 16 AWG (GPS, 4x4 relay, 4LO, +12V sw Pin 7, inputs, CAN) gets a 16 AWG pigtail at the PMU connector — 18 AWG is below the terminal range.[^pmu-manual]

**Configuration Software:** [PMU Setup v101.2.1][pmu-setup] | **Full Specs:** [PMU Manual][pmu-manual]

## Capacity Analysis

| Outputs        |  Rating  | Total  |  Used  | Available |
| :------------- | :------: | :----: | :----: | :-------: |
| 1-5, 12-16     | 25A each |   10   |   7    |     3     |
| 6-11           | 15A each |   6    |   2    |     4     |
| 17-24          | 7A each  |   8    |   8    |     0     |
| **Total**      |    -     | **24** | **17** |  **7**    |

**Utilization:** 17 of 24 outputs used (71%). OUT15 freed when the winch trigger was reallocated to BODY PDU CB43 (2026-05-30); OUT19 and OUT24 taken by the 4x4/4LO indicators (2026-09-18); OUT12 taken by the parking/tail markers when they were split off the DRL circuit (2026-09-22); OUT14 taken by the Garmin GPS when it moved off the SwitchPros (2026-09-24). Re-mapped to the pinout's true ratings on 2026-10-17: fans to OUT1/OUT16 (25 A, flyback), Dakota Digital to OUT3 (25 A), TCU back onto OUT15 (25 A, kept alive by Delayed turn off), CT4 off the PMU to the START+ Forward Bus. The 7A bank (OUT17-24) is full — future low-current loads go on the 15A bank.

**Primary loads:** oil cooler fan (OUT1: ~15A), Dakota Digital HDX (OUT3: ~12A typ / 25A worst), HVAC (OUT5: ~20A load), GMRS radio (OUT6: ~15A load), wipers (OUT11: 15A), parking/tail markers (OUT12: ~2A), Garmin GPS (OUT14: ~2A), Turbolamik TCU (OUT15: 15A continuous), PS cooler fan (OUT16: ~15A), A/C clutch (OUT17: 7A), horn (OUT18: 7A), intercom (OUT20: 7A), brake lights (OUT21: 7A), reverse lights (OUT22: 7A), DRL (OUT23: 7A), 4x4 indicator relay (OUT19: <0.2A), 4LO indicator (OUT24: <0.1A). _Radiator fan (was OUT2+3+4), iBooster main + enable (was OUT1+10, OUT19) and the CT4 (was OUT13) are on the [START+ Forward Distribution Bus][start-fwd-bus]; the winch contactor trigger (was OUT15) went to BODY PDU CB43 — OUT2, 4, 13 (25 A) and OUT7–10 (15 A) are free._

**Load:** With the radiator fan, iBooster and CT4 on the START+ Forward Bus and the TCU back on OUT15, the PMU's theoretical all-on load is ~146A (all radios transmitting, both fans running), ~85-115A typical continuous — within the 150A stud limit.[^pmu-pinout] **7 of 24 outputs are unassigned.** The two indicator outputs are signal-level (<0.3A combined) and do not move the load figures.

**Mounting:** Engine bay, accessible for LED diagnostics and USB configuration

## Related Documentation

- [PMU Inputs][pmu-inputs] - Input configuration and CAN bus integration
- [PMU Outputs][pmu-outputs] - 24-output configuration and load details
- [PMU Programming][pmu-programming] - Logic examples and configuration
- [START battery Distribution][starter-battery-distribution] - PMU power source (1 AWG, ~7 ft) and 150A MRBF terminal fuse
- [Wire Distance Reference][wire-distance] - PMU to battery routing distance

[pmu-inputs]: 02-pmu-inputs.md
[pmu-outputs]: 03-pmu-outputs.md
[pmu-programming]: 04-pmu-programming.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[start-fwd-bus]: ../02-starter-battery-distribution/index.md#start-forward-bus
[wire-distance]: ../01-power-generation/05-wire-distance-reference.md
[ecumaster-pmu24]: https://www.ecumaster.com/products/pmu24/
[pmu-manual]: https://www.ecumaster.com/files/PMU/PMU_Manual.pdf
[pmu-pinout]: https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf
[usb-to-can]: https://www.ecumaster.com/products/usb-to-can/
[pmu-setup]: https://www.ecumaster.com/files/PMU/PMUSetup_101_2_1.exe

[^pmu-pinout]: ECUMaster, *PMU-24 DL Pinout v1.1* (2023-10-06): battery stud "Maximum constant current: 150 A"; O1–O5, O12–O16 25 A; O6–O11 15 A; O17–O24 7 A; terminals 211CC2S2160P 13–17 AWG, 211CC3S2120 14–16 AWG, 211CC3S3120 10–12 AWG. https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf (accessed 2026-10-17).
[^pmu-manual]: ECUMaster, *PMU User Manual* 122.3.1 (2026-09-21): §2.13 connector current capacity (2.8 mm terminal 25 A @ 23°C with 12 AWG, 23 A @ 40°C, two adjacent 38 A; 1.5 mm terminal 19 A @ 23°C with 14 AWG); §16.7 Delayed turn off ("By default, the PMU switches off immediately when the ignition is switched off"); wire table p.137. https://www.ecumaster.com/files/PMU/PMU_Manual.pdf (accessed 2026-10-17).
