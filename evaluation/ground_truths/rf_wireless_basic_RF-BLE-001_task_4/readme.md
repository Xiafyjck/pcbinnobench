# RF-BLE-001

## Introduction

This project is a BLE minimum system board based on nRF52832, suitable for BLE communication, program download, and serial debugging.

Due to antenna impedance matching requirements, this board uses a 4-layer PCB.

## Power Supply

The board is powered by 5V input.

5V is stepped down to 3.3V by on-board LDO to power the nRF52832 and peripherals.

## Connectors

This board brings out the following interfaces:

\- 5V power input
\- SWD programming/debugging interface
\- UART serial interface
\- RESET button
\- User button
\- Status LED
\- PCB antenna

## SWD Interface

SWD interface for program download and debugging, includes:

\- 3.3V
\- GND
\- SWDIO
\- SWDCLK
\- RESET

## UART Interface

UART interface for serial communication and debug output, includes:

\- 3.3V
\- GND
\- TXD
\- RXD

When connecting to USB-TTL, crossover connection is required:

\- nRF52832 TXD → USB-TTL RXD
\- nRF52832 RXD → USB-TTL TXD
\- GND → GND

## Notes

\- Input power is 5V.
\- Chip operating voltage is 3.3V.
\- UART level is 3.3V, do not connect directly to 5V serial.
\- Check power, GND, SWD, and UART connections before use.
