Please directly revise the KiCad project in the current workspace.

This is a differential voltage sampling KiCad project using INA333, ADS1115, REF3012, and STM32F103. The whole board operates from a 3.3V single supply, and REF3012 provides a 1.2V reference. Based on the project files, project description, and `datasheets/`, review whether the current design meets the measurement target, and complete the necessary schematic or PCB modification.

This task requires correcting the loading problem that the INA333 input presents to the external signal source: in the schematic, each of the two INA333 differential input terminals is connected to GND through a pulldown resistor, forming a low-impedance load for the external signal source, disrupting interface impedance matching and causing measurement error. Delete these two input-to-GND pulldown resistors and the GND power symbols connected to them, so that the two INA333 inputs maintain high input impedance to the external signal source.
