# Section 1: Power Systems - Navigation Guide

## Section Overview

Power generation and distribution architecture for the Jeep LJ build.

**Key Principle:** Direct battery connections via circuit breakers - no intermediate bus bars between batteries and major loads.

## File Organization

### 1.1 Power Generation (`01-power-generation/`)

Batteries, alternator, BCDC charger, solar panel

### 1.2 START Battery Distribution (`02-starter-battery-distribution/`)

Driver rear wheel well power distribution, circuit breakers, SafetyHub

### 1.3 AUX Battery Distribution (`03-aux-battery-distribution/`)

Passenger rear wheel well power distribution, BODY PDU, SwitchPros power source

### 1.4 PMU (`04-pmu/`)

ECUMaster PMU24 outputs, inputs, CAN bus, programming

### 1.5 Grounding Architecture (`05-grounding/`)

Ground bus bars (direct battery grounds documented in 1.2/1.3)

### 1.6 Ignition Signal Distribution (`06-ignition-signal/`)

Ignition sense signal to CT4, SwitchPros, Fusion Radio, BCDC

### Installation Checklist

`../09-installation/01-power-systems-checklist.md` - Build sequence organized by workflow phases

## Cross-Section Integration

| Section                | Power Connection                               | Find In                     |
| :--------------------- | :--------------------------------------------- | :-------------------------- |
| Engine Systems (2)     | HVAC→OUT5, Fan→OUT2+3+4, Starter direct        | `02-engine-systems/`        |
| Lighting (3)           | DRL→OUT14, Brake→OUT21, Reverse→OUT22          | `03-lighting-systems/`      |
| Control Interfaces (4) | CT4→OUT13, Dakota→OUT9, SwitchPros→AUX 150A CB | `05-control-interfaces/`    |
| Audio (5)              | Fusion→BODY PDU                                | `06-audio-systems/`         |
| Communication (6)      | Radios→PMU OUT6/20                             | `07-communication-systems/` |
| Exterior (7)           | Winch→AUX direct, ARB→SafetyHub MIDI           | `08-exterior-systems/`      |

## Common Navigation Scenarios

| Question                                  | Answer Location                                            |
| :---------------------------------------- | :--------------------------------------------------------- |
| Where does \[component\] get power?         | Battery distribution `index.md` terminal tables            |
| What's on PMU OUT\[X\]?                     | `04-pmu/03-pmu-outputs.md`                                 |
| Where does \[wire\] route through firewall? | `02-engine-systems/07-firewall-ingress.md`                 |
| What CB protects \[load\]?                  | Battery distribution `01-circuit-breakers.md`              |
| Where does \[component\] ground?            | `05-grounding/` or battery distribution for direct grounds |

## When Changing Content

**Adding load:** Determine battery → update terminal table → add CB if needed → update grounding → add to checklist

**Moving content:** Update cross-references → search for old links → verify build

**Updating specs:** Find authoritative source → update ONE location → ensure others link to it

## Standards Exceptions

Some designs differ from marine standards (ABYC E-11) intentionally - this is automotive.

**See [STANDARDS-EXCEPTIONS.md](STANDARDS-EXCEPTIONS.md)** before flagging:

- Winch: No external CB (per WARN specs, internal thermal protection)
- Starter: No external CB (cable sizing as protection)
- Grid heater: Direct battery (fusible link in relay)
- Alternator: No output CB (self-limiting)

Apply SAE J1128 (automotive), not blanket marine rules.
