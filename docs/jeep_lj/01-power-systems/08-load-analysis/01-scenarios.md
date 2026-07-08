---
hide:
  - toc
---

# 1.8.1 Combined Scenarios {#combined-scenarios}

Multi-battery load analysis for realistic operating conditions where both START and AUX batteries are under significant load.

## Scenario: Night Offroad (Worst Realistic Case)

Both batteries under significant load simultaneously:

**START Battery (Alternator):**

| Circuit             |     Load |
| :------------------ | -------: |
| Radiator Fan (max)  |      53A |
| HVAC Blower         |      15A |
| GMRS Radio (TX)     |       5A |
| Oil/PS Cooler Fans  |      30A |
| Dakota Digital      |      25A |
| CT4 (headlights)    |      10A |
| iBooster + Ignition |       7A |
| STX Intercom        |       3A |
| BCDC (charging AUX) |      50A |
| **START Total**     | **198A** |

**AUX Battery (BCDC-Charged):**

| Circuit           |    Load |
| :---------------- | ------: |
| Roof Lights (8x)  |     18A |
| Ditch + Fog       |     14A |
| Rock + Chase      |      4A |
| Lockers           |      4A |
| Camera + USB      |      4A |
| **AUX Total**     | **44A** |

**Analysis:**

- START: 198A / 270A = **73% alternator utilization**
- AUX: 44A - 50A BCDC = **+6A net charge**

**Verdict:** Full night offroad lighting is now fully covered by BCDC. Battery maintains charge even in worst realistic case.

---

## Scenario: Recovery Operation

Winch recovery with engine idling:

**START Battery:**

| Circuit             |     Load |
| :------------------ | -------: |
| Radiator Fan (idle) |      25A |
| Dakota Digital      |      25A |
| CT4                 |      10A |
| iBooster + Ignition |       5A |
| BCDC                |      50A |
| **START Total**     | **115A** |

**AUX Battery:**

| Circuit       |     Load |
| :------------ | -------: |
| Winch Motor   |     250A |
| Winch Trigger |      10A |
| Camera        |       2A |
| **AUX Total** | **262A** |

**Analysis:**

- START: 115A / 270A = **43% alternator**
- AUX: 262A - 50A = **-212A net discharge**
- 30-sec pull: 212A × (30/3600)h = **1.8Ah** (3% of battery)

**Verdict:** Brief winch pulls have minimal impact. Multiple recoveries possible.

---

## Scenario: Extended Camp (Engine Off)

Overnight camping with minimal power:

**AUX Battery Only (engine off):**

| Circuit          |    Load |
| :--------------- | ------: |
| Dome/Rock Lights |      7A |
| Radio (music)    |      8A |
| USB Charging     |     10A |
| Camera           |      2A |
| **Total**        | **27A** |

**With Solar (daytime):** 27A - 6A = **-21A net**

**Without Solar (night):** **-27A net**

**Runtime:**

- Day: 34Ah / 21A = **97 minutes** to 50% SOC
- Night: 34Ah / 27A = **76 minutes** to 50% SOC

**Recommendations:**

- Minimize lighting to essentials
- Idle engine every 60-90 minutes to recharge
- Use solar panel during daytime
- Consider lithium upgrade for extended camping

---

## Scenario: Airing Up After Trail

ARB compressor running with engine idling:

**START Battery:**

| Circuit             |     Load |
| :------------------ | -------: |
| Radiator Fan (idle) |      25A |
| Dakota Digital      |      25A |
| CT4                 |      10A |
| iBooster + Ignition |       5A |
| BCDC                |      50A |
| **START Total**     | **115A** |

**AUX Battery:**

| Circuit                      |     Load |
| :--------------------------- | -------: |
| ARB Compressor (both motors) |      90A |
| Compressor Control           |      15A |
| Camera + USB                 |       4A |
| **AUX Total**                | **109A** |

**Analysis:**

- START: 115A / 270A = **43% alternator**
- AUX: 109A - 50A = **-59A net discharge**
- 10-minute air-up: 59A × (10/60)h = **9.8Ah** (14% of battery)

**Verdict:** Standard air-up has minimal battery impact. Battery recovers in ~12 minutes of driving.

---

## Summary

| Scenario      | START Load | START % | AUX Net | AUX Duration | Status    |
| :------------ | :--------- | :------ | :------ | :----------- | :-------- |
| Night Offroad | 198A       | 73%     | +6A     | N/A (charging) | Excellent |
| Recovery      | 115A       | 43%     | -212A   | 30-sec pulls | Brief OK  |
| Extended Camp | —          | —       | -27A    | 76 min       | Limited   |
| Airing Up     | 115A       | 43%     | -59A    | 10 min       | Excellent |

**Key Insight:** With corrected XL Sport specs (2.2A/pod), the dual battery architecture now provides net positive charging even during full night offroad lighting. The 50A BCDC fully covers all lighting loads with margin to spare.

## Related Documentation

- [Load Analysis Overview][load-analysis] - Methodology and system architecture
- [START Battery Load Analysis][start-load] - Individual START battery scenarios
- [AUX Battery Load Analysis][aux-load] - Individual AUX battery scenarios
- [PMU ARB Load Shedding][arb-shedding] - Load management during compressor operation

[load-analysis]: index.md
[start-load]: 02-start-battery.md
[aux-load]: 03-aux-battery.md
[arb-shedding]: ../04-pmu/05-pmu-arb-load-shedding.md
