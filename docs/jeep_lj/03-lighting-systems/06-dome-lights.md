---
tags:
  - lighting
  - interior
  - switchpros-controlled
  - kc-hilites
---

# Dome Lights

Roll bar-mounted interior lighting for cabin illumination.

## Specifications

**Type:** KC HiLiTES Cyclone V2
**Quantity:** 4 pods
**Output:** 200 lumens each (800 total)
**Draw:** 0.5A each (2A total)
**Size:** 2.4" diameter round
**Part #:** 1352 (single light)
**Wire Gauge:** 16 AWG

**Mounting Bracket:** KC HiLiTES Dual Cyclone Dome Light Mount (#6337)

- ADC12 aluminum, powder coated black
- Roll cage mount design
- Includes hardware and switch
- Dimensions: 5.45" W × 2.61" D × 1.54" H

## Control

**Controller:** SwitchPros Button 4 (OUTPUT-4)

- Manual: Button 4 press
- Rear-seat switch via TRIGGER-1 (see below)

There are no door switches: the Jeep has none, and it runs half doors or no doors (owner, 2026-09-24).

Dome lights are interior convenience lights, not required street lighting, so they run from the SwitchPros rather than the CT4.

See [SwitchPros SP-1200][switchpros-sp-1200] for wiring and trigger configuration.

## Mounting

- 2x front roll bar (above driver/passenger seats)
- 2x rear roll bar (above rear cargo area)

## Rear Seat Switch

A rear-seat switch turns the dome lights on through the SwitchPros, independent of Button 4 (resolved 2026-09-24, {{ tbd(148) }}).

**Wiring:** the switch is a signal switch on the SwitchPros trigger input, not a power path:

- Blue Sea 4160 latching push button, closing SwitchPros TRIGGER-1 to ground
- TRIGGER-1 (set active low) turns on OUTPUT-4, which feeds all four dome pods
- No CONSTANT tap and nothing in parallel with OUTPUT-4, so nothing backfeeds the output
- The KC #6337 bracket's own switch is not used for this

Mounting location: {{ tbd(77) }}. Trigger setup: [SwitchPros SP-1200][switchpros-sp-1200].

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Plan wire routing from SwitchPros to roll bar mounts

## Related Documentation

- [Vehicle Lighting Overview][vehicle-lighting-overview]
- [SwitchPros SP-1200][switchpros-sp-1200]

[vehicle-lighting-overview]: 01-lighting-overview.md
[switchpros-sp-1200]: ../05-control-interfaces/02-switchpros-sp1200.md
