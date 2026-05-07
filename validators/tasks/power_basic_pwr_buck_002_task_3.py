from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_PWR-BUCK-002_task_3',
    project_files=['PWR-BUCK-002.kicad_pcb', 'PWR-BUCK-002.kicad_pro', 'PWR-BUCK-002.kicad_sch'],
    golden_hashes={'PWR-BUCK-002.kicad_pcb': 'cb1c751909520a698cdd6799e893f946f6320630677e2c7cf9ced567696b92c2', 'PWR-BUCK-002.kicad_pro': '0975a6bdd650ea520294ebfaecc4acd84d44a66ea75385c5b8d9fd7913282fa7', 'PWR-BUCK-002.kicad_sch': '0c36aef0fa5ed211e24c0cae199f575bb10a358cd8c81ebf75ad663e24072666'},
    source_hashes={'PWR-BUCK-002.kicad_pcb': '105b568e96adf9ef360b7e69e439a9282ff59965f6247f69763e7a09800abfd3', 'PWR-BUCK-002.kicad_pro': '0975a6bdd650ea520294ebfaecc4acd84d44a66ea75385c5b8d9fd7913282fa7', 'PWR-BUCK-002.kicad_sch': 'aba3f0c15a571cbd85d384b0d5a8a077d8f486ff6d429a8db7309908a1c52c4c'},
    schematic_file='PWR-BUCK-002.kicad_sch',
    pcb_file='PWR-BUCK-002.kicad_pcb',
    kicad_cli_checks=('drc', 'erc'),
    position_checks={'TP_GND1': {'footprint': 'TestPoint:TestPoint_Pad_D2.0mm', 'x': 44.196, 'y': 41.656, 'rotation': 90.0}, 'C1': {'footprint': 'Capacitor_SMD:C_1206_3216Metric', 'x': 53.594, 'y': 49.784, 'rotation': 90.0}, 'C4': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 74.947, 'y': 45.466, 'rotation': 0.0}},
    netlist_checks={'TP_GND1': {'1': 'GND'}, 'C1': {'1': '+24V', '2': 'GND'}, 'C4': {'1': '+3.3V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
