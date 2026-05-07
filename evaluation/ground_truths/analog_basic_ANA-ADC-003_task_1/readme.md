# Differential Voltage Sampling Using ADS1115 and STM32F103C8

Sampling uses INA333, powered by 3.3V, REF3012 provides 1.2V reference voltage. Note that common-mode voltage must not exceed 3.3V, see INA333 datasheet for details.

Uses PB5, PB6, PB7 pins to communicate with ADS1115.
