from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_CUR-SHUNT-001_task_4',
    project_files=['CUR-SHUNT-001.kicad_pcb', 'CUR-SHUNT-001.kicad_pro', 'CUR-SHUNT-001.kicad_sch'],
    golden_hashes={'CUR-SHUNT-001.kicad_pcb': '7000aa14b0a9c2f4d6bd804e95ab901f395d877eaf9fac7f9bd09a8b5ff96d9f', 'CUR-SHUNT-001.kicad_pro': 'ed30c105e22cbc5d7aeb5f0fda351430bab0a36880256925ba9dbe5fb0bfed90', 'CUR-SHUNT-001.kicad_sch': '506745611ca46725d9aaccb724d4df729cff72d21a936968844173ef87e4d1e0'},
    source_hashes={'CUR-SHUNT-001.kicad_pcb': '8b13935d809e7d67b69f4478de12268fc536f62815feb7aea6257a3a59dd466e', 'CUR-SHUNT-001.kicad_pro': 'ed30c105e22cbc5d7aeb5f0fda351430bab0a36880256925ba9dbe5fb0bfed90', 'CUR-SHUNT-001.kicad_sch': '4a94d7cb9d4d85c3b256e6692f6ce66177cafa43bdbd7912bb6d33b8f804a50a'},
    schematic_file='CUR-SHUNT-001.kicad_sch',
    pcb_file='CUR-SHUNT-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'J2': {'footprint': 'Connector_JST:JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical', 'x': 163.2, 'y': 71.1, 'rotation': 90.0}, 'C2': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 143.5, 'y': 70.99, 'rotation': 90.0}, 'C4': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 159.1, 'y': 70.3, 'rotation': 90.0}},
    netlist_checks={'J2': {'1': 'GND', '2': 'Net-(J2-Pin_2)'}, 'C2': {'1': 'Net-(U2--)', '2': 'Net-(U2-+)'}, 'C4': {'1': 'GND', '2': 'Net-(J2-Pin_2)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
