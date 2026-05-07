Directly revise the KiCad project in the current workspace.

This is a 4-20mA current-loop sampling KiCad project. It uses a sampling resistor to convert loop current into a voltage difference, which is directly acquired differentially by the ADS1115, and the REF3033 provides a 3.3V reference. Review whether the current design meets the measurement goals, using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on the values of the interface components around the ADS1115, confirming that the value ranges of auxiliary interface components such as I²C pull-up resistors and power/reference decoupling capacitors match the ADS1115 operating level and frequency.
