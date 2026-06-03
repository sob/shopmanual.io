---
hide:
  - toc
---

# 1.7 Wire Routing & Physical Layout {#wire-routing}

## Wire Protection Standards

All wire runs require appropriate protection based on location and environment:

### Protection Methods

| Method              | Application                                 | Products                                        |
| :------------------ | :------------------------------------------ | :---------------------------------------------- |
| **Braided Sleeve (expandable)** | Preferred wrap for power runs and cabin/trunk bundles | PET expandable braid sized to bundle OD; plain or with a tracer stripe for harness ID — see [Protective Sleeve & Tracers][sleeve-convention] |
| **Split Loom**      | General protection, bundling multiple wires; short/branchy small-wire runs | 1/4" to 1" diameter, slit for easy installation |
| **Heat Sleeve**     | Engine bay, exhaust proximity               | Fiberglass sleeve rated 500°F+, 1/2" to 1"      |
| **Abrasion Sleeve** | Frame rail contact, sharp edges             | Braided nylon or polyester                      |
| **P-Clamps**        | Securing runs to frame/body                 | Rubber-lined, stainless steel                   |
| **Grommets**        | Firewall/body penetrations                  | Rubber with appropriate ID for wire bundle      |
| **Heat Shrink**     | Terminal connections, splice protection     | Adhesive-lined marine grade                     |
| **Spiral Wrap**     | Areas needing frequent access               | Allows wire additions without re-routing        |

### Protection by Location

| Location          | Primary Protection        | Secondary Protection       | Notes                                   |
| :---------------- | :------------------------ | :------------------------- | :-------------------------------------- |
| **Engine Bay**    | Heat sleeve               | Split loom                 | Within 12" of exhaust use heat sleeve   |
| **Frame Rails**   | Split loom                | P-clamps every 18"         | Abrasion sleeve at metal contact points |
| **Wheel Wells**   | Split loom                | Abrasion sleeve            | Water exposure - seal all connections   |
| **Under Vehicle** | Split loom                | P-clamps every 12"         | Maximum protection from road debris     |
| **Firewall**      | Grommets                  | Heat shrink at penetration | Seal grommets with RTV silicone         |
| **Interior**      | Split loom or spiral wrap | Minimal                    | Behind panels, minimal exposure         |

### High-Current Cable Protection

| Circuit                    | Wire Gauge | Protection Required                           |
| :------------------------- | :--------- | :-------------------------------------------- |
| Alternator → START battery | 2/0 AWG    | Heat sleeve (engine bay) → split loom (frame) |
| PMU power feed             | 2/0 AWG    | Heat sleeve entire run (engine bay exposure)  |
| BCDC inter-battery         | 4 AWG      | Split loom + P-clamps (under vehicle)         |
| Winch cables               | 1/0 AWG    | Split loom + abrasion sleeve (frame contact)  |
| Battery grounds            | 2/0 AWG    | Heat sleeve (engine) → split loom (frame)     |

---

## 🔧 Driver Rear Wheel Well (START Battery)

**High-current power distribution from START battery:**

| Circuit                       | Wire Gauge | Distance | Destination                         | Current        | Notes                                                |
| :---------------------------- | :--------- | :------- | :---------------------------------- | :------------- | :--------------------------------------------------- |
| **Alternator charging input** | 2/0 AWG    | 8 ft     | FROM Alternator (engine bay)        | 270A           | Charges START battery - see [Alternator][alternator] |
| **Starter motor power**       | 2/0 AWG    | 6 ft     | TO Starter motor (engine bay)       | 400-600A       | Brief cranking load - see [Starter][starter]         |
| **PMU24 power feed**          | 2/0 AWG    | 7 ft     | TO PMU24 (engine bay)               | 220A max       | Via 250A CB - see [PMU][pmu]                         |
| **BCDC input feed**           | 4 AWG      | 5-6 ft   | TO BCDC (passenger rear wheel well) | 50-55A         | Via 80A CB - see [BCDC][bcdc]                        |
| **Primary ground**            | 2/0 AWG    | 3 ft     | TO Rear frame rail                  | 600A+ peak     | Primary return path                                  |
| **Battery cross-ground**      | 1/0 AWG    | 5-6 ft   | TO AUX battery- (passenger)         | BCDC reference | Critical for BCDC operation                          |

**Routing:** Driver rear wheel well → up inside driver rear quarter sill → forward along **inside floor board / side wall (driver side)** → driver A-pillar area → driver-side firewall grommet → engine bay. Path is fully inside the body (no exposed frame rail). BCDC input (4 AWG) takes the H3 cross-cab path instead (under rear bench seat to passenger side).

---

## 🔋 Passenger Rear Wheel Well (AUX Battery)

**Power distribution from AUX battery:**

| Circuit                                | Wire Gauge | Distance | Destination                                       | Current             | Notes                                                                |
| :------------------------------------- | :--------- | :------- | :------------------------------------------------ | :------------------ | :------------------------------------------------------------------- |
| **Warn ZEON 10-S Winch power**       | 1/0 AWG    | 13 ft    | TO Front bumper winch                             | 250A typ, 409A peak | Direct connection (no CB) - see [Recovery Systems][recovery-systems] |
| **Warn ZEON 10-S Winch ground**      | 1/0 AWG    | 13 ft    | TO Winch motor ground                             | 250A typ, 409A peak | Return path - routing TBD                                            |
| **Forward feed (Firewall CONSTANT bus)** | 2/0 AWG  | ~13 ft   | TO Firewall CONSTANT Bus (cabin trunk)            | ~232A max           | Protected by 300A CB at battery - feeds SwitchPros, BODY PDU, Fusion |
| **SafetyHub local feed**               | 2 AWG      | ~2 ft    | TO SafetyHub 150 (local in wheel well)            | ~100A max           | Protected by 150A CB at battery                                      |
| **BCDC output**                        | 4 AWG      | Short    | FROM BCDC (local in wheel well)                   | 50A                 | Charging input to AUX battery                                        |
| **Primary ground**                     | 2/0 AWG    | 3 ft     | TO Rear frame rail                                | 569A peak           | Winch + accessories return                                           |
| **Cross-ground reference**             | 1/0 AWG    | 5-6 ft   | FROM START battery- (driver)                      | BCDC reference      | Critical for BCDC operation                                          |

**Routing:**

- **Forward feed (2/0 AWG) + Winch power/ground (2× 1/0 AWG) (H1):** Passenger rear wheel well → up inside passenger rear quarter sill → forward along **inside floor board / side wall (passenger side)** → A-pillar area → through passenger firewall (forward feed terminates at Firewall CONSTANT bus; winch cables continue to engine bay → grille → front bumper). Three heavy cables bundled together. Fully inside body, no exposed frame rail.
- **BCDC input + cross-ground reference (H3):** **Under the rear bench seat** cushion → passenger rear wheel well. Short, dry, physically protected.
- **SafetyHub local feed (2 AWG):** ~2 ft local in wheel well, no routing concern.

---

## ⚙️ Engine Bay

**Engine compartment wiring:**

| Circuit                   | Wire Gauge | Distance | Source                | Destination           | Current    | Notes                         |
| :------------------------ | :--------- | :------- | :-------------------- | :-------------------- | :--------- | :---------------------------- |
| **Alternator to battery** | 2/0 AWG    | 8 ft     | Alternator            | START battery+        | 270A       | See Driver Rear Wheel Well section |
| **Starter motor**         | 2/0 AWG    | 6 ft     | START battery+        | Starter motor         | 400-600A   | See Driver Rear Wheel Well section |
| **Engine block ground**   | 2/0 AWG    | 8 ft     | Engine block          | Engine bay ground bus | 600A+ peak | Starter/alternator return     |
| **Frame ground**          | 2/0 AWG    | 3 ft     | Engine bay ground bus | Front frame rail      | 600A+ peak | Chassis ground point          |

**BCDC Location:** Passenger rear wheel well (near AUX battery) - charges AUX battery from START battery/alternator

---

## 🏠 Firewall Cluster (Cabin Side, Passenger Area)

**Cabin distribution cluster mounted on the firewall** - co-located components fed by the 2/0 AWG forward feed from AUX battery:

| Component                              | Wire Gauge | Distance | Source/Destination                         | Notes                                           |
| :------------------------------------- | :--------- | :------- | :----------------------------------------- | :---------------------------------------------- |
| **Firewall CONSTANT Bus (input)**      | 2/0 AWG    | ~13 ft   | FROM AUX battery+ via 300A master CB       | Heavy feed via H1: passenger floor/side wall → A-pillar → firewall (resolved 2026-05-30) |
| **Bus → SwitchPros**                   | 2 AWG      | ~2 ft    | TO SwitchPros power module                 | Via 150A CB                                     |
| **Bus → BODY PDU**                     | 2 AWG      | ~2 ft    | TO BODY PDU                                | Via 100A CB                                     |
| **AUX bat → JL Audio MV800/8i Amp**    | 4 AWG      | ~3-4 ft  | TO MV800/8i amp (under rear seat)          | Via 100A CB at AUX battery (not via firewall bus) |
| **SwitchPros Ground Bus**              | 1 AWG      | ~3 ft    | TO chassis ground at firewall              | Lighting/aux load returns                       |
| **SwitchPros control cable**           | Multi-pin  | ~5 ft    | TO SwitchPros panel on dash                | Standard SwitchPros cable                       |
| **SwitchPros outputs (12 circuits)**   | Various    | TBD      | TO various loads (front/cabin/rear/roof)   | Mostly short forward fan-out from firewall      |

---

## 🚪 Firewall Penetrations

**Wire bundles passing through firewall:**

| Penetration | Location | Direction | Circuits | Wire Count | Notes |
|:------------|:---------|:----------|:---------|:-----------|:------|
| **Cummins Harness** | Factory location | Engine ↔ Cabin | Engine harness, J1939 CAN | Factory | Dedicated bulkhead connector |
| **Deutsch HDP24-24-29** | TBD (near PMU) | Bidirectional | All custom wiring | 17 | Single weatherproof connector |
| **Temp Probe Grommet** | Near grille | Cabin → Grille | BIM-17-2 temp sensor | 2 (22 AWG) | Small grommet, twisted pair |

!!! info "J1939 CAN Bus"
J1939 CAN High/Low wires tap into Cummins harness at firewall punch-through, then route to Dakota Digital 01-2-J1939 module on firewall HDPE panel (cabin side).

**Complete Details:** See [Firewall Ingress][firewall-ingress] for Deutsch HDP24-24-29 connector pinout and BOM

---

## 🏠 Cabin & Dashboard

**Interior wiring and controls:**

| Routing Path        | Circuits                              | Method      | Notes                      |
| :------------------ | :------------------------------------ | :---------- | :------------------------- |
| **Dash → Console**  | Switch panels, USB, radio             | TBD         | Under dash routing         |
| **Firewall → Dash** | Dakota Digital cluster, CT4, controls | Behind dash | Main instrument panel area |

**Dakota Digital Firewall Panel (Cabin Side):**

| Component    | Function             | External Connections                            |
| :----------- | :------------------- | :---------------------------------------------- |
| 01-2-J1939   | J1939 CAN interface  | CAN High/Low from Cummins harness (engine side) |
| GPS-50-2     | GPS speed sensor     | Antenna (dash/windshield mount)                 |
| BIM-22-3     | TPMS module          | Wireless (no external wiring)                   |
| BIM-17-2     | Compass/outside temp | Temp probe (through firewall to grille)         |
| Main harness | BIM/IO cable         | Dakota Digital cluster in dash                  |

**Panel Location:** TBD - firewall behind dashboard
**Mounting:** TBD - HDPE sheet dimensions and fasteners

---

## 📦 Cargo & Rear

**Rear area wiring:**

| Routing Path                     | Circuits                         | Method         | Notes                         |
| :------------------------------- | :------------------------------- | :------------- | :---------------------------- |
| **Cab → Cargo**                       | Rear lights, compressor, lockers | TBD | Under seats or floor channels |
| **Passenger rear wheel well → Cargo** | SwitchPros rear outputs          | TBD | Rear auxiliary power (avoid exposed frame rail) |

---

## 🌐 Roof & Exterior

**External and overhead wiring:**

| Routing Path       | Circuits                          | Method              | Notes                      |
| :----------------- | :-------------------------------- | :------------------ | :------------------------- |
| **Roof/Roll bar**  | Light bars, dome lights           | TBD                 | A-pillar or along roll bar |
| **Front exterior** | Turn signals, offroad lights      | Engine bay to front | SwitchPros outputs         |
| **Rear exterior**  | Tail/brake/reverse, license plate | Cargo to rear       | PMU and SwitchPros outputs |

---

## Ground Points Summary

**Primary grounding locations - see [Section 1.5 - Grounding Architecture][grounding] for complete details:**

| Location                      | Ground Bus            | Wire Gauge | Connections                                           | Notes                     |
| :---------------------------- | :-------------------- | :--------- | :---------------------------------------------------- | :------------------------ |
| 🔧 **Driver rear wheel well**      | Engine bay ground bus | 2/0 AWG    | START battery-, engine block, frame rail, AUX battery | Primary ground hub        |
| 🔋 **Passenger rear wheel well**   | Rear frame rail       | 2/0 AWG    | AUX battery-                                          | AUX battery ground point  |
| 🏠 **Firewall (cabin side)**  | Firewall stud bus     | 4 AWG max  | Body electronics, sensors                             | Cabin electronics ground  |
| ⚙️ **Firewall (engine side)** | Engine bay ground bus | Various    | PMU, controllers, accessories                         | Engine bay ground hub     |
| 🌐 **SwitchPros controller**  | SwitchPros ground bus | 1 AWG      | Lighting/aux loads                                    | Dedicated lighting ground |

---

## Related Documentation

- [Harness Inventory][harness-inventory] - Fabricatable harness overview (H1–H9): summary, harness map, bundle interference assessment, and optimization notes
- [Build Sheet — Power Distribution][power-build] - H1, H2, H3 with tub-map diagram
- [Build Sheet — Lighting & SwitchPros][lighting-build] - H4, H5 with tub-map diagram
- [Build Sheet — Controls, Recovery & Drivetrain][controls-build] - H6–H9 with tub-map diagram
- [Grounding Architecture][grounding] - Complete grounding system design
- [START battery Distribution][starter-battery] - Driver rear wheel well power
- [AUX battery Distribution][aux-battery] - Passenger rear wheel well power
- [PMU][pmu] - Power management unit
- [SafetyHub][safetyhub] - Fused distribution
- [BCDC][bcdc] - DC-DC charger
- [Alternator][alternator] - Charging system routing
- [Starter][starter] - Starter motor routing
- [Firewall Ingress][firewall-ingress] - Detailed firewall penetrations and grommet specifications
- [Recovery Systems][recovery-systems] - Winch installation and wiring

[harness-inventory]: 03-harness-inventory.md
[power-build]: 04-harness-power-distribution.md
[lighting-build]: 05-harness-lighting-switchpros.md
[controls-build]: 06-harness-controls-recovery-drivetrain.md
[sleeve-convention]: 03-harness-inventory.md#sleeve-convention

[grounding]: ../05-grounding/index.md
[starter-battery]: ../02-starter-battery-distribution/index.md
[aux-battery]: ../03-aux-battery-distribution/index.md
[pmu]: ../04-pmu/index.md
[safetyhub]: ../03-aux-battery-distribution/04-safetyhub.md
[bcdc]: ../01-power-generation/03-bcdc.md
[alternator]: ../01-power-generation/02-alternator.md
[starter]: ../../02-engine-systems/01-starter.md
[firewall-ingress]: 02-firewall-ingress.md
[recovery-systems]: ../../08-exterior-systems/01-winch.md
