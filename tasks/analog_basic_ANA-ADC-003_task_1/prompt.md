Directly revise the KiCad project in the current workspace.

This is a differential voltage-sampling KiCad project using an INA333, ADS1115, REF3012, and STM32F103. The entire board runs from a 3.3V single supply, and the REF3012 provides a 1.2V reference. Review whether the current design meets the measurement goals, using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on the reference-voltage use and biasing strategy of the single-supply analog front end, confirming that the instrumentation amplifier output operating range and the downstream ADC input range can be aligned around the same reference point.
