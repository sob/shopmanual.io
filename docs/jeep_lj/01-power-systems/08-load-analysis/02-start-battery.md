---
hide:
  - toc
---

# 1.8.2 START Battery Load Analysis {#start-battery-load-analysis}

Scenario-based load analysis for START battery circuits (alternator-supplied).

## START Battery Circuit Summary

All circuits powered by START battery (alternator charging):

| Source           | Circuit           | Typical |     Peak | Duty Cycle             | Notes                 |
| :--------------- | :---------------- | ------: | -------: | :--------------------- | :-------------------- |
| **PMU Outputs**  |                   |         |          |                        |                       |
| OUT1+10          | iBooster          |   0.25A |      40A | Seconds during braking | Non-adjacent combined |
| OUT2+3+4         | Radiator Fan      |     20A |      53A | Variable PWM           | 3× combined outputs   |
| OUT5             | HVAC Blower       |     10A |      20A | Continuous when on     | Speed-dependent       |
| OUT6             | GMRS Radio        |      1A |      15A | Brief TX bursts        | Standby vs transmit   |
| OUT7             | Oil Cooler Fan    |      0A |      15A | Temp-triggered         | Off unless hot        |
| OUT8             | PS Cooler Fan     |      0A |      15A | Temp-triggered         | Off unless hot        |
| OUT9             | Dakota Digital    |     25A |      25A | Continuous             | Gauges always on      |
| OUT11            | Wiper Controller  |      0A |      15A | Intermittent           | Rain only             |
| OUT13            | CT4 Controller    |     10A |      10A | Continuous             | Street lighting       |
| OUT15            | Winch Trigger     |      0A |       1A | Recovery only          | Control signal only   |
| OUT17            | A/C Clutch        |      0A |       5A | Summer only            | Seasonal              |
| OUT18            | Horn              |      0A |     5.4A | Seconds                | Emergency only        |
| OUT19            | iBooster Ignition |      5A |       5A | Continuous             | Ignition signal       |
| OUT20            | STX Intercom      |      1A |       5A | Brief TX bursts        | Standby vs transmit   |
| OUT21            | Brake Lights      |      0A |       3A | Seconds during braking | Traffic-dependent     |
| OUT22            | Reverse Lights    |      0A |       3A | Seconds in reverse     | Parking only          |
| OUT23            | DRL               |      8A |       8A | Daytime only           | Auto-off at night     |
| **BCDC Charger** |                   |         |          |                        |                       |
| -                | BCDC to AUX       |     30A |      50A | Continuous             | Charges AUX battery   |
| **Direct Loads** |                   |         |          |                        |                       |
| -                | Starter           |      0A | 400-600A | 3-5 seconds            | Cranking only         |
| -                | ECM               |     ~2A |      ~5A | Continuous             | Engine management     |
| -                | Grid Heater       |      0A |     250A | 3-5 seconds            | Cold start only       |

## Scenario Analysis

### Scenario 1: Daily Highway Driving

**Conditions:** Highway cruising, moderate temps (70°F), radio on standby, climate control on

| Circuit                       |      Load | Reason                      |
| :---------------------------- | --------: | :-------------------------- |
| **iBooster (OUT1+10)**        | **0.25A** | Idle - no braking           |
| **Radiator Fan (OUT2+3+4)**   |   **16A** | Low speed - highway airflow |
| **HVAC Blower (OUT5)**        |   **10A** | Medium speed                |
| **GMRS Radio (OUT6)**         |    **1A** | Standby                     |
| Oil Cooler Fan (OUT7)         |        0A | Temp normal                 |
| PS Cooler Fan (OUT8)          |        0A | Temp normal                 |
| **Dakota Digital (OUT9)**     |   **25A** | Always on                   |
| Wiper (OUT11)                 |        0A | Dry weather                 |
| **CT4 (OUT13)**               |   **10A** | Running lights              |
| **iBooster Ignition (OUT19)** |    **5A** | Always on                   |
| **STX Intercom (OUT20)**      |    **1A** | Standby                     |
| **DRL (OUT23)**               |    **8A** | Daytime                     |
| **BCDC Charger**              |   **30A** | Maintaining AUX             |
| **TOTAL**                     |  **106A** |                             |

**Alternator Load:** 106A of 270A capacity = **39% utilization** Excellent

---

### Scenario 2: Hot Day City Driving (Stop-and-Go)

**Conditions:** City traffic, hot day (95°F), A/C on, frequent braking

| Circuit                       |     Load | Reason                       |
| :---------------------------- | -------: | :--------------------------- |
| **iBooster (OUT1+10)**        |   **5A** | Average - frequent braking   |
| **Radiator Fan (OUT2+3+4)**   |  **42A** | High speed - no airflow, hot |
| **HVAC Blower (OUT5)**        |  **20A** | Max speed for A/C            |
| **GMRS Radio (OUT6)**         |   **1A** | Standby                      |
| **Oil Cooler Fan (OUT7)**     |  **15A** | Hot - active                 |
| **PS Cooler Fan (OUT8)**      |  **15A** | Hot - active                 |
| **Dakota Digital (OUT9)**     |  **25A** | Always on                    |
| Wiper (OUT11)                 |       0A | Dry weather                  |
| **CT4 (OUT13)**               |  **10A** | Running lights               |
| **A/C Clutch (OUT17)**        |   **5A** | A/C on                       |
| **iBooster Ignition (OUT19)** |   **5A** | Always on                    |
| **STX Intercom (OUT20)**      |   **1A** | Standby                      |
| **Brake Lights (OUT21)**      |   **1A** | Average - traffic            |
| **DRL (OUT23)**               |   **8A** | Daytime                      |
| **BCDC Charger**              |  **40A** | Higher rate                  |
| **TOTAL**                     | **193A** |                              |

**Alternator Load:** 193A of 270A capacity = **71% utilization** Good

---

### Scenario 3: Offroad Trail (Slow Speed, Hot Engine)

**Conditions:** Technical trail, slow speed (<10 mph), engine working hard, radio use

| Circuit                       |     Load | Reason                            |
| :---------------------------- | -------: | :-------------------------------- |
| **iBooster (OUT1+10)**        |   **2A** | Occasional braking                |
| **Radiator Fan (OUT2+3+4)**   |  **53A** | Max speed - no airflow            |
| **HVAC Blower (OUT5)**        |  **15A** | Moderate                          |
| **GMRS Radio (OUT6)**         |   **5A** | Occasional TX                     |
| **Oil Cooler Fan (OUT7)**     |  **15A** | Hot - active                      |
| **PS Cooler Fan (OUT8)**      |  **15A** | Hot - active                      |
| **Dakota Digital (OUT9)**     |  **25A** | Always on                         |
| Wiper (OUT11)                 |       0A | Dry                               |
| **CT4 (OUT13)**               |  **10A** | Running lights                    |
| **iBooster Ignition (OUT19)** |   **5A** | Always on                         |
| **STX Intercom (OUT20)**      |   **3A** | Occasional TX                     |
| **DRL (OUT23)**               |   **8A** | Daytime                           |
| **BCDC Charger**              |  **50A** | Full rate - supporting SwitchPros |
| **TOTAL**                     | **206A** |                                   |

**Alternator Load:** 206A of 270A capacity = **76% utilization** Good

**Note:** Offroad lighting (SwitchPros) draws from AUX battery, not alternator.

---

### Scenario 4: Emergency Braking in Rain

**Conditions:** Highway, sudden hard braking, wipers on, headlights on

| Circuit                       |     Load | Reason                   |
| :---------------------------- | -------: | :----------------------- |
| **iBooster (OUT1+10)**        |  **40A** | Peak braking assist      |
| **Radiator Fan (OUT2+3+4)**   |  **20A** | Normal - highway airflow |
| **HVAC Blower (OUT5)**        |  **15A** | Defrost                  |
| **GMRS Radio (OUT6)**         |   **1A** | Standby                  |
| Oil Cooler Fan (OUT7)         |       0A | Temp normal              |
| PS Cooler Fan (OUT8)          |       0A | Temp normal              |
| **Dakota Digital (OUT9)**     |  **25A** | Always on                |
| **Wiper (OUT11)**             |  **15A** | High speed               |
| **CT4 (OUT13)**               |  **10A** | Headlights               |
| **iBooster Ignition (OUT19)** |   **5A** | Always on                |
| **STX Intercom (OUT20)**      |   **1A** | Standby                  |
| **Brake Lights (OUT21)**      |   **3A** | Braking                  |
| DRL (OUT23)                   |       0A | Off - headlights on      |
| **BCDC Charger**              |  **30A** | Normal rate              |
| **TOTAL**                     | **165A** |                          |

**Duration:** iBooster peak lasts 2-5 seconds only

**Alternator Load:** 165A of 270A capacity = **61% utilization** Excellent

---

### Scenario 5: Parked with Engine Idling (Engine Warm)

**Conditions:** Stationary, engine idling, waiting, moderate accessories

| Circuit                       |      Load | Reason                |
| :---------------------------- | --------: | :-------------------- |
| **iBooster (OUT1+10)**        | **0.25A** | Idle                  |
| **Radiator Fan (OUT2+3+4)**   |   **35A** | Moderate - no airflow |
| **HVAC Blower (OUT5)**        |   **10A** | Comfortable           |
| **GMRS Radio (OUT6)**         |    **1A** | Standby               |
| Oil Cooler Fan (OUT7)         |        0A | Temp stable           |
| PS Cooler Fan (OUT8)          |        0A | Temp stable           |
| **Dakota Digital (OUT9)**     |   **25A** | Always on             |
| Wiper (OUT11)                 |        0A | Off                   |
| **CT4 (OUT13)**               |   **10A** | Parking lights        |
| **A/C Clutch (OUT17)**        |    **5A** | If summer             |
| **iBooster Ignition (OUT19)** |    **5A** | Always on             |
| **STX Intercom (OUT20)**      |    **1A** | Standby               |
| DRL (OUT23)                   |        0A | Off - parked          |
| **BCDC Charger**              |   **30A** | Normal rate           |
| **TOTAL**                     |  **122A** |                       |

**Alternator Load:** 122A of 270A capacity = **45% utilization** Excellent

---

## Summary

| Scenario          | Total Load | Alternator | Utilization | Status    |
| :---------------- | :--------- | :--------- | :---------- | :-------- |
| Highway Driving   | 106A       | 270A       | 39%         | Excellent |
| Hot City Driving  | 193A       | 270A       | 71%         | Good      |
| Offroad Trail     | 206A       | 270A       | 76%         | Good      |
| Emergency Braking | 165A       | 270A       | 61%         | Excellent |
| Parked Idling     | 122A       | 270A       | 45%         | Excellent |

**Worst Realistic Case:** 206A (offroad with hot engine) = **64A margin**

**Key Insight:** All realistic scenarios stay well within alternator capacity. The 270A alternator provides adequate margin for all operating conditions.

## Load Exclusions (Not Alternator Loads)

The following high-current loads are **NOT** supplied by the alternator:

| Load                     | Current   | Source        | Why Not Alternator        |
| :----------------------- | :-------- | :------------ | :------------------------ |
| SwitchPros (all outputs) | 127A max  | AUX battery   | BCDC-fed, isolated        |
| ARB Compressor           | 90A       | AUX battery   | Via SafetyHub on AUX      |
| Winch                    | 400A peak | AUX battery   | Direct connection         |
| BODY PDU circuits        | 56A max   | AUX battery   | CONSTANT bus fed          |
| Starter                  | 400-600A  | START battery | Cranking only, engine off |
| Grid Heater              | 250A      | START battery | 3-5 sec cold start only   |

**Architecture:** The dual battery system isolates high-current accessory loads (AUX battery) from engine/safety loads (START battery). The BCDC charger (50A max) is the only connection between batteries during normal operation.

## Related Documentation

- [Alternator Specifications][alternator] - 270A capacity details
- [PMU Outputs][pmu-outputs] - Individual circuit assignments
- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [AUX Battery Load Analysis][aux-load-analysis] - Companion analysis for AUX battery

[alternator]: ../01-power-generation/02-alternator.md
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[bcdc]: ../01-power-generation/03-bcdc.md
[aux-load-analysis]: 03-aux-battery.md
