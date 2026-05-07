Please directly revise the KiCad project in the current workspace.

This is a low-side shunt-resistor current-sensing KiCad project using an INA282 and a 1.65V reference bias to acquire load current and send the output to an MCU or ADC. In a low-side shunt scheme, the main load return necessarily passes through the shunt resistor, so the voltage drop from that return path must not be coupled into the system sampling reference. Please review whether the current design meets the engineering goals in terms of separation between the power return and signal reference, using the project files, project description, and `datasheets/`, and complete any necessary schematic or PCB modifications.

This task focuses on the network separation between the main load return path and the INA282 / MCU sampling reference in a low-side shunt scheme.
