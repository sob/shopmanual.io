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

- 24 programmable high-side outputs (10×25A, 6×15A, 8×7A)
- **Total capacity:** 170A continuous (power supply limited, not sum of outputs)
- **Constraint:** Only same-rated outputs can be combined (e.g., 25A + 25A ✓, 25A + 15A ✗)
- **Out 17-24:** Dual-purpose - configurable as 7A outputs OR 0-20V analog inputs

**Key Features:**

- Dedicated 12V switched input (Pin 7), up to 16 analog inputs, 9 digital inputs
- 256MB data logger (500 Hz), real-time clock, IMU, inertia switch
- 2× CAN 2.0 A/B (J1939 compatible), 24× tricolor LED indicators
- PC config via USB ([USB to CAN adapter][usb-to-can] required)

**Physical:** 131×112×33mm, 385g, -40°C to +125°C operating range

**Grounding Note:** PMU is **high-side switching only** - it switches the positive wire to loads. Each load must have its own ground path back to the battery/chassis. The PMU's ground connection (14 AWG) is only for internal electronics reference, not load current return. This is why PMU doesn't require a heavy ground wire matching the 2/0 AWG power feed.

**Configuration Software:** [PMU Setup v101.2.1][pmu-setup] | **Full Specs:** [PMU Manual][pmu-manual]

## Capacity Analysis

| Outputs   |  Rating  | Total  |  Used  | Available |
| :-------- | :------: | :----: | :----: | :-------: |
| 1-10      | 25A each |   10   |   5    |     5     |
| 11-16     | 15A each |   6    |   3    |     3     |
| 17-24     | 7A each  |   8    |   6    |     2     |
| **Total** |    -     | **24** | **14** |  **10**   |

**Utilization:** 14 of 24 outputs used (58%) — 7 freed by relocating the radiator fan, iBooster, and TCU

**Load:** With the radiator fan, iBooster, and TCU relocated to the START+ Forward Bus, PMU peak drops to ~145A theoretical (all radios transmitting), ~85-115A typical continuous — comfortably within the 300A PMU capacity, with 10 of 24 outputs now free.

**Mounting:** Engine bay, accessible for LED diagnostics and USB configuration

## Related Documentation

- [PMU Inputs][pmu-inputs] - Input configuration and CAN bus integration
- [PMU Outputs][pmu-outputs] - 24-output configuration and load details
- [PMU Programming][pmu-programming] - Logic examples and configuration
- [START battery Distribution][starter-battery-distribution] - PMU power source (2/0 AWG, 7 ft) and circuit breaker (250A)
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
