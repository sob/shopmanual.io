---
hide:
  - toc
tags:
  - product-details
  - power-generation
  - solar-panel
---

# 1.1.4 Solar Charging {#solar-charging}

/// html | div.product-info
![Cascadia 4x4 Solar Panel](../../images/cascadia-solar-80w.jpg){ loading=lazy }

**Type:** Flexible Monocrystalline Solar Panel

**Model:** Cascadia 4x4 80W Hood Solar Panel (VSS System for TJ/LJ 2003-2006)

**Manufacturer:** Cascadia 4x4

**Product Page:** [Cascadia 4x4 VSS System][cascadia-solar]

**Note:** VSS System includes MPPT controller, but using BCDC's built-in solar MPPT instead (panel only from VSS kit)

///

## Electrical Specifications

**Power Output:**

- **Maximum Power @ STC:** 80W
- **Optimum Operating Voltage (Vmp):** 40.1V
- **Optimum Operating Current (Imp):** 1.95A
- **Open Circuit Voltage (Voc):** 46.8V
- **Short Circuit Current (Isc):** 2.23A

**BCDC Compatibility:** Voc 46.8V within BCDC solar input range (9-48V) at STC (25°C)

!!! warning "Cold Weather Voc"
    Solar panel Voc **increases** in cold temperatures (~0.35%/°C). At 0°F (-18°C), Voc may reach ~53V, exceeding BCDC's 48V limit. The BCDC Alpha has overvoltage protection - soft fault (LED warning) progressing to hard fault as voltage increases. See [Optional Overvoltage Protection](#optional-overvoltage-protection) below for automatic disconnect solution.

## Physical Specifications

- **Dimensions:** 68 × 66 × 5 cm (27 × 26 × 2 in)
- **Weight:** 2.6 kg (5.7 lb)
- **Top Sheet Material:** ETFE (fluoropolymer)
- **Mounting Method:** SolarClasp™ adhesive system
- **Connector Type:** MC4 (standard solar connectors)
- **Cable Length:** 190 cm (74.8 in)
- **Mounting:** Permanently adhered to hood surface
- **Connection:** Wired to BCDC Alpha 50 solar input

## Wiring

**Solar Panel Connections:**

- **Positive (+):** Panel output → BCDC Alpha 50 solar input positive terminal
- **Negative (-):** Panel output → Chassis ground (NOT to BCDC negative)
- **Wire Gauge:** 10 AWG minimum (for 2.23A Isc with safety margin)
- **Routing:** Hood → Firewall → BCDC location in passenger rear wheel well
- **Maximum Current:** 2.23A (Isc) - well within BCDC solar input capacity

**VSS System Note:** VSS kit includes standalone MPPT controller - **not used**. BCDC has built-in MPPT on solar input, providing Green Power Priority and unified charge control.

**Important:** Solar negative connects to chassis ground per REDARC specifications. The BCDC requires a common ground system where all batteries and components share the same ground reference (vehicle chassis).

## Function

80W panel maintains AUX battery during extended stops via BCDC solar input. Full sun output at optimal conditions: 80W (1.95A @ 40V), variable in partial sun/clouds.

**BCDC Green Power Priority:** Solar input used first when available, alternator supplements to reach 50A total charging current. In full sun, solar contributes ~1.95A, reducing alternator load by same amount.

**Charging Contribution:**

- **Full sun:** ~1.95A to AUX battery (reduces alternator load from 50A to ~48A)
- **Partial sun:** Variable 0.8-1.5A depending on conditions
- **Overcast/Night:** 0A (BCDC uses alternator only)

**Alternator Load Relief:** Minimal but measurable - reduces worst-case alternator load by ~1.95A during sunny daytime operation

See [BCDC Alpha 50][bcdc] for complete charging system details.

**Installation:** See [Section 1 Installation Checklist][installation-checklist]

**Critical:** Verify polarity before connection - reverse polarity damages BCDC.

## Optional Overvoltage Protection {#optional-overvoltage-protection}

To automatically disconnect the solar panel when cold-weather Voc exceeds the BCDC's 48V limit, install an adjustable overvoltage disconnect module.

### Recommended Component

**Over/Under Voltage Protection Relay Module**

- **Type:** Compact PCB module with adjustable thresholds
- **Example:** [Amazon DC Over/Under Voltage Relay Module][overvoltage-module] (~$15-25)
- **Voltage Range:** DC 36V version has overvoltage adjustment range of 39-51V
- **Delay:** Adjustable 0.1-15s (prevents nuisance trips from brief voltage spikes)
- **Contacts:** Relay with NO/NC contacts, rated 10A (solar is only 2.2A)
- **Power:** Self-powered from monitored circuit (no separate 12V tap needed)
- **Size:** Compact (~2" x 2") - mount near BCDC or in small enclosure

### Wiring Diagram

```text
Solar Panel (+) ──┬── Voltage Module Sense Input
                  │
                  └── Voltage Module Relay (NC) ──── BCDC Solar Input (+)

Solar Panel (-) ────────────────────────────────── Chassis Ground

Voltage Module Power: Self-powered from solar panel voltage
```

### Configuration

| Setting | Value | Purpose |
|:--------|:------|:--------|
| **Overvoltage Threshold** | 47V | Disconnect before BCDC 48V limit |
| **Undervoltage Threshold** | Disabled or 10V | Don't disconnect at low voltage |
| **Reconnect Hysteresis** | ~3V (44V reconnect) | Prevent rapid cycling |
| **Trip Delay** | 1-2 seconds | Ignore brief voltage spikes |

### Operation

1. **Normal conditions (Voc < 47V):** Relay closed, solar charges normally
2. **Cold weather (Voc > 47V):** Relay opens, disconnects solar from BCDC
3. **Panel warms up (Voc drops < 44V):** Relay closes, charging resumes automatically
4. **BCDC protected:** Never sees voltage above 47V

### Installation Notes

- Mount module in weatherproof location (near BCDC in passenger rear wheel well, or sealed enclosure)
- Use MC4 inline connectors for easy solar disconnect during installation
- Consider conformal coating on PCB for moisture protection
- Test threshold settings before final installation

### Alternative: Series Diode Voltage Drop

For a passive (no electronics) solution, install 4-5 series rectifier diodes (10A10 type) in the solar positive line:

- **Voltage drop:** ~0.7V per diode × 5 = 3.5V permanent drop
- **Result:** Reduces 53V cold Voc to ~49.5V (still marginal)
- **Cons:** Permanent ~8% power loss, generates heat
- **Pros:** No moving parts, no adjustment needed

**Recommendation:** The relay module is preferred - no power loss during normal operation and provides automatic protection only when needed.

## Outstanding Items

- [ ] Order overvoltage protection relay module (DC 36V version, ~$15-25)
- [ ] Determine mounting location for voltage module (near BCDC or inline with solar wiring)
- [ ] Test and configure voltage thresholds before final installation (47V disconnect, 44V reconnect)

[cascadia-solar]: https://www.cascadia4x4.com/
[bcdc]: 03-bcdc.md
[installation-checklist]: ../../09-installation/01-power-systems-checklist.md#phase-4-integration-wiring
[overvoltage-module]: https://www.amazon.com/Over-Voltage-Under-Voltage-Protection-Monitoring-Adjustable/dp/B07Y2PTB4M
