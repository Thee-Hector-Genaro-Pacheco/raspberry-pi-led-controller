"""Raspberry Pi GPIO17 LED controller.

Hardware:
- Raspberry Pi 5
- Blue LED
- Current-limiting resistor
- Breadboard
- Jumper wires

GPIO numbering uses Broadcom (BCM) numbering.
BCM GPIO17 corresponds to physical pin 11.
"""

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    print("ON")
    led.on()
    sleep(1)

    print("OFF")
    led.off()
    sleep(1)