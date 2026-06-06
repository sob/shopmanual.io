---
search:
  exclude: true
---

# Dakota Digital HDX Gauge System - Navigation Guide

## What's Here

Dakota Digital HDX instrumentation: control module, dashboard cluster, and 4 BIM expansion modules.

## Files

| File                      | Contains                                | Use When                                 |
| :------------------------ | :-------------------------------------- | :--------------------------------------- |
| `index.md`                | System architecture, power distribution | Finding power/wiring summary             |
| `01-hdx-control.md`       | Control box specs, BIM connectivity     | Finding BIM daisy-chain or config        |
| `02-dashboard-cluster.md` | HDX-96J-TJ gauge display                | Finding gauge ranges or display features |
| `03-bim-j1939.md`         | J1939 CAN interface                     | Understanding ECM data integration       |
| `04-bim-gps.md`           | GPS speedometer module                  | Finding antenna placement                |
| `05-bim-tpms.md`          | TPMS wireless sensors                   | Finding sensor installation              |
| `06-bim-compass.md`       | Compass/temperature module              | Finding temp probe mounting              |

## Cross-Section References

**Power:** PMU OUT9 (25A) → See `01-power-systems/04-pmu/03-pmu-outputs.md`

**Ground:** Firewall Stud Bus T4-5 → See `01-power-systems/05-grounding/02-firewall-stud-bus.md`

**CAN Bus:** Cummins J1939 → See `02-engine-systems/` ECM documentation

## When Updating

**Adding BIM module:** Create product page, update `index.md` architecture, update `01-hdx-control.md` daisy-chain

**Changing power source:** Update `index.md` and PMU outputs table
