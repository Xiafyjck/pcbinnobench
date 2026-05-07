Please directly revise the KiCad project in the current workspace.

This is a CH340C-based USB-to-UART interface KiCad project. USB D+ / D- enter the CH340C through series resistors, with ESD protection devices in between. On the UART side, TX / RX / GND / 3.3V are brought out through a pin header, TX / RX each have 22-100Ω in series, and a 10µF local bulk capacitor is placed near the CH340. Please review whether the current design meets the communication goals, using the project files, project description, and `datasheets/`, and complete any necessary schematic or PCB modifications.

This task focuses on overcurrent/backfeed protection in the USB input power path, confirming that an appropriate current-limiting/resettable protection device exists on the power branch entering the board from USB VBUS, can withstand USB bus faults, and automatically recovers after the fault is removed.
