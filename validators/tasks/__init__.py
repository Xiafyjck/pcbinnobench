from __future__ import annotations

import importlib

TASK_VALIDATORS = {
    'Power_basic_CUR-HALL-001_task_1': 'power_basic_cur_hall_001_task_1',
    'Power_basic_CUR-HIGHSIDE-001_task_3': 'power_basic_cur_highside_001_task_3',
    'Power_basic_CUR-HIGHSIDE-001_task_4': 'power_basic_cur_highside_001_task_4',
    'Power_basic_CUR-SHUNT-001_task_2': 'power_basic_cur_shunt_001_task_2',
    'Power_basic_CUR-SHUNT-001_task_4': 'power_basic_cur_shunt_001_task_4',
    'Power_basic_PWR-BUCK-001_task_2': 'power_basic_pwr_buck_001_task_2',
    'Power_basic_PWR-BUCK-002_task_3': 'power_basic_pwr_buck_002_task_3',
    'Power_basic_PWR-BUCK-003_task_3': 'power_basic_pwr_buck_003_task_3',
    'Power_basic_PWR-LDO-001_task_1': 'power_basic_pwr_ldo_001_task_1',
    'Power_basic_PWR-LDO-004_task_4': 'power_basic_pwr_ldo_004_task_4',
    'analog_basic_ANA-ADC-003_task_1': 'analog_basic_ana_adc_003_task_1',
    'analog_basic_ANA-ADC-003_task_2': 'analog_basic_ana_adc_003_task_2',
    'analog_basic_ANA-ADC-004_task_1': 'analog_basic_ana_adc_004_task_1',
    'analog_basic_ANA-ADC-004_task_3': 'analog_basic_ana_adc_004_task_3',
    'analog_basic_ANA-MID-007_task_4': 'analog_basic_ana_mid_007_task_4',
    'analog_basic_ANA-OPAMP-001_task_2': 'analog_basic_ana_opamp_001_task_2',
    'analog_basic_ANA-OPAMP-001_task_3': 'analog_basic_ana_opamp_001_task_3',
    'analog_basic_ANA-OPAMP-003_task_4': 'analog_basic_ana_opamp_003_task_4',
    'analog_medium_ANA-MID-004_task_4': 'analog_medium_ana_mid_004_task_4',
    'digital_interface_basic_basic_CLK-RTC-001_task_3': 'digital_interface_basic_basic_clk_rtc_001_task_3',
    'digital_interface_basic_basic_DIG-I2C-002_task_3': 'digital_interface_basic_basic_dig_i2c_002_task_3',
    'digital_interface_basic_basic_DIG-SPI-003_task_3': 'digital_interface_basic_basic_dig_spi_003_task_3',
    'digital_interface_basic_basic_DIG-UART-002_task_3': 'digital_interface_basic_basic_dig_uart_002_task_3',
    'digital_interface_basic_basic_DIG-UART-003_task_4': 'digital_interface_basic_basic_dig_uart_003_task_4',
    'industrial_bus_basic_BUS-RS485-001_task_4': 'industrial_bus_basic_bus_rs485_001_task_4',
    'industrial_bus_basic_BUS-RS485-004_task_1': 'industrial_bus_basic_bus_rs485_004_task_1',
    'industrial_bus_basic_BUS-RS485-004_task_4': 'industrial_bus_basic_bus_rs485_004_task_4',
    'protection_basic_HSWAP-PMOS-001_task_4': 'protection_basic_hswap_pmos_001_task_4',
    'protection_basic_PROT-FUSE-001_task_1': 'protection_basic_prot_fuse_001_task_1',
    'protection_basic_PROT-FUSE-001_task_2': 'protection_basic_prot_fuse_001_task_2',
    'protection_basic_PROT-FUSE-002_task_1': 'protection_basic_prot_fuse_002_task_1',
    'protection_basic_PROT-TVS-003_task_2': 'protection_basic_prot_tvs_003_task_2',
    'rf_wireless_basic_RF-BLE-001_task_2': 'rf_wireless_basic_rf_ble_001_task_2',
    'rf_wireless_basic_RF-BLE-001_task_3': 'rf_wireless_basic_rf_ble_001_task_3',
    'rf_wireless_basic_RF-BLE-001_task_4': 'rf_wireless_basic_rf_ble_001_task_4',
}

def load_validator(task_id: str):
    try:
        module_name = TASK_VALIDATORS[task_id]
    except KeyError as exc:
        raise KeyError(f"unknown task validator: {task_id}") from exc
    module = importlib.import_module(f"validators.tasks.{module_name}")
    return module.validate
