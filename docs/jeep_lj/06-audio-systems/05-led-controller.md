---
hide:
  - toc
tags:
  - product-details
  - audio-systems
  - jl-audio
---

# 6.5 LED Controller {#led-controller}

RGB LED controller for speaker lighting and footwell pods, with WiFi app and rotary encoder control.

/// html | div.product-info
![JL Audio MLC-RW](../images/jl-audio-mlc-rw.jpg){ loading=lazy }

**Type:** Marine LED Lighting Controller

**Model:** MLC-RW

**Manufacturer:** JL Audio

**Product Page:** [MLC-RW][product-link]

**Manual:** [Installation Manual][manual-link]

**Mounting:** Near amplifier (behind dash or cargo area)

**Power Source:** SwitchPros OUTPUT-5 (15A)

///

## Specifications

| Spec         |                         Value |
| :----------- | ----------------------------: |
| Power Output |         30A (400W) continuous |
| Capacity     |    Up to 60 JL Audio speakers |
| Actual Load  | 5-10A (5 speakers + footwell) |
| Control      |     WiFi app + rotary encoder |
| Technology   |  PWM (Pulse Width Modulation) |

## Protection Features

- Over-current protection
- Short-circuit protection
- Voltage monitoring
- Temperature monitoring

## Control Options

**Rotary Encoder (dash-mounted):**

- Press & hold 2 sec: Power ON
- Press & hold 5 sec: Power OFF
- Rotate: Color/brightness/speed

**WiFi App:** LiteWave ITI (iOS/Android)

## LED Loads

| Device              | LED Draw | Notes                   |
| :------------------ | :------- | :---------------------- |
| Front Speakers (2x) | ~1A      | M6-650X-S-GmTi-i        |
| Rear Speakers (2x)  | ~1A      | M6-650VEX-Mb-S-GmTi-i   |
| Subwoofers (2x)     | ~2A      | M6-8IB-S-GmTi-i-4 (one tap per sub) |
| Footwell Pods (4x)  | ~1A      | LED4Life RGBW           |
| **Total**           | **~6A**  | Well under 30A capacity |

## Wiring

| Connection | Wire      | Source           | Notes              |
| :--------- | :-------- | :--------------- | :----------------- |
| Power (+)  | 14 AWG    | SwitchPros OUT-5 | 15A capacity       |
| Ground (−) | 14 AWG    | Dash ground      | Same ground as head unit |
| RGB Out    | 20 AWG    | To speakers | Via XM-WHTMFC     |
| Encoder    | Extension | To dash     | Rotary control    |

## Integrated Speaker/LED Cable

**JL Audio XM-WHTMFC Multifunction Cable:**

| Wire    | Gauge         | Function     |
| :------ | :------------ | :----------- |
| Speaker | 2x 16 AWG OFC | Audio signal |
| LED     | 4x 20 AWG OFC | RGB + common |

- Single cable per speaker (audio + LED)
- Marine-grade white PVC jacket
- Stannum-plated for corrosion resistance
- Available: 25 ft or 250 ft spools

## Footwell Integration

Footwell pods wire in parallel with speaker LEDs:

| LED4Life Wire | MLC-RW Wire     | Function       |
| :------------ | :-------------- | :------------- |
| +12V          | White           | Common anode   |
| R             | Red             | Red LED (−)    |
| G             | Green           | Green LED (−)  |
| B             | Blue            | Blue LED (−)   |
| W             | _Not connected_ | White (unused) |

W channel capped - MLC-RW is RGB only.

See [Footwell Lights][footwell-lights] for pod details.

## Outstanding Items

- [ ] Confirm LED4Life pod wire colors match MLC-RW pinout

## Related Documentation

- [Audio Systems Overview][audio-overview]
- [Speakers][speakers]
- [Subwoofer][subwoofer]
- [Footwell Lights][footwell-lights]
- [BODY PDU][body-pdu]

[audio-overview]: index.md
[speakers]: 03-speakers.md
[subwoofer]: 04-subwoofer.md
[footwell-lights]: ../04-offroad-lighting/09-footwell-lights.md
[body-pdu]: ../01-power-systems/03-aux-battery-distribution/03-body-pdu.md
[product-link]: https://www.garmin.com/en-US/p/1669617/
[manual-link]: https://static.garmin.com/pumac/MLC_RW_MAN.pdf
