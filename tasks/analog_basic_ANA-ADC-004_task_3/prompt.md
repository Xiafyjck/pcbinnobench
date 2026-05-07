Directly revise the KiCad project in the current workspace.

This is a 4-20mA current-sampling KiCad project. It uses a 10Ω sampling resistor to convert current into a voltage difference, then uses an INA333, ADS1115, and STM32F103 to complete differential amplification and ADC acquisition. The REF3012 provides a 1.2V reference, and the entire board runs from a 3.3V single supply. Review whether the current design meets the measurement goals, using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on the reference voltage, bias node, decoupling, and noise transfer in the sampling chain, confirming that the reference-source accuracy and load capability, bypass capacitors, instrumentation-amplifier reference pin, ADC input reference, and power-supply noise paths together meet the measurement-stability requirements.
