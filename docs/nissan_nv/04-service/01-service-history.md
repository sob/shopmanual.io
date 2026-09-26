---
hide:
  - toc
tags:
  - troubleshooting
---

# 4.1 Service History {#service-history}

This log lists repairs and diagnoses, newest first. Electrical faults are
written up in full on their own pages and summarized here.

| Date | Issue | Outcome |
| :--- | :---- | :------ |
| 2026-09-25 | Headlights, highs, and fogs dead | **Resolved:** Viper wiring. See [Viper SmartStart](../03-body-electrical/01-viper-smartstart.md#fault-2026-09) |
| August 2026 | Cranks but won't start | **Not recorded** ([below](#2026-08)) |
| May 2026 | Oil change | Spec recorded; what was installed is not confirmed ([below](#2026-05)) |
| March 2026 | Limp mode, no acceleration past about 20 mph | **Resolved:** accelerator pedal + MAF ([below](#2026-03)) |
| October 2025 | Headlights, highs, and fogs dead; parking lights stuck on | **Not recorded.** See [Exterior Lighting](../03-body-electrical/02-exterior-lighting.md#history-2025-10) |

---

## August 2026: cranks but won't start {#2026-08}

- Happened right after the van came back from a long trip with no problems
- The engine cranks but won't fire, which rules out the battery and starter
- Suspects: fuel pump, crank position sensor (P0335), or NATS immobilizer
- **Outcome not recorded**

!!! note "NATS and the Viper"
    A month later the September 2026 scan showed a past **P1615** (key
    mismatch). That is a NATS code, and it has been put down to the Viper's
    bypass connections. If the no-start was an immobilizer fault, the Viper
    wiring may have caused it as well. This is **unconfirmed**.

---

## May 2026: oil change {#2026-05}

The recommended spec is on [Procedures](02-procedures.md#oil-change). Check the
invoice to confirm what was installed.

---

## March 2026: limp mode {#2026-03}

The van would not accelerate past about 20 mph.

| Module | Codes |
| :----- | :---- |
| Engine (MAF) | P0100, P10F2, P100B, P100C, P2FBD |
| Engine (other) | P1130, P0041 |
| ABS / chassis | C0100, C010C, C010D, C0490. The wheel speed codes are likely left over from the lift |
| Body | B3F93, B2893 |
| Network | U3C41 |

**Repair:**

1. Replaced the accelerator pedal assembly. The pedal commander had been
   hiding the failure.
2. Replaced the MAF sensor, which **fixed it**. Use OEM Nissan **22680-7S000**
   rather than aftermarket.

After this work, run the [relearn sequence](02-procedures.md#relearn). A
throttle body replacement (about $800) was considered but was not needed.

---

## Outstanding Items

- [ ] Record what fixed the August 2026 no-start
- [ ] Confirm the oil and filter installed at the May 2026 change, and log each UOA result
- [ ] Decide whether to remove the pedal commander now that the pedal assembly is new
