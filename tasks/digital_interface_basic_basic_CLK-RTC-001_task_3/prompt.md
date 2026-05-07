Directly revise the KiCad project in the current workspace.

This is an RTC low-frequency crystal clock KiCad project based on an STM32 minimum system board. A 32.768 kHz low-frequency crystal, Y2, and a backup battery, BT1, are connected on the board to build an independent RTC clock domain. Based on the project files, project description, and `datasheets/`, review whether the current design meets the RTC clock stable startup and timekeeping goals, and complete the necessary schematic or PCB modifications.

This task focuses on the placement of the low-frequency crystal on the PCB, confirming that the crystal is close enough to the MCU oscillator pins and load capacitors, and avoids noise sources such as buttons, reset circuits, and switching power supplies.
