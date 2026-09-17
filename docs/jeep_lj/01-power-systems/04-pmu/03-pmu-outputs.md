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
| **Out 1**  | **[Available]**             | -        | -                                                     | -                  | Freed — iBooster relocated to [START+ Forward Bus][start-fwd-bus] |
| **Out 2**  | **[Available]**             | -        | -                                                     | -                  | Freed — radiator fan relocated to [START+ Forward Bus][start-fwd-bus] |
| **Out 3**  | **[Available]**             | -        | -                                                     | -                  | Freed — radiator fan relocated     |
| **Out 4**  | **[Available]**             | -        | -                                                     | -                  | Freed — radiator fan relocated     |
| **Out 5**  | HVAC Blower Motor            | ~20A     | Restomod Air kit ground (verify on arrival)           | Auto (ignition ON) | Restomod Air kit blower; draw verification {{ tbd(146) }} — see [HVAC System][hvac-system] |
| **Out 6**  | GMRS Radio (Midland G1)      | 15A      | [Direct START battery-][starter-battery-distribution] | CONSTANT           | RF noise isolation             |
| **Out 7**  | Oil Cooler Fan               | ~15A     | [Engine Bay Bus][engine-ground] Stud 8                | Auto (CAN temp)    | SPN 175 oil temp trigger       |
| **Out 8**  | PS Cooler Fan                | ~15A     | [Engine Bay Bus][engine-ground] Stud 8                | 180°F inline thermostat | Mishimoto PS cooler fan; thermostat-switched on PS fluid temp (not engine coolant) |
| **Out 9**  | Dakota Digital System        | ~25A     | [Firewall Stud Bus][firewall-ground] T4-5             | CONSTANT           | Cluster + 4 BIM modules; gauge power architecture (OUT9 vs Critical Cabin PDU) {{ tbd(144) }} |
| **Out 10** | **[Available]**             | -        | -                                                     | -                  | Freed — iBooster relocated to [START+ Forward Bus][start-fwd-bus] |

### 15A High-Side Outputs (OUT11-OUT16)

| Output     | Circuit                   | Load | Ground                                                | Control Type         | Notes                                         |
| :--------- | :------------------------ | :--- | :---------------------------------------------------- | :------------------- | :-------------------------------------------- |
| **Out 11** | WS-51C Wiper Controller   | 15A  | [Firewall Stud Bus][firewall-ground] T2               | Auto (ignition ON)   | See [Wipers][windshield-wiper-control-system] |
| **Out 12** | **[Available]**           | -    | -                                                     | -                    | Future expansion (15A)                        |
| **Out 13** | Command Touch CT4         | ~9A  | [Firewall Stud Bus][firewall-ground] T1               | CONSTANT             | Turn signals, headlights, hazards             |
| **Out 14** | **[Available]**           | -    | -                                                     | -                    | Future expansion (15A)                        |
| **Out 15** | **[Available]**           | -    | -                                                     | -                    | (Was Winch Contactor Trigger — reallocated 2026-05-30 to BODY PDU CB43) |
| **Out 16** | **[Available]**           | -    | -                                                     | -                    | Freed — TCU relocated to [START+ Forward Bus][start-fwd-bus] |

### 7A High-Side Outputs (OUT17-OUT24)

**Note:** OUT17-24 are dual-purpose - configurable as 7A outputs OR 0-20V analog inputs. See [PMU Inputs][pmu-inputs] for analog input configuration.

| Output     | Circuit                  | Load | Ground                                                | Control Type        | Notes                          |
| :--------- | :----------------------- | :--- | :---------------------------------------------------- | :------------------ | :----------------------------- |
| **Out 17** | A/C Clutch               | 3-5A | Compressor clutch ground (Restomod Air kit — verify)  | Auto (A/C request)  | Request via Restomod Air control head → trinary → In 9 — see [HVAC System][hvac-system] |
| **Out 18** | Horn                     | 5.4A | [Engine Bay Bus][engine-ground] Stud 6                | External input      | PIAA horns (2.7A × 2)          |
| **Out 19** | **[Available]**          | -    | -                                                     | -                   | Freed — iBooster enable now on ignition bus    |
| **Out 20** | STX Intercom             | ~5A  | [Direct START battery-][starter-battery-distribution] | Auto (ignition ON)  | RF noise isolation             |
| **Out 21** | Brake Lights             | ~3A  | [SwitchPros Ground Bus][switchpros-ground]            | External input      | Shared tail light ground       |
| **Out 22** | Reverse Lights           | ~5A  | [SwitchPros Ground Bus][switchpros-ground]            | External input      | Maxbilt + Squadron Sport       |
| **Out 23** | DRL/Parking Lights       | ~2.6A | [SwitchPros Ground Bus][switchpros-ground]           | Auto (ignition)     | See [DRL & Parking][drl-parking-lights] |
| **Out 24** | **[Available]**          | -    | -                                                     | -                   | Available for future expansion (7A)                                                                                                                          |

## Combined Outputs

_The radiator fan (formerly OUT2+3+4) and iBooster main (formerly OUT1+10) were relocated to the [START+ Forward Distribution Bus][start-fwd-bus]. No PMU outputs are currently combined; OUT1–4, OUT10, OUT15, OUT16, and OUT19 are now free (8 spare outputs). The combining rules below are retained for any future high-current output._

**Combining Rules:**

- Only same-rated outputs can be combined (25A + 25A ✓, 25A + 15A ✗)
- **Outputs do NOT need to be adjacent** - combine via external wiring at load
- **Thermal limits:** Two adjacent 2.8mm terminals = 38A max @ 23°C, 32A @ 40°C for continuous loads
- **Non-adjacent terminals:** Each rated 23A @ 40°C individually = 46A combined capacity (much better thermal performance)
- **Brief peak loads:** Thermal derating less critical for loads <5 seconds (e.g., brake booster)
- **Load balancing:** Avoid placing heavily loaded outputs adjacent to each other - use non-adjacent combining for high-current loads

## Thermal Analysis

**High-Current Outputs (Thermal Concerns):**

| Outputs     | Load             | Terminal Rating                          | Utilization @ 40°C            | Status      | Notes                                                                     |
| :---------- | :--------------- | :--------------------------------------- | :---------------------------- | :---------- | :------------------------------------------------------------------------ |
| **OUT5**    | 20A continuous   | 23A (single @ 40°C)                      | 87%                           | ✓ OK        | HVAC blower - now the largest continuous PMU load after fan/iBooster relocation |
| **OUT11**   | 15A continuous   | 19A (1.5mm terminal)                     | 79%                           | ✓ OK        | Wiper controller - avoid adjacent high-current load on OUT12              |

**Installation Notes:**

- PMU thermal protection will shut down overloaded outputs
- Monitor output temperatures during initial testing (PMU displays thermal status)
- **Non-adjacent combining recommended** for all high-current loads (>30A) to maximize thermal margin
- **Continuous loads** (HVAC, fans) require more conservative thermal margins than brief peaks

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
[start-fwd-bus]: ../02-starter-battery-distribution/index.md#start-forward-bus
[engine-ground]: ../05-grounding/01-engine-bay-ground-bus.md
[firewall-ground]: ../05-grounding/02-firewall-stud-bus.md
[switchpros-ground]: ../05-grounding/03-switchpros-ground-bus.md
[hvac-system]: ../../02-engine-systems/03-hvac.md
[windshield-wiper-control-system]: ../../02-engine-systems/04-wipers.md
[drl-parking-lights]: ../../03-lighting-systems/05-drl-parking.md
