Please directly revise the KiCad project in the current workspace.

This is a KiCad project based on an STM32 MCU using a shared SPI bus (SCK / MOSI / MISO) to mount both W25Q32 and W25Q128 SPI Flash devices. Each Flash has an independent CS that is pulled low by the MCU in time division for selection. Both Flash devices use 3.3V power, SPI mode 0/3 is consistent, and the PCB uses a star topology. Please review whether the current design meets the communication goals, using the project files, project description, and `datasheets/`, and complete any necessary schematic or PCB modifications.

This task focuses on power-domain unity between the two Flash devices and the MCU, confirming that all Flash devices and the master controller operate in the same 3.3V power domain and that no separate power rail of another voltage is routed specifically for one Flash device.
