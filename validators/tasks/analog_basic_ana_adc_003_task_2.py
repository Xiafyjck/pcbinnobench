from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-ADC-003_task_2',
    project_files=['ANA-ADC-003.kicad_pcb', 'ANA-ADC-003.kicad_pro', 'ANA-ADC-003.kicad_sch', 'stm32_ads1115.kicad_sch'],
    golden_hashes={'ANA-ADC-003.kicad_pcb': 'c67d13a5e0360fbd25f81063d1cf225ed3e9a0b3d59fa2829adb43753e1ee70c', 'ANA-ADC-003.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-003.kicad_sch': 'a7b71220ab5899da1d562f0927b379af0e68c511753d607eb1c29ee7ac0aa85a', 'stm32_ads1115.kicad_sch': '24c952bab213c9d8990dd98c901689db9def89f0efc3aad710bbb416d919d45e'},
    source_hashes={'ANA-ADC-003.kicad_pcb': '17ac38289570b799994ca22ab232b3b2adc52998745c9cdf2c58f891e0d23fa3', 'ANA-ADC-003.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-003.kicad_sch': '5f3c07126caaa32519b0042860c93970fea93ab94d1296c68ebe82ff4cd912ee', 'stm32_ads1115.kicad_sch': '24c952bab213c9d8990dd98c901689db9def89f0efc3aad710bbb416d919d45e'},
    schematic_file='ANA-ADC-003.kicad_sch',
    pcb_file='ANA-ADC-003.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'U2': {'footprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'x': 132.0, 'y': 95.0, 'rotation': 0.0}, 'SW1': {'footprint': 'Button_Switch_THT:SW_PUSH_6mm', 'x': 109.25, 'y': 102.25, 'rotation': 90.0}, 'C8': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 141.5, 'y': 76.0, 'rotation': -90.0}},
    netlist_checks={'U2': {'1': '+3.3V', '10': 'unconnected-(U2-PA0-Pad10)', '11': 'unconnected-(U2-PA1-Pad11)', '12': 'unconnected-(U2-PA2-Pad12)', '13': 'unconnected-(U2-PA3-Pad13)', '14': 'unconnected-(U2-PA4-Pad14)'}, 'SW1': {'1': 'GND', '2': '/stm32/NRST'}, 'C8': {'1': '+3.3V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
