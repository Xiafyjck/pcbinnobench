Please directly revise the KiCad project in the current workspace.

This is a low-side shunt resistor current sensing KiCad project, using an INA282 and a 1.65V reference bias to acquire load current up to about 3A, and sending the output to a low-voltage sampling interface. The shunt resistor is both the measurement element and a heat-generating element, so its resistance, package, and rated power must be able to withstand the target load current over long-term operation. Please review whether the current design meets this goal using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on whether the shunt resistor's power dissipation under a 3A continuous load current matches the carrying capability of the selected package.
