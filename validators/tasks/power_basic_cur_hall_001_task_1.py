from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_CUR-HALL-001_task_1',
    project_files=['CUR-HALL-001.kicad_pcb', 'CUR-HALL-001.kicad_pro', 'CUR-HALL-001.kicad_sch'],
    golden_hashes={'CUR-HALL-001.kicad_pcb': 'd36b72c0f7de95e26a69c0fcc5375f3fdfcc98e39d8c7358becb3f3a25108920', 'CUR-HALL-001.kicad_pro': '09de545a736e1c825e6e659549386e5d0596fba1d55f5cbf0c0d19b98b60b5b2', 'CUR-HALL-001.kicad_sch': '95ae2572833eae292c02800e07be343901f1ab8ac450a87b2b0c67000bb63401'},
    source_hashes={'CUR-HALL-001.kicad_pcb': '4354203b9ce0fbab2a5504ad550db67f13797920b455b9506594a70155556874', 'CUR-HALL-001.kicad_pro': '09de545a736e1c825e6e659549386e5d0596fba1d55f5cbf0c0d19b98b60b5b2', 'CUR-HALL-001.kicad_sch': '95ae2572833eae292c02800e07be343901f1ab8ac450a87b2b0c67000bb63401'},
    schematic_file='CUR-HALL-001.kicad_sch',
    pcb_file='CUR-HALL-001.kicad_pcb',
    kicad_cli_checks=('drc', 'netlist_export'),
    position_checks={'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 109.5, 'y': 64.4, 'rotation': 0.0}, 'J3': {'footprint': 'Connector_JST:JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical', 'x': 122.8, 'y': 64.0, 'rotation': -90.0}, 'R3': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 117.2, 'y': 68.2, 'rotation': 180.0}},
    netlist_checks={'R1': {'1': 'Net-(U1-VIOUT)', '2': 'Net-(U2-+)'}, 'J3': {'1': 'GND', '2': 'Net-(J3-Pin_2)'}, 'R3': {'1': 'Net-(J3-Pin_2)', '2': 'Net-(U2--)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
