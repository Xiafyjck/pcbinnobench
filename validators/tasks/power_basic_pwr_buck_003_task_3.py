from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_PWR-BUCK-003_task_3',
    project_files=['PWR-BUCK-003.kicad_pcb', 'PWR-BUCK-003.kicad_pro', 'PWR-BUCK-003.kicad_sch'],
    golden_hashes={'PWR-BUCK-003.kicad_pcb': '3f73d325bbb76699322781c652932d96b68e711e48a5a54eb9f5c03cfcd1007e', 'PWR-BUCK-003.kicad_pro': 'caa6593c1031443e52fc9428f004f8cfdec505bd80b183a0c92804cebb6b40b9', 'PWR-BUCK-003.kicad_sch': '0f904a5ee36308b108558ccc44e49129a59bac7dbd3d7f937b565c740170396b'},
    source_hashes={'PWR-BUCK-003.kicad_pcb': '2f901feb4442f8137c618bb471b51dc0de860e9f229fa801edcd0a7a7455ac4a', 'PWR-BUCK-003.kicad_pro': 'caa6593c1031443e52fc9428f004f8cfdec505bd80b183a0c92804cebb6b40b9', 'PWR-BUCK-003.kicad_sch': 'cb5505d6149abe14888910413d9516e3685757eeaa75410c70938241af704ed5'},
    schematic_file='PWR-BUCK-003.kicad_sch',
    pcb_file='PWR-BUCK-003.kicad_pcb',
    kicad_cli_checks=('drc', 'netlist_export'),
    position_checks={'J2': {'footprint': 'Connector_JST:JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical', 'x': 89.4, 'y': 59.15, 'rotation': -90.0}, 'C6': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 95.5, 'y': 65.4, 'rotation': 90.0}, 'C1': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 100.0, 'y': 77.2, 'rotation': 180.0}},
    netlist_checks={'J2': {'1': 'GND', '2': '/+1.8V'}, 'C6': {'1': 'Net-(U1-VBST)', '2': 'Net-(U1-SW)'}, 'C1': {'1': '+5V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
