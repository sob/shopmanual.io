---
hide:
  - toc
tags:
  - product-details
  - control-interfaces
  - ignition
  - keyless
  - pbs-i
---

# 5.6 Keyless Ignition System {#keyless-ignition}

Push-button ignition for the Cummins R2.8 + 8HP70 build. Replaces the factory keyswitch entirely. Self-contained Digital Guard Dawg PBS-I handles RFID immobilizer, brake interlock, and ACC/IGN/START sequencing internally. One external SPST relay gates cranking through the diesel wait-to-start lamp so cold-day starts auto-wait for grid heater preheat. PMU is not involved.

## Architecture

/// html | div.product-info

**Module:** Digital Guard Dawg PBS-I (Intelligent Push Button Start)

**Type:** Self-contained RFID push-button start/stop; onboard 60A relays (IGN, START, ACC1, ACC2)

**Mounting:** Cabin, under dash (vendor mandate: not in engine bay)

**Product Page:** [Digital Guard Dawg PBS-I][pbs-i]

**Install Manual:** [PBS-I Manual PDF][pbs-i-manual]

///

## Components

### Digital Guard Dawg PBS-I

| Specification | Value |
| :------------ | :---- |
| Type | RFID push-button start, self-contained |
| Onboard Relays | 4× 60A[^pbs-i-specs] (IGN, START, ACC1 drops during crank, ACC2 stays on during crank) |
| Inrush Capacity | 300A[^pbs-i-specs] |
| Supply Voltage | 12V DC |
| Detection Range | ~10 ft (iTag fob) |
| Auto-arm | 60 sec after fob leaves range |
| Module Dimensions | ~5.5" × 3" × 1.25" |
| Wiring | Heavy-duty Molex high-current connectors, 12 GA bus wiring |
| Mounting | **Cabin, under dash** (vendor mandate: do NOT mount in engine bay) |
| Kit Contents | ICM + 2 iTag fobs + Start Button (36" pre-wired harness) + Programming Button + Bypass Card + 4-digit PIN |

### WAIT-gate Relay

Single SPST automotive relay with normally-closed contacts. Blocks PBS-I's START output from reaching the Cole Hersee coil while the Cummins WAIT-to-Start lamp is illuminated.

The Cummins R2.8 ECM uses a **sink-circuit lamp topology**: keyswitch +12V → lamp → ECM Pin 35 (yellow) → ECM internal sink to ground when condition is active. The WAIT signal at Pin 35 is therefore **active LOW** (~0V when WAIT lamp on, ~+12V when WAIT lamp off).[^wait-polarity]

| Specification | Value |
| :------------ | :---- |
| Type | 5-pin SPDT changeover, used as SPST-NC (30/87a wired, 87 unused); 30A NO / 20A NC contacts[^wait-relay] |
| Coil | 12V DC, ~160 mA |
| Coil+ | Switched +12V (tap from ignition signal bus bar — same source as the WAIT lamp itself) |
| Coil- | ECM Pin 35 (yellow WAIT-to-Start wire) tap on cabin side (shared with HDX WAIT/EX input) |
| Contacts | NC (87a); closed when coil de-energized (WAIT lamp off), opens when coil energized (WAIT lamp on) |
| Mounting | Cabin, adjacent to PBS-I |
| Part | **Bosch 0332209150** (superseded by 0986332400) — 5-pin changeover[^wait-relay] |

### Cole Hersee 24213 Solenoid

Unchanged from existing starter design. See [Starter System][starter].

## Daily Start Sequence

**Warm engine (no preheat cycle):**

1. Approach vehicle — iTag fob in pocket — Start Button LED illuminates
2. Press brake pedal — Start Button LED begins flashing
3. Press and hold Start Button — starter cranks immediately, release on engine start

**Cold engine (grid heater active):**

1. Approach — fob recognized — Start Button LED illuminates
2. Press brake + press and hold Start Button
3. PBS-I energizes PINK IGN immediately → ECM powers up → grid heater runs → WAIT-to-Start lamp illuminates
4. PBS-I asserts PURPLE START, but WAIT-gate relay holds it open while WAIT lamp on — **keep holding button**
5. ~3-5 seconds later (per [Grid Heater][grid-heater]), WAIT lamp extinguishes → WAIT-gate relay NC closes → starter cranks
6. Release on engine start

**Shut off:** Press brake + press and hold Start Button for 2 seconds.

**Accessory-only mode** (e.g., radio without engine): press button once without brake — ACC2 energizes. Second press adds ACC1 + IGN.

**Emergency bypass** (lost or damaged fob): Use Programming Button + 4-digit PIN from the Bypass Card stored in wallet. See [PBS-I Manual][pbs-i-manual].

## Wiring

### PBS-I Power Harness (6 wires)

| Wire | Function | Source | Destination | Notes |
| :--- | :------- | :----- | :---------- | :---- |
| RED | +12V Battery | Critical Cabin PDU (CONSTANT) | PBS-I module | 14 AWG; ~50 mA standby ({{ tbd(84) }}) |
| BLACK | Chassis Ground | Cabin ground bus | PBS-I module | 14 AWG |
| PINK | 1st Ignition Out (60A) | PBS-I module | Ignition signal bus bar (cabin), Stud 1 | Does NOT drop during crank; bus bar Stud 2 outbounds to ECM Pin 41 via 5A inline fuse[^ecm-fuse] |
| PURPLE | Starter Out (60A) | PBS-I module | WAIT-gate relay common (NC input) | Cranks while button held |
| PINK/BLK | Accessory 1 (60A) | PBS-I module | **[Reserve]** | Drops during crank |
| BROWN | Accessory 2 (60A) | PBS-I module | **[Reserve]** | Stays on during crank |

### PBS-I Accessory Harness (2 wires used)

| Wire | Function | Source | Destination | Notes |
| :--- | :------- | :----- | :---------- | :---- |
| BROWN | Brake (+) input | Stop-lamp switch cold side | PBS-I Brake input | T-tap shared with PMU In 2 and Turbolamik brake input |
| PURPLE | Ground upon Disarm | PBS-I module | **[Reserve]** | Active-low fob-present signal; available for future use |

### Start and Programming Buttons

| Connector | Connection | Notes |
| :-------- | :--------- | :---- |
| Start Button | Pre-wired 36" harness → PBS-I side port | Dash mount; included in kit |
| Programming Button | Pre-wired harness → PBS-I side port | Stash under dash or in trunk; needed only for fob-learn and emergency bypass PIN entry |

### WAIT-Gate Relay

| Wire | Source | Destination | Notes |
| :--- | :----- | :---------- | :---- |
| Coil (+) | Switched +12V tap (ignition signal bus bar terminal) | WAIT-gate relay coil+ | Same source that powers the WAIT lamp |
| Coil (-) | WAIT-gate relay coil- | T-tap on ECM Pin 35 wire (cabin side, shared with HDX WAIT/EX input) | Active-low sink path; ECM grounds this wire when WAIT lamp on |
| Contact COM | PBS-I PURPLE START | WAIT-gate relay COM terminal | |
| Contact NC | WAIT-gate relay NC terminal | Firewall Pin 15 → Cole Hersee 24213 coil+ | Closed when WAIT off; opens when WAIT on |

See [HDX Control][hdx-control] for the existing WAIT/EX wiring on the cabin side.

### Firewall Crossings

Two PBS-I outputs need to cross the firewall from cabin (PBS-I location) to engine bay:

| Signal | Direction | Approximate Current | Notes |
| :----- | :-------- | :------------------ | :---- |
| Ignition signal (outbound from cabin bus bar) | Cabin → EB (HDP24 Pin 12) | ~5A typical (ECM + PMU Pin 7) | 14 AWG; feeds ECM Pin 41 (black, via **5A inline fuse**[^ecm-fuse]) and PMU Pin 7 |
| WAIT-gated PURPLE | Cabin → EB (HDP24 Pin 15) | ~0.69A (Cole Hersee coil)[^ch-coil] | 16 AWG sufficient; drives Cole Hersee 24213 coil+ during crank only |

See [Firewall Ingress][firewall-ingress] for pin assignments.

## Why Not the Engine-Running Lockout or P/N Interlock Relay?

Earlier iterations of this design included a discrete engine-running lockout relay and a P/N interlock relay in series with the starter coil. Both were removed in favor of simpler, layered protection:

- **Brake interlock** is built into PBS-I (Accessory Harness Brake input).
- **Engine-running protection** relies on the starter's Bendix overrunning clutch plus the deliberate brake + button-hold required to crank — accidental restart of a running engine takes two-handed misuse.
- **P/N interlock** is provided by the 8HP70 + Turbolamik: the transmission can't leave Park without brake pressed, and the vehicle is always in Park at start time. The Turbolamik P/N aux output can inhibit the start signal in a future phase if needed (documented, unused today).

## Diesel Runaway Note

Normal engine shutdown (press brake + 2 sec button hold) drops PBS-I's PINK IGN output, cutting ECM power. However, ECM-only kill does not stop a runaway sustained by oil or hydrocarbon vapor. Independent mechanical protection is provided by the Mishimoto catch can (prevention) plus the AMOT 4261M air shutoff valve with dash-mounted manual cable (termination). See [Diesel Runaway Protection][runaway-protection].

## Outstanding Items

{{ tbds() }}

## Build Tasks

- [ ] Confirm the WAIT-gate relay coil (~150 mA) in parallel with the dash WAIT lamp does not exceed the ECM lamp-driver sink rating (Pin 35 polarity itself is confirmed active-low per Cummins 5504137 — see [^wait-polarity]). If marginal, drive the relay from the lamp's keyswitch side or use a higher-impedance/solid-state relay
- [ ] Order Digital Guard Dawg PBS-I kit (includes ICM, 2 fobs, Start Button, Programming Button, Bypass Card, harnesses)
- [ ] Add 5A inline fuse on the ignition (keyswitch) feed to ECM Pin 41 — pink wire, per Cummins 5504137 (see [^ecm-fuse])
- [ ] Select PBS-I module mounting location (cabin under-dash, away from heat and water)
- [ ] Select Start Button dash mounting position (within easy reach of driver)
- [ ] Select Programming Button storage location (hidden but accessible)
- [ ] Verify PBS-I quiescent current draw to add to START battery parasitic budget

## Related Documentation

- [Starter System][starter] - Cole Hersee 24213 and PBS-I PURPLE → WAIT-gate → coil chain
- [Ignition Signal Distribution][ignition-signal] - PBS-I PINK IGN feeds the bus bar
- [HDX Control][hdx-control] - WAIT/EX signal source for the gate relay
- [Grid Heater System][grid-heater] - R2.8 grid heater duty cycle (3-5 sec typical)
- [Firewall Ingress][firewall-ingress] - PBS-I pin assignments

[^pbs-i-specs]: Onboard relay ratings (4× 60A), 300A inrush capacity, and kit contents per the Digital Guard Dawg PBS-I install manual ([PBS-I Manual PDF][pbs-i-manual]) and product page ([Digital Guard Dawg PBS-I][pbs-i]).

[^wait-relay]: **Bosch 0332209150** — 5-pin SPDT *changeover* mini-relay, 12V, 30A NO / **20A NC**, ~160 mA coil (Bosch/Amazon listing, accessed 2026-06-03; superseded by **0986332400**). This circuit energizes the coil to *open* the start path (WAIT lamp on → coil energized → contacts open), so it must use the **NC (87a)** contact — which requires a changeover relay. The earlier "suggested" parts were both wrong for this: Bosch **0332019150** is a twin-87 NO-only relay (no 87a terminal) and Hella **4RA** is an SPST make-only series — neither has an NC contact. The NC side here carries only the Cole Hersee 24213 coil (~0.69A), far under the 20A NC rating. Equivalent changeover relays (Hella **4RD** series, Tyco/TE V23234) are acceptable substitutes.

[^ch-coil]: Cole Hersee 24213 coil draw ~0.69A (17.5 Ω @ 12V) per the Littelfuse datasheet — see the `[^ch-24213]` footnote in [Starter System][starter]. Supersedes the earlier unsourced "~1.6A" figure that appeared in pre-merge drafts.

[^ecm-fuse]: **Confirmed.** Cummins Repower R2.8 CM2220 R101B Installation Guide, Bulletin 5504137 (Jan 2018), §2 *Wiring Harness* (pp. 2-19/2-20): the keyswitch feed to the ECM is **Pink, ECM pin 41**, with a **5 amp inline fuse** (Figure 2, item 3: *"Keyswitch – pink, 5 amp inline fuse"*). The guide requires this *"pink 5 amp wire … provide a minimum of 12 volts in the run position and during engine cranking."* Supersedes the unverified "document 0042728" cited in pre-merge drafts.

[^wait-polarity]: **Confirmed active-low.** Cummins Repower R2.8 CM2220 R101B Installation Guide, Bulletin 5504137 (Jan 2018), §2 *Wiring Harness* / *Engine Indicator Lamps* (pp. 2-19 → 2-24): the Circuit Wiring table lists **Lamp, Wait To Start — Yellow — ECM pin 35**, and the guide states *"The lamp circuits require power from the keyswitch to each lamp, with the ECM providing a path to ground via a sink circuit as engine conditions dictate"* and *"The ECM will enable a grounding path for the warning light to illuminate."* Pin 35 is therefore active-low (ECM sinks to ground when WAIT is active), validating the WAIT-gate relay logic above. The full schematic is the separate **R2.8 CM2220 R101B Wiring Diagram, Bulletin 5467560** (QuickServe Online). Supersedes the unverified "document 0042728" cited in pre-merge drafts. Note: the relay taps ECM Pin 35 directly, so it is governed by this Cummins spec — independent of the HDX *cluster-input* polarity question in [HDX Control][hdx-control].

[pbs-i]: https://www.digitalguarddawg.com/keyless-ignition/automotive/pbs-i
[pbs-i-manual]: https://cdn.shopify.com/s/files/1/0896/8005/2530/files/PBS-I-Manual.pdf
[tbd-tracker]: ../tbd-tracker.md
[starter]: ../02-engine-systems/01-starter.md
[ignition-signal]: ../01-power-systems/06-ignition-signal/index.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
[hdx-control]: ../02-engine-systems/09-gauge-cluster/01-hdx-control.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
