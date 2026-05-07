Directly revise the KiCad project in the current workspace.

This is a 4-20mA current sampling KiCad project that uses a 10Ω sampling resistor to convert current into a voltage difference, then uses INA333, ADS1115, and STM32F103 to complete differential amplification and ADC acquisition. REF3012 provides a 1.2V reference, and the entire board operates from a 3.3V single supply. Based on the project files, project description, and `datasheets/`, review whether the current design meets the measurement goals, and complete the necessary schematic or PCB modifications.

This task focuses on the range budget, gain setting, and ADC input range matching of the 4-20mA current sampling chain, confirming that the sampling resistor, instrumentation amplifier, reference/bias nodes, ADC input configuration, and minimum/maximum input conditions are mutually consistent.
