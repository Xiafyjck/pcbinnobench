from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_CUR-HIGHSIDE-001_task_4',
    project_files=['CUR-HIGHSIDE-001.kicad_pcb', 'CUR-HIGHSIDE-001.kicad_pro', 'CUR-HIGHSIDE-001.kicad_sch'],
    golden_hashes={'CUR-HIGHSIDE-001.kicad_pcb': '4fbf4787be6af045aca5914de3761116989069d87e77662f6a67bd81d068215f', 'CUR-HIGHSIDE-001.kicad_pro': '67e098fee2a2ba1aa160746e4f5fd8ecfe28debdf39f68822449fea80024a633', 'CUR-HIGHSIDE-001.kicad_sch': '6009395d51058c76a3df84bc2ce0caac999a55f667caeb6cdc85ab81ac825506'},
    source_hashes={'CUR-HIGHSIDE-001.kicad_pcb': '3a89e3274568a9f551412c43e026004e1524dd230eb3ad9869b9e679002927ad', 'CUR-HIGHSIDE-001.kicad_pro': '67e098fee2a2ba1aa160746e4f5fd8ecfe28debdf39f68822449fea80024a633', 'CUR-HIGHSIDE-001.kicad_sch': '5a007f2fd7bc229bef07760ad36c092c7e2bc2d94a783cfda40e836fe601af99'},
    schematic_file='CUR-HIGHSIDE-001.kicad_sch',
    pcb_file='CUR-HIGHSIDE-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'NC2': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 63.7, 'y': 44.4, 'rotation': 90.0}, 'U1': {'footprint': 'Package_SO:TSSOP-8_4.4x3mm_P0.65mm', 'x': 74.0, 'y': 44.0, 'rotation': 0.0}, 'J4': {'footprint': 'Connector_JST:JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical', 'x': 75.45, 'y': 53.1, 'rotation': 180.0}},
    netlist_checks={'NC2': {'1': 'Net-(U1--)', '2': 'Net-(U1-+)'}, 'U1': {'1': 'GND', '2': 'Net-(U1-+)', '3': 'Net-(U1--)', '4': 'GND', '5': '+3V3', '6': '+3V3'}, 'J4': {'1': 'GND', '2': '+3V3'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
