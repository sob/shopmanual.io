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

Push-button ignition for the Cummins R2.8 + 8HP70 build. Replaces the factory keyswitch entirely. Self-contained Digital Guard Dawg PBS-I handles RFID immobilizer, brake interlock, and ACC/IGN/START sequencing internally. On a cold start the driver waits for the Cummins WAIT-to-Start lamp to extinguish before cranking — Digital Guard Dawg's documented diesel start procedure. PMU is not involved.

## Architecture

/// html | div.product-info

**Module:** Digital Guard Dawg PBS-I (Intelligent Push Button Start)

**Type:** Self-contained RFID push-button start/stop; onboard 60A relays (IGN, START, ACC1, ACC2)

**Mounting:** On the Dakota Digital HDPE panel under the dash, co-located with the HDX control module (vendor mandate: cabin only, never engine bay)

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
| Mounting | **Dakota Digital HDPE panel, under dash** — co-located with the HDX control module (panel detailed in the [HDX Control][hdx-control] plan). Vendor mandate: cabin only, never engine bay |
| Kit Contents | ICM + 2 iTag fobs + Start Button (36" pre-wired harness) + Programming Button + Bypass Card + 4-digit PIN |

### Cole Hersee 24213 Solenoid

Unchanged from existing starter design. See [Starter System][starter].

## Daily Start Sequence

**Warm engine (no preheat cycle):**

1. Approach vehicle — iTag fob in pocket — Start Button LED illuminates
2. Press brake pedal — Start Button LED begins flashing
3. Press and hold Start Button — starter cranks immediately, release on engine start

**Cold engine (grid heater active):**

1. Approach — fob recognized — Start Button LED illuminates
2. Press Start Button twice (no brake) → IGN energizes → ECM powers up → grid heater runs → WAIT-to-Start lamp illuminates
3. Wait ~3-5 seconds (per [Grid Heater][grid-heater]) for the WAIT-to-Start lamp to extinguish
4. Press brake + press and hold Start Button → starter cranks
5. Release on engine start

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
| PURPLE | Starter Out (60A) | PBS-I module | Firewall Pin 15 → Cole Hersee 24213 coil+ | Cranks while button held |
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
| Start Button | Pre-wired 36" harness → PBS-I side port | Mounts at the factory keyswitch location on the dash (within the 36" harness reach of the panel); included in kit |
| Programming Button | Pre-wired harness → PBS-I side port | Stash under dash or in trunk; needed only for fob-learn and emergency bypass PIN entry |

### Firewall Crossings

Two PBS-I outputs need to cross the firewall from cabin (PBS-I location) to engine bay:

| Signal | Direction | Approximate Current | Notes |
| :----- | :-------- | :------------------ | :---- |
| Ignition signal (outbound from cabin bus bar) | Cabin → EB (HDP24 Pin 12) | ~5A typical (ECM + PMU Pin 7) | 14 AWG; feeds ECM Pin 41 (black, via **5A inline fuse**[^ecm-fuse]) and PMU Pin 7 |
| PURPLE START | Cabin → EB (HDP24 Pin 15) | ~0.69A (Cole Hersee coil)[^ch-coil] | 16 AWG sufficient; drives Cole Hersee 24213 coil+ during crank only |

See [Firewall Ingress][firewall-ingress] for pin assignments.

## Why Not the Engine-Running Lockout or P/N Interlock Relay?

Earlier iterations of this design included a discrete engine-running lockout relay and a P/N interlock relay in series with the starter coil. Both were removed in favor of simpler, layered protection:

- **Brake interlock** is built into PBS-I (Accessory Harness Brake input).
- **Engine-running protection** relies on the starter's Bendix overrunning clutch plus the deliberate brake + button-hold required to crank — accidental restart of a running engine takes two-handed misuse.
- **P/N interlock** is provided by the 8HP70 + Turbolamik: the transmission can't leave Park without brake pressed, and the vehicle is always in Park at start time. The Turbolamik P/N aux output can inhibit the start signal in a future phase if needed (documented, unused today).

## Diesel Runaway Note

Normal engine shutdown (press brake + 2 sec button hold) drops PBS-I's PINK IGN output, cutting ECM power — but that alone can't stop a runaway sustained by oil or hydrocarbon vapor. See [Diesel Runaway Protection][runaway-protection] for the independent mechanical defense (catch can + AMOT air shutoff).

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [Starter System][starter] - Cole Hersee 24213 and PBS-I PURPLE START → coil chain
- [Ignition Signal Distribution][ignition-signal] - PBS-I PINK IGN feeds the bus bar
- [HDX Control][hdx-control] - ECM Pin 35 WAIT/EX signal (dash display)
- [Grid Heater System][grid-heater] - R2.8 grid heater duty cycle (3-5 sec typical)
- [Firewall Ingress][firewall-ingress] - PBS-I pin assignments

[^pbs-i-specs]: Onboard relay ratings (4× 60A), 300A inrush capacity, and kit contents per the Digital Guard Dawg PBS-I install manual ([PBS-I Manual PDF][pbs-i-manual]) and product page ([Digital Guard Dawg PBS-I][pbs-i]).

[^ch-coil]: Cole Hersee 24213 coil draw ~0.69A (17.5 Ω @ 12V) per the Littelfuse datasheet — see the `[^ch-24213]` footnote in [Starter System][starter]. Supersedes the earlier unsourced "~1.6A" figure that appeared in pre-merge drafts.

[^ecm-fuse]: **Confirmed.** Cummins Repower R2.8 CM2220 R101B Installation Guide, Bulletin 5504137 (Jan 2018), §2 *Wiring Harness* (pp. 2-19/2-20): the keyswitch feed to the ECM is **Pink, ECM pin 41**, with a **5 amp inline fuse** (Figure 2, item 3: *"Keyswitch – pink, 5 amp inline fuse"*). The guide requires this *"pink 5 amp wire … provide a minimum of 12 volts in the run position and during engine cranking."* Supersedes the unverified "document 0042728" cited in pre-merge drafts.

[pbs-i]: https://www.digitalguarddawg.com/keyless-ignition/automotive/pbs-i
[pbs-i-manual]: https://cdn.shopify.com/s/files/1/0896/8005/2530/files/PBS-I-Manual.pdf
[tbd-tracker]: ../tbd-tracker.md
[starter]: ../02-engine-systems/01-starter.md
[ignition-signal]: ../01-power-systems/06-ignition-signal/index.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[runaway-protection]: ../02-engine-systems/11-runaway-protection.md
[hdx-control]: ../02-engine-systems/09-gauge-cluster/01-hdx-control.md
[grid-heater]: ../02-engine-systems/07-grid-heater.md
