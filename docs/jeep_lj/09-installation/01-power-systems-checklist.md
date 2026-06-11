# Section 1: Power Systems - Installation Checklist

Organized by installation order for efficient build workflow. Each item is a
check-off confirmation — wire gauges, lengths, torque values, and part numbers
live in the linked source docs, not here.

---

## Phase 1: Foundations

### Battery Compartments

- [ ] Install Odyssey PC1500 (START) in driver rear wheel well with access panel
- [ ] Build enclosed AUX compartment in passenger rear wheel well with access panel
- [ ] Install Barnes 4WD battery box in passenger rear wheel well
- [ ] Install Dakota Lithium (AUX) in Barnes battery box

### Grounding System

**Ground Bus Bars:**

- [ ] Mount Engine Bay Ground Bus on firewall (engine bay side) near PMU
- [ ] Mount Firewall Stud Bus on firewall (cabin side)
- [ ] Mount SwitchPros Ground Bus near SwitchPros controller

**Frame Rail Grounds:**

- [ ] Confirm front frame rail ground point located
- [ ] Confirm rear frame rail ground point located
- [ ] Confirm START battery- → Engine Bay Ground Bus
- [ ] Confirm Engine Bay Ground Bus → engine block
- [ ] Confirm Engine Bay Ground Bus → front frame rail
- [ ] Confirm AUX battery- → rear frame rail
- [ ] Confirm Firewall Stud Bus → chassis ground
- [ ] Confirm SwitchPros Ground Bus → chassis/frame rail
- [ ] Confirm Engine Bay Ground Bus → AUX battery- (cross-battery reference)

**Ground Testing:**

- [ ] Verify ground voltage drop within spec on all battery-to-frame paths (engine @ 2000 RPM)
- [ ] Verify cross-battery ground drop within spec under BCDC charging
- [ ] Verify cross-battery ground drop within spec under winch load

---

## Phase 2: Power Distribution

### START Battery Circuit Breakers

- [ ] Mount 250A circuit breaker (PMU main power) within reach of START battery
- [ ] Mount 80A circuit breaker (BCDC input) within reach of START battery
- [ ] Mount 150A circuit breaker (Forward Distribution Bus master) within reach of START battery
- [ ] Confirm START battery+ → 250A CB → PMU main power
- [ ] Confirm START battery+ → 80A CB → BCDC input
- [ ] Confirm START battery+ → 150A CB → 2 AWG forward feed → START+ Forward Distribution Bus
- [ ] Confirm PMU ground reference (Pin 25) → Engine Bay Ground Bus

**START+ Forward Distribution Bus (engine bay):**

- [ ] Mount START+ Forward Distribution Bus (Blue Sea 2105, {{ tbd(135) }}) in engine bay with insulated cover
- [ ] Mount 60A / 50A / 25A load breakers on a bracket beside the bus
- [ ] Confirm Forward Bus → 60A CB → radiator fan power (via relay)
- [ ] Confirm Forward Bus → 50A CB → iBooster main
- [ ] Confirm Forward Bus → 25A CB → Turbolamik TCU power
- [ ] Confirm iBooster enable → Ignition bus Term 5 (7.5A fuse) → firewall Pin 18
- [ ] Install Lingenfelter VSFM-002 radiator-fan controller + coolant sensor (sensor P/N {{ tbd(134) }}); verify fail-to-full-speed on lost sensor

**Direct Battery Connections (No Circuit Breaker):**

- [ ] Confirm ECM power/ground connected directly to START battery (per Cummins harness)
- [ ] Confirm grid heater relay powered from START battery+ (via integrated fusible link)
- [ ] Confirm grid heater ground connected directly to START battery-

**Radio Grounds (RF Noise Isolation):**

- [ ] Confirm GMRS Radio ground → START battery- (direct run for RF isolation)
- [ ] Confirm STX Intercom ground → START battery- (direct run for RF isolation)

**Testing:**

- [ ] Verify PMU main power always on
- [ ] Verify main power cable voltage drop within spec under load

### AUX Battery Inline CBs & Firewall CONSTANT Bus

- [ ] Mount 300A circuit breaker (forward feed to firewall bus) within reach of AUX battery
- [ ] Mount 150A circuit breaker (SafetyHub local feed) within reach of AUX battery
- [ ] Confirm AUX battery+ ring lugs landed: Winch, BCDC output, 300A CB, 150A CB
- [ ] Confirm AUX battery+ → 300A CB → Firewall CONSTANT Bus
- [ ] Confirm AUX battery+ → 150A CB → SafetyHub 150

**Firewall CONSTANT Bus:**

- [ ] Mount Firewall CONSTANT Bus on firewall (cabin side, near BODY PDU)
- [ ] Confirm forward feed terminates at bus input stud
- [ ] Mount 150A circuit breaker (SwitchPros) at Firewall CONSTANT Bus
- [ ] Mount 100A circuit breaker (BODY PDU) at Firewall CONSTANT Bus
- [ ] Mount 100A circuit breaker (JL Audio amp) at AUX battery bracket
- [ ] Confirm Firewall CONSTANT Bus → 150A CB → SwitchPros power module
- [ ] Confirm Firewall CONSTANT Bus → 100A CB → BODY PDU power studs
- [ ] Confirm AUX battery+ → 100A CB → JL Audio amp (direct AUX feed, not via firewall bus)

**Direct AUX Battery Connections (No Circuit Breaker):**

- [ ] Confirm AUX battery+ → Winch positive (direct connection per WARN spec)
- [ ] Confirm AUX battery- → Winch negative
- [ ] Confirm AUX battery- → JL Audio amp ground

### BCDC Alpha 50 Installation

- [ ] Mount BCDC in passenger rear wheel well (water-protected, LED visible)
- [ ] Confirm START battery+ → 80A CB → BCDC input
- [ ] Confirm BCDC output → AUX battery+
- [ ] Confirm BCDC negative → AUX battery-
- [ ] Confirm ignition signal → PMU ignition sense tap

**Battery Temperature Sensor (REQUIRED for LiFePO4):**

- [ ] Install BCDC temp sensor on AUX battery positive terminal
- [ ] Plug temp sensor into BCDC sensor port

**BCDC Configuration & Testing:**

- [ ] Configure Green Power Priority via RedArc app
- [ ] Test jump start assist function
- [ ] Verify BCDC LED indicates proper charging mode

### Alternator

- [ ] Install 270A alternator (Premier Power Welder HO-C28)
- [ ] Confirm alternator output → START battery+
- [ ] Confirm alternator case grounded through engine block mounting

---

## Phase 3: Controllers - Physical Installation & Main Power

### PMU24

- [ ] Mount PMU on firewall or inner fender (accessible for LED/USB diagnostics)
- [ ] Confirm PMU ground reference (Pin 25) → Engine Bay Ground Bus

### SafetyHub 150

- [ ] Mount SafetyHub 150 in passenger rear wheel well (co-located with AUX battery)
- [ ] Confirm AUX battery+ → 150A CB → SafetyHub input
- [ ] Confirm SafetyHub ground bus → chassis ground

### BODY PDU

- [ ] Verify all circuit breakers and relays functional in LR-2 unit
- [ ] Replace 24V relays (K40, K42, K53) with 12V relays ({{ tbd(70) }})
- [ ] Mount LR-2 on firewall (body side, near Firewall CONSTANT Bus)
- [ ] Confirm Firewall CONSTANT Bus → 100A CB → BODY PDU power studs
- [ ] Confirm BODY PDU ground → Firewall Stud Bus
- [ ] Build harnesses to adapt J301-J306 connectors to civilian loads ({{ tbd(69) }})
- [ ] Route heated seat dash switches to LR-2 relay control inputs (K21, K22)
- [ ] Label repurposed circuits on LR-2 enclosure

### SwitchPros RCR-Force 12

- [ ] Mount SwitchPros power module on firewall (cabin side, next to BODY PDU)
- [ ] Mount SwitchPros Ground Bus at firewall near power module
- [ ] Confirm Firewall CONSTANT Bus → 150A CB → SwitchPros power input
- [ ] Confirm SwitchPros logic ground → chassis ground at firewall
- [ ] Mount SwitchPros control panel on dash; order control cable
- [ ] Build custom 2-pin Delphi harnesses for each output (plug-and-play lighting)

---

## Phase 4: Integration & Wiring

### Firewall Bulkhead Connector

- [ ] Drill firewall hole for bulkhead connector
- [ ] Mount Deutsch HDP24-24-29 receptacle (engine side)
- [ ] Assemble Deutsch plug (cabin side)
- [ ] Crimp contacts for all 17 wires
- [ ] Install sealing plugs in unused cavities
- [ ] Verify bulkhead connector seal engagement
- [ ] Confirm Pin 1-6 assignments (Engine→Cabin): radio power, PMU lighting outputs
- [ ] Confirm Pin 7-17 assignments (Cabin→Engine): CT4 outputs, switch signals, winch control
- [ ] Install ferrite chokes on radio power leads (RF mitigation)

### Ignition Signal Distribution

- [ ] Confirm PBS-I PINK IGN (cabin) → ignition signal bus bar
- [ ] Confirm ignition signal bus bar → Deutsch connector (outbound to engine bay)
- [ ] Install inline fuse on ECM ignition feed (Cummins-mandated ECM Pin 41 protection per 5504137)
- [ ] Confirm engine-bay junction → ECM 12V supply + PMU Pin 7
- [ ] Confirm bus bar taps split to: CT4, SwitchPros, Fusion Radio, BCDC
- [ ] Verify total ignition signal current within spec

### PMU Input Wiring

- [ ] Confirm ignition RUN → PMU Pin 7
- [ ] Confirm horn button → PMU In 1
- [ ] Confirm brake pedal switch → PMU In 2
- [ ] Confirm reverse signal → PMU In 3 (Turbolamik aux output)
- [ ] Confirm A/C request → PMU In 9
- [ ] Confirm CT4 SW3 (headlight status) → PMU In 7
- [ ] PMU In 4, 5, 6, 8 — reserved for future expansion (no wiring)

### PMU Output Wiring

- [ ] Confirm HVAC blower → OUT5
- [ ] Confirm GMRS Radio → OUT6
- [ ] Confirm oil cooler fan → OUT7
- [ ] Confirm PS cooler fan → OUT8
- [ ] Confirm Dakota Digital system → OUT9
- [ ] Confirm wipers (WS-51C) → OUT11
- [ ] Confirm CT4 → OUT13
- [ ] Confirm A/C clutch → OUT17
- [ ] Confirm horn → OUT18
- [ ] Confirm STX Intercom → OUT20
- [ ] Confirm brake lights → OUT21
- [ ] Confirm reverse lights → OUT22
- [ ] Confirm DRL/parking → OUT23
- [ ] OUT1–4, 10, 16, 19, 24 — free (no wiring); radiator fan, iBooster, and TCU relocated to the START+ Forward Distribution Bus (see below)

### PMU CAN Bus Integration

- [ ] Confirm J1939 CAN High T-tap → PMU Pin 23/24
- [ ] Confirm J1939 CAN Low T-tap → PMU Pin 36/37
- [ ] Disable PMU internal CAN termination in software
- [ ] Verify CAN bus termination resistance at ECM connector
- [ ] Configure PMU to read J1939 SPNs: 100, 110, 175, 190

### BODY PDU Circuit Wiring

- [ ] Confirm Fusion Radio memory → CB30 (CONSTANT)
- [ ] Confirm USB ports → CB48 (CONSTANT)
- [ ] Confirm WolfBox camera → CB39 (CONSTANT)
- [ ] Confirm driver heated seat → CB45 via relay K21
- [ ] Confirm passenger heated seat → CB42 via relay K22
- [ ] Confirm cargo lights → CB20
- [ ] Confirm winch control → CB43

### SafetyHub Circuit Wiring

- [ ] Confirm ARB compressor motor 1 → MIDI-1
- [ ] Confirm ARB compressor motor 2 → MIDI-2

### Solar Panel Installation

- [ ] Install Cascadia 4x4 80W panel on hood per manufacturer instructions
- [ ] Route solar wiring: hood → firewall → BCDC
- [ ] Confirm solar positive → BCDC solar input
- [ ] Confirm solar negative → chassis ground (NOT BCDC negative)
- [ ] **CRITICAL:** Verify polarity before connection — reverse polarity damages BCDC

**Optional Overvoltage Protection (cold weather):**

- [ ] Mount overvoltage relay module near BCDC
- [ ] Configure overvoltage thresholds and trip delay
- [ ] Test threshold settings before final installation

**Solar Testing:**

- [ ] Verify solar charging via BCDC LED in daylight
- [ ] Verify solar input voltage within range at operating temperature

---

## Phase 5: Testing & Programming

### PMU Programming

- [ ] Program DRL auto-off when headlights active
- [ ] Program A/C clutch engagement logic
- [ ] Program horn activation
- [ ] Program brake light activation
- [ ] Program reverse light activation
- [ ] Program oil cooler fan from SPN 175
- [ ] Program PS cooler fan from SPN 110
- [ ] Configure sequential load startup delays
- [ ] Export/backup configuration to git repository

### PMU Testing

- [ ] Verify J1939 communication and data accuracy
- [ ] Test DRL auto-off logic
- [ ] Test A/C clutch engagement
- [ ] Test CAN-based fan controls at threshold temps
- [ ] Test sequential load startup timing
- [ ] Verify LED diagnostics show correct states
- [ ] Verify iBooster power always on

### System Integration Testing

- [ ] Verify all PMU outputs operate correctly
- [ ] Test all BODY PDU circuits
- [ ] Test SafetyHub circuits
- [ ] Verify SwitchPros Delphi connectors and outputs
- [ ] Verify Deutsch bulkhead connector seal integrity
- [ ] Final voltage drop measurements under load (within spec)
- [ ] Final ground resistance verification (within spec)

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
