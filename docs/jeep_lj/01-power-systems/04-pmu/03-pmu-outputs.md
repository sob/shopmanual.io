---
hide:
  - toc
---

# 1.4.3 PMU Outputs {#pmu-outputs}

Complete configuration of all 24 PMU outputs, load allocations, and combined output configurations.

## PMU24 Output Configuration {#pmu-output-wiring-diagram}

### 25A High-Side Outputs (OUT1–OUT5, OUT12–OUT16)

2.8 mm terminals (12 AWG for a 25 A load); OUT1 and OUT16 carry high-power flyback diodes, so they take the two fans.[^pmu-pinout] Rows: pins 1–13 top, 14–26 middle, 27–39 bottom.

| Output     | Pin | Circuit                      | Load                 | Ground                                                | Control Type       | Notes                          |
| :--------- | :-: | :--------------------------- | :------------------- | :---------------------------------------------------- | :----------------- | :----------------------------- |
| **Out 1**  | 38  | Oil Cooler Fan               | ~15A                 | [Engine Bay Bus][engine-ground] Stud 8                | Auto (CAN temp)    | SPN 175 oil temp trigger; 12 AWG; flyback output — was Out 7 (2026-10-17) |
| **Out 2**  | 39  | **[Available]**             | -                    | -                                                     | -                  | Freed — radiator fan relocated to [START+ Forward Bus][start-fwd-bus] |
| **Out 3**  | 26  | Dakota Digital HDX System    | ~12A typ / 25A worst | [Firewall Stud Bus][firewall-ground] T4-5             | On while PMU on (ignition, plus Delayed turn off window) | Cluster + 4 BIM modules (bus-powered via the BIM/IO cable); 12 AWG — was Out 9, a 15 A output (2026-10-17) |
| **Out 4**  | 13  | **[Available]**             | -                    | -                                                     | -                  | Freed — radiator fan relocated; left free beside Out 5 |
| **Out 5**  | 12  | HVAC Blower Motor            | ~20A                 | Restomod Air kit ground (verify on arrival)           | Auto (ignition ON) | Restomod Air kit blower; draw verification {{ tbd(146) }} — see [HVAC System][hvac-system] |
| **Out 12** | 2   | Parking / Tail Markers       | ~2A                  | [SwitchPros Ground Bus][switchpros-ground] T5          | Auto: with headlights (In 7 OR In 5), ignition-independent | Maxbilt RED + RTL-S running + license-plate lamp; also feeds the SwitchPros LIGHTS input — see [DRL & Parking][drl-parking-lights] |
| **Out 13** | 1   | **[Available]**             | -                    | -                                                     | -                  | Freed — CT4 moved to the [START+ Forward Bus][start-fwd-bus] so hazards work with the PMU off (2026-10-17) |
| **Out 14** | 14  | Garmin Tread 2 GPS           | ~2A                  | Chassis, local to the dash mount                      | Auto (ignition ON) | Moved off SwitchPros button 8 (2026-09-24); 16 AWG pigtail at the PMU connector; HDP24 pin 21 — see [Navigation][navigation] |
| **Out 15** | 27  | Turbolamik TCU               | 15A continuous       | [Engine Bay Bus][engine-ground] via TCU harness       | On while PMU on; kept alive after key-off by Delayed turn off | 12 AWG; Delayed turn off maximum = TCU sleep time {{ tbd(332) }}; moved back from the START+ Forward Bus (2026-10-17) — see [Transmission][transmission] |
| **Out 16** | 28  | PS Cooler Fan                | ~15A                 | [Engine Bay Bus][engine-ground] Stud 8                | 180°F inline thermostat | Mishimoto PS cooler fan; thermostat-switched on PS fluid temp (not engine coolant); 12 AWG; flyback output — was Out 8 (2026-10-17) |

### 15A High-Side Outputs (OUT6–OUT11)

1.5 mm terminals (14 AWG for a 15 A load); OUT8 has wiper-motor braking.[^pmu-pinout]

| Output     | Pin | Circuit                   | Load | Ground                                                | Control Type         | Notes                                         |
| :--------- | :-: | :------------------------ | :--- | :---------------------------------------------------- | :------------------- | :-------------------------------------------- |
| **Out 6**  | 11  | GMRS Radio (Rugged G1)    | 15A  | [Direct START battery-][starter-battery-distribution] | On while PMU on (ignition, plus Delayed turn off window) | RF noise isolation |
| **Out 7**  | 10  | **[Available]**           | -    | -                                                     | -                    | Freed — oil cooler fan moved to Out 1 (2026-10-17) |
| **Out 8**  | 9   | **[Available]**           | -    | -                                                     | -                    | Freed — PS cooler fan moved to Out 16 (2026-10-17); wiper-motor braking output |
| **Out 9**  | 5   | **[Available]**           | -    | -                                                     | -                    | Freed — Dakota Digital moved to Out 3 (2026-10-17) |
| **Out 10** | 4   | **[Available]**           | -    | -                                                     | -                    | Freed — iBooster relocated to [START+ Forward Bus][start-fwd-bus] |
| **Out 11** | 3   | WS-51C Wiper Controller   | 15A  | [Firewall Stud Bus][firewall-ground] T2               | Auto (ignition ON)   | See [Wipers][windshield-wiper-control-system] |

### 7A High-Side Outputs (OUT17–OUT24)

**Note:** OUT17-24 are dual-purpose - configurable as 7A outputs OR 0-20V analog inputs (A9–A16).[^pmu-pinout] See [PMU Inputs][pmu-inputs] for analog input configuration.

| Output     | Pin | Circuit                  | Load | Ground                                                | Control Type        | Notes                          |
| :--------- | :-: | :----------------------- | :--- | :---------------------------------------------------- | :------------------ | :----------------------------- |
| **Out 17** | 6   | A/C Clutch               | 3-5A | Compressor clutch ground (Restomod Air kit — verify)  | Auto (A/C request)  | Request via Restomod Air control head → trinary → In 9 — see [HVAC System][hvac-system] |
| **Out 18** | 33  | Horn                     | 5.4A | [Engine Bay Bus][engine-ground] Stud 6                | External input      | CT4 kit horn ({{ tbd(326) }})  |
| **Out 19** | 20  | 4x4 Indicator Relay      | <0.2A | Relay coil → [Firewall Stud Bus][firewall-ground]    | Auto (An 1 position) | Coil only; contacts ground the HDX 4x4 input (PMU is high-side). Active in 4H or 4L — see [Transfer Case][transfer-case] |
| **Out 20** | 34  | STX Intercom             | ~5A  | [Direct START battery-][starter-battery-distribution] | Auto (ignition ON)  | RF noise isolation             |
| **Out 21** | 21  | Brake Lights             | ~3A  | [SwitchPros Ground Bus][switchpros-ground]            | External input      | Shared tail light ground       |
| **Out 22** | 8   | Reverse Lights           | ~5A  | [SwitchPros Ground Bus][switchpros-ground]            | External input      | Maxbilt + Squadron Sport       |
| **Out 23** | 35  | LP6 DRL                  | 0.8A | LP6 ground (Pin 2)                                    | Auto (ignition; off with headlights) | Tail markers moved to Out 12 (2026-09-22) — see [DRL & Parking][drl-parking-lights] |
| **Out 24** | 22  | 4LO Indicator            | <0.1A | n/a (signal into HDX EXTRA(+))                       | Auto (An 1 position) | 12V direct to HDX EXTRA(+), label "4LO". Active in 4L only — see [Transfer Case][transfer-case] |

No PMU output is CONSTANT: the PMU switches off when Pin 7 (ignition) drops, apart from the Delayed turn off window used for the TCU.[^pmu-manual] Loads that must work with the key off (CT4 hazards, PBS-I) are fed from the [START+ Forward Bus][start-fwd-bus] instead.

## Combined Outputs

_The radiator fan (formerly OUT2+3+4) and iBooster main (formerly OUT1+10) were relocated to the [START+ Forward Distribution Bus][start-fwd-bus]. No PMU outputs are currently combined; OUT2, OUT4 and OUT13 (25 A) and OUT7–OUT10 (15 A) are free (7 spare outputs; the 7 A bank is full). The combining rules below are retained for any future high-current output._

**Combining Rules:**

- Only same-rated outputs can be combined (25A + 25A ✓, 25A + 15A ✗)
- **Outputs do NOT need to be adjacent** - combine via external wiring at load
- **Thermal limits:** Two adjacent 2.8mm terminals = 38A max @ 23°C, 32A @ 40°C for continuous loads
- **Non-adjacent terminals:** Each rated 23A @ 40°C individually = 46A combined capacity (much better thermal performance)
- **Brief peak loads:** Thermal derating less critical for loads <5 seconds (e.g., brake booster)
- **Load balancing:** Avoid placing heavily loaded outputs adjacent to each other - use non-adjacent combining for high-current loads

## Thermal Analysis

**High-Current Outputs (Thermal Concerns):**

| Outputs     | Load                      | Terminal Rating                          | Utilization @ 40°C            | Status      | Notes                                                                     |
| :---------- | :------------------------ | :--------------------------------------- | :---------------------------- | :---------- | :------------------------------------------------------------------------ |
| **OUT5**    | 20A continuous            | 23A (2.8 mm, single @ 40°C)[^pmu-manual] | 87%                           | ✓ OK        | HVAC blower (pin 12) - largest continuous PMU load; OUT4 (pin 13) left free beside it |
| **OUT1**    | 15A intermittent          | 23A (2.8 mm @ 40°C)                      | 65%                           | ✓ OK        | Oil cooler fan (pin 38, bottom row) - not adjacent to OUT16 or OUT5       |
| **OUT16**   | 15A intermittent          | 23A (2.8 mm @ 40°C)                      | 65%                           | ✓ OK        | PS cooler fan (pin 28) - adjacent to OUT15 (TCU); fan is thermostat-switched, so the pair is not 30A continuous |
| **OUT15**   | 15A continuous            | 23A (2.8 mm @ 40°C)                      | 65%                           | ✓ OK        | TCU (pin 27) - sits beside OUT16 (fan B, intermittent); next closest continuous load is OUT3 (pin 26, middle row) |
| **OUT3**    | ~12A typ / 25A worst      | 23A (2.8 mm @ 40°C)                      | 52% typ                       | ✓ OK        | Dakota HDX (pin 26) - 25A is the fuse-sizing ceiling, not a measured draw |
| **OUT11**   | 15A continuous            | 19A (1.5 mm terminal)[^pmu-manual]       | 79%                           | ✓ OK        | Wiper controller (pin 3) - OUT12 beside it is ~2A                         |

**Installation Notes:**

- PMU thermal protection will shut down overloaded outputs
- Monitor output temperatures during initial testing (PMU displays thermal status)
- **Non-adjacent combining recommended** for all high-current loads (>30A) to maximize thermal margin
- **Continuous loads** (HVAC, fans) require more conservative thermal margins than brief peaks

**Grounding Architecture:**

- **PMU uses high-side outputs** (switches positive power to loads)
- **Each load grounds separately** (chassis ground, battery ground, or ground bus)
- **Pin 25 is reference ground ONLY** (<100mA logic/CAN reference) - 12 AWG to [Engine Bay Ground Bus][grounding] stud 5, as short as possible
- **Output current does NOT return through Pin 25** - returns through individual load grounds
- See [Grounding Architecture][grounding] for load ground connections

[grounding]: ../05-grounding/index.md

## Related Documentation

- [PMU Overview][pmu-overview] - Product specifications and capacity
- [PMU Inputs][pmu-inputs] - Input configuration and triggers
- [PMU Programming][pmu-programming] - Logic configuration for outputs
- [START battery Distribution][starter-battery-distribution] - PMU power source and MRBF terminal fuse

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
[transfer-case]: ../../10-drivetrain/02-transfer-case.md#position-sensing
[navigation]: ../../07-communication-systems/05-navigation.md
[transmission]: ../../10-drivetrain/01-transmission.md

[^pmu-pinout]: ECUMaster, *PMU-24 DL Pinout v1.1* (2023-10-06): battery stud "Maximum constant current: 150 A"; O1–O5, O12–O16 25 A; O6–O11 15 A; O17–O24 7 A; terminals 211CC2S2160P 13–17 AWG, 211CC3S2120 14–16 AWG, 211CC3S3120 10–12 AWG. https://www.ecumaster.com/files/PMU/PMU-24_Pinout_v1.1.pdf (accessed 2026-10-17).
[^pmu-manual]: ECUMaster, *PMU User Manual* 122.3.1 (2026-09-21): §2.13 connector current capacity (2.8 mm terminal 25 A @ 23°C with 12 AWG, 23 A @ 40°C, two adjacent 38 A; 1.5 mm terminal 19 A @ 23°C with 14 AWG); §16.7 Delayed turn off ("By default, the PMU switches off immediately when the ignition is switched off"); wire table p.137. https://www.ecumaster.com/files/PMU/PMU_Manual.pdf (accessed 2026-10-17).

