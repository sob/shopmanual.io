---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - horn
---

# 2.5 Horn System {#horn}

/// html | div.product-info

**Type:** Horn

**Part:** Supplied with the SwitchPros [CT4 Turn Signal & Accessory Kit][ct4] (purchased; replaces the planned PIAA 85115)

**Mounting:** Engine bay, on the kit's bracket

**Power Source:** PMU Out 18 (7A capacity, CONSTANT)

///

## Specifications

- **Current draw:** {{ tbd(326) }} — PMU Out 18 keeps the previous 5.4A budget until measured
- **Polarity:** Not polarity-sensitive[^kit-horn]
- **Ground:** Chassis ground (engine bay)

The kit wires this horn to CT4 SW3. This build uses SW3 for the low beams, so the horn runs from PMU Out 18 instead and keeps the steering-wheel button below.

## Control

**Button:** Momentary push button (normally open) on steering wheel PTT bracket

**PMU Configuration:**

- Input: In 1 (horn button signal)
- Output: Out 18 (7A capacity, powers horns directly)
- Logic: When In 1 closes, Out 18 activates (no external relay needed)
- Power: CONSTANT (works with ignition off for safety)

## Wiring Configuration

```text
START battery CONSTANT → PMU → Out 18 → CT4 kit horn → Chassis Ground
                          ↑
                      Horn Button → In 1 (trigger)  [column path undefined — {{ tbd(152) }}]
```

## Outstanding Items

{{ tbds() }}

[install-checklist]: ../09-installation/02-engine-systems-checklist.md

## Related Documentation

- [PMU Outputs][pmu-outputs] - PMU Out 18 circuit and programming
- [START Battery Distribution][starter-battery-distribution] - Inline CBs (250A PMU, 80A BCDC)
- [Firewall Ingress][firewall-ingress] - Horn button trigger wire routing

[ct4]: ../05-control-interfaces/03-command-touch-ct4.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[starter-battery-distribution]: ../01-power-systems/02-starter-battery-distribution/index.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md

[^kit-horn]: SwitchPros *Command-Touch CT4* manual, Rev. 1.0091524 — p.5 (step 8: secure the horn with the supplied bracket and connect it; "polarity does not matter") and p.6 (wiring diagram: Orange SW3 = horn). <https://www.switchpros.com/wp-content/uploads/CT4-Rev-1.0.pdf>
