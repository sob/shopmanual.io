---
hide:
  - toc
---

# 1.1 Power Generation & Storage {#power-generation}

## System Overview

See [Power Systems Overview][power-systems] for the START/AUX battery specs and dual-battery charging architecture. This section covers the battery hardware, alternator, BCDC, and solar charging in detail. Beyond isolated charging, the BCDC also supports a jump-start assist mode (AUX → START), and an 80W hood solar panel maintains AUX battery charge.

## Components

- **[Batteries](01-batteries.md)** - Odyssey PC1500 AGM (START), Dakota Lithium 135Ah LiFePO4 (AUX), mounting locations
- **[Alternator](02-alternator.md)** - 270A alternator, output routing
- **[BCDC Alpha 50](03-bcdc.md)** - Battery isolation, DC-DC charging (50A), jump start assist
- **[Solar Charging](04-solar.md)** - 80W hood panel, BCDC integration

## Related Documentation

- **[Grounding Architecture][grounding]** - Battery ground connections and distributed grounding system (Section 1.5)

[grounding]: ../05-grounding/index.md
[power-systems]: ../index.md
