---
hide:
  - toc
tags:
  - design-note
  - engine-systems
  - starter
  - keyless
search:
  exclude: false
---

# WAIT-to-Start Crank Lockout — Design Note (Deferred)

!!! warning "Status: NOT IMPLEMENTED — deferred by design"
    The build does **not** automatically lock out cranking during grid-heater
    preheat. The current design is **watch the lamp**: on a cold start the driver
    waits for the Cummins WAIT-to-Start lamp to extinguish before cranking — Digital
    Guard Dawg's own documented diesel start procedure. See [Starter System][starter]
    and [Keyless Ignition][keyless-ignition].

    This page preserves the full analysis so that, if an automatic lockout is ever
    revived, the design and the dead ends are already mapped out. It is intentionally
    **only linked from the [Starter System][starter] page** and is not in the main nav.

## Why it was deferred

An automatic lockout was evaluated in depth and set aside as **not worth the complexity** for this build:

- **Skipping the wait is harmless.** On a common-rail R2.8 the grid heater is an ECM-managed cold-start *aid*; cranking during preheat doesn't damage anything — worst case is a marginally harder fire. The WAIT lamp is advisory, not a protection interlock.
- **It's a 3–5 second wait, once per cold start** (per [Grid Heater][grid-heater]), and watching the lamp is the **manufacturer's documented diesel procedure**.
- **Every automatic option adds disproportionate cost** — parts, wiring, and/or coupling the start path to another module — to automate something a glance handles.
- **Direction of travel.** Critical systems (TCU, iBooster) are being moved *off* the PMU; adding the crank lockout *onto* the PMU runs against that.

## The requirement (if revived)

Block the crank signal while the WAIT lamp is on, ANDed with the PBS-I crank command, **without loading ECM Pin 35**:

- **WAIT signal:** ECM **Pin 35** (yellow), sink-circuit lamp topology — **active LOW** (~0 V when WAIT on, ~13 V off).[^wait-polarity]
- **Constraint:** the Pin 35 lamp-driver **sink-current rating is not published** in any public Cummins crate document, so a design must not lean on it. A relay coil on Pin 35 (~160 mA) was the original concern tracked as issue #117.[^pin35-rating]
- **AND logic:** crank only when the PBS-I is commanding START *and* WAIT is off.
- **Fail-safe:** any fault must default to **crank-enabled** (engine still starts).

## Options evaluated

| Approach | Auto? | Loads Pin 35? | Verdict |
| :------- | :---- | :------------ | :------ |
| Original Bosch changeover relay, coil on Pin 35 | ✅ | ❌ ~160 mA | Rejected — this is #117 |
| Confirm the Cummins sink rating on paper | — | — | Dead end — not in public docs |
| Bench-measure lamp + coil draw | — | — | Measures draw, not the limit — insufficient |
| Opto / SSR high-impedance buffer | ✅ | ✅ ~µA | Works, but it's loose electronics (rejected: error-prone, hard to troubleshoot) |
| Low-coil-current **plug-in** relay (~30 mA) | ✅ | ⚠️ ~30 mA | **Does not exist off-the-shelf** — plug-in automotive relays are all ~150 mA; low-power coils are PCB-mount only |
| Enclosed automotive SSR (MRS 1.069) | ✅ | ✅ | Doesn't fit — high-side output fights the series AND; "don't energize I/O unpowered" caution; 6.3 mm body |
| ISO 280 **micro** SSR (to fit BODY PDU sockets) | ✅ | ✅ | Doesn't exist — micro footprint is electromechanical-only |
| PBS-I built-in crank delay (~7 s) | ⏱️ timer | ✅ none | Blind timer, not lamp-sensed; covers typical preheat only |
| iKey Premier sensed wait (Pink wire, 18 s) | ✅ | ✅ | **Remote-start only** — not active for driver-present push-button start |
| **PMU-sensed gate relay** (see below) | ✅ | ✅ ~µA | The clean implementation if revived |
| **Watch the lamp** | ❌ manual | ✅ none | **Chosen** — zero parts, mfr procedure |

## Recommended implementation, if revived

A relay-based gate where the **PMU is only the sensor**, never in the crank path. This was fully worked out and is the design to resurrect:

```text
PMU In 4  ← ECM Pin 35 (WAIT lamp)        high-Z digital input → ~µA on Pin 35
PMU Out 24 → gate-relay coil+             (from +12, NOT Pin 35); coil− to cabin ground
relay NC   in series:  PBS-I PURPLE START → relay COM → NC → firewall Pin 15 → Cole Hersee coil+
```

- **PMU logic:** `IF In4_WaitToStart == LOW THEN Out24 = ON (block) ELSE OFF (pass)`.
- **Behavior:** WAIT on → PMU energizes relay → NC opens → crank blocked. WAIT off → relay drops → NC closed → start passes.
- **Zero Pin 35 load:** the PMU senses with a high-impedance input; the relay coil is driven from the PMU output, so the coil current never touches Pin 35 — a standard ~150 mA relay is fine.
- **Block-only:** the PMU drives the *relay coil*, not the starter solenoid, so it can only interrupt an already-authorized PBS-I crank, never command one.
- **Fail-safe, no bypass needed:** dead/unpowered PMU, failed Out 24, or open coil → relay de-energized → NC closed → PBS-I cranks. A dead PMU also stops the cooling fan, so the start path is never the limiting failure.

**Proposed I/O (both currently spare):** PMU **In 4** (WAIT sense) and **Out 24** (gate-relay coil, ~0.16 A). See [PMU Inputs][pmu-inputs] / [PMU Outputs][pmu-outputs].

**Parts:**

- Gate relay: any standard 12 V SPDT (changeover) automotive relay wired SPST-NC; NC contact carries only the ~0.69 A Cole Hersee coil. Mount cabin, adjacent to the PBS-I.
- (Optional limp-home, not required) a manual bypass across the relay's COM↔NC — a latching illuminated push-button such as the **Blue Sea 4160** (build standard) glowing when engaged, or simply a spare relay / a COM-NC jumpered "bypass plug" in the glovebox. The NC topology already self-enables on the common faults, so this is belt-and-suspenders.

## Why not the simpler-looking alternatives

- **No off-the-shelf "WAIT-gate" module exists.** Plug-in SSRs don't come in a form that does a fail-safe series AND of two 12 V signals, and low-coil-current relays only exist as PCB parts. Anything that gets Pin 35 to ~zero load while staying a finished, plug-in product ends up being the PMU (sensor) + relay (gate) above.
- **It can't live in the BODY PDU.** The Bussmann LR-2 uses ISO 280 micro relays (~150 mA coils → re-creates #117), and it's a high-side power panel, not a series-signal-gate host.

## Sources

[^wait-polarity]: **Active-low confirmed.** Cummins Repower R2.8 CM2220 R101B Installation Guide, Bulletin 5504137 (Jan 2018), §2 *Wiring Harness* / *Engine Indicator Lamps*: "Lamp, Wait To Start — Yellow — ECM pin 35"; lamps are fed +12 V from the keyswitch with the ECM "providing a path to ground via a sink circuit." Full schematic = Wiring Diagram Bulletin 5467560 (QuickServe Online). Also documented on [HDX Control][hdx-control].

[^pin35-rating]: The CM2220 lamp-driver sink-current rating is **not published** in the public crate documents (Installation Guide 5504137, spec flyer 5410825, Wiring Diagram 5467560, Lamp ID card 4971518) — same gap the grid-heater current carries. It would require Cummins QuickServe / Care to obtain. This is why a design that *senses* Pin 35 (high-Z) is preferred over one that *loads* it.

## Related Documentation

- [Starter System][starter] - The crank circuit this would gate (sole inbound link to this note)
- [Keyless Ignition][keyless-ignition] - PBS-I architecture and the current watch-the-lamp cold-start sequence
- [Grid Heater System][grid-heater] - R2.8 preheat duty cycle (3–5 s typical)
- [HDX Control][hdx-control] - ECM Pin 35 WAIT signal and its active-low sourcing

[starter]: 01-starter.md
[keyless-ignition]: ../05-control-interfaces/06-keyless-ignition.md
[grid-heater]: 07-grid-heater.md
[hdx-control]: 09-gauge-cluster/01-hdx-control.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
