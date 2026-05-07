from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='digital_interface_basic_basic_DIG-SPI-003_task_3',
    project_files=['DIG-SPI-003.kicad_pcb', 'DIG-SPI-003.kicad_pro', 'DIG-SPI-003.kicad_sch'],
    golden_hashes={'DIG-SPI-003.kicad_pcb': '2d15dc933fb80ab1f000e8302f57e25f8f5c9a920314a4f6e3a66959401956f6', 'DIG-SPI-003.kicad_pro': 'fee58de1ae98f66585d3365f566b6d3e327b96f62ebdb4a6205e48713a593ae1', 'DIG-SPI-003.kicad_sch': '19cc5ccb6ccf72e8c9084ef1f5ecdd0e59ad963f67ddc9ee75bb2371530ed3ad'},
    source_hashes={'DIG-SPI-003.kicad_pcb': '2b61e56ab731be7a34396ee28e841b53d3acc90f9969790cb800166c66ccbe97', 'DIG-SPI-003.kicad_pro': 'fee58de1ae98f66585d3365f566b6d3e327b96f62ebdb4a6205e48713a593ae1', 'DIG-SPI-003.kicad_sch': 'e8bc7ed446069a249600f567dcc95ceb475071a5fe2ba07e55745179c441cb82'},
    schematic_file='DIG-SPI-003.kicad_sch',
    pcb_file='DIG-SPI-003.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'R1': {'footprint': 'Resistor_SMD:R_0201_0603Metric', 'x': 101.5, 'y': 93.0, 'rotation': -90.0}, 'C2': {'footprint': 'Capacitor_SMD:C_0603_1608Metric', 'x': 109.0, 'y': 91.0, 'rotation': 0.0}, 'C6': {'footprint': 'Capacitor_SMD:C_0603_1608Metric', 'x': 109.5, 'y': 83.0, 'rotation': 90.0}},
    netlist_checks={'R1': {'1': 'Net-(U1-PA4)', '2': '/CS1'}, 'C2': {'1': '+3V3', '2': 'GND'}, 'C6': {'1': '+3V3', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
