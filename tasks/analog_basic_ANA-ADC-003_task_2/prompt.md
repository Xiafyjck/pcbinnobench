Please directly revise the KiCad project in the current workspace.

This is a differential voltage-sampling KiCad project using an INA333, ADS1115, REF3012, and STM32F103. The whole board runs from a 3.3V single supply, and the REF3012 provides a 1.2V reference. Please review whether the current design meets the measurement goals, using the project files, project description, and `datasheets/`, and complete any necessary schematic or PCB modifications.

This task focuses on interface impedance matching between the signal source and analog front end, confirming that there is no interaction affecting measurement accuracy among the input network, gain/feedback network, equivalent impedance of the preceding signal source, and downstream load.
