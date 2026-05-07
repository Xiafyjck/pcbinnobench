from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_CUR-HIGHSIDE-001_task_3',
    project_files=['CUR-HIGHSIDE-001.kicad_pcb', 'CUR-HIGHSIDE-001.kicad_pro', 'CUR-HIGHSIDE-001.kicad_sch'],
    golden_hashes={'CUR-HIGHSIDE-001.kicad_pcb': '4fbf4787be6af045aca5914de3761116989069d87e77662f6a67bd81d068215f', 'CUR-HIGHSIDE-001.kicad_pro': '67e098fee2a2ba1aa160746e4f5fd8ecfe28debdf39f68822449fea80024a633', 'CUR-HIGHSIDE-001.kicad_sch': '6009395d51058c76a3df84bc2ce0caac999a55f667caeb6cdc85ab81ac825506'},
    source_hashes={'CUR-HIGHSIDE-001.kicad_pcb': '3fa40f7230a330611b56d1a07c48f271581de6c425fef4588a0f160f556edea4', 'CUR-HIGHSIDE-001.kicad_pro': '67e098fee2a2ba1aa160746e4f5fd8ecfe28debdf39f68822449fea80024a633', 'CUR-HIGHSIDE-001.kicad_sch': '6009395d51058c76a3df84bc2ce0caac999a55f667caeb6cdc85ab81ac825506'},
    schematic_file='CUR-HIGHSIDE-001.kicad_sch',
    pcb_file='CUR-HIGHSIDE-001.kicad_pcb',
    kicad_cli_checks=('drc', 'netlist_export'),
    position_checks={'NC1': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 67.5, 'y': 40.525, 'rotation': 90.0}, 'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 63.7, 'y': 40.5, 'rotation': 90.0}, 'D1': {'footprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'x': 49.25, 'y': 44.2, 'rotation': 90.0}},
    netlist_checks={'NC1': {'1': 'Net-(U1-+)', '2': 'GND'}, 'R2': {'1': 'Net-(U1-+)', '2': 'Net-(R1-Pad3)'}, 'D1': {'1': 'GND', '2': '+3V3', '3': '/IN-', '4': 'GND', '5': '+3V3', '6': '/IN+'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
