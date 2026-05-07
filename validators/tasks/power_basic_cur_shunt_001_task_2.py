from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_CUR-SHUNT-001_task_2',
    project_files=['CUR-SHUNT-001.kicad_pcb', 'CUR-SHUNT-001.kicad_pro', 'CUR-SHUNT-001.kicad_sch'],
    golden_hashes={'CUR-SHUNT-001.kicad_pcb': '8b13935d809e7d67b69f4478de12268fc536f62815feb7aea6257a3a59dd466e', 'CUR-SHUNT-001.kicad_pro': 'ed30c105e22cbc5d7aeb5f0fda351430bab0a36880256925ba9dbe5fb0bfed90', 'CUR-SHUNT-001.kicad_sch': '4a94d7cb9d4d85c3b256e6692f6ce66177cafa43bdbd7912bb6d33b8f804a50a'},
    source_hashes={'CUR-SHUNT-001.kicad_pcb': '37e58f70f88f6b219aa6f8ffcadfb3d0dd3e686508de78ebc61650da76aadca3', 'CUR-SHUNT-001.kicad_pro': 'ed30c105e22cbc5d7aeb5f0fda351430bab0a36880256925ba9dbe5fb0bfed90', 'CUR-SHUNT-001.kicad_sch': '44b0b3d2fce6570377094f646867cc043d991cde512071fc4333f5510c39624c'},
    schematic_file='CUR-SHUNT-001.kicad_sch',
    pcb_file='CUR-SHUNT-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'C5': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 150.8, 'y': 66.7, 'rotation': 180.0}, 'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 138.5, 'y': 68.3, 'rotation': 180.0}, 'J1': {'footprint': 'Connector_JST:JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical', 'x': 125.5, 'y': 69.05, 'rotation': -90.0}},
    netlist_checks={'C5': {'1': 'GND', '2': '+3.3V'}, 'R1': {'1': 'Net-(U2-+)', '2': 'Net-(R1-Pad2)'}, 'J1': {'1': 'Net-(J1-Pin_1)', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
