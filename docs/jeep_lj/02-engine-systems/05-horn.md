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
![PIAA 85115 Superior Bass Horn](../images/piaa-85115-horn.jpg){ loading=lazy }

**Type:** Dual Tone Horns

**Model:** 85115

**Part Number:** 85115

**Manufacturer:** PIAA

**Product Page:** [PIAA Superior Bass Horn 85115][piaa-horns]

**Mounting:** Engine bay

**Power Source:** PMU Out 18 (7A capacity, CONSTANT)

///

## Specifications

- **Current draw:** 2.7A per horn × 2 = 5.4A total
- **Ground:** Chassis ground (engine bay)

## Control

**Button:** Momentary push button (normally open) on steering wheel PTT bracket

**PMU Configuration:**

- Input: In 1 (horn button signal)
- Output: Out 18 (7A capacity, powers horns directly)
- Logic: When In 1 closes, Out 18 activates (no external relay needed)
- Power: CONSTANT (works with ignition off for safety)

## Wiring Configuration

```text
START battery CONSTANT → PMU → Out 18 → PIAA Horns (5.4A) → Chassis Ground
                          ↑
                      Horn Button → In 1 (trigger)
```

**Power Flow:**

1. START battery+ → 250A inline CB → PMU
2. Horn button (steering wheel) → PMU In 1 (trigger signal)
3. PMU Out 18 activated when In 1 closes
4. PMU Out 18 → PIAA horns (5.4A) → chassis ground (engine bay)

**Notes:**

- PMU Out 18 switches directly (no external relay needed)
- Works with ignition off (CONSTANT power for safety)

## Outstanding Items

None - design complete. See [installation checklist][install-checklist] for build tasks.

[install-checklist]: ../09-installation/02-engine-systems-checklist.md

## Related Documentation

- [PMU Outputs][pmu-outputs] - PMU Out 18 circuit and programming
- [START Battery Distribution][starter-battery-distribution] - Inline CBs (250A PMU, 80A BCDC)
- [Firewall Ingress][firewall-ingress] - Horn button trigger wire routing

[piaa-horns]: https://www.piaa.com/product/85115/
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[starter-battery-distribution]: ../01-power-systems/02-starter-battery-distribution/index.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
