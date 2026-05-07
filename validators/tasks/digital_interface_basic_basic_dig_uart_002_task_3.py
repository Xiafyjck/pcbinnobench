from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='digital_interface_basic_basic_DIG-UART-002_task_3',
    project_files=['groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch', 'ldo.kicad_sch', 'stm32f1.kicad_sch', 'untitled2.kicad_sch'],
    golden_hashes={'groundtruth.kicad_pcb': '6f6fe8df3d15b5765cb8fd0edc5c88299936e4ec7faec575826c4e5ee3e22453', 'groundtruth.kicad_pro': '13e3b24af37b2180f8f8984dd5f1c3abf8362e3f44bceefabcf6f9cec491d38a', 'groundtruth.kicad_sch': '249d688c010ae331da1113a98949ec05226c561cf003512cf12d2f86cfc0745c', 'ldo.kicad_sch': '11500a66e6253fd4c19e4fe7b2b837fc794458345c5f991b082e5c634165f457', 'stm32f1.kicad_sch': '39eb213f84824d56705f125ad90a47cef20a6375492ee07ffd875c760f12eddf', 'untitled2.kicad_sch': '9fca8cfb3d02c7b8c8093417d99aa75cc2c005f7386e89ffa5e020f33a844cb4'},
    source_hashes={'groundtruth.kicad_pcb': 'bb3a4f26bad340b5f23715adaed4243a1e040c91fcc30bdae7ba0d3a84927520', 'groundtruth.kicad_pro': '13e3b24af37b2180f8f8984dd5f1c3abf8362e3f44bceefabcf6f9cec491d38a', 'groundtruth.kicad_sch': '249d688c010ae331da1113a98949ec05226c561cf003512cf12d2f86cfc0745c', 'ldo.kicad_sch': '109429eda28d02b218eed3b89e93ea21ea3534fbf1efac981023a12de6954b15', 'stm32f1.kicad_sch': '39eb213f84824d56705f125ad90a47cef20a6375492ee07ffd875c760f12eddf', 'untitled2.kicad_sch': '9fca8cfb3d02c7b8c8093417d99aa75cc2c005f7386e89ffa5e020f33a844cb4'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('erc', 'netlist_export'),
    position_checks={'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 81.925, 'y': 104.25, 'rotation': 0.0}, 'C11': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 73.0, 'y': 113.55, 'rotation': 90.0}, 'C5': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 84.01, 'y': 112.95, 'rotation': -90.0}},
    netlist_checks={'R2': {'1': 'Net-(U1-PA9)', '2': '/usb-uart/RX'}, 'C11': {'1': '+5V', '2': 'GND'}, 'C5': {'1': 'Net-(U4-VO)', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
