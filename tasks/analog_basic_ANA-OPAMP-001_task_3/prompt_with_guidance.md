Please directly revise the KiCad project in the current workspace.

This is an OPA333 single-supply op-amp follower KiCad project using OPA333 as a voltage follower. The input is AC-coupled with DC bias and includes input protection diodes; power is brought in through XH254, and signal input / output can use either SMA or XH254 interfaces. Based on the project files, project description, and `datasheets/`, review whether the current design meets the measurement target, and complete the necessary schematic or PCB modification.

This task requires strengthening the reliability of power-related vias at the PCB level: on the current PCB, the pad-via connections of power / ground related nets (VCC, GND, bias midpoint, etc.) lack teardrop transitions, creating reliability and current-carrying concerns. In the PCB editor, add teardrops to pad-via nodes on power-type nets (typically marked `$teardrop_padvia$`), without affecting the existing routing or component positions of signal nets.
