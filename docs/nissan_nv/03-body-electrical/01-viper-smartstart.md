---
hide:
  - toc
tags:
  - remote-start
  - troubleshooting
---

# 3.1 Viper SmartStart {#viper-smartstart}

A **Viper alarm with SmartStart remote start** is installed on T-harnesses, with
the Viper brain behind the **driver-side dash**. It sits between the factory
switches, the BCM, and the CAN network. A bad connection in its wiring can
kill factory functions and set codes in modules it doesn't power, so check
this bundle **before** condemning a Nissan module.

| Item | Value |
| :--- | :---- |
| System | Viper alarm + SmartStart remote start |
| Install method | T-harnesses (factory connectors not cut) |
| Brain location | Behind the driver-side dash |
| Brain model / SmartStart module | **TBD** |
| Bypass / data interface module | **TBD** - model and which network it connects to |
| Power feed and fuse | **TBD** - which battery and fuse feed the brain |

---

## Known fault: headlights dead from Viper wiring (September 2026) {#fault-2026-09}

**Resolved (owner, 2026-09-25).** An intermittent connection in the Viper
wiring behind the driver-side dash caused this fault. No Nissan module had
failed.

### Symptoms {#symptoms}

- Headlights, high beams (including flash-to-pass), and fog lights all dead
- Dash lights working
- **"Lights on" buzzer** sounded with the driver door open, key out, and the
  headlight switch **OFF**. The BCM was reading the switch as on.
- The alarm went off during troubleshooting
- Van started and drove normally

### Diagnostics {#diagnostics}

| Check | Result |
| :---- | :----- |
| Negative battery terminal | Already tight |
| [IPDM E/R auto active test](02-exterior-lighting.md#ipdm-auto-active-test) | Did not start (no horn chirp) |
| Innova 5610 all-module scan | All codes **past**, none current (below) |
| BCM and IPDM E/R | Both answered the scan with no DTCs |

| Module | Code | Meaning |
| :----- | :--- | :------ |
| Engine | P1615 | Difference of key (key mismatch) |
| ABS | C1143, C1130 | - |
| Combination meter | U1000 | CAN communication circuit |

### Fix {#fix}

Moving the Viper wiring bundle behind the driver-side dash brought the
headlights back and stopped the buzzer. The bundle stayed plugged in and was
only moved from where it sat.

- **Cause:** an intermittent connection in the Viper/T-harness wiring. The
  likely causes are a loose pin, a partly seated connector, or a chafed wire.
- **Not the cause:** the BCM and IPDM E/R, which both answered the scan clean.
- The past CAN (U1000), key mismatch (P1615), and ABS codes fit the Viper's
  bypass and data connections disturbing the network.

!!! tip "Check the Viper first"
    Suspect the Viper bundle if several factory functions fail together while
    the van still starts and drives. Watch for the "lights on" buzzer with the
    switch off and for past CAN or key codes. To rule the Viper in or out
    quickly, unplug it from the T-harnesses and run the van on factory wiring.

### Possibly related: October 2025 lighting failure {#related-2025-10}

In October 2025, headlights, high beams, and fogs failed together at night,
with the parking lights stuck on key-off. The fix was never recorded. The
failure pattern matches this fault, but the link is **unconfirmed**. See
[Exterior Lighting](02-exterior-lighting.md#history).

---

## Outstanding Items

- [ ] Wiggle-test the Viper bundle with the key out and the driver door open, and record the exact spot where the "lights on" buzzer returns
- [ ] Reseat the connectors, repair any damaged insulation, and zip-tie the bundle clear of brackets and the steering column
- [ ] Clear the past codes (P1615, C1143, C1130, U1000) and record any that return
- [ ] Record the Viper brain and SmartStart module models, the bypass/interface module, and the brain's power feed and fuse
- [ ] Record which factory circuits the T-harnesses tap (headlight switch, door, ignition, CAN)
- [ ] Check whether a remote start turns on ACC/IGN loads such as the BCDC ignition sense or [Rear Powerswitch (A)'s ACC trigger](../01-power-systems/03-switch-panels.md#rear-a)
