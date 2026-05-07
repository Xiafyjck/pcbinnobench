This project aims to connect MCU with SHT30 and LM75B for communication.
Schematic part:
Each power supply pin of the MCU has a decoupling capacitor.
NRST pin pulled high.
BOOT0 pin pulled low.
PB10 as I2C SCL pin, PB11 as SDA pin.
PB12, PB13 as general-purpose MCU pins.
I2C SCL and SDA pulled high.
SHT30 R pin connected to GND, RESET pulled high, ADDR pin pulled low.
LM75B A0, A1, A2 address pins pulled low.
PCB part:
Decoupling capacitors placed near power pins.
