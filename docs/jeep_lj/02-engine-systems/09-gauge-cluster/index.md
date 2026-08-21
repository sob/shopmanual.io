---
hide:
  - toc
---

# 2.9 Dakota Digital HDX Gauge System {#dakota-digital-gauge-cluster}

## Overview

Complete digital instrumentation system replacing factory TJ gauge cluster. HDX control module processes sensor inputs and BIM module data to drive analog/digital hybrid dashboard display.

**Power:** [PMU OUT9][pmu-outputs] (25A capacity, ~25A worst-case, ~12A typical). Expansion modules are bus-powered via the BIM/IO daisy-chain (no separate feed) and their draw is included in this budget — Dakota Digital publishes no per-module current for these data modules (only power modules like the BIM-RGB, 7.4A, list a figure).

**Mounting:** Dashboard cluster in factory location, HDX control + BIM modules on HDPE firewall panel

## System Components

**Core:**

- [HDX Control Module][hdx-control] - Main control box with Bluetooth configuration
- [Dashboard Cluster][dashboard-cluster] - HDX-96J-TJ analog/digital display (black background)

**Expansion Modules:**

- [BIM-01-2-J1939][bim-j1939] - J1939 CAN interface for ECM data
- [GPS-50-2][bim-gps] - GPS speedometer/compass/altimeter
- [BIM-22-3][bim-tpms] - Tire pressure monitoring (4× wireless sensors)
- [BIM-17-2][bim-compass] - Compass/outside temperature

## Related Documentation

- [PMU Outputs][pmu-outputs] - Power source (OUT9, 25A)
- [Grounding Architecture][grounding] - Ground connections
- [Firewall Ingress][firewall-ingress] - Wire routing
- [Cummins R2.8 ECM][ecm] - J1939 integration

[hdx-control]: 01-hdx-control.md
[dashboard-cluster]: 02-dashboard-cluster.md
[bim-j1939]: 03-bim-j1939.md
[bim-gps]: 04-bim-gps.md
[bim-tpms]: 05-bim-tpms.md
[bim-compass]: 06-bim-compass.md
[pmu-outputs]: ../../01-power-systems/04-pmu/03-pmu-outputs.md
[grounding]: ../../01-power-systems/05-grounding/index.md
[firewall-ingress]: ../../01-power-systems/07-wire-routing/02-firewall-ingress.md
[ecm]: ../index.md
