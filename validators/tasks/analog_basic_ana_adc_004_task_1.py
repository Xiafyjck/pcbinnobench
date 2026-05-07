from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-ADC-004_task_1',
    project_files=['ANA-ADC-004.kicad_pcb', 'ANA-ADC-004.kicad_pro', 'ANA-ADC-004.kicad_sch', 'stm32_ads1115.kicad_sch'],
    golden_hashes={'ANA-ADC-004.kicad_pcb': '83dc263d1e6b8cb2cecd3a7b45831e1d76d15cd5edef155acf88761163bbec8e', 'ANA-ADC-004.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-004.kicad_sch': 'f837538ffdbb198fc8c14d928ed621cd1996265faedfbe433f36cd73e5e66e8b', 'stm32_ads1115.kicad_sch': '549679d229e4e0ad5f96f244a53a109fd4f90e217ac4cd9442f2000def1c0f5f'},
    source_hashes={'ANA-ADC-004.kicad_pcb': '6a63041064c67a7f73607e7aad667146d87c498157b342954081cf866e847e97', 'ANA-ADC-004.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-004.kicad_sch': 'cbc4bd7fa0a26604346b103b766b37a81c9b1f231cf63cd3446df3c67f1b5365', 'stm32_ads1115.kicad_sch': '549679d229e4e0ad5f96f244a53a109fd4f90e217ac4cd9442f2000def1c0f5f'},
    schematic_file='ANA-ADC-004.kicad_sch',
    pcb_file='ANA-ADC-004.kicad_pcb',
    kicad_cli_checks=('erc', 'netlist_export'),
    position_checks={'R9': {'footprint': 'Resistor_SMD:R_2512_6332Metric', 'x': 113.0, 'y': 74.5, 'rotation': -90.0}, 'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 117.125, 'y': 77.75, 'rotation': 0.0}, 'C9': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 132.0, 'y': 71.5, 'rotation': 90.0}},
    netlist_checks={'R9': {'1': '/ADC_LIN', '2': '/ADC_HIN'}, 'R1': {'1': '/ADC_HIN', '2': 'Net-(U4-+)'}, 'C9': {'1': '+3.3V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
