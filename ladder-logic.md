# Ladder Logic Comparison

## Purpose

This document compares the Raspberry Pi Python program with an industrial PLC
ladder-logic implementation.

The Raspberry Pi GPIO output behaves similarly to a PLC digital output module
controlling a pilot light.

---

## Hardware Comparison

| Raspberry Pi Project | Industrial Control Equivalent |
|---|---|
| BCM GPIO17 | PLC digital output channel |
| Blue LED | Panel-mounted pilot light |
| Python program | PLC control program |
| GPIO HIGH | Output energized |
| GPIO LOW | Output de-energized |
| Ground rail | 0 VDC/common |
| Breadboard | Terminal strip or prototype panel |
| Multimeter verification | Output and field-device testing |

---

## Basic Output Rung

A continuously energized LED could be represented as:

```text
      System Enable                         Blue Pilot Light
|---------] [------------------------------------( )---------|
          XIC                                      OTE
```

### Interpretation

- `] [` represents an XIC instruction: Examine If Closed
- `( )` represents an OTE instruction: Output Energize
- When `System Enable` is true, the output coil energizes
- The energized output turns on the pilot light

---

## Timed Blink Sequence

The Python program turns the LED on for one second and off for one second.

A conceptual PLC implementation could use two timers and an internal state bit.

### Rung 1 — ON timer

```text
      Blink Enabled       LED State OFF
|---------] [----------------]/[---------------[TON T4:0]----|
                                      Preset: 1 second
```

### Rung 2 — Set LED state

```text
      T4:0/DN
|---------] [-----------------------------(OTL LED_State)----|
```

### Rung 3 — OFF timer

```text
      Blink Enabled        LED State ON
|---------] [----------------] [---------------[TON T4:1]----|
                                      Preset: 1 second
```

### Rung 4 — Reset LED state

```text
      T4:1/DN
|---------] [-----------------------------(OTU LED_State)----|
```

### Rung 5 — Physical output

```text
      LED_State                            GPIO17 / Pilot Light
|---------] [------------------------------------( )----------|
```

---

## Python Equivalent

```python
while True:
    blue_led.on()
    sleep(1)

    blue_led.off()
    sleep(1)
```

---

## Sequence of Operation

1. The program initializes BCM GPIO17 as a digital output.
2. GPIO17 transitions HIGH.
3. Current flows through the resistor and LED to ground.
4. The LED illuminates for one second.
5. GPIO17 transitions LOW.
6. Current flow stops.
7. The LED remains off for one second.
8. The cycle repeats until the operator presses `Ctrl+C`.
9. The cleanup routine commands GPIO17 LOW before the program exits.

---

## Control Narrative

**Equipment:** Raspberry Pi 5 LED demonstration circuit  
**Controlled device:** Blue LED  
**Output:** BCM GPIO17, physical pin 11  
**Common:** Raspberry Pi ground, physical pin 14  

When the LED controller is running, the software alternates GPIO17 between HIGH
and LOW states at one-second intervals. A HIGH state energizes the LED circuit.
A LOW state de-energizes the LED circuit.

When the program receives a keyboard interrupt, it commands the LED off,
releases the GPIO resource, and exits safely.
