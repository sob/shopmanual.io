---
hide:
  - toc
---

# 1.8.3 AUX Battery Load Analysis {#aux-battery-load-analysis}

Scenario-based load analysis for AUX battery circuits (BCDC-charged at 50A max).

## AUX Battery Circuit Summary

All circuits powered by AUX battery (charged by BCDC at 50A max):

| Source                 | Circuit                  | Typical | Peak | Duty Cycle        | Notes                     |
| :--------------------- | :----------------------- | ------: | ---: | :---------------- | :------------------------ |
| **SwitchPros Outputs** |                          |         |      |                   |                           |
| OUTPUT-1               | Roof Lights (8x XL Sport)|      0A |  18A | Night offroad     | 2.2A per pod              |
| OUTPUT-2               | Ditch Lights (2x LP4 Pro)|      0A |   8A | Night offroad     | Driving pattern           |
| OUTPUT-3               | Fog Light (1x S8 10")    |      0A |   6A | Night/weather     | Amber wide cornering      |
| OUTPUT-4               | Dome Lights (4x Cyclone) |      0A |   2A | Doors open        | Manual + trigger          |
| OUTPUT-5               | Available                |      0A |   0A | —                 | Freed by roof consolidation |
| OUTPUT-6               | Rock Lights (6x Cyclone) |      0A |   3A | Night offroad     | Under vehicle             |
| OUTPUT-7               | Chase Light (RTL-S)      |      0A |   1A | Night offroad     | Amber chase only          |
| OUTPUT-8               | Available                |      0A |   0A | —                 | Footwell lights on MLC-RW |
| OUTPUT-10              | Rear Locker              |      0A |   2A | Technical terrain | Solenoid                  |
| OUTPUT-11              | Compressor Control       |      0A |  15A | Control signal    | To ARB                    |
| OUTPUT-12              | Rear Lights (2x S1 Pro)  |      0A |   5A | Night driving     | License plate             |
| OUTPUT-13              | Cargo Light              |      0A |   5A | Loading/unloading | Trigger-2                 |
| OUTPUT-17              | Front Locker             |      0A |   2A | Technical terrain | Low-side                  |
| **SafetyHub 150**      |                          |         |      |                   |                           |
| MIDI-1                 | ARB Compressor Motor 1   |      0A |  45A | Airing up         | Half of twin              |
| MIDI-2                 | ARB Compressor Motor 2   |      0A |  45A | Airing up         | Half of twin              |
| **BODY PDU**           |                          |         |      |                   |                           |
| CB30                   | Fusion Radio (memory)    |      1A |   1A | Continuous        | Clock/presets             |
| CB30                   | Fusion Radio (head unit) |      0A |  15A | Audio playing     | Ignition-triggered (consolidated on CB30) |
| CB48                   | USB Charging (2x 75W)    |      2A |  13A | Devices charging  | Always on                 |
| CB39                   | WolfBox Camera           |      2A |  10A | Continuous        | Dash + backup             |
| CB45                   | Driver Heated Seat       |      0A |   5A | Winter            | Relay K21                 |
| CB42                   | Passenger Heated Seat    |      0A |   5A | Winter            | Relay K22                 |
| CB43                   | Winch Control (dash)     |      0A |   2A | Recovery only     | Rocker signal             |
| **Direct**             |                          |         |      |                   |                           |
| -                      | Winch Motor              |      0A | 409A | 10-30 sec bursts  | Recovery only             |

## Charging Source

**BCDC Alpha 50:** Charges AUX battery at up to 50A from START battery/alternator

- **Solar input:** Up to ~5.8A additional, battery-side (80W panel; see [Solar Charging][solar])
- **Combined max:** ~56A charging rate (sunny day, engine running)
- **Typical charging:** 30-50A depending on AUX battery SOC

**AUX Battery:** Dakota Lithium DL+ 135Ah LiFePO4

- **Capacity:** 135Ah nominal
- **Usable capacity:** 108Ah (80% DOD safe for LiFePO4)
- **Heated BMS:** Enables charging down to -4°F (critical for rear wheel well mount)
- **Recovery rate:** At 50A charging, recovers 108Ah in ~2.2 hours

## Scenario Analysis

### Scenario 1: Daily Driving (Minimal Draw)

**Conditions:** Daytime driving, no offroad lights, radio off, no accessories

| Circuit                        |   Load | Reason           |
| :----------------------------- | -----: | :--------------- |
| **Fusion Radio memory (CB30)** | **1A** | Clock/presets    |
| **USB Charging (CB48)**        | **2A** | Phone charging   |
| **WolfBox Camera (CB39)**      | **2A** | Always recording |
| **TOTAL**                      | **5A** |                  |

**BCDC Charging:** 30-50A typical

**Net Battery Effect:** +25 to +45A (battery charging)

**Battery SOC Trend:** Rising - battery maintains full charge quickly

---

### Scenario 2: Night Highway Driving

**Conditions:** Night driving, fog lights on, music playing, heated seats (winter)

| Circuit                          |    Load | Reason             |
| :------------------------------- | ------: | :----------------- |
| **Fog Light (OUTPUT-3)**         |  **6A** | Visibility         |
| **Rear Lights (OUTPUT-12)**      |  **5A** | License plate area |
| **Fusion Radio memory (CB30)**   |  **1A** | Always on          |
| **Fusion head unit (CB44)**      | **10A** | Music moderate     |
| **USB Charging (CB48)**          |  **5A** | Devices            |
| **WolfBox Camera (CB39)**        |  **2A** | Always recording   |
| **Driver Heated Seat (CB45)**    |  **3A** | Cycling            |
| **Passenger Heated Seat (CB42)** |  **3A** | Cycling            |
| **TOTAL**                        | **35A** |                    |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** +15A (battery charging!)

**Battery SOC Trend:** Rising - battery maintains full charge even with high accessory use

**Assessment:** Excellent - 50A BCDC fully covers all night highway loads with margin to spare

---

### Scenario 3: Night Offroad (Full Lighting)

**Conditions:** Technical trail at night, all forward lighting, rock lights, lockers engaged

| Circuit                        |    Load | Reason             |
| :----------------------------- | ------: | :----------------- |
| **Roof Lights (OUTPUT-1)**     | **18A** | Primary forward    |
| **Ditch Lights (OUTPUT-2)**    |  **8A** | Peripheral         |
| **Fog Light (OUTPUT-3)**       |  **6A** | Close range        |
| **Rock Lights (OUTPUT-6)**     |  **3A** | Obstacle spotting  |
| **Chase Light (OUTPUT-7)**     |  **1A** | Following vehicles |
| **Front Locker (OUTPUT-17)**   |  **2A** | Engaged            |
| **Rear Locker (OUTPUT-10)**    |  **2A** | Engaged            |
| **Fusion Radio memory (CB30)** |  **1A** | Always on          |
| **USB Charging (CB48)**        |  **2A** | Phone              |
| **WolfBox Camera (CB39)**      |  **2A** | Recording          |
| **TOTAL**                      | **45A** |                    |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** +5A (battery charging!)

**Assessment:** Excellent - full night offroad lighting is fully covered by BCDC charging. Battery maintains charge even with all lights on.

---

### Scenario 4: Airing Up Tires (ARB Compressor)

**Conditions:** Parked after trail, engine idling, airing up 4 tires (5-10 minutes)

| Circuit                             |     Load | Reason         |
| :---------------------------------- | -------: | :------------- |
| **ARB Compressor Motor 1 (MIDI-1)** |  **45A** | Running        |
| **ARB Compressor Motor 2 (MIDI-2)** |  **45A** | Running        |
| **Compressor Control (OUTPUT-11)**  |  **15A** | Control signal |
| **Fusion Radio memory (CB30)**      |   **1A** | Always on      |
| **USB Charging (CB48)**             |   **2A** | Phone          |
| **WolfBox Camera (CB39)**           |   **2A** | Recording      |
| **TOTAL**                           | **110A** |                |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -60A (moderate discharge)

**5-minute air-up:** 60A × (5/60)h = **5Ah used** (5% of usable capacity)

**10-minute air-up:** 60A × (10/60)h = **10Ah used** (9% of usable capacity)

**Assessment:** Excellent - minimal battery impact. Full recovery in 10-20 minutes of driving.

---

### Scenario 5: Extended Airing Up (30+ minutes)

**Conditions:** Airing up 5 tires + air tank refill, extended compressor operation

| Circuit                             |     Load | Reason         |
| :---------------------------------- | -------: | :------------- |
| **ARB Compressor Motor 1 (MIDI-1)** |  **45A** | Running        |
| **ARB Compressor Motor 2 (MIDI-2)** |  **45A** | Running        |
| **Compressor Control (OUTPUT-11)**  |  **15A** | Control signal |
| **Fusion Radio memory (CB30)**      |   **1A** | Always on      |
| **USB Charging (CB48)**             |   **2A** | Phone          |
| **WolfBox Camera (CB39)**           |   **2A** | Recording      |
| **TOTAL**                           | **110A** |                |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -60A (moderate discharge)

**30-minute operation:** 60A × 0.5h = **30Ah used** (28% of usable capacity)

**Time to 20% SOC:** 108Ah / 60A = **108 minutes** of continuous compressor operation

**Assessment:** Extended air-up no longer a concern. Can run compressor for nearly 2 hours before reaching 20% SOC.

---

### Scenario 6: Winch Recovery (Brief High-Current)

**Conditions:** Vehicle recovery, 30-second winch pull at moderate load

| Circuit                        |     Load | Reason         |
| :----------------------------- | -------: | :------------- |
| **Winch Motor**                | **250A** | Moderate pull  |
| **Winch Control (CB43)**       |   **2A** | Dash push, control signal via BODY PDU CB43 |
| **Fusion Radio memory (CB30)** |   **1A** | Always on      |
| **WolfBox Camera (CB39)**      |   **2A** | Recording      |
| **TOTAL**                      | **255A** |                |

**BCDC Charging:** 50A (full rate)

**Net Battery Effect:** -205A (heavy discharge)

**30-second pull:** 205A × (30/3600)h = **1.7Ah used** (1.6% of usable capacity)

**Assessment:** Winch operations have negligible battery impact. Can perform 50+ pulls before approaching 20% SOC.

---

### Scenario 7: Camp Mode (Engine Off)

**Conditions:** Parked at camp, engine off, minimal lighting, music

| Circuit                        |    Load | Reason           |
| :----------------------------- | ------: | :--------------- |
| **Dome Lights (OUTPUT-4)**     |  **4A** | Camp lighting    |
| **Rock Lights (OUTPUT-6)**     |  **3A** | Ground lighting  |
| **Footwell Lights (MLC-RW)**   |  **1A** | Ambiance         |
| **Fusion Radio memory (CB30)** |  **1A** | Always on        |
| **Fusion head unit (CB44)**    |  **8A** | Music            |
| **USB Charging (CB48)**        | **10A** | Multiple devices |
| **TOTAL**                      | **27A** |                  |

**BCDC Charging:** 0A (engine off)

**Solar (daytime):** ~5.8A battery-side (80W panel — see [Solar Charging][solar])

**Net Battery Effect (day):** -21A

**Net Battery Effect (night):** -27A

**Time to 20% SOC (no solar):** 108Ah / 27A = **4 hours**

**Time to 20% SOC (with solar):** 108Ah / 21A = **5+ hours** (daytime only)

**Assessment:** Camp mode now practical. 4+ hours of music, lights, and charging without engine. For extended camping:

- Solar extends daytime runtime significantly
- Idle engine 30 min to recover ~25Ah
- Multi-day camping still benefits from periodic charging

---

## Summary

| Scenario          | Total Draw | BCDC | Net Effect | Time to 20% SOC | Status    |
| :---------------- | :--------- | :--- | :--------- | :-------------- | :-------- |
| Daily Driving     | 5A         | 50A  | +45A       | N/A (charging)  | Excellent |
| Night Highway     | 35A        | 50A  | +15A       | N/A (charging)  | Excellent |
| Night Offroad     | 45A        | 50A  | +5A        | N/A (charging)  | Excellent |
| Air Up (5-10 min) | 110A       | 50A  | -60A       | 108 minutes     | Excellent |
| Air Up Extended   | 110A       | 50A  | -60A       | 108 minutes     | Excellent |
| Winch Recovery    | 255A       | 50A  | -205A      | 50+ pulls       | Excellent |
| Camp Mode         | 27A        | 0A   | -27A       | **4 hours**     | Good      |

**Key Insight:** With corrected XL Sport specs (2.2A/pod vs 6A), full night offroad lighting (45A) is now fully covered by 50A BCDC charging. The Dakota Lithium 135Ah upgrade provides effectively unlimited runtime for all driving scenarios including full lighting. Camp mode provides 4+ hours without engine.

## Related Documentation

- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [SafetyHub 150][safetyhub] - ARB compressor fusing
- [SwitchPros SP-1200][switchpros] - Lighting control outputs
- [BODY PDU][body-pdu] - Cabin circuit details
- [START Battery Load Analysis][start-load-analysis] - Companion analysis for START battery
- [PMU ARB Load Shedding][arb-load-shedding] - Load management during ARB operation

[bcdc]: ../01-power-generation/03-bcdc.md
[solar]: ../01-power-generation/04-solar.md
[safetyhub]: ../03-aux-battery-distribution/04-safetyhub.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[body-pdu]: ../03-aux-battery-distribution/03-body-pdu.md
[start-load-analysis]: 02-start-battery.md
[arb-load-shedding]: ../04-pmu/05-pmu-arb-load-shedding.md
