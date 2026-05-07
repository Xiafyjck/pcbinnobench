# 4-20mA Current Sampling Using ADS1115 and STM32F103C8

Use 10Ω resistor to generate a voltage difference, and sample using INA333. Note that common-mode voltage should not exceed 3.3V. See INA333 datasheet for details.

REF3012 provides 1.2V reference voltage.

Uses PB5, PB6, PB7 pins to communicate with ADS1115.
