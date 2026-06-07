---
hide:
  - toc
---

# 1.4.4 PMU Programming {#pmu-programming}

PMU configuration examples, logic sequences, and implementation checklist.

## Programming Examples

### DRL Auto-Off Logic (Output 23)

```text
IF (Pin7_IgnitionRUN == ON) AND (In7_CT4_Headlights == OFF)
  THEN Out23_DRL = ON
ELSE Out23_DRL = OFF
```

DRL on with ignition, off when headlights active.

**Note:** Pin 7 is the dedicated 12V switched input (physical pin), different from In 7 which is a digital input channel. See [PMU Inputs][pmu-inputs] for complete pin assignments.

### A/C Clutch Logic (Output 17)

```text
IF (In9_AC_Request == ON) AND (BatteryVoltage > 11.5V)
  THEN Out17_AC_Clutch = ON
ELSE Out17_AC_Clutch = OFF
```

A/C engages when requested and voltage adequate.

### Oil Cooler Fan Control (Output 7) - CAN-based

```text
IF (J1939_SPN175_OilTemp > 230°F) THEN Out7_OilFan = ON
ELSEIF (J1939_SPN175_OilTemp < 220°F) THEN Out7_OilFan = OFF
```

10°F hysteresis prevents rapid cycling. Uses J1939 engine oil temperature from ECM (SPN 175).

### PS Cooler Fan Control (Output 8) - CAN-based

```text
IF (J1939_SPN110_CoolantTemp > 220°F) THEN Out8_PSFan = ON
ELSEIF (J1939_SPN110_CoolantTemp < 210°F) THEN Out8_PSFan = OFF
```

10°F hysteresis prevents rapid cycling. Uses J1939 coolant temperature from ECM (SPN 110) as proxy for PS fluid temp.

### Radiator Fan Control — relocated off the PMU

The radiator fan no longer runs on PMU outputs. It is powered START-direct from the [START+ Forward Distribution Bus][start-fwd-bus] and speed-controlled by a **Lingenfelter VSFM-002** controller with its own coolant sensor, independent of the PMU and J1939 — see [Radiator Fan][radiator-fan]. The VSFM-002 is to be configured to command **full speed on lost/invalid sensor signal** (the former PMU/CAN PWM path defaulted the fan OFF on lost coolant-temp data — the failure mode this relocation closes).

### Sequential Load Startup

```text
DELAY Out5_HVAC = 0.5s
DELAY Out7_OilFan = 1.0s
DELAY Out8_PSFan = 1.5s
```

Prevents voltage sag during ignition-on by staggering high-current load activation.

### Battery Load Monitoring

**Purpose:** Monitor battery voltage and current to track actual system load and verify alternator capacity.

**Data Logging Configuration:**

```text
LOG BatteryVoltage (continuous, 1 Hz)
LOG TotalCurrent_PMU (continuous, 1 Hz)
LOG AlternatorVoltage (if available)
LOG EngineRPM (J1939_SPN190)
```

**Critical Voltage Thresholds:**

- **14.2-14.4V** (engine running): Alternator charging normally
- **13.8-14.1V** (engine running, high load): Alternator near capacity
- **12.6-12.8V** (engine off): Fully charged battery at rest
- **<12.5V** (engine running): Alternator undersized or failing
- **<11.5V** (engine running): Critical - load exceeds alternator output

**Warning Triggers:**

```text
IF (BatteryVoltage < 12.5V) AND (EngineRPM > 1000)
  THEN Trigger_Low_Voltage_Warning = ON
```

### ARB Compressor Load Shedding

**Purpose:** Automatically shed non-critical loads when ARB compressor runs (90A) to prevent exceeding 270A alternator capacity.

**Summary:** Detects ARB activation and disables DRL (~2.6A), A/C (5A), and conditionally oil/PS cooler fans (15A each) to reduce total load from 266A to 243A, providing +27A alternator margin during tire inflation.

**See:** [ARB Load Shedding Logic][arb-load-shedding] for complete implementation details, load analysis, testing procedures, and operator guidelines.

## Configuration Software

**Software:** ECUMaster PMU Configuration Software

**Connection:** USB to PMU (PC configuration)

**Configuration File:** Export and backup PMU configuration file (.pmu format)

**Backup Strategy:** Store configuration in git repository + printed copy of critical logic (DRL, fan control, starter safety)

**Features:**

- Visual output state monitoring
- Real-time data logging
- Logic programming interface
- CAN bus configuration
- Output combining setup
- Diagnostic LED configuration

**Installation & Testing:** See [Section 1 Installation Checklist][installation]

[installation]: ../../09-installation/01-power-systems-checklist.md#phase-3-controllers-physical-installation-main-power

## Related Documentation

- [PMU Overview][pmu-overview] - Product specifications and capacity
- [PMU Inputs][pmu-inputs] - Input configuration and CAN bus integration
- [PMU Outputs][pmu-outputs] - Output configuration and load details
- [START battery Distribution][starter-battery-distribution] - PMU power source and circuit breaker
- [Gauge Cluster][gauge-cluster] - Dakota Digital J1939 CAN bus tap location

[pmu-overview]: 01-pmu-overview.md
[pmu-inputs]: 02-pmu-inputs.md
[pmu-outputs]: 03-pmu-outputs.md
[arb-load-shedding]: 05-pmu-arb-load-shedding.md
[starter-battery-distribution]: ../02-starter-battery-distribution/index.md
[start-fwd-bus]: ../02-starter-battery-distribution/index.md#start-forward-bus
[radiator-fan]: ../../02-engine-systems/06-radiator-fan.md
[gauge-cluster]: ../../02-engine-systems/09-gauge-cluster/index.md
