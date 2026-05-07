Directly revise the KiCad project in the current workspace.

This is a high-side current-sense amplifier KiCad project that uses an INA240-class current-sense amplifier to measure the voltage drop across a shunt resistor on a 24V industrial power bus and sends the output to a 3.3V sampling interface. The sense inputs must operate stably within the normal high-side common-mode range and must also withstand input stress caused by industrial load disconnection, cable disturbance, or bus transients. Please review the project files, project description, and `datasheets/` to determine whether the current design meets these engineering goals, and complete any necessary schematic or PCB modifications.

This task focuses on the withstand capability of the sense amplifier IN+ / IN- inputs under abnormal conditions such as industrial load transients and bus disturbances.
