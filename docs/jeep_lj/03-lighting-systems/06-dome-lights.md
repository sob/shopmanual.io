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
- Automatic: Door switches via TRIGGER-1

See [SwitchPros SP-1200][switchpros-sp-1200] for wiring and trigger configuration.

## Mounting

- 2x front roll bar (above driver/passenger seats)
- 2x rear roll bar (above rear cargo area)

## Rear Seat Override

Physical switch on KC #6337 bracket for rear dome control independent of SwitchPros panel.

**Wiring:** KC bracket switch wired in parallel with SwitchPros OUTPUT-4:

- KC switch input: 12V CONSTANT (tap from SwitchPros power input or BODY PDU)
- KC switch output: Rear dome lights positive (parallel with SwitchPros OUTPUT-4)
- Either switch can turn on rear domes independently

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Plan wire routing from SwitchPros to roll bar mounts

## Related Documentation

- [Vehicle Lighting Overview][vehicle-lighting-overview]
- [SwitchPros SP-1200][switchpros-sp-1200]

[vehicle-lighting-overview]: 01-lighting-overview.md
[switchpros-sp-1200]: ../05-control-interfaces/02-switchpros-sp1200.md
