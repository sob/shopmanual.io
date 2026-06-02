---
hide:
  - toc
---

# Control Interfaces - Overview {#control-interfaces-overview}

This section documents all control interfaces in the Jeep LJ build - the switches, controllers, and input devices that allow the driver to control various vehicle systems.

## System Controllers

- **[SwitchPros SP-1200][switchpros-sp-1200-rcr-force-12]** - Main lighting and accessory controller
  - 12-button control panel with Bluetooth app
  - 17 total outputs (12 main + 5 low-side drivers)
  - 150A capacity, fed by Firewall CONSTANT Bus (via 150A CB)
  - Controls all auxiliary lighting and accessories

- **[Command Touch CT4][command-touch-ct4]** - Steering column turn signal and headlight controller
  - 4 programmable outputs for turn signals and headlights
  - GPS module for intelligent turn signal auto-cancel
  - Replaces factory multifunction stalk
  - Controls turn signals, headlights, and high beams

## Physical Switches

- **[Dashboard Controls][dashboard-physical-controls]** - Physical dash-mounted switches
  - Winch control switch
  - Other dash-mounted controls

- **[Keyless Ignition][keyless-ignition]** - RFID + push-button start/stop replacing the factory keyswitch
  - Digital Guard Dawg PBS-I self-contained module with RFID iTag fobs
  - Single dash push-button included with kit
  - WAIT-gate relay handles cold-start grid heater preheat automatically
  - Emergency Bypass Card with 4-digit PIN (no hidden toggle)

## System Integration

All control interfaces integrate with the dual-battery electrical system:

- **SwitchPros SP-1200:** Powered by Firewall CONSTANT Bus (sourced from AUX battery via 300A master CB + 2/0 AWG forward feed)
- **Command Touch CT4:** Powered by PMU OUT 13 (15A CONSTANT, sourced from START battery), integrates with PMU
- **Dashboard switches:** Various power sources depending on function

## Related Documentation

- **[Vehicle Lighting][vehicle-lighting-overview]** - Complete vehicle lighting circuits controlled by these interfaces
- **[Offroad Lighting][offroad-auxiliary-lighting]** - Auxiliary and offroad lighting controlled by SwitchPros
- **[Engine Systems][pmu-power-distribution]** - PMU power distribution and engine bay subsystems
- **[Horn][horn]** - PIAA horn system (engine bay component)
- **[Wipers][windshield-wiper-control-system]** - Ron Francis WS-51C wiper controller (engine bay component)

[switchpros-sp-1200-rcr-force-12]: 02-switchpros-sp1200.md
[command-touch-ct4]: 03-command-touch-ct4.md
[dashboard-physical-controls]: 05-dashboard-controls.md
[keyless-ignition]: 06-keyless-ignition.md
[vehicle-lighting-overview]: ../03-lighting-systems/01-lighting-overview.md
[offroad-auxiliary-lighting]: ../04-offroad-lighting/index.md
[pmu-power-distribution]: ../01-power-systems/04-pmu/index.md
[horn]: ../02-engine-systems/05-horn.md
[windshield-wiper-control-system]: ../02-engine-systems/04-wipers.md
