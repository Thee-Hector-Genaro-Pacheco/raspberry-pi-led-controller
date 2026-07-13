# raspberry-pi-led-controller
# Raspberry Pi LED Controller

## Overview

This project demonstrates how to control an LED using a Raspberry Pi GPIO output pin, a resistor, and a breadboard circuit.

The objective of this project was to learn:

- Raspberry Pi GPIO fundamentals
- Breadboard wiring
- LED polarity
- Electrical troubleshooting
- Voltage measurements using a multimeter
- Python hardware control

---

## Components

- Raspberry Pi
- Breadboard
- LED
- Resistor
- Jumper wires
- Digital multimeter

---

## Wiring

### Raspberry Pi Connections

| Raspberry Pi Pin | Function | Breadboard |
|------------------|----------|-------------|
| Pin 11 | GPIO17 Output | A10 |
| Pin 14 | Ground (GND) | Blue ground rail |

---

## Circuit Path

GPIO17 → Resistor → LED → Ground

---

## Project Lessons Learned

During testing, the circuit initially failed because the LED polarity was reversed.

Troubleshooting steps included:

- Verifying GPIO voltage output
- Measuring 3.3 V with a multimeter
- Confirming ground continuity
- Testing the LED independently
- Correcting LED polarity

---

## Run the Program

```bash
python3 blink.py
```

---

## Stop the Program

```bash
CTRL + C
```

