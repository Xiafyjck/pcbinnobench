from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_PWR-LDO-004_task_4',
    project_files=['groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch'],
    golden_hashes={'groundtruth.kicad_pcb': '7f93bf3a1eb91e26c420aec0542ef2ca7a594345a813b299343b1ab4550fd012', 'groundtruth.kicad_pro': '01302473a6fd5dc4fac6082134ae5000b314e8408c4cb0b3dc992c07b71033dc', 'groundtruth.kicad_sch': 'd9a33f80e24b2c8f675f1ca355ccf40f2ff525aee4d5d79afebe6823522d35f1'},
    source_hashes={'groundtruth.kicad_pcb': '2fc159f6d7d3fa22d4c266ec8ab4486a3a8e84aaee4ec93b8bd5cd5576f05268', 'groundtruth.kicad_pro': '76128a572d63add12693dc0b250e71b54b9e35e3c14de9d3dd567922cf363dc3', 'groundtruth.kicad_sch': 'd9a33f80e24b2c8f675f1ca355ccf40f2ff525aee4d5d79afebe6823522d35f1'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('drc', 'erc'),
    position_checks={'J2': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical', 'x': 118.5, 'y': 91.725, 'rotation': 0.0}, 'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder', 'x': 123.5, 'y': 93.0, 'rotation': 180.0}, 'D1': {'footprint': 'Diode_SMD:Nexperia_DSN1608-2_1.6x0.8mm', 'x': 130.0, 'y': 95.285, 'rotation': -90.0}},
    netlist_checks={'J2': {'1': '+5V', '2': 'GND'}, 'R1': {'1': 'Net-(U2-SNS)', '2': '+5V'}, 'D1': {'1': '+12V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
