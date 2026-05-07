Directly revise the KiCad project in the current workspace.

This is a photodiode transimpedance-amplifier sampling KiCad project using an OPA847 for transimpedance amplification, an ADS1115 for ADC conversion, and a REF3033 to provide the reference voltage. Review whether the current design meets the measurement goals, using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on the actual usable bandwidth of the sampling chain, confirming that there are no extra filtering / bandwidth-limiting components on the signal path from the TIA output to the ADC input that conflict with the sampling target, and that capacitance to ground outside the feedback / compensation network does not introduce an unintended low-pass corner.
