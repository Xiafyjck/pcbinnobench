Directly revise the KiCad project in the current workspace.

This is a KiCad project where an STM32F103 mounts both SHT30 and LM75B sensors on the I²C bus. PB10/PB11 are used as I²C SCL/SDA, SHT30 RESET is pulled high and ADDR is pulled low, LM75B A0/A1/A2 are all pulled low, and the I²C bus SCL/SDA are pulled up to the operating supply. Please review whether the current design meets the communication goals based on the project files, project notes, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task requires repositioning pull-up resistor R4 on the PCB: the current R4 footprint position is approximately (135.0, 84.5), too far from the I²C main bus node, resulting in a long branch to the main bus. Please move R4's footprint to a position closer to the I²C main bus node (reference target coordinates approximately (144.0, 97.0)), making the branch between the pull-up and the main bus as short as possible, while keeping the schematic nets unchanged.
