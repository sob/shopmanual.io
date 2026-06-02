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
| 2 | **Drive mode select** (transmission) | 🔴 TBD | 3-position mode select (Street / Default / Offroad) — exact action depends on TCU spec | TBD (likely BODY PDU) | Verify TCU input requirements before sourcing |
| 3 | **Driver heated seat** | 🔴 TBD | ON/OFF latching (or momentary for Hi/Lo if available) | BODY PDU CB45 via relay K21 | Toyota-style equivalent needed |
| 4 | **Passenger heated seat** | 🔴 TBD | ON/OFF latching | BODY PDU CB42 via relay K22 | Toyota-style equivalent needed |

**Excluded from this panel** (different aesthetic/form factor by design):

- Keyless ignition push button — round illuminated momentary (Otto/Apem 19-22mm), separate dash location
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

**Dual Control:** Dash push switch + handheld remote work simultaneously in parallel (both wired to the contactor's same trigger inputs).

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

## Rear Seat Switch

**Type:** [Blue Sea 4160 Push Button Switch][bluesea-4160] (10A latching, OFF-ON)
**Location:** Rear seat area (for rear passenger control)
**Function:** Controls rear roll bar dome lights (4x KC Cyclone)
**Wire Gauge:** 16 AWG

### Wiring

Wired in parallel with SwitchPros OUTPUT-4:

- SwitchPros OUTPUT-4 → Splice → Blue Sea 4160 → Dome lights
- Allows rear passenger to turn on/off dome lights independently
- Both SwitchPros Button 4 and rear switch can control the same lights
- Switch rating (10A) exceeds dome light load (4A)

### Rear Seat Switch Outstanding Items

- [ ] Determine rear seat switch mounting location
- [ ] Route 16 AWG wire from SwitchPros OUTPUT-4 splice to rear seat switch location

## Related Documentation

- [Control Interfaces Overview][control-interfaces-overview] - Main control interfaces overview
- [SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12] - Main lighting controller
- [Recovery Systems][recovery-systems] - Winch system complete documentation

[recovery-systems]: ../08-exterior-systems/01-winch.md
[control-interfaces-overview]: 01-overview.md
[switchpros-sp-1200-rcr-force-12]: 02-switchpros-sp1200.md
[bluesea-4160]: https://www.bluesea.com/products/4160/10A_Push_Button_LED_Ring_Switch_OFF-ON_Blue
