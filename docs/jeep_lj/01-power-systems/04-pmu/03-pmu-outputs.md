---
hide:
  - toc
---

# 1.4.3 PMU Outputs {#pmu-outputs}

Complete configuration of all 24 PMU outputs, load allocations, and combined output configurations.

## PMU24 Output Configuration {#pmu-output-wiring-diagram}

### 25A High-Side Outputs (OUT1-OUT10)

| Output     | Circuit                      | Load     | Ground                                                | Control Type       | Notes                          |
| :--------- | :--------------------------- | :------- | :---------------------------------------------------- | :----------------- | :----------------------------- |
| **Out 1**  | **iBooster Main (combined)** | Combined | [Engine Bay Bus][engine-ground] Stud 7                | CONSTANT           | Combined with OUT10, 40A peak  |
| **Out 2**  | **Radiator Fan (combined)**  | Combined | Fan housing → engine block                            | PWM (CAN temp)     | Combined with OUT3+4, 53A max  |
| **Out 3**  | **Radiator Fan (combined)**  | Combined | Fan housing → engine block                            | PWM (CAN temp)     | Combined with OUT2+4           |
| **Out 4**  | **Radiator Fan (combined)**  | Combined | Fan housing → engine block                            | PWM (CAN temp)     | Combined with OUT2+3           |
| **Out 5**  | HVAC Blower Motor            | ~20A     | Factory HVAC ground                                   | Auto (ignition ON) | See [HVAC System][hvac-system] |
| **Out 6**  | GMRS Radio (Midland G1)      | 15A      | [Direct START battery-][starter-battery-distribution] | CONSTANT           | RF noise isolation             |
| **Out 7**  | Oil Cooler Fan               | ~15A     | [Engine Bay Bus][engine-ground] Stud 8                | Auto (CAN temp)    | SPN 175 oil temp trigger       |
| **Out 8**  | PS Cooler Fan                | ~15A     | [Engine Bay Bus][engine-ground] Stud 8                | 180°F inline thermostat | Mishimoto PS cooler fan; thermostat-switched on PS fluid temp (not engine coolant) |
| **Out 9**  | Dakota Digital System        | ~25A     | [Firewall Stud Bus][firewall-ground] T4-5             | CONSTANT           | Cluster + 4 BIM modules        |
| **Out 10** | **iBooster Main (combined)** | Combined | [Engine Bay Bus][engine-ground] Stud 7                | CONSTANT           | Combined with OUT1             |

### 15A High-Side Outputs (OUT11-OUT16)

| Output     | Circuit                   | Load | Ground                                                | Control Type         | Notes                                         |
| :--------- | :------------------------ | :--- | :---------------------------------------------------- | :------------------- | :-------------------------------------------- |
| **Out 11** | WS-51C Wiper Controller   | 15A  | [Firewall Stud Bus][firewall-ground] T2               | Auto (ignition ON)   | See [Wipers][windshield-wiper-control-system] |
| **Out 12** | **[Available]**           | -    | -                                                     | -                    | Future expansion (15A)                        |
| **Out 13** | Command Touch CT4         | ~9A  | [Firewall Stud Bus][firewall-ground] T1               | CONSTANT             | Turn signals, headlights, hazards             |
| **Out 14** | **[Available]**           | -    | -                                                     | -                    | Future expansion (15A)                        |
| **Out 15** | Winch Contactor Trigger   | 1A   | Via winch contactor                                   | Manual (dash rocker) | Control signal only                           |
| **Out 16** | Turbolamik TCU            | 15A  | Engine bay ground bus                                 | CONSTANT             | 8HP70 transmission controller                 |

### 7A High-Side Outputs (OUT17-OUT24)

**Note:** OUT17-24 are dual-purpose - configurable as 7A outputs OR 0-20V analog inputs. See [PMU Inputs][pmu-inputs] for analog input configuration.

| Output     | Circuit                  | Load | Ground                                                | Control Type        | Notes                          |
| :--------- | :----------------------- | :--- | :---------------------------------------------------- | :------------------ | :----------------------------- |
| **Out 17** | A/C Clutch               | 3-5A | Factory A/C ground                                    | Auto (A/C request)  | See [HVAC System][hvac-system] |
| **Out 18** | Horn                     | 5.4A | [Engine Bay Bus][engine-ground] Stud 6                | External input      | PIAA horns (2.7A × 2)          |
| **Out 19** | iBooster Ignition Signal | ~5A  | [Engine Bay Bus][engine-ground] Stud 7                | Auto (ignition RUN) | Same ground as iBooster main   |
| **Out 20** | STX Intercom             | ~5A  | [Direct START battery-][starter-battery-distribution] | Auto (ignition ON)  | RF noise isolation             |
| **Out 21** | Brake Lights             | ~3A  | [SwitchPros Ground Bus][switchpros-ground]            | External input      | Shared tail light ground       |
| **Out 22** | Reverse Lights           | ~5A  | [SwitchPros Ground Bus][switchpros-ground]            | External input      | Maxbilt + Squadron Sport       |
| **Out 23** | DRL/Parking Lights       | ~2A  | [SwitchPros Ground Bus][switchpros-ground]            | Auto (ignition)     | See [DRL & Parking][drl-parking-lights] |
| **Out 24** | **[Available]**          | -    | -                                                     | -                   | Available for future expansion (7A)                                                                                                                          |

## Combined Outputs

**Radiator Fan (OUT2+3+4):** GM Camaro electric fan, 53A @ full speed, 3×25A outputs paralleled = 75A capacity, PWM variable speed control

**iBooster Main (OUT1+10):** Bosch Gen 2, 40A peak, 2×25A outputs paralleled (non-adjacent) = 46A @ 40°C capacity, CONSTANT power

**Combining Rules:**

- Only same-rated outputs can be combined (25A + 25A ✓, 25A + 15A ✗)
- **Outputs do NOT need to be adjacent** - combine via external wiring at load
- **Thermal limits:** Two adjacent 2.8mm terminals = 38A max @ 23°C, 32A @ 40°C for continuous loads
- **Non-adjacent terminals:** Each rated 23A @ 40°C individually = 46A combined capacity (much better thermal performance)
- **Brief peak loads:** Thermal derating less critical for loads <5 seconds (e.g., brake booster)
- **Load balancing:** Avoid placing heavily loaded outputs adjacent to each other - use non-adjacent combining for high-current loads
- Use proper terminal crimping and wire gauge to maximize current capacity

## Thermal Analysis

**High-Current Outputs (Thermal Concerns):**

| Outputs     | Load             | Terminal Rating                          | Utilization @ 40°C            | Status      | Notes                                                                     |
| :---------- | :--------------- | :--------------------------------------- | :---------------------------- | :---------- | :------------------------------------------------------------------------ |
| **OUT1+10** | 40A peak (brief) | 46A @ 40°C (non-adjacent)<br/>50A @ 23°C | 87% @ 40°C peak<br/>1% @ idle | ✓ EXCELLENT | iBooster - non-adjacent combining eliminates thermal concerns, 0.25A idle |
| **OUT5**    | 20A continuous   | 23A (single @ 40°C)                      | 87%                           | ✓ OK        | HVAC blower - relocated from OUT1, same thermal margin                    |
| **OUT11**   | 15A continuous   | 19A (1.5mm terminal)                     | 79%                           | ✓ OK        | Wiper controller - avoid adjacent high-current load on OUT12              |

**Installation Notes:**

- PMU thermal protection will shut down overloaded outputs
- Monitor output temperatures during initial testing (PMU displays thermal status)
- **iBooster thermal design:** Non-adjacent combining (OUT1+10) provides 46A @ 40°C capacity vs 40A peak load = 87% utilization ✓
- **Non-adjacent combining recommended** for all high-current loads (>30A) to maximize thermal margin
- **Continuous loads** (HVAC, fans) require more conservative thermal margins than brief peaks

!!! success "Thermal Analysis - iBooster Resolved"
**iBooster relocated from OUT5+6 (adjacent) to OUT1+10 (non-adjacent)** per ECUMaster PMU24 manual Section 2.13:

    - Non-adjacent 2.8mm terminals @ 40°C: 46A combined capacity (23A each)
    - iBooster 40A peak: 87% utilization ✓ Excellent thermal margin
    - Maximum physical separation eliminates adjacent terminal heating concerns
    - HVAC blower relocated to OUT5 (single output, 87% utilization, unchanged)

**Grounding Architecture:**

- **PMU uses high-side outputs** (switches positive power to loads)
- **Each load grounds separately** (chassis ground, battery ground, or ground bus)
- **Pin 25 is reference ground ONLY** (<100mA logic/CAN reference)
- **Output current does NOT return through Pin 25** - returns through individual load grounds
- See [Grounding Architecture][grounding] for load ground connections

[grounding]: ../05-grounding/index.md

## Related Documentation

- [PMU Overview][pmu-overview] - Product specifications and capacity
- [PMU Inputs][pmu-inputs] - Input configuration and triggers
- [PMU Programming][pmu-programming] - Logic configuration for outputs
- [START battery Distribution][starter-battery-distribution] - PMU power source and circuit breaker

[pmu-overview]: 01-pmu-overview.md
[pmu-inputs]: 02-pmu-inputs.md
[pmu-programming]: 04-pmu-programming.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[engine-ground]: ../05-grounding/01-engine-bay-ground-bus.md
[firewall-ground]: ../05-grounding/02-firewall-stud-bus.md
[switchpros-ground]: ../05-grounding/03-switchpros-ground-bus.md
[hvac-system]: ../../02-engine-systems/03-hvac.md
[windshield-wiper-control-system]: ../../02-engine-systems/04-wipers.md
[drl-parking-lights]: ../../03-lighting-systems/05-drl-parking.md
