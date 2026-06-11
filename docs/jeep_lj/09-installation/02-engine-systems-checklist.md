---
hide:
  - toc
tags:
  - engine-systems
  - installation
---

# Section 2: Engine Systems - Installation Checklist

Organized by installation order for efficient build workflow. Each item is a
check-off confirmation — specs and part numbers live in the linked source docs;
parts to buy live in the [Purchase Tracker][purchase-tracker].

---

## Phase 1: Starter System

- [ ] Confirm starter motor mounted to engine block
- [ ] Confirm START battery+ → starter battery post
- [ ] Confirm Cole Hersee solenoid mounted on firewall (engine bay side)
- [ ] Confirm starter battery post → Cole Hersee input
- [ ] Confirm Cole Hersee output → starter switch post
- [ ] Confirm PBS-I module mounted under-dash, powered from Critical Cabin PDU
- [ ] Confirm PBS-I PURPLE START → firewall Pin 15 → Cole Hersee coil+
- [ ] Confirm Cole Hersee coil- grounded to engine bay ground bus
- [ ] Confirm PBS-I PINK IGN → cabin ignition bus bar → firewall Pin 12 → ECM 12V + PMU Pin 7
- [ ] Confirm Start Button mounted on dash, harness plugged into PBS-I
- [ ] Confirm Programming Button stashed accessibly for tag-learn / Emergency Bypass

---

## Phase 2: Brake System

### Pre-Install Fab + Bench Test

- [ ] Bench test donor iBooster: apply ignition signal, verify motor cycles and pedal rod assists
- [ ] Discard factory Honda master cylinder
- [ ] Install Back Bay Customs adapter + Wilwood MC onto iBooster
- [ ] Mock up iBooster + MC assembly against firewall — verify engine-bay clearance BEFORE drilling
- [ ] Drill firewall for iBooster mounting (factory booster holes abandoned)
- [ ] Mock up reservoir standoff location, verify hood clearance

### Brake Pedal Swap

- [ ] Remove factory manual-trans pedal assembly
- [ ] Verify donor auto pedal: stop-lamp switch + clip present, bushing OK, arm not bent
- [ ] Install 03-06 auto brake pedal assembly
- [ ] Reconnect stop-lamp switch wiring: PMU In 2, PBS-I Brake input, Turbolamik brake input (T-tap, cabin splice)
- [ ] Plug clutch master cylinder firewall hole
- [ ] Bench-measure pedal ratio vs factory pedal (confirm MC stroke + iBooster rod travel headroom)
- [ ] Re-measure iBooster pushrod length after pedal install; adjust per harness vendor instructions

### iBooster Installation

- [ ] Confirm factory vacuum brake booster removed
- [ ] Confirm custom firewall bracket installed at factory booster location
- [ ] Confirm iBooster + Wilwood MC assembly mounted to firewall bracket
- [ ] Confirm secondary front support bracket installed
- [ ] Confirm Wilwood dual bracket + reservoirs mounted on standoff
- [ ] Confirm flexlines installed: reservoir → MC
- [ ] Confirm brake hardlines routed from MC to front/rear brakes
- [ ] Confirm iBooster wiring harness connected ({{ tbd(105) }}: Tulay's or EVcreate)
- [ ] Confirm iBooster main power connected (START+ Forward Dist Bus, 50A CB)
- [ ] Confirm iBooster ignition enable connected (Ignition bus Term 5, 7.5A fuse, firewall Pin 18)
- [ ] Confirm iBooster ground connected to engine bay ground bus (dedicated/redundant ground recommended)
- [ ] Bleed brake system; verify no leaks

---

## Phase 3: Grid Heater

- [ ] Confirm ECM pins 46/21 → grid heater relay coil
- [ ] Confirm fusible link from START battery+ to grid heater relay
- [ ] Confirm grid heater relay ground → START battery- or NEGATIVE bus
- [ ] Confirm grid heater relay mounted near intake manifold
- [ ] Verify grid heater element resistance confirms design current ({{ tbd(42) }})

---

## Phase 4: HVAC

- [ ] Confirm factory TJ HVAC system complete and functional
- [ ] Confirm vacuum system installed: R2.8 manifold → check valve → reservoir → firewall → dash
- [ ] Verify vacuum system holds vacuum

---

## Phase 5: Wipers

- [ ] Confirm WS-51C wiper controller mounted in dash
- [ ] Confirm PMU OUT11 → WS-51C power input
- [ ] Confirm WS-51C ground connected
- [ ] Confirm WS-51C low/high outputs → factory wiper motor
- [ ] Confirm wiper motor park switch → WS-51C park input
- [ ] Confirm WS-51C washer output → factory washer pump

---

## Phase 6: Radiator Fan

- [ ] Confirm GM 84100128 fan mounted to radiator shroud
- [ ] Confirm START+ Forward Dist Bus (60A CB) → relay → fan power
- [ ] Confirm Lingenfelter VSFM-002 + coolant sensor installed (sensor P/N + port {{ tbd(134) }})
- [ ] Confirm fan ground connected to engine bay ground bus
- [ ] Confirm VSFM-002 commands full speed on lost sensor signal ({{ tbd(134) }})

---

## Phase 7: Horn

- [ ] Confirm PIAA 85115 horns mounted in engine bay
- [ ] Confirm PMU OUT18 → horns
- [ ] Confirm horns grounded to engine bay ground bus
- [ ] Confirm horn button trigger routed through firewall to PMU In 1
- [ ] Confirm PMU programmed: In 1 → OUT18

---

## Phase 8: Runaway Protection

### Catch Can Installation

- [ ] Confirm catch can bracket mounted ({{ tbd(58) }} — intake side, away from exhaust)
- [ ] Confirm catch can installed vertically with petcock at bottom
- [ ] Confirm hose from valve cover breather → catch can INLET
- [ ] Confirm hose from catch can OUTLET → turbo inlet
- [ ] Verify catch can petcock closed before first engine start

### AMOT Air Shutoff Installation

- [ ] Confirm AMOT installed in pre-turbo intake tract
- [ ] Confirm NPT-to-hose adapters secure on both AMOT ports
- [ ] Confirm AMOT butterfly cocks open and latches; lever orientation matches cable pull
- [ ] Confirm intake clamps secured (no boost or vacuum leaks)
- [ ] Confirm AMOT body oriented so trip lever clears obstructions through full motion

### Cable and T-Handle Installation

- [ ] Confirm T-handle mounted at dash location ({{ tbd(56) }})
- [ ] Confirm cable conduit passes through dedicated firewall grommet ({{ tbd(57) }})
- [ ] Confirm cable secured along run; no sharp bends
- [ ] Confirm cable end attaches to AMOT trip lever; pull stroke clears trip point
- [ ] Confirm T-handle sits flush against dash bezel when AMOT is cocked open
- [ ] Confirm T-handle labeled `EMERGENCY ENGINE SHUTOFF — PULL TO STOP`

---

## Phase 9: Testing

### iBooster Testing

- [ ] Verify iBooster main power present (ignition OFF and ON)
- [ ] Verify iBooster ignition signal present (RUN only)
- [ ] Verify iBooster ground continuity to battery negative
- [ ] Verify brake pedal feel with iBooster powered
- [ ] Verify fail-safe mode (disconnect ignition signal, confirm basic assist)
- [ ] Verify iBooster standby current within spec (ignition OFF) — {{ tbd(151) }}: standby spec not yet sourced
- [ ] Road test: light braking, hard braking, engine-off coasting

### HVAC Testing

- [ ] Verify temperature control (hot/cold blend)
- [ ] Verify mode control (defrost/vent/floor)
- [ ] Verify blower speeds
- [ ] Verify A/C clutch engagement
- [ ] Verify heater output

### Wiper Testing

- [ ] Verify wiper speeds: Off / Mist / Delay / Low / High
- [ ] Verify wiper park position
- [ ] Verify washer pump activates
- [ ] Verify auto-wipe triggers after washer spray

### Starter Testing

- [ ] Verify starter does NOT crank with brake released (PBS-I brake interlock)
- [ ] Verify starter does NOT crank when Start Button not pressed
- [ ] Verify starter does NOT crank without valid iTag fob in range
- [ ] Verify starter cranks when fob + Start Button + brake all asserted (warm engine)
- [ ] Verify cold-start sequence: IGN on → WAIT lamp illuminates → extinguishes → driver cranks (no auto-gate; driver waits for the lamp)
- [ ] Verify engine shutoff: brake + button hold → engine stops
- [ ] Verify Emergency Bypass: Programming Button + PIN authorizes start with fob absent
- [ ] Verify fob auto-arm after fob leaves range

### Grid Heater Testing

- [ ] Verify grid heater activates in cold conditions
- [ ] Verify "Wait to Start" lamp illuminates during preheat

### Horn Testing

- [ ] Verify horn sounds when button pressed (ignition OFF and ON)

### Radiator Fan Testing

- [ ] Verify voltage at fan terminals under load
- [ ] Verify fan activates at temperature setpoints
- [ ] Verify inverted duty cycle behavior (high duty = low speed)
- [ ] Tune temperature setpoints for R2.8 under real-world conditions

### Runaway Protection Testing

- [ ] Static test: engine OFF, pull T-handle, verify AMOT butterfly snaps fully closed
- [ ] Reset test: re-cock AMOT, push T-handle to flush, verify butterfly returns open
- [ ] Cable freedom: pull T-handle through full stroke, verify no binding
- [ ] Functional test (engine idling, clear area): pull T-handle, verify engine stalls
- [ ] Catch can drain check after first 100 miles (confirms PCV flow)

---

## Reference Documentation

- **Starter:** [Starter System][starter]
- **iBooster:** [Brake Booster System][ibooster]
- **Grid Heater:** [Grid Heater System][grid-heater]
- **HVAC:** [HVAC System][hvac]
- **Wipers:** [Wiper System][wipers]
- **Horn:** [Horn System][horn]
- **Radiator Fan:** [Radiator Fan System][radiator-fan]
- **Runaway Protection:** [Diesel Runaway Protection][runaway-protection]
- **Parts to buy:** [Purchase Tracker][purchase-tracker]

[starter]: ../02-engine-systems/01-starter.md
[ibooster]: ../02-engine-systems/02-brake-booster.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
[hvac]: ../02-engine-systems/03-hvac.md
[wipers]: ../02-engine-systems/04-wipers.md
[horn]: ../02-engine-systems/05-horn.md
[radiator-fan]: ../02-engine-systems/06-radiator-fan.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
[purchase-tracker]: 03-purchase-tracker.md
