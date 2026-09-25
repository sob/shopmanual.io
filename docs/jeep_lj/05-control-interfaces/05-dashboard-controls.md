---
hide:
  - toc
---

# Dashboard Physical Controls {#dashboard-physical-controls}

This section documents physical switches mounted in the dashboard area (separate from the SwitchPros control panel).

## Dash Switch Panel Standard

All dash-mounted physical switches use the **Toyota OEM cutout standard: 1.54" × 0.83" (39 mm × 21 mm)**. This is the de facto "Toyota-style" switch dimension used by Tacoma / 4Runner / FJ Cruiser / Tundra OEM, and supported by multiple aftermarket switch vendors (CH4X4, STEDI, sPOD, etc.).

**Why this standard:**

- Single consistent dash cutout dimension across all custom switches
- Wide vendor selection at this size (better than custom Carling Contura cutouts)
- LED-backlit OEM-look aesthetic
- Switches snap-lock into their own cutout — no fascia/bezel required

**Mounting:** Cutouts machined directly into the existing **Genright dash** at chosen positions — no separate fascia panel. Each switch snap-locks into its 1.54" × 0.83" rectangular cutout.

---

## Identified Dash Switches

| # | Switch | Status | Function | Power | Notes |
|:-:|:-------|:-------|:---------|:------|:------|
| 1 | **Winch IN/OUT** | ✓ Selected: CH4X4-TOY-D-WINIO | Dual-momentary push, IN and OUT | BODY PDU CB43 (10A) | See [Winch Control Switch](#winch-control-switch) below |
| 2 | **Drive mode select** (transmission) | {{ tbd(72) }} | 3-position mode select (Street / Default / Offroad) — exact action depends on TCU spec | {{ tbd(72) }} (likely BODY PDU) | Verify TCU input requirements before sourcing |
| 3 | **Driver heated seat** | {{ tbd(73) }} | ON/OFF latching (or momentary for Hi/Lo if available) | BODY PDU CB45 via relay K21 | Toyota-style equivalent needed |
| 4 | **Passenger heated seat** | {{ tbd(73) }} | ON/OFF latching | BODY PDU CB42 via relay K22 | Toyota-style equivalent needed |
| 5 | **Rear air locker** | Part not chosen ([Purchase Tracker][purchase-tracker]) | ON/OFF latching | BODY PDU CB44 via relay K27 (ignition) | Moved off SwitchPros button 10 (2026-09-24). See [Locker Switches](#locker-switches) |
| 6 | **Front air locker** | Part not chosen ([Purchase Tracker][purchase-tracker]) | ON/OFF latching | Rear locker switch output | Works only while the rear locker is on. Moved off SwitchPros button 9 |

Heated seats stay in the build (owner, 2026-09-24). With the lockers added, the panel needs **6 cutouts** ({{ tbd(76) }}).

**Excluded from this panel** (different aesthetic/form factor by design):

- Keyless ignition push button — round illuminated momentary (Otto/Apem 19-22mm), separate dash location
- Intercom remote head — Rugged STX-RS, with the volume and VOX knob, in a standard 0.83" × 1.45" rocker-switch hole. See [Intercom][intercom]
- Hidden bypass toggle — under-dash, intentionally not visible
- AMOT runaway shutoff T-handle — mechanical push-pull cable handle, dash bezel mount

---

## Winch Control Switch

!!! info "Winch System Documentation"
For complete winch specifications, wiring details, and recovery system information, see [Recovery Systems][recovery-systems].

**Selected part:** [CH4X4 Momentary Dual Push Switch for Toyota — Winch IN/OUT][ch4x4-winch]

| Spec | Value |
|:-----|:------|
| SKU | CH4X4-TOY-D-WINIO |
| Type | Dual independent momentary push buttons in one housing |
| Cutout | 1.54" × 0.83" (Toyota OEM standard) |
| Per-circuit rating | 3A @ 12V |
| Illumination | Dual-color LED (blue = OFF, green = ON) |
| Includes | Switch + connector + cable + wiring diagram |
| Price | ~$24 |

**Function:** In-cab winch control (works in parallel with handheld remote).

### How It Works

The CH4X4 has **two independent momentary push circuits** (not a polarity-reversing rocker). Each press sends a momentary +12V signal:

- **Top button (IN symbol):** momentary +12V → winch contactor IN trigger
- **Bottom button (OUT symbol):** momentary +12V → winch contactor OUT trigger

This is the **correct** design for the Warn ZEON 10-S contactor, which has separate IN and OUT trigger inputs that internally handle the motor polarity reversal. Two discrete push buttons are safer than a single rocker (can't accidentally activate both directions at once).

### Wiring

| Connection | Wire | Source | Destination |
|:-----------|:-----|:-------|:------------|
| Switch +12V supply | 1× 18 AWG | BODY PDU CB43 (10A) | Switch common terminal |
| IN signal | 1× 18 AWG | Switch IN button output | HDP24 pin 16 → winch contactor IN trigger |
| OUT signal | 1× 18 AWG | Switch OUT button output | HDP24 pin 17 → winch contactor OUT trigger |
| Illumination supply | 1× 18 AWG | Dash illumination circuit | Switch LED+ |
| Switch ground | 1× 18 AWG | Switch LED−/common | Chassis ground at dash |

**Routing:** BODY PDU (firewall, cabin side) → ~3 ft 18 AWG to dash switch → out through HDP24 pins 16/17 → engine bay → winch contactor (front bumper).

**Parallel Remote:** Handheld remote (wireless or wired) connects in parallel at winch contactor trigger terminals. Both dash switch and remote can trigger IN/OUT independently.

### Winch Control Outstanding Items

- [x] ~~Source center-off momentary rocker switch~~ → **Resolved 2026-05-30:** CH4X4-TOY-D-WINIO selected (dual-momentary push, not rocker; matches WARN contactor architecture)
- [x] ~~Assign BODY PDU circuit breaker slot~~ → **Resolved:** CB43 (10A) already allocated
- [ ] Verify winch contactor IN/OUT terminal connections for parallel wiring (with handheld remote)
- [ ] Order CH4X4 switch
- [ ] Mark and machine 1.54" × 0.83" cutouts in Genright dash at chosen positions for winch + future switches

[ch4x4-winch]: https://ch4x4.com/product/ch4x4-momentary-dual-push-switch-for-toyota-winch-in-out-symbol/

## Locker Switches

The ARB air lockers moved from SwitchPros buttons 9 and 10 to two latching dash switches (owner, 2026-09-24). ARB's own locker switches are ON/OFF rockers; the locker stays engaged while its switch is ON.[^arb-switch]

### Locker Wiring

Wired the way ARB recommends for two lockers: the front switch is fed from the rear switch's output, so "SOLENOID 2 [front] can be actuated only if SOLENOID 1 [rear] is already on".[^arb-dual]

| Connection | Wire | Source | Destination |
|:-----------|:-----|:-------|:------------|
| Feed | 18 AWG | BODY PDU CB44 (10A) → relay K27 (closes with the ignition) | Rear locker switch input |
| Rear locker | 18 AWG | Rear locker switch output | Rear locker solenoid (at the air manifold, under the passenger seat); also feeds the front switch input |
| Front locker | 18 AWG | Front locker switch output | Front locker solenoid (at the air manifold) |
| Solenoid grounds | 18 AWG | Each solenoid | Chassis ground near the manifold |

All of this stays in the cabin: dash → BODY PDU (firewall, cabin side) → under the passenger seat. Nothing crosses the firewall. See [Air Lockers][air-lockers] for the solenoids and air lines.

### Switch Choice

ARB's switches need a 21 mm × 36.5 mm cutout[^arb-switch], not this panel's 1.54" × 0.83" Toyota standard. Use Toyota-style latching switches instead, so every dash switch shares one cutout size.

ARB's placement guidance: within the driver's reach and line of sight so the ON/OFF state is visible, positioned to avoid accidental operation, with at least 2" (50 mm) of clearance behind the cutout. ARB also recommends its Air Locker warning sticker (part 210101) near the switches.[^arb-switch]

### Locker Switch Outstanding Items

- [ ] Choose the two Toyota-style latching locker switches and add them to the [Purchase Tracker][purchase-tracker]
- [ ] Wire each switch's LED to match the part chosen

## Rear Seat Switch

**Type:** [Blue Sea 4160 Push Button Switch][bluesea-4160] (10A latching, OFF-ON)
**Location:** Rear seat area (for rear passenger control), {{ tbd(77) }}
**Function:** Turns on the dome lights (4x KC Cyclone) through the SwitchPros
**Wire Gauge:** 18 AWG (signal only)

### Rear Seat Switch Wiring

The switch is a signal switch on SwitchPros TRIGGER-1, not a power path (2026-09-24, replacing the in-line design that could only turn the lights off):

- Blue Sea 4160 closes SwitchPros TRIGGER-1 (Pin 7) to ground
- TRIGGER-1 is set active low and turns on OUTPUT-4 (dome lights)
- Button 4 still works on its own; either one turns the dome lights on
- No lamp current flows through the switch, and nothing backfeeds OUTPUT-4

There are no door switches on this Jeep, so TRIGGER-1 is free for this. See [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12].

### Rear Seat Switch Outstanding Items

- [ ] Determine rear seat switch mounting location
- [ ] Route 18 AWG signal wire from the rear seat switch to SwitchPros TRIGGER-1 (Pin 7) and a chassis ground

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12] - Main lighting controller
- [Air Lockers][air-lockers] - ARB lockers, solenoids, and air lines
- [Recovery Systems][recovery-systems] - Winch system complete documentation

[recovery-systems]: ../08-exterior-systems/01-winch.md
[control-interfaces-overview]: 01-overview.md
[switchpros-sp-1200-rcr-force-12]: 02-switchpros-sp1200.md
[bluesea-4160]: https://www.bluesea.com/products/4160/10A_Push_Button_LED_Ring_Switch_OFF-ON_Blue
[purchase-tracker]: ../09-installation/03-purchase-tracker.md
[air-lockers]: ../08-exterior-systems/03-air-lockers.md
[intercom]: ../07-communication-systems/02-intercom.md

[^arb-switch]: ARB, "Dana 60HD, 35 Spline, 4.56 & Up Air Operated Locking Differential Installation Guide" (RD166), §5.1 "Mounting the Actuator Switch(es)", p. 31: 21 mm × 36.5 mm [0.83" × 1.44"] cutout; ON/OFF rocker; mounting guidance; warning sticker 210101. §6.3 "Testing the Air Locker Actuation", p. 37: switch ON locks the axle (both wheels turn together), switch OFF releases it. <https://store.arbusa.com/content/RD166.pdf> (accessed 2026-09-24).
[^arb-dual]: ARB RD166 Installation Guide, §5.2.2.2 "Dual Air Locker System", p. 35: "For safety reasons, this configuration allows SOLENOID 2 to be actuated only if SOLENOID 1 is already on", with SWITCH 1 / SOLENOID 1 = rear and SWITCH 2 / SOLENOID 2 = front.
