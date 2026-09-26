---
hide:
  - toc
tags:
  - lighting
  - troubleshooting
---

# 3.2 Exterior Lighting {#exterior-lighting}

The factory headlights, high beams, and fog lights are not switched directly
by the stalk. The BCM reads the switch and sends the command over CAN to the
IPDM E/R, and the IPDM E/R drives the lights.

---

## Control path {#control-path}

Headlight stalk (combination switch) → **BCM** → **CAN bus** → **IPDM E/R** → lights

When headlights, highs, and fogs all fail together, suspect this path, not
bulbs or individual fuses. The Viper T-harnesses also sit on this path; see
[Viper SmartStart](01-viper-smartstart.md).

---

## IPDM E/R auto active test {#ipdm-auto-active-test}

This test runs the IPDM E/R outputs without a scan tool. **Lift the wiper arms
first**, because the wipers will run.

1. Hood and passenger door closed, driver door open.
2. Key OFF, then key ON.
3. Within 20 seconds, press or cycle the driver door switch 10 times.
4. Key OFF, then key ON again within 10 seconds.
5. The horn chirps once and the test runs three cycles: oil pressure light,
   wipers, parking/tail/fog lights, low beams then high beams, A/C clutch.

Turn the key off to cancel.

| Result | Meaning |
| :----- | :------ |
| Test starts | The BCM-to-IPDM CAN link is working. If a light still fails in the test, look at the IPDM output, the fuse, or the bulb |
| Test does not start | Suspect the door switch input, the BCM, or the BCM-to-IPDM link. On this van, check the [Viper wiring](01-viper-smartstart.md) first |

!!! note "The Innova 5610 can't reach the body modules"
    On this van the Innova 5610 shows no BCM live data and runs no active
    tests outside the engine module. The auto active test above is the only
    way to exercise the IPDM E/R outputs without a dealer-level tool.

---

## Fault history {#history}

| Date | Symptoms | Outcome |
| :--- | :------- | :------ |
| October 2025 | Headlights, highs, and fogs dead at night, roadside. Parking lights stuck on, including key-off. No dash warnings | **Not recorded.** See below |
| 2026-09-25 | Headlights, highs, and fogs dead; "lights on" buzzer with the switch off | **Resolved:** intermittent connection in the Viper wiring. See [Viper SmartStart](01-viper-smartstart.md#fault-2026-09) |

### October 2025 {#history-2025-10}

| Step | Result |
| :--- | :----- |
| Negative terminal found loose and tightened | No change |
| Negative terminal disconnected | Parking lights went off |
| BCM hard reset (negative off for several minutes) | Dash lights flashed on reconnect; still no headlights, and the parking lights came back on key-off |
| Pulled the tail lamp relay (IPDM E/R) | No change |
| Pulled the DTRL 1 relay | No change |

Next steps were discussed, but there is no record that they were done:

- Pull IPDM E/R fuse **#9** (10 A, illumination/parking/tail) to stop the battery drain
- Check the **40 A BCM fuse (#16)** in the battery fuse box

This fault matches the September 2026 Viper fault closely: three lighting
functions dead together and the BCM misreading the switch state. The link is
**unconfirmed**.

---

## Bulbs {#bulbs}

| Position | Bulb | Notes |
| :------- | :--- | :---- |
| Brake light | 3157 wedge base | A SuperBrightLEDs bulb that was fitted sat loose in the socket |

---

## Outstanding Items

- [ ] Record how the October 2025 lighting failure was cleared, and whether it was the Viper wiring
- [ ] Confirm the IPDM E/R #9 and battery fuse box #16 fuse positions and ratings against the service manual
