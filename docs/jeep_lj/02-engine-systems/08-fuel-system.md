---
hide:
  - toc
tags:
  - product-details
  - engine-systems
  - fuel-system
---

# 2.8 Fuel System {#fuel-system}

## Overview

The Cummins R2.8 includes a **gear-driven mechanical fuel pump** mounted on the back of the block (similar to the 24-valve 5.9L and 6.7L Cummins engines). No external electric lift pump is required.

## Fuel System Components

| Component                   | Source             | Notes                               |
| :-------------------------- | :----------------- | :---------------------------------- |
| Gear-driven fuel pump       | Included with R2.8 | Mechanical, on back of block        |
| Fuel filter/water separator | Included with R2.8 | Has manual priming hand pump        |
| Fuel lines                  | User-supplied      | Tank → filter → pump, return → tank |

## Fuel Flow Path

```text
Fuel Tank
    ↓
Fuel pickup (in-tank)
    ↓
Fuel Filter/Water Separator (with priming pump)
    ↓
Gear-Driven Fuel Pump (back of block)
    ↓
High-Pressure Injection Pump (front of engine)
    ↓
Common Rail → Injectors
    ↓
Return line → Fuel Tank
```

## Electrical Requirements

**None** - The gear-driven pump is mechanically driven by the engine. No fuel pump relay, ECM control, or safety shutoff circuit is required.

The factory Jeep LJ in-tank electric fuel pump is **not used** in this configuration.

## Priming

Use the manual hand pump on the fuel filter/water separator to prime the system before initial startup or after filter changes.

## Outstanding Items

{{ tbds() }}

## Related Documentation

- [R2.8 Installation Guide][r28-guide] - Cummins official documentation

[r28-guide]: https://www.cummins.com/engines/repower
