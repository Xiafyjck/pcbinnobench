from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_PWR-BUCK-001_task_2',
    project_files=['PWR-BUCK-001.kicad_pcb', 'PWR-BUCK-001.kicad_pro', 'PWR-BUCK-001.kicad_sch'],
    golden_hashes={'PWR-BUCK-001.kicad_pcb': 'f7fb86b49f2be0f9329666b309bb531a5df849169e9d57b5a05cf63a23a48595', 'PWR-BUCK-001.kicad_pro': '938e833d49cbf39dbc50472adf01cdd934194ea423971009c52b2687a01aed23', 'PWR-BUCK-001.kicad_sch': '9b4acecdf7fc6bcf866a2db19f97afd2d44c65da2312fabe6db07f08b1126ae0'},
    source_hashes={'PWR-BUCK-001.kicad_pcb': '22daeaa32aeba9d80d05117d8d2881e9e7d15c84ed518b9783cda721e0414cdd', 'PWR-BUCK-001.kicad_pro': '938e833d49cbf39dbc50472adf01cdd934194ea423971009c52b2687a01aed23', 'PWR-BUCK-001.kicad_sch': '187fbca226a9c3930e3b6ea7fd2f6fb431d337d0b8c1e787526a60cf7470cf52'},
    schematic_file='PWR-BUCK-001.kicad_sch',
    pcb_file='PWR-BUCK-001.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'TP_OUT1': {'footprint': 'TestPoint:TestPoint_Pad_D2.0mm', 'x': 57.658, 'y': 102.108, 'rotation': 0.0}, 'C3': {'footprint': 'Capacitor_SMD:C_1206_3216Metric', 'x': 33.716, 'y': 94.234, 'rotation': 180.0}, 'J2': {'footprint': 'Connector_JST:JST_XH_B2B-XH-AM_1x02_P2.50mm_Vertical', 'x': 35.346, 'y': 99.314, 'rotation': 0.0}},
    netlist_checks={'TP_OUT1': {'1': '+5V'}, 'C3': {'1': '+5V', '2': 'GND'}, 'J2': {'1': '+5V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
