---
hide:
  - toc
---

# 1.4.5 PMU ARB Load Shedding Logic {#pmu-arb-load-shedding}

Automatic load management during ARB compressor operation to preserve AUX battery capacity and maintain system voltage.

## Dual Battery Architecture

**Critical Understanding:** ARB compressor draws from **AUX battery**, NOT directly from alternator:

- **ARB Compressor (90A):** Powered by AUX battery via SafetyHub 150
- **BCDC Charging (50A max):** Replenishes AUX battery from alternator
- **Net AUX battery drain:** 90A - 50A = 40A during compressor operation

The alternator is NOT overloaded during ARB operation. The 50A BCDC significantly reduces net discharge rate, making extended air-up practical. Load shedding provides additional margin and maintains optimal voltage.

## Problem Statement

**AUX Battery Depletion During Extended Air-Up:**

```text
ARB compressor draw:        90A  (from AUX battery)
Other AUX loads:             5A  (camera, radio, USB)
BCDC charging rate:         50A  (to AUX battery)
─────────────────────────────────
Net AUX battery drain:      45A

AUX battery capacity:       135Ah (Dakota Lithium LiFePO4)
Usable capacity (80% DOD):  108Ah
Time to 20% SOC:           ~144 minutes continuous (2.4 hours)
```

**Impact Without Load Shedding:** Minor — the 135Ah/50A BCDC combination already leaves comfortable margin; load shedding maximizes it further for extended sessions.

## Solution Overview

**Load Shedding Strategy:**

- Shed cosmetic loads first (DRL)
- Shed comfort loads second (A/C)
- Conditionally shed cooling loads if temperatures allow (oil/PS cooler fans)
- Maintain critical PMU systems (HVAC blower, lights, CT4)

_Note: the iBooster and radiator fan are no longer PMU loads — both relocated to the [START+ Forward Bus][start-fwd-bus] — so they are outside this PMU shed logic. They remain START-battery loads and still appear in the START-side totals below._

## Load Shedding Logic

```text
// Monitor SwitchPros OUTPUT-11 state via shared CAN bus or hardwired trigger
IF (SwitchPros_OUT11_ARB == ON) OR (BatteryVoltage < 13.0V AND EngineRPM > 1000):

  // Shed non-critical loads (priority order: lowest to highest impact)
  Out23_DRL = OFF              // -2.6A: Daytime running lights (cosmetic)
  Out17_AC_Clutch = OFF        // -5A: Air conditioning (comfort)

  // Conditionally shed cooler fans if temperatures allow
  IF (J1939_SPN175_OilTemp < 220°F):
    Out7_OilFan = OFF          // -15A: Oil cooler fan (temp-dependent)

  IF (J1939_SPN110_CoolantTemp < 210°F):
    Out8_PSFan = OFF           // -15A: PS cooler fan (temp-dependent)

  // Total load reduction: ~8-38A depending on temperatures

  // Optional: Trigger dashboard indicator
  Out_ARB_Active_Indicator = ON  // Visual feedback to driver

ELSE:
  // Restore normal operation when ARB stops
  Out23_DRL = (Per DRL auto-off logic)
  Out17_AC_Clutch = (Per A/C request logic)
  Out7_OilFan = (Per oil temp thresholds)
  Out8_PSFan = (Per coolant temp thresholds)
  Out_ARB_Active_Indicator = OFF
```

## Load Reduction Analysis

| Load Shed             | Current Saved | Impact                       | When Disabled         |
| :-------------------- | :------------ | :--------------------------- | :-------------------- |
| DRL (OUT23)           | 2.6A          | Low - cosmetic only          | Always when ARB runs  |
| A/C Clutch (OUT17)    | 5A            | Medium - comfort loss        | Always when ARB runs  |
| Oil Cooler Fan (OUT7) | 15A           | Low - if oil temp <220°F     | Temperature-dependent |
| PS Cooler Fan (OUT8)  | 15A           | Low - if coolant temp <210°F | Temperature-dependent |
| **Total Saved**       | **~8-38A**    | -                            | -                     |

## AUX Battery Impact Analysis

**See [AUX Battery Load Analysis][aux-load-analysis] for complete scenario details.**

### WITHOUT Load Shedding

```text
ARB compressor draw:     90A   (from AUX battery)
Other AUX loads:          5A   (camera, radio memory, USB)
─────────────────────────────
Total AUX draw:          95A

BCDC charging:           50A   (to AUX battery)
─────────────────────────────
Net AUX drain:           45A

Time to 50% SOC:         45 minutes
```

**Alternator Load (START battery):** See [START Battery Load Analysis][start-load-analysis]

- PMU + radiator fan + BCDC = ~165A typical
- Alternator: 270A
- **Margin: +105A** Alternator is NOT the constraint

### WITH Load Shedding (Minimum - ~8A shed from START)

Shedding DRL (~2.6A) and A/C clutch (5A) from PMU reduces START battery load, allowing maximum BCDC output:

```text
START battery:
PMU reduced:          93A   (was 101A, shed DRL + A/C)
Radiator fan:         35A   (moderate, stationary)
BCDC at full rate:    50A   (maximized)
─────────────────────────────
START total:         178A
Alternator:          270A
Margin:              +92A

AUX battery:
ARB compressor:       90A
Other AUX loads:       5A
BCDC charging:        50A   (full rate maintained)
─────────────────────────────
Net AUX drain:        45A   (unchanged - BCDC still maxed)
```

**Primary benefit:** Ensures BCDC maintains full 50A output even if START battery voltage sags.

### WITH Load Shedding (Maximum - ~38A shed from START)

**When oil/coolant temps allow disabling cooler fans:**

```text
START battery:
PMU reduced:          63A   (shed DRL + A/C + oil fan + PS fan)
Radiator fan:         35A   (moderate)
BCDC at full rate:    50A
─────────────────────────────
START total:         148A
Alternator:          270A
Margin:             +122A   Excellent

AUX battery:
Net AUX drain:        45A   (unchanged)
```

**Benefit:** Maximum alternator headroom, stable voltage for all electronics.

## Implementation Details

### Detection Methods (Priority Order)

**1. Hardwired Trigger (Preferred):**

- Wire from SwitchPros OUTPUT-11 to PMU digital input
- Direct, reliable detection
- Lowest latency

**2. CAN Bus Monitoring:**

- If SwitchPros broadcasts output states on CAN
- No additional wiring required
- Slight latency

**3. Voltage-Based Fallback:**

- `IF (BatteryVoltage < 13.0V) AND (EngineRPM > 1000)`
- Triggers on ANY high load (not just ARB)
- Universal protection regardless of cause

### Temperature Safety Checks

**Critical:** Always verify temperatures before disabling cooler fans.

```text
// Oil Cooler Fan
IF (J1939_SPN175_OilTemp < 220°F):
  Safe to disable Out7_OilFan
ELSE:
  KEEP Out7_OilFan = ON (engine protection priority)

// PS Cooler Fan
IF (J1939_SPN110_CoolantTemp < 210°F):
  Safe to disable Out8_PSFan
ELSE:
  KEEP Out8_PSFan = ON (engine protection priority)
```

**Hysteresis:** Use 10°F hysteresis to prevent rapid cycling when temps hover near threshold.

### User Communication

**Dashboard Indicator Options:**

1. **Simple LED:** ARB button backlight changes color
2. **Message:** "ARB MODE - DRL/AC OFF"
3. **Dakota Digital Display:** Custom message via BIM module
4. **No indicator:** Silent operation (driver may not notice DRL/AC disabled)

**Recommended:** Backlight color change (green → amber when load shedding active)

## Operational Procedures (Supplemental)

**Best Practices for ARB Use:**

1. **Increase Engine RPM:** Run engine at 1500+ RPM during tire inflation
   - Alternator output increases with RPM
   - Better voltage regulation at higher speeds
   - Faster tire inflation

2. **Monitor Voltage:** Watch Dakota Digital voltage gauge during ARB use
   - Normal: 14.0-14.4V (load shedding working)
   - Marginal: 13.5-14.0V (acceptable, brief periods)
   - Low: <13.5V (increase RPM or reduce loads)

3. **Hot Weather:** Avoid prolonged ARB use at idle when ambient temp >95°F
   - Radiator fan + ARB + heat soak = high total load
   - Let engine cool between inflation cycles

4. **Avoid Simultaneous High Loads:**
   - ❌ ARB + winch (both 90A+ loads)
   - ❌ ARB + all accessories at idle
   - ARB + normal driving loads at 1500+ RPM

## Testing & Validation

### Initial Shakedown Testing

#### Test 1: ARB Load Shedding Activation

1. Start engine, let idle stabilize
2. Activate ARB (SwitchPros Button 11)
3. **Verify:**
   - DRL turns OFF
   - A/C compressor disengages (if running)
   - Dashboard indicator activates (if implemented)
   - Voltage stays >13.5V

#### Test 2: Temperature-Based Fan Shedding

1. Start engine cold (<180°F coolant)
2. Activate ARB
3. **Verify:**
   - Oil cooler fan OFF (temp below threshold)
   - PS cooler fan OFF (temp below threshold)
4. Run engine to operating temp (>220°F)
5. Activate ARB
6. **Verify:**
   - Cooler fans stay ON (engine protection priority)

#### Test 3: Load Restoration

1. Activate ARB
2. Verify loads shed
3. Deactivate ARB
4. **Verify:**
   - DRL returns to normal logic (on with ignition)
   - A/C returns if requested
   - Cooler fans return to temp-based control

### Data Logging

**Enable PMU Continuous Logging:**

```text
LOG BatteryVoltage (1 Hz)
LOG TotalCurrent_PMU (1 Hz)
LOG EngineRPM (J1939_SPN190)
LOG Out23_DRL (state)
LOG Out17_AC_Clutch (state)
LOG Out7_OilFan (state)
LOG Out8_PSFan (state)
LOG SwitchPros_OUT11_ARB (state or trigger input)
```

**Analysis:**

1. Export logs after tire inflation sessions
2. Verify voltage stays >13.5V during ARB operation
3. Confirm load shedding activates/deactivates correctly
4. Identify any unexpected load combinations

## Related Documentation

**Load Analysis:**

- [START Battery Load Analysis][start-load-analysis] - Alternator scenarios
- [AUX Battery Load Analysis][aux-load-analysis] - ARB impact scenarios

**Power Systems:**

- [Alternator Specifications][alternator] - 270A capacity
- [PMU Overview][pmu-overview] - PMU capacity and limitations
- [PMU Outputs][pmu-outputs] - Individual output assignments
- [PMU Programming][pmu-programming] - Other programming examples

**ARB Compressor:**

- [Air System][air-system] - ARB twin compressor specifications (90A total load)
- [SwitchPros][switchpros] - OUTPUT-11 control integration

[alternator]: ../01-power-generation/02-alternator.md
[pmu-overview]: 01-pmu-overview.md
[pmu-outputs]: 03-pmu-outputs.md
[pmu-programming]: 04-pmu-programming.md
[air-system]: ../../08-exterior-systems/02-air-compressor.md
[switchpros]: ../../05-control-interfaces/02-switchpros-sp1200.md
[start-load-analysis]: ../08-load-analysis/02-start-battery.md
[aux-load-analysis]: ../08-load-analysis/03-aux-battery.md
[start-fwd-bus]: ../02-starter-battery-distribution/index.md#start-forward-bus
