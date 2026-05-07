from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='protection_basic_PROT-TVS-003_task_2',
    project_files=['STM32.kicad_sch', 'groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch'],
    golden_hashes={'STM32.kicad_sch': '05c2b9a7a24b1ab39e276428b0b3fa31dea2bbb8a51998aa374d73c04d851d00', 'groundtruth.kicad_pcb': 'b86bce68aef44aca8120e80b78bee01ec9d85db980f0eaeb446f44d01c9d9063', 'groundtruth.kicad_pro': 'adc24fc96836082c7d132449b46b967b2c51bd1148e903c8903da98922f511ff', 'groundtruth.kicad_sch': '85536f87d53c379aa57d50f06a7a42fd9ffcc0e1866a8f23c6493334a6b70241'},
    source_hashes={'STM32.kicad_sch': '05c2b9a7a24b1ab39e276428b0b3fa31dea2bbb8a51998aa374d73c04d851d00', 'groundtruth.kicad_pcb': '55609b7b57027b3c6f4d02c9c7c275b5ff065b2d129237e6048b80c27d4f9520', 'groundtruth.kicad_pro': 'adc24fc96836082c7d132449b46b967b2c51bd1148e903c8903da98922f511ff', 'groundtruth.kicad_sch': '74ef3d7b8753cb5a5658066ce6c60ccc1fe705fca70d5e5f9bba6e5acc8e7428'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('drc', 'netlist_export'),
    position_checks={'U2': {'footprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'x': 95.475, 'y': 68.5, 'rotation': 0.0}, 'J3': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical', 'x': 86.0, 'y': 67.5, 'rotation': 180.0}, 'C4': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 95.0, 'y': 74.95, 'rotation': -90.0}},
    netlist_checks={'U2': {'1': 'Net-(J3-Pin_1)', '2': 'GND', '3': '+3V3', '4': 'Net-(J3-Pin_2)', '5': 'unconnected-(U2-Vref-Pad5)', '6': '/CAN_L'}, 'J3': {'1': 'Net-(J3-Pin_1)', '2': 'Net-(J3-Pin_2)', '3': 'GND'}, 'C4': {'1': 'Net-(C4-Pad1)', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
