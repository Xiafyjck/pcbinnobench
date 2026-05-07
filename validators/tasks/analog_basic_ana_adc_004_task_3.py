from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-ADC-004_task_3',
    project_files=['ANA-ADC-004.kicad_pcb', 'ANA-ADC-004.kicad_pro', 'ANA-ADC-004.kicad_sch', 'stm32_ads1115.kicad_sch'],
    golden_hashes={'ANA-ADC-004.kicad_pcb': '83dc263d1e6b8cb2cecd3a7b45831e1d76d15cd5edef155acf88761163bbec8e', 'ANA-ADC-004.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-004.kicad_sch': 'f837538ffdbb198fc8c14d928ed621cd1996265faedfbe433f36cd73e5e66e8b', 'stm32_ads1115.kicad_sch': '549679d229e4e0ad5f96f244a53a109fd4f90e217ac4cd9442f2000def1c0f5f'},
    source_hashes={'ANA-ADC-004.kicad_pcb': '7a39272aafee8d3993a84167dc80b46d26d8416f43b4147f2eccbd36e5a7800d', 'ANA-ADC-004.kicad_pro': 'a184bfb239f12328529224c6c8fc983cecf21788abbc72fce50a008c35408b27', 'ANA-ADC-004.kicad_sch': 'ce063df602ab6ec39c314268712ace0f4c9e35ccb191785c9598a208c06a16eb', 'stm32_ads1115.kicad_sch': '549679d229e4e0ad5f96f244a53a109fd4f90e217ac4cd9442f2000def1c0f5f'},
    schematic_file='ANA-ADC-004.kicad_sch',
    pcb_file='ANA-ADC-004.kicad_pcb',
    kicad_cli_checks=('drc', 'erc'),
    position_checks={'C4': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 120.625, 'y': 80.75, 'rotation': 90.0}, 'C2': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 131.5, 'y': 64.5, 'rotation': 90.0}, 'R3': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 131.0, 'y': 86.5, 'rotation': 180.0}},
    netlist_checks={'C4': {'1': 'GND', '2': 'Net-(U4-+)'}, 'C2': {'1': '+3.3V', '2': 'GND'}, 'R3': {'1': '/stm32/BOOT0', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
