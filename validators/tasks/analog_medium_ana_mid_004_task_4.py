from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_medium_ANA-MID-004_task_4',
    project_files=['ANA-MID-004.kicad_pcb', 'ANA-MID-004.kicad_pro', 'ANA-MID-004.kicad_sch'],
    golden_hashes={'ANA-MID-004.kicad_pcb': 'f65328770b1522af992d3a9105235599af7728b892a0006cb4c270af7d615b8f', 'ANA-MID-004.kicad_pro': '09fc87f932f68bbd7d373a433c433e708ee7bcc8a664c39efef5846b9073c6b8', 'ANA-MID-004.kicad_sch': '8d8965f66523d5fc2937c4b178054684d080c3900b31a9f0c27b6f515ce6ecf3'},
    source_hashes={'ANA-MID-004.kicad_pcb': '7f73baa203c397916c53b391ac695a182489b7879351f62657c30b5c2265e624', 'ANA-MID-004.kicad_pro': '09fc87f932f68bbd7d373a433c433e708ee7bcc8a664c39efef5846b9073c6b8', 'ANA-MID-004.kicad_sch': '5deb485ca48faa175b5bdc3fde56393330f377b04cc7712e325ccd9edeb180a6'},
    schematic_file='ANA-MID-004.kicad_sch',
    pcb_file='ANA-MID-004.kicad_pcb',
    kicad_cli_checks=('drc', 'netlist_export'),
    position_checks={'U3': {'footprint': 'Package_TO_SOT_SMD:SOT-23', 'x': 101.412, 'y': 69.4205, 'rotation': 90.0}, 'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 103.378, 'y': 56.896, 'rotation': 0.0}, 'J3': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Horizontal', 'x': 104.394, 'y': 74.93, 'rotation': -90.0}},
    netlist_checks={'U3': {'1': '+5V', '2': '/3V3', '3': 'GND'}, 'R2': {'1': 'Net-(J1-Pin_1)', '2': '/3V3'}, 'J3': {'1': 'GND', '2': '/3V3'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
