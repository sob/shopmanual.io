---
hide:
  - toc
tags:
  - product-details
  - power-distribution
  - relay-panel
---

# 1.3.3 BODY PDU {#body-rtmr}

/// html | div.product-info
![Bussmann LR-2 BODY PDU](../../images/bussmann-lr2-body-pdu.jpg){ loading=lazy }

**Type:** Military-Spec Relay/Circuit Breaker Panel

**Model:** Bussmann LR-2

**Part Number:** 301-1C-C-R1 (NSN: 6110-01-523-6374)

**Manufacturer:** Bussmann (Eaton)

**Source:** Military surplus (MRAP/LMTV truck)

**eBay Listing:** [Bussmann LR-2 Relay Breaker Block][ebay-listing]

**Mounting:** Firewall - body side (cabin), passenger side

**Power Source:** Firewall CONSTANT bus via 100A CB (2 AWG, ~2 ft local — bus is fed from AUX battery through 300A master CB and 2/0 AWG forward feed)

**Ground:** [Firewall Stud Bus][firewall-stud-bus] Terminal 3 (14 AWG) - relay coil/logic reference only

**Configuration:** 8 circuit breaker positions + 8 relay positions

**Input:** Military-spec power studs (accepts up to 2 AWG wire)

**Output:** J301-J306 Metri-Pack connectors (military-spec sealed)

**Protection:** IP65+ sealed military-grade enclosure

**Temperature Rating:** Military spec (-40°F to 221°F typical)

**Voltage:** 12V DC (originally 12V/24V dual voltage)

///

## Circuit Breaker Configuration

| CB Position | Original Military Label | Repurposed Circuit          | Size | Gauge | Load                  | Relay | Notes                                       |
| :---------- | :---------------------- | :-------------------------- | :--- | :---- | :-------------------- | :---- | :------------------------------------------ |
| CB30        | CHEM DETECT             | Fusion Head Unit            | 15A  | 14AWG | ~15A                  | -     | CONSTANT power, ignition sense from bus bar |
| CB48        | ARCT CRAN               | USB Charging Ports          | 20A  | 14AWG | ~13A                  | -     | 2x Powerwerx PanelUSB-75W (78W each, 7.5A fuse ea) |
| CB39        | TRLR BO STOP            | WolfBox Camera/Mirror       | 10A  | 16AWG | ~10A                  | -     | Dash cam + backup camera                    |
| CB45        | IGNITION                | Driver Heated Seat          | 15A  | 14AWG | 5A peak, 2A sustained | K21   | Manual switch → relay K21 → seat element    |
| CB42        | 2WAY INTRCM             | Passenger Heated Seat       | 20A  | 14AWG | 5A peak, 2A sustained | K22   | Manual switch → relay K22 → seat element    |
| CB20        | RADIO                   | Cargo Lights                | 10A  | 16AWG | 4A                    | -     | Switch on rear wheel well top               |
| CB43        | TRANS ECU               | Winch Control (CH4X4 dual-push) | 10A  | 18AWG | ~3A peak per direction | -    | CH4X4-TOY-D-WINIO dual-momentary push at dash → HDP24 pins 16/17 → contactor; Warn remote parallel at contactor |
| CB44        | TRLR LIGHT              | **\[Available\]**             | -    | -     | -                     | -     | Future expansion                            |

**Circuit Breaker Utilization:** 7 of 8 used (1 available)

## Relay Configuration

| Relay Position | Original Military Label | Repurposed Function   | Voltage | Control     | Notes                                  |
| :------------- | :---------------------- | :-------------------- | :------ | :---------- | :------------------------------------- |
| K21            | REAR LEFT LIGHT         | Driver Heated Seat    | 12V     | Dash switch | Controls CB45 output to driver seat    |
| K22            | REAR RIGHT LIGHT        | Passenger Heated Seat | 12V     | Dash switch | Controls CB42 output to passenger seat |
| K27            | TRAILER BO STOP         | **\[Available\]**       | 12V     | -           | Future expansion                       |
| K30            | TRAILER REAR LEFT       | **\[Available\]**       | 12V     | -           | Future expansion                       |
| K31            | TRAILER REAR RIGHT      | **\[Available\]**       | 12V     | -           | Future expansion                       |
| K53            | RADIO                   | **\[Available\]**       | 24V→12V | -           | Replace with 12V relay                 |
| K40            | START DISABEL           | **\[Available\]**       | 24V→12V | -           | Replace with 12V relay                 |
| K42            | ENGINE PTO              | **\[Available\]**       | 24V→12V | -           | Replace with 12V relay                 |

**Relay Utilization:** 2 of 8 used, 6 available (3 require 12V relay replacement)

**Total Load:** ~60A maximum (Radio 15A + USB 13A + Camera 10A + Seats 10A peak + Winch control 2A + Cargo lights 4A)

**Control:** All circuits on CONSTANT power with trigger-wire or manual switch control for on/off

!!! info "Communication Devices"
G1 GMRS Radio and STX Intercom are powered from [SafetyHub 150][safetyhub] (START battery) as critical infrastructure, with direct grounds to START battery to minimize RF noise.

## Outstanding Items

- [ ] Identify pinout for J301-J306 Metri-Pack connectors (military TM manual or reverse engineering)
- [ ] Determine replacement 12V relay part numbers for K40, K42, K53 (currently 24V coils)

**Design Notes:**

- **High-side switching:** BODY PDU switches positive power to loads; load current returns through each load's own ground wire, NOT through the PDU. The PDU ground connection (~3A) is only for relay coils and internal logic.
- Heated seat current: 5A peak, 2A sustained per seat (verified with vendor)
- Military relays K21/K22 provide fault isolation and independent operation
- J301-J306 connectors require custom harness fabrication

## Related Documentation

- [AUX battery Distribution][house-battery] - Power source and circuit breaker (passenger rear wheel well)
- [Circuit Breakers][circuit-breakers] - 100A CB protection for LR-2 power feed
- [Dashboard Controls][dashboard] - Physical switch panel layout
- [Audio Systems][audio] - Fusion radio specifications
- [Firewall Ingress][firewall] - Power feed routing through firewall

[ebay-listing]: https://www.ebay.com/itm/224625878742
[safetyhub]: 04-safetyhub.md
[house-battery]: index.md
[circuit-breakers]: 01-circuit-breakers.md
[dashboard]: ../../05-control-interfaces/05-dashboard-controls.md
[audio]: ../../06-audio-systems/01-head-unit.md
[firewall]: ../07-wire-routing/02-firewall-ingress.md
[firewall-stud-bus]: ../05-grounding/02-firewall-stud-bus.md
