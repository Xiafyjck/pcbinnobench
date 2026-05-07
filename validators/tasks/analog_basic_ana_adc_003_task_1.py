from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-ADC-003_task_1',
    project_files=['ANA-ADC-003.kicad_pcb', 'ANA-ADC-003.kicad_pro', 'ANA-ADC-003.kicad_sch', 'stm32_ads1115.kicad_sch'],
    golden_hashes={'ANA-ADC-003.kicad_pcb': 'c67d13a5e0360fbd25f81063d1cf225ed3e9a0b3d59fa2829adb43753e1ee70c', 'ANA-ADC-003.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-003.kicad_sch': 'a7b71220ab5899da1d562f0927b379af0e68c511753d607eb1c29ee7ac0aa85a', 'stm32_ads1115.kicad_sch': '24c952bab213c9d8990dd98c901689db9def89f0efc3aad710bbb416d919d45e'},
    source_hashes={'ANA-ADC-003.kicad_pcb': 'fc28c30fb7111754c8fd989952ff727664a395e265df2b26eec11f845d642e98', 'ANA-ADC-003.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-003.kicad_sch': 'cefe4f61996e5078012226582f67af239d3907ef0a212cd0daa4d5ab32152401', 'stm32_ads1115.kicad_sch': '24c952bab213c9d8990dd98c901689db9def89f0efc3aad710bbb416d919d45e'},
    schematic_file='ANA-ADC-003.kicad_sch',
    pcb_file='ANA-ADC-003.kicad_pcb',
    kicad_cli_checks=('erc',),
    position_checks={'C5': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 119.675, 'y': 74.25, 'rotation': 90.0}, 'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 116.125, 'y': 70.75, 'rotation': 0.0}, 'J1': {'footprint': 'Connector_JST:JST_XH_B2B-XH-AM_1x02_P2.50mm_Vertical', 'x': 107.625, 'y': 75.75, 'rotation': 90.0}},
    netlist_checks={'C5': {'1': 'Net-(U4-+)', '2': 'Net-(U4--)'}, 'R2': {'1': '/ADC_LIN', '2': 'Net-(U4--)'}, 'J1': {'1': '/ADC_HIN', '2': '/ADC_LIN'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
