Directly revise the KiCad project in the current workspace.

This is a KiCad project based on an STM32F103 that mounts both an SHT30 and an LM75B sensor on an I²C bus. PB10/PB11 are used as I²C SCL/SDA, the SHT30 RESET is pulled high and ADDR is pulled low, all LM75B A0/A1/A2 pins are pulled low, and the I²C bus SCL/SDA are pulled up to the operating supply. Review whether the current design meets the communication goals, using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on the topology of the I²C bus on the PCB, confirming that the pull-up resistors are placed as close as possible to the main bus node and that the branch from each slave device to the main bus is kept as short as possible, avoiding excessive parasitic capacitance from long stubs.
