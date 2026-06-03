# Section 1: Power Systems - Installation Checklist

Organized by installation order for efficient build workflow.

---

## Phase 1: Foundations

### Battery Compartments

- [ ] Install Odyssey PC1500 (START) in driver rear wheel well with access panel
- [ ] Build enclosed compartment in passenger rear wheel well with access panel (AUX)
- [ ] Install Barnes 4WD battery box (Group 24) in passenger rear wheel well - powdercoat before install
- [ ] Install Dakota Lithium 135Ah LiFePO4 (AUX) in Barnes battery box

### Grounding System

**Ground Bus Bars:**

- [ ] Mount Engine Bay Ground Bus (Blue Sea 2107 PowerBar, 600A) on firewall (engine bay side) near PMU
- [ ] Mount Firewall Stud Bus (Blue Sea 2105 MaxiBus, 250A) on firewall (cabin side)
- [ ] Mount SwitchPros Ground Bus (Blue Sea 2105 MaxiBus, 250A) near SwitchPros controller

**Frame Rail Grounds:**

- [ ] Confirm front frame rail ground point location (clean metal-to-metal)
- [ ] Confirm rear frame rail ground point location (clean metal-to-metal)
- [ ] Confirm 2/0 AWG: START battery- → Engine Bay Ground Bus Stud 1
- [ ] Confirm 2/0 AWG: Engine Bay Ground Bus Stud 2 → Engine block
- [ ] Confirm 2/0 AWG: Engine Bay Ground Bus Stud 3 → Front frame rail
- [ ] Confirm 2/0 AWG: AUX battery- → Rear frame rail (~3 ft)
- [ ] Confirm 4 AWG: Firewall Stud Bus Stud 1 → Chassis ground (~2 ft)
- [ ] Confirm 1/0 AWG: SwitchPros Ground Bus Stud 1 → Chassis/frame rail

**Battery Ground Reference:**

- [ ] Confirm 1/0 AWG: Engine Bay Ground Bus Stud 4 → AUX battery- (5-6 ft, 75A capacity)

**Ground Testing:**

- [ ] Verify <0.1V drop: START battery- to front frame rail (engine @ 2000 RPM)
- [ ] Verify <0.1V drop: AUX battery- to rear frame rail (engine @ 2000 RPM)
- [ ] Verify <0.05V drop: START battery- to AUX battery- (engine @ 2000 RPM)
- [ ] Verify <0.05V drop: START battery- to AUX battery- (BCDC charging @ 25A)
- [ ] Verify <0.2V drop: START battery- to AUX battery- (winch operation @ 400A)
- [ ] Verify ground bus stud torque: 100-120 in-lb (3/8"-16 studs on PowerBar)

---

## Phase 2: Power Distribution

### START Battery Circuit Breakers

**Circuit Breakers (mount within 7" of battery):**

- [ ] Mount Mechanical Products 174-S2-250-2 250A CB (PMU main power)
- [ ] Mount Mechanical Products 174-S2-080-2 80A CB (BCDC input)

**START Battery Positive Wiring:**

- [ ] Confirm 2/0 AWG: START battery+ → 250A CB → PMU main power (~7 ft, temp-derated for 60°C)
- [ ] Confirm 4 AWG: START battery+ → 80A CB → BCDC input (~6 ft)

**PMU Ground Reference:**

- [ ] Confirm PMU Pin 25 connected to Engine Bay Ground Bus Stud 5 (per harness, <100mA logic/CAN reference)

**Direct Battery Connections (No Circuit Breaker):**

- [ ] Confirm ECM power/ground connected directly to START battery terminals (per Cummins harness)
- [ ] Confirm grid heater relay powered from START battery+ (via integrated fusible link)
- [ ] Confirm grid heater ground connected directly to START battery-

**Radio Grounds (RF Noise Isolation):**

- [ ] Confirm 10 AWG: GMRS Radio ground → START battery- (route through floor/frame, ~8 ft)
- [ ] Confirm 10 AWG: STX Intercom ground → START battery- (route through floor/frame, ~8 ft)

**Testing:**

- [ ] Verify PMU main power always on (via 250A CB)
- [ ] Verify voltage drop across main power cables under load (<3% at 60°C)
- [ ] Verify ground resistance: Engine Bay Ground Bus to battery- (<0.1Ω)

### AUX Battery Inline CBs & Firewall CONSTANT Bus

**Inline CBs at AUX battery (mount within 7" of battery on wheel well bracket):**

- [ ] Mount Mechanical Products 174-S2-300-2 300A CB (forward feed to firewall bus)
- [ ] Mount Mechanical Products 174-S2-150-2 150A CB (SafetyHub local feed)
- [ ] Confirm AUX battery+ has 4 stacked ring lugs: Winch (1/0), BCDC output (4 AWG), 300A CB input (2/0), 150A CB input (2 AWG)

**Battery-Side Protected Feeds:**

- [ ] Confirm 2/0 AWG: AUX battery+ → 300A CB → Firewall CONSTANT Bus (~13 ft via cabin trunk)
- [ ] Confirm 2 AWG: AUX battery+ → 150A CB → SafetyHub 150 (~2 ft local)

**Firewall CONSTANT Bus:**

- [ ] Mount Blue Sea 2105 MaxiBus (250A) on firewall (passenger cabin side, near BODY PDU mounting area)
- [ ] Confirm 2/0 AWG forward feed terminates at bus input stud

**Firewall-Side CBs (mount within 7" of Firewall CONSTANT Bus):**

- [ ] Mount Mechanical Products 174-S2-150-2 150A CB (SwitchPros)
- [ ] Mount Mechanical Products 174-S2-100-2 100A CB (BODY PDU)
- [ ] Mount Blue Sea 187-100A 100A CB (JL Audio MV800/8i Amp) — note this CB is on the battery-side bracket, not at the firewall bus

**Firewall CONSTANT Bus Wiring:**

- [ ] Confirm 2 AWG: Firewall CONSTANT Bus → 150A CB → SwitchPros power module (~2 ft)
- [ ] Confirm 2 AWG: Firewall CONSTANT Bus → 100A CB → BODY PDU power studs (~2 ft)
- [ ] Confirm 4 AWG: AUX battery+ → 100A CB → JL Audio MV800/8i Amp (~3-4 ft, under rear seat — direct AUX feed, not via firewall bus)

**Direct AUX Battery Connections (No Circuit Breaker):**

- [ ] Confirm 1/0 AWG: AUX battery+ → Winch positive (13 ft one-way, direct connection per WARN spec)
- [ ] Confirm 1/0 AWG: AUX battery- → Winch negative (13 ft one-way, matches positive path)
- [ ] Confirm 4 AWG: AUX battery- → JL Audio MV800/8i amplifier ground (~3-4 ft)

### BCDC Alpha 50 Installation

- [ ] Mount BCDC in passenger rear wheel well (water-protected, LED visibility access)
- [ ] Confirm 4 AWG: START battery+ → 80A CB → BCDC input (red terminal, M8, ~6 ft)
- [ ] Confirm 4 AWG: BCDC output (brown terminal, M8) → AUX battery+
- [ ] Confirm 4 AWG: BCDC negative (black terminal, M8) → AUX battery-
- [ ] Confirm 18 AWG: Ignition signal (blue spade terminal) → PMU ignition sense tap

**Battery Temperature Sensor (REQUIRED for LiFePO4):**

- [ ] Install BCDC temp sensor ring terminal on AUX battery positive terminal bolt
- [ ] Route sensor cable to BCDC (short run - both in passenger rear wheel well)
- [ ] Plug sensor into BCDC temperature sensor port (2-pin connector, polarity reversible)

**BCDC Configuration & Testing:**

- [ ] Configure Green Power Priority via RedArc app
- [ ] Test jump start assist function
- [ ] Verify BCDC LED status indicates proper charging mode

### Alternator

- [ ] Install 270A alternator (Premier Power Welder HO-C28)
- [ ] Confirm 2/0 AWG: Alternator output → START battery+ (shortest path, ~8 ft)
- [ ] Confirm alternator case grounded through engine block mounting

---

## Phase 3: Controllers - Physical Installation & Main Power

### PMU24 Physical Installation

- [ ] Mount PMU on firewall or inner fender (accessible for LED/USB diagnostics)
- [ ] Confirm PMU ground reference Pin 25 connected to Engine Bay Ground Bus Stud 5

### SafetyHub 150 Physical Installation

- [ ] Mount SafetyHub 150 in passenger rear wheel well (co-located with AUX battery and inline CBs)
- [ ] Confirm 2 AWG: AUX battery+ → 150A CB → SafetyHub input (~2 ft local)
- [ ] Verify SafetyHub internal ground bus connected to chassis ground (rear frame rail)

### BODY PDU Physical Installation

- [ ] Verify all circuit breakers and relays functional in LR-2 unit
- [ ] Replace 24V relays (K40, K42, K53) with 12V relays (determine part numbers)
- [ ] Mount LR-2 on firewall (body side, passenger side, near Firewall CONSTANT Bus)
- [ ] Confirm 2 AWG: Firewall CONSTANT Bus → 100A CB → BODY PDU power studs (~2 ft)
- [ ] Confirm 14 AWG: BODY PDU ground → Firewall Stud Bus Terminal 3 (relay coil/logic only)
- [ ] Create custom wiring harnesses to adapt J301-J306 military connectors to civilian loads
- [ ] Route heated seat dash switches to LR-2 relay control inputs (K21, K22)
- [ ] Label repurposed circuits on LR-2 enclosure (match CB positions to new functions)

### SwitchPros RCR-Force 12 Physical Installation

- [ ] Mount SwitchPros power module on firewall (cabin side, passenger area, next to BODY PDU)
- [ ] Mount SwitchPros Ground Bus (Blue Sea 2105 MaxiBus) at firewall near power module
- [ ] Confirm 2 AWG: Firewall CONSTANT Bus → 150A CB → SwitchPros power input (~2 ft)
- [ ] Confirm 4 AWG: SwitchPros logic ground → chassis ground at firewall (short run)
- [ ] Mount SwitchPros control panel on dash; order 5 ft control cable (firewall to dash)

**SwitchPros Custom Harness Note:**

!!! info "Custom Delphi Harness Design"
Create 12 custom 2-pin Delphi harnesses at SwitchPros:

    - Each SwitchPros output → 2-pin Delphi plug (power + ground combined)
    - Each light → matching 2-pin Delphi plug
    - Back of SwitchPros: ~12 Delphi connectors for plug-and-play lighting
    - Eliminates individual wire routing - each light is single plug connection

---

## Phase 4: Integration & Wiring

### Firewall Bulkhead Connector

**Deutsch HDP24-24-29 Installation:**

- [ ] Drill 1.5" diameter hole in firewall for bulkhead connector
- [ ] Mount HDP24-24-21PE-L015 receptacle (flange mount, engine side)
- [ ] Assemble HDP26-24-21SE plug (cabin side)
- [ ] Crimp size 16 contacts (0460-202-16141 pins, 0462-201-16141 sockets) for 17 wires
- [ ] Install sealing plugs (114017/114018) in unused cavities
- [ ] Verify IP67/IP68 seal engagement with bayonet coupling

**Pin Assignment Verification:**

- [ ] Confirm Pin 1-6 (Engine→Cabin): Radio power (3), PMU lighting outputs (3)
- [ ] Confirm Pin 7-17 (Cabin→Engine): CT4 outputs (4), switch signals (5), winch control (2)
- [ ] Install ferrite chokes on radio power leads at radio end (RF mitigation)

### Ignition Signal Distribution

- [ ] Confirm 14 AWG: PBS-I PINK IGN (cabin) → Ignition signal bus bar Stud 1
- [ ] Confirm ignition signal bus bar Stud 2 → Deutsch connector Pin 12 (outbound to engine bay)
- [ ] Confirm engine-bay junction off Pin 12 → ECM 12V supply + PMU Pin 7
- [ ] Confirm bus bar terminals split to: CT4, SwitchPros, Fusion Radio, BCDC
- [ ] Verify total ignition signal current <500mA for all bus bar taps

### PMU Input Wiring

- [ ] Confirm 18 AWG: Ignition RUN (from engine-bay distribution off Pin 12) → PMU Pin 7
- [ ] Confirm horn button → PMU In 1 (via Deutsch connector Pin 11)
- [ ] Confirm brake pedal switch → PMU In 2 (via Deutsch connector Pin 13)
- [ ] Confirm reverse signal → PMU In 3 (Turbolamik aux output, Reverse gear)
- [ ] Confirm A/C request → PMU In 9 (via Deutsch connector Pin 14)
- [ ] Confirm CT4 SW3 (headlight status) → PMU In 7 (tap on engine bay side of connector)
- [ ] PMU In 4, In 5, In 6, In 8 — Available for future expansion (no current wiring)

### PMU Output Wiring

**High-Current Outputs (Combined):**

- [ ] Confirm iBooster main power → OUT1+10 combined (46A @ 40°C capacity, non-adjacent)
- [ ] Confirm radiator fan → OUT2+3+4 combined (75A total capacity)

**25A Outputs:**

- [ ] Confirm HVAC blower → OUT5 (20A max) - ground: factory HVAC ground
- [ ] Confirm GMRS Radio → OUT6 (15A) - ground: direct to START battery-
- [ ] Confirm oil cooler fan → OUT7 (15A) - ground: Engine Bay Bus Stud 8
- [ ] Confirm PS cooler fan → OUT8 (15A) - ground: Engine Bay Bus Stud 8
- [ ] Confirm Dakota Digital system → OUT9 (25A) - ground: Firewall Stud Bus T4-5

**15A Outputs:**

- [ ] Confirm wipers (WS-51C) → OUT11 (15A) - ground: Firewall Stud Bus T2
- [ ] Confirm CT4 → OUT13 (9A, CONSTANT) - ground: Firewall Stud Bus T1
- [ ] Confirm winch contactor trigger → OUT15 (1A) - control signal only

**7A Outputs:**

- [ ] Confirm A/C clutch → OUT17 (5A) - ground: factory A/C ground
- [ ] Confirm horn → OUT18 (5.4A) - ground: Engine Bay Bus Stud 6
- [ ] Confirm iBooster ignition signal → OUT19 (5A) - ground: Engine Bay Bus Stud 7
- [ ] Confirm STX Intercom → OUT20 (5A) - ground: direct to START battery-
- [ ] Confirm brake lights → OUT21 (3A) - ground: SwitchPros Ground Bus T4
- [ ] Confirm reverse lights → OUT22 (5A) - ground: SwitchPros Ground Bus T4
- [ ] Confirm DRL/parking → OUT23 (2A) - ground: SwitchPros Ground Bus T5
- [ ] OUT24 — Available for future expansion (no current wiring)

### PMU CAN Bus Integration

- [ ] Confirm J1939 CAN High T-tap → PMU Pin 23/24 (18-20 AWG twisted pair, <12" stub)
- [ ] Confirm J1939 CAN Low T-tap → PMU Pin 36/37 (18-20 AWG twisted pair, <12" stub)
- [ ] Disable PMU internal CAN termination in software (bus already terminated at ECM + harness end)
- [ ] Verify 60Ω resistance across CAN High/Low at ECM connector (harness disconnected, ignition off)
- [ ] Configure PMU to read J1939 SPNs: 100 (oil pressure), 110 (coolant temp), 175 (oil temp), 190 (RPM)

### BODY PDU Circuit Wiring

- [ ] Confirm Fusion Radio memory → CB30 (15A, 14 AWG, CONSTANT)
- [ ] Confirm USB ports → CB48 (20A, 14 AWG, CONSTANT) - 2× Powerwerx PanelUSB-75W (7.5A fuse ea)
- [ ] Confirm WolfBox camera → CB39 (10A, 16 AWG, CONSTANT)
- [ ] Confirm driver heated seat → CB45 (15A, 14 AWG) via relay K21 - 5A peak, 2A sustained
- [ ] Confirm passenger heated seat → CB42 (20A, 14 AWG) via relay K22 - 5A peak, 2A sustained
- [ ] Confirm cargo lights → CB20 (10A, 16 AWG) - switch on rear wheel well top
- [ ] Confirm winch control → CB43 (10A, 18 AWG) - dash rocker + remote parallel control

**Verification:**

- [ ] Verify Fusion radio current draw matches fuse ratings
- [ ] Verify WolfBox model and 10A fuse adequate
- [ ] Verify all BODY PDU load grounds route to individual load ground points (high-side switching)

### SafetyHub Circuit Wiring

- [ ] Confirm ARB compressor motor 1 → MIDI-1 (60A, 6 AWG, ~12 ft to under passenger seat)
- [ ] Confirm ARB compressor motor 2 → MIDI-2 (60A, 6 AWG, ~12 ft to under passenger seat)
- [ ] Confirm winch contactor trigger → ATC-1 (15A, 14 AWG, ~13 ft to front bumper)

### Solar Panel Installation

- [ ] Install Cascadia 4x4 80W panel on hood per manufacturer instructions (SolarClasp adhesive)
- [ ] Route wiring: Hood → Firewall → BCDC (~10-12 ft, MC4 connectors)
- [ ] Confirm solar positive → BCDC solar input (yellow terminal)
- [ ] Confirm solar negative → Chassis ground (NOT BCDC negative)
- [ ] **CRITICAL:** Verify polarity before connection - reverse polarity damages BCDC

**Optional Overvoltage Protection (cold weather):**

- [ ] Mount overvoltage relay module near BCDC (weatherproof location)
- [ ] Configure overvoltage threshold: 47V disconnect, 44V reconnect
- [ ] Configure trip delay: 1-2 seconds (ignore brief spikes)
- [ ] Test threshold settings before final installation

**Solar Testing:**

- [ ] Monitor BCDC LED in daylight to verify solar charging
- [ ] Verify solar input voltage within range (9-48V) at operating temperature

---

## Phase 5: Testing & Programming

### PMU Programming

**Output Combining:**

- [ ] Configure iBooster combining (OUT1+10, non-adjacent terminals)
- [ ] Configure radiator fan combining (OUT2+3+4, PWM variable speed)

**Logic Programming:**

- [ ] Program DRL auto-off when headlights active (In 7 CT4 SW3 → OUT23 disable)
- [ ] Program A/C clutch engagement logic (In 9 → OUT17)
- [ ] Program horn activation (In 1 → OUT18)
- [ ] Program brake light activation (In 2 → OUT21)
- [ ] Program reverse light activation (In 3 → OUT22)
- [ ] Program oil cooler fan based on SPN 175 (220-230°F hysteresis) → OUT7
- [ ] Program PS cooler fan based on SPN 110 (210-220°F hysteresis) → OUT8
- [ ] Configure sequential load startup delays (0.5s, 1.0s, 1.5s)

**Backup:**

- [ ] Export/backup configuration (.pmu format) to git repository
- [ ] Print critical logic (DRL, fan control) for emergency recovery

### PMU Testing

- [ ] Verify J1939 communication and data accuracy (SPNs 100, 110, 175, 190)
- [ ] Test DRL auto-off logic (verify OUT23 disables when headlights active)
- [ ] Test A/C clutch engagement (verify OUT17 activates with In 9)
- [ ] Test CAN-based fan controls at threshold temps (OUT7, OUT8)
- [ ] Test sequential load startup timing
- [ ] Verify LED diagnostics show correct states
- [ ] Verify iBooster CONSTANT power (OUT1+10 always on)

### Ground Bus Testing

- [ ] Verify Engine Bay Ground Bus stud torque: 100-120 in-lb
- [ ] Verify Firewall Stud Bus terminal torque per Blue Sea spec
- [ ] Verify SwitchPros Ground Bus terminal torque per Blue Sea spec
- [ ] Verify all ground bus connections have clean metal-to-metal contact

### System Integration Testing

- [ ] Verify all PMU outputs operate correctly (test each output individually)
- [ ] Test all BODY PDU circuits (CB30, CB48, CB39, CB45, CB42, CB20, CB43)
- [ ] Test SafetyHub circuits (MIDI-1/2 ARB, ATC-1 winch trigger)
- [ ] Verify SwitchPros Delphi connectors and outputs
- [ ] Verify Deutsch bulkhead connector seal integrity
- [ ] Final voltage drop measurements under load (<3% at operating temp)
- [ ] Final ground resistance verification (<0.1Ω all paths)

---

## Reference Documentation

**Power Systems:**

- [Batteries][batteries] - START (Odyssey PC1500) and AUX (Dakota Lithium 135Ah) specifications
- [BCDC Alpha 50][bcdc] - DC-DC charger installation and configuration
- [Solar Charging][solar] - Cascadia 80W panel and overvoltage protection
- [START Battery Distribution][start-dist] - Driver rear wheel well connections
- [AUX Battery Distribution][aux-dist] - Passenger rear wheel well connections

**Ground Bus Bars:**

- [Engine Bay Ground Bus][engine-ground] - Blue Sea 2107 PowerBar stud assignments
- [Firewall Stud Bus][firewall-ground] - Blue Sea 2105 MaxiBus terminal assignments
- [SwitchPros Ground Bus][switchpros-ground] - Blue Sea 2105 MaxiBus terminal assignments

**PMU:**

- [PMU Overview][pmu-overview] - Product specifications
- [PMU Inputs][pmu-inputs] - Input configuration and CAN bus
- [PMU Outputs][pmu-outputs] - Output assignments and ground locations
- [PMU Programming][pmu-programming] - Logic configuration

**Distribution:**

- [BODY PDU][body-pdu] - LR-2 circuit breaker and relay assignments
- [SafetyHub 150][safetyhub] - ARB and winch fuse assignments
- [Firewall Ingress][firewall-ingress] - Deutsch HDP24-24-29 connector pinout

**External Manuals:**

- [PMU24 User Manual v101.1.5][pmu-manual]
- [BCDC Alpha 50 Installation Manual][bcdc-install]
- [Blue Sea BusBar Installation Guide][bluesea-busbar-guide]

[batteries]: ../01-power-systems/01-power-generation/01-batteries.md
[bcdc]: ../01-power-systems/01-power-generation/03-bcdc.md
[solar]: ../01-power-systems/01-power-generation/04-solar.md
[start-dist]: ../01-power-systems/02-starter-battery-distribution/index.md
[aux-dist]: ../01-power-systems/03-aux-battery-distribution/index.md
[engine-ground]: ../01-power-systems/05-grounding/01-engine-bay-ground-bus.md
[firewall-ground]: ../01-power-systems/05-grounding/02-firewall-stud-bus.md
[switchpros-ground]: ../01-power-systems/05-grounding/03-switchpros-ground-bus.md
[pmu-overview]: ../01-power-systems/04-pmu/01-pmu-overview.md
[pmu-inputs]: ../01-power-systems/04-pmu/02-pmu-inputs.md
[pmu-outputs]: ../01-power-systems/04-pmu/03-pmu-outputs.md
[pmu-programming]: ../01-power-systems/04-pmu/04-pmu-programming.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[safetyhub]: ../01-power-systems/03-aux-battery-distribution/04-safetyhub.md
[firewall-ingress]: ../01-power-systems/07-wire-routing/02-firewall-ingress.md
[pmu-manual]: https://www.ecumaster.com/files/PMU/PMU_Manual.pdf
[bcdc-install]: https://cdn.intelligencebank.com/au/share/yE9N/zJpl/NNRlJ/original/Install+Guide+BCDC+Alpha+50R+EN
[bluesea-busbar-guide]: https://www.bluesea.com/resources/108
