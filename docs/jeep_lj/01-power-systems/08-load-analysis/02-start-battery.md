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
| OUT5             | HVAC Blower       |     10A |      20A | Continuous when on     | Speed-dependent       |
| OUT6             | GMRS Radio        |      1A |      15A | Brief TX bursts        | Standby vs transmit   |
| OUT7             | Oil Cooler Fan    |      0A |      15A | Temp-triggered         | Off unless hot        |
| OUT8             | PS Cooler Fan     |      0A |      15A | Temp-triggered         | Off unless hot        |
| OUT9             | Dakota Digital    |     25A |      25A | Continuous             | Gauges always on      |
| OUT11            | Wiper Controller  |      0A |      15A | Intermittent           | Rain only             |
| OUT13            | CT4 Controller    |     10A |      10A | Continuous             | Street lighting       |
| OUT17            | A/C Clutch        |      0A |       5A | Summer only            | Seasonal              |
| OUT18            | Horn              |      0A |     5.4A | Seconds                | Emergency only        |
| OUT20            | STX Intercom      |      1A |       5A | Brief TX bursts        | Standby vs transmit   |
| OUT21            | Brake Lights      |      0A |       3A | Seconds during braking | Traffic-dependent     |
| OUT22            | Reverse Lights    |      0A |       3A | Seconds in reverse     | Parking only          |
| OUT23            | DRL               |    2.6A |     2.6A | Daytime only           | Auto-off at night     |
| **Fwd Dist Bus (START-direct)** | |       |          |                        | relocated off the PMU |
| Fwd Bus          | iBooster main     |   0.25A |      40A | Seconds during braking | Brief peak            |
| Fwd Bus          | Radiator Fan      |     20A |      53A | Variable (own controller) | Controller {{ tbd(134) }} |
| Fwd Bus          | Turbolamik TCU    |     15A |      15A | Continuous             | Must stay on          |
| Ign bus          | iBooster Enable   |      5A |       5A | Continuous             | Ignition-switched     |
| **BCDC Charger** |                   |         |          |                        |                       |
| -                | BCDC to AUX       |     30A |      50A | Continuous             | Charges AUX battery   |
| **Direct Loads** |                   |         |          |                        |                       |
| -                | Starter           |      0A | 400-600A | 3-5 seconds            | Cranking only         |
| -                | ECM               |     ~2A |      ~5A | Continuous             | Engine management     |
| -                | Grid Heater       |      0A |     250A | 3-5 seconds            | Cold start only       |

!!! info "Forward Distribution Bus relocation — totals unchanged"
    The radiator fan, iBooster, and TCU now feed START-direct via the [Forward Distribution Bus][start-fwd-bus] instead of the PMU. Because they were *already* powered by the START battery through the PMU, the battery and alternator totals are unchanged — only the distribution path moved. The TCU (~15A continuous) is now itemized separately; folding it into the scenarios below raises the worst realistic case from 201A to ~216A (80% of the 270A alternator) — still within margin.

## Scenario Analysis

### Scenario 1: Daily Highway Driving

**Conditions:** Highway cruising, moderate temps (70°F), radio on standby, climate control on

| Circuit                       |      Load | Reason                      |
| :---------------------------- | --------: | :-------------------------- |
| **iBooster (Fwd Bus)**        | **0.25A** | Idle - no braking           |
| **Radiator Fan (Fwd Bus)**   |   **16A** | Low speed - highway airflow |
| **HVAC Blower (OUT5)**        |   **10A** | Medium speed                |
| **GMRS Radio (OUT6)**         |    **1A** | Standby                     |
| Oil Cooler Fan (OUT7)         |        0A | Temp normal                 |
| PS Cooler Fan (OUT8)          |        0A | Temp normal                 |
| **Dakota Digital (OUT9)**     |   **25A** | Always on                   |
| Wiper (OUT11)                 |        0A | Dry weather                 |
| **CT4 (OUT13)**               |   **10A** | Running lights              |
| **iBooster Enable (ign bus)** |    **5A** | Always on                   |
| **STX Intercom (OUT20)**      |    **1A** | Standby                     |
| **DRL (OUT23)**               |    **2.6A** | Daytime                     |
| **BCDC Charger**              |   **30A** | Maintaining AUX             |
| **TOTAL**                     |  **101A** |                             |

**Alternator Load:** 101A of 270A capacity = **37% utilization** Excellent

---

### Scenario 2: Hot Day City Driving (Stop-and-Go)

**Conditions:** City traffic, hot day (95°F), A/C on, frequent braking

| Circuit                       |     Load | Reason                       |
| :---------------------------- | -------: | :--------------------------- |
| **iBooster (Fwd Bus)**        |   **5A** | Average - frequent braking   |
| **Radiator Fan (Fwd Bus)**   |  **42A** | High speed - no airflow, hot |
| **HVAC Blower (OUT5)**        |  **20A** | Max speed for A/C            |
| **GMRS Radio (OUT6)**         |   **1A** | Standby                      |
| **Oil Cooler Fan (OUT7)**     |  **15A** | Hot - active                 |
| **PS Cooler Fan (OUT8)**      |  **15A** | Hot - active                 |
| **Dakota Digital (OUT9)**     |  **25A** | Always on                    |
| Wiper (OUT11)                 |       0A | Dry weather                  |
| **CT4 (OUT13)**               |  **10A** | Running lights               |
| **A/C Clutch (OUT17)**        |   **5A** | A/C on                       |
| **iBooster Enable (ign bus)** |   **5A** | Always on                    |
| **STX Intercom (OUT20)**      |   **1A** | Standby                      |
| **Brake Lights (OUT21)**      |   **1A** | Average - traffic            |
| **DRL (OUT23)**               |   **2.6A** | Daytime                      |
| **BCDC Charger**              |  **40A** | Higher rate                  |
| **TOTAL**                     | **188A** |                              |

**Alternator Load:** 188A of 270A capacity = **70% utilization** Good

---

### Scenario 3: Offroad Trail (Slow Speed, Hot Engine)

**Conditions:** Technical trail, slow speed (<10 mph), engine working hard, radio use

| Circuit                       |     Load | Reason                            |
| :---------------------------- | -------: | :-------------------------------- |
| **iBooster (Fwd Bus)**        |   **2A** | Occasional braking                |
| **Radiator Fan (Fwd Bus)**   |  **53A** | Max speed - no airflow            |
| **HVAC Blower (OUT5)**        |  **15A** | Moderate                          |
| **GMRS Radio (OUT6)**         |   **5A** | Occasional TX                     |
| **Oil Cooler Fan (OUT7)**     |  **15A** | Hot - active                      |
| **PS Cooler Fan (OUT8)**      |  **15A** | Hot - active                      |
| **Dakota Digital (OUT9)**     |  **25A** | Always on                         |
| Wiper (OUT11)                 |       0A | Dry                               |
| **CT4 (OUT13)**               |  **10A** | Running lights                    |
| **iBooster Enable (ign bus)** |   **5A** | Always on                         |
| **STX Intercom (OUT20)**      |   **3A** | Occasional TX                     |
| **DRL (OUT23)**               |   **2.6A** | Daytime                           |
| **BCDC Charger**              |  **50A** | Full rate - supporting SwitchPros |
| **TOTAL**                     | **201A** |                                   |

**Alternator Load:** 201A of 270A capacity = **74% utilization** Good

**Note:** Offroad lighting (SwitchPros) draws from AUX battery, not alternator.

---

### Scenario 4: Emergency Braking in Rain

**Conditions:** Highway, sudden hard braking, wipers on, headlights on

| Circuit                       |     Load | Reason                   |
| :---------------------------- | -------: | :----------------------- |
| **iBooster (Fwd Bus)**        |  **40A** | Peak braking assist      |
| **Radiator Fan (Fwd Bus)**   |  **20A** | Normal - highway airflow |
| **HVAC Blower (OUT5)**        |  **15A** | Defrost                  |
| **GMRS Radio (OUT6)**         |   **1A** | Standby                  |
| Oil Cooler Fan (OUT7)         |       0A | Temp normal              |
| PS Cooler Fan (OUT8)          |       0A | Temp normal              |
| **Dakota Digital (OUT9)**     |  **25A** | Always on                |
| **Wiper (OUT11)**             |  **15A** | High speed               |
| **CT4 (OUT13)**               |  **10A** | Headlights               |
| **iBooster Enable (ign bus)** |   **5A** | Always on                |
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
| **iBooster (Fwd Bus)**        | **0.25A** | Idle                  |
| **Radiator Fan (Fwd Bus)**   |   **35A** | Moderate - no airflow |
| **HVAC Blower (OUT5)**        |   **10A** | Comfortable           |
| **GMRS Radio (OUT6)**         |    **1A** | Standby               |
| Oil Cooler Fan (OUT7)         |        0A | Temp stable           |
| PS Cooler Fan (OUT8)          |        0A | Temp stable           |
| **Dakota Digital (OUT9)**     |   **25A** | Always on             |
| Wiper (OUT11)                 |        0A | Off                   |
| **CT4 (OUT13)**               |   **10A** | Parking lights        |
| **A/C Clutch (OUT17)**        |    **5A** | If summer             |
| **iBooster Enable (ign bus)** |    **5A** | Always on             |
| **STX Intercom (OUT20)**      |    **1A** | Standby               |
| DRL (OUT23)                   |        0A | Off - parked          |
| **BCDC Charger**              |   **30A** | Normal rate           |
| **TOTAL**                     |  **122A** |                       |

**Alternator Load:** 122A of 270A capacity = **45% utilization** Excellent

---

## Summary

| Scenario          | Total Load | Alternator | Utilization | Status    |
| :---------------- | :--------- | :--------- | :---------- | :-------- |
| Highway Driving   | 101A       | 270A       | 37%         | Excellent |
| Hot City Driving  | 188A       | 270A       | 70%         | Good      |
| Offroad Trail     | 201A       | 270A       | 74%         | Good      |
| Emergency Braking | 165A       | 270A       | 61%         | Excellent |
| Parked Idling     | 122A       | 270A       | 45%         | Excellent |

**Worst Realistic Case:** 201A (offroad with hot engine) = **69A margin** (74% utilization). Folding in the now-itemized TCU (~15A continuous) raises this to ~216A (54A margin) — still within capacity.

## Load Exclusions (Not Alternator Loads)

The following high-current loads are **NOT** supplied by the alternator:

| Load                     | Current   | Source        | Why Not Alternator        |
| :----------------------- | :-------- | :------------ | :------------------------ |
| SwitchPros (all outputs) | 127A max  | AUX battery   | BCDC-fed, isolated        |
| ARB Compressor           | 90A       | AUX battery   | Via SafetyHub on AUX      |
| Winch                    | 409A peak | AUX battery   | Direct connection         |
| BODY PDU circuits        | 54A max   | AUX battery   | CONSTANT bus fed          |
| Starter                  | 400-600A  | START battery | Cranking only, engine off |
| Grid Heater              | 250A      | START battery | 3-5 sec cold start only   |

**Architecture:** The dual battery system isolates high-current accessory loads (AUX battery) from engine/safety loads (START battery). The BCDC charger (50A max) is the only connection between batteries during normal operation.

## Key-Off Parasitic Budget (START Battery)

Loads on the **CONSTANT** (always-on) feed continue to draw with the ignition off. The BCDC isolates the AUX battery but does **not** offload the START side, so these draws come straight out of the 68 Ah Odyssey PC1500[^pc1500-cap] and set how long the vehicle can sit before cranking is at risk.

| Load | Source | Key-Off Draw | Notes |
| :--- | :----- | -----------: | :---- |
| PBS-I keyless module | Critical Cabin PDU (CONSTANT) | ~50 mA[^pbs-i-standby] | RFID auto-arm standby (arms 60 s after fob leaves range) |
| HDX + BIM cluster electronics | Critical Cabin PDU Slot 2 (CONSTANT) | not characterized | Dakota Digital keep-alive / sleep current — small, not yet measured |
| ECM keep-alive | START battery (direct) | not characterized | Cummins R2.8 ECM sleep current |

**Characterized draw:** ~50 mA (PBS-I) ≈ **1.2 Ah/day**.

**Time to 50% SOC** (34 Ah usable[^pc1500-cap]) from the PBS-I alone: **~28 days**. The uncharacterized cluster and ECM sleep draws shorten this, so treat ~28 days as a ceiling, not a guarantee.

**Recommendation:** No mitigation needed for daily/weekly use. For storage beyond ~3 weeks, use a battery maintainer or a START-side disconnect — the ~50 mA floor alone reaches 50% SOC in about a month, and the unmeasured loads only add to it.

## Related Documentation

- [Alternator Specifications][alternator] - 270A capacity details
- [PMU Outputs][pmu-outputs] - Individual circuit assignments
- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [AUX Battery Load Analysis][aux-load-analysis] - Companion analysis for AUX battery

[alternator]: ../01-power-generation/02-alternator.md
[start-fwd-bus]: ../02-starter-battery-distribution/index.md#start-forward-bus
[pmu-outputs]: ../04-pmu/03-pmu-outputs.md
[bcdc]: ../01-power-generation/03-bcdc.md
[aux-load-analysis]: 03-aux-battery.md
[keyless-ignition]: ../../05-control-interfaces/06-keyless-ignition.md

[^pc1500-cap]: Odyssey PC1500 capacity **68 Ah** (20-hr rate), 34 Ah usable at 50% DOD — see [Batteries][batteries] (Odyssey Extreme Series spec table, checked 2026-05-30).

[^pbs-i-standby]: PBS-I ~50 mA standby is an **engineering estimate, not vendor-confirmed** (Digital Guard Dawg PBS-I, [Keyless Ignition][keyless-ignition]). Carried into this budget rather than chasing a vendor figure: at 1.2 Ah/day it changes no wire gauge or part selection. Field-verify with a clamp meter on the RED feed at first power-up if a precise number is ever needed.

[batteries]: ../01-power-generation/01-batteries.md
