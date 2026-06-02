---
hide:
  - toc
---

# 1.8 Load Analysis {#load-analysis}

Scenario-based load analysis for the dual battery electrical system.

## System Architecture

The Jeep LJ uses a dual battery architecture with isolated power domains:

| Battery   | Location             | Charging                | Primary Loads                   |
| :-------- | :------------------- | :---------------------- | :------------------------------ |
| **START** | Driver rear wheel well    | Alternator (270A)       | PMU, engine systems, BCDC       |
| **AUX**   | Passenger rear wheel well | BCDC (50A) + Solar (6A) | SwitchPros, SafetyHub, BODY PDU |

**Key Principle:** The BCDC is the only connection between batteries during normal operation. AUX battery loads do NOT draw from the alternator directly.

## Analysis Methodology

### Realistic Scenario Approach

Load analysis uses realistic operating scenarios rather than theoretical worst-case sums:

1. **Identify which battery** powers each circuit (START vs AUX)
2. **Analyze each battery separately** with its own charging source
3. **Use realistic scenarios** (daily driving, offroad, airing up, recovery)
4. **Account for duty cycles** (brief peaks vs continuous loads)
5. **Consider mutually exclusive activities** (can't brake hard while winching)

### Why Not Sum All Loads?

**Never create "theoretical worst case" scenarios:**

- Do NOT sum all loads at peak simultaneously
- Do NOT combine mutually exclusive activities (braking + winching + radio TX)
- Do NOT add AUX battery loads to alternator calculations
- Do NOT flag alternator "undersizing" based on impossible scenarios

**Example - WRONG:**

```text
PMU max: 253A + SwitchPros max: 127A + ARB: 90A + Winch: 400A = 870A
Alternator: 270A = CRITICAL UNDERSIZING ❌
```

**Example - CORRECT:**

```text
START Battery Scenario (Offroad):
PMU typical: 115A + Radiator fan: 53A + BCDC: 50A = 218A
Alternator: 270A = 52A margin

AUX Battery Scenario (Night Offroad):
SwitchPros: 70A, BCDC charging: 50A
Net drain: 20A, Time to 50% SOC: 102 minutes
```

### Load Categories

| Category               | Characteristic           | Analysis Approach                      |
| :--------------------- | :----------------------- | :------------------------------------- |
| **Continuous**         | Always on when operating | Include in all scenarios               |
| **Intermittent**       | Cycles on/off            | Use average or typical duty            |
| **Peak**               | Brief bursts (seconds)   | Note duration, don't add to continuous |
| **Seasonal**           | A/C, heated seats        | Include in relevant scenarios only     |
| **Mutually Exclusive** | Braking vs accelerating  | Never combine                          |

## Load Exclusions

These loads are **NOT** included in running alternator calculations:

| Load              | Current  | Reason                     |
| :---------------- | :------- | :------------------------- |
| Starter           | 400-600A | Cranking only (engine off) |
| Grid Heater       | 250A     | 3-5 sec cold start only    |
| Winch             | 400A     | AUX battery (isolated)     |
| ARB Compressor    | 90A      | AUX battery (isolated)     |
| SwitchPros lights | 100A+    | AUX battery (isolated)     |

## Summary Results

### START Battery (Alternator-Supplied)

| Scenario          | Total Load | Alternator | Utilization | Status    |
| :---------------- | :--------- | :--------- | :---------- | :-------- |
| Highway Driving   | 107A       | 270A       | 40%         | Excellent |
| Hot City Driving  | 194A       | 270A       | 72%         | Good      |
| Offroad Trail     | 207A       | 270A       | 77%         | Good      |
| Emergency Braking | 166A       | 270A       | 61%         | Excellent |
| Parked Idling     | 123A       | 270A       | 46%         | Excellent |

**Worst Case:** 207A (offroad) = 63A margin

### AUX Battery (BCDC-Charged)

| Scenario          | Total Draw | BCDC | Net Effect | Duration Limit | Status    |
| :---------------- | :--------- | :--- | :--------- | :------------- | :-------- |
| Daily Driving     | 5A         | 50A  | +45A       | Unlimited      | Charging  |
| Night Highway     | 38A        | 50A  | +12A       | Unlimited      | Charging  |
| Night Offroad     | 70A        | 50A  | -20A       | 102 min        | Excellent |
| Air Up (5-10 min) | 110A       | 50A  | -60A       | 10 min         | Excellent |
| Air Up Extended   | 110A       | 50A  | -60A       | 34 min         | Practical |
| Winch Recovery    | 265A       | 50A  | -215A      | 30-sec pulls   | Brief OK  |
| Camp Mode         | 27A        | 0A   | -27A       | 76 min         | Limited   |

**Key Insight:** 50A BCDC enables night highway charging and 102-minute night offroad runtime.

## Related Documentation

- [Combined Scenarios][scenarios] - Multi-battery load analysis
- [START Battery Load Analysis][start-load] - Detailed START battery scenarios
- [AUX Battery Load Analysis][aux-load] - Detailed AUX battery scenarios
- [Alternator][alternator] - 270A capacity specifications
- [BCDC Alpha 50][bcdc] - DC-DC charger specifications
- [PMU ARB Load Shedding][arb-shedding] - Load management during compressor operation

[scenarios]: 01-scenarios.md
[start-load]: 02-start-battery.md
[aux-load]: 03-aux-battery.md
[alternator]: ../01-power-generation/02-alternator.md
[bcdc]: ../01-power-generation/03-bcdc.md
[arb-shedding]: ../04-pmu/05-pmu-arb-load-shedding.md
