Please directly revise the KiCad project in the current workspace.

This is a photodiode transimpedance amplifier sampling KiCad project using OPA847 for transimpedance amplification, ADS1115 for ADC conversion, and REF3033 for the reference voltage. Based on the project files, project description, and `datasheets/`, review whether the current design meets the measurement target, and complete the necessary schematic or PCB modification.

This task requires correcting an extra capacitor to ground in the signal path: in the schematic, a 10pF capacitor (reference C1) is attached to the signal path between the TIA output and the ADC input, forming an additional load to ground and creating a low-pass corner that conflicts with the sampling target. It is not part of the feedback compensation branch and should be regarded as a mistakenly placed component. Delete this capacitor and its connections so that the signal path is restored to a direct connection.
