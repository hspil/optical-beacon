# Optical ham radio beacon

Raspberry Pi Pico microcontroller as an optical beacon

Generates MCW by rapidly flickering an LED

Uses PIO (programmable IO) subprocessor for precise timing

First flash the [micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) .uf2 firmware to the pico, then use `flash` to transfer `beacon.py`

CW speed, pitch, and beacon message can be set in `beacon.py`
