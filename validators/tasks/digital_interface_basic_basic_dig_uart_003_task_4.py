from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='digital_interface_basic_basic_DIG-UART-003_task_4',
    project_files=['groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch', 'stm32f1.kicad_sch', 'untitled2.kicad_sch'],
    golden_hashes={'groundtruth.kicad_pcb': 'e377746dec6b5cd24b85150b6609e01d598ff7f7802c7855070402a3049f5f41', 'groundtruth.kicad_pro': '0aa3b5e6d9354d88c6ac353efbc3eb23f15c82b87d121aa3859ed3b774f85701', 'groundtruth.kicad_sch': '2784981e021902d03f27ef706445bb9f3b92b99583f482fc4eaacc82a18fa0ca', 'stm32f1.kicad_sch': '450fed8d1a76f2c0d976c79130108ae19b3102db48f9fd88124fb2a1199984f4', 'untitled2.kicad_sch': '55e6f30438afb5e1e78bd7da8b7f248c71da3717cdb675571b7af1f1fb6ff226'},
    source_hashes={'groundtruth.kicad_pcb': '7258273a510832fb71196d4d32dc81eb976b02ec1ca38461e8e6d13731225319', 'groundtruth.kicad_pro': '0aa3b5e6d9354d88c6ac353efbc3eb23f15c82b87d121aa3859ed3b774f85701', 'groundtruth.kicad_sch': '436ba302144d403c49640b37eef762fae570d48b6ffb8d71a274ec2121edfa3d', 'stm32f1.kicad_sch': '450fed8d1a76f2c0d976c79130108ae19b3102db48f9fd88124fb2a1199984f4', 'untitled2.kicad_sch': '55e6f30438afb5e1e78bd7da8b7f248c71da3717cdb675571b7af1f1fb6ff226'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'C4': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 86.5, 'y': 119.5, 'rotation': 0.0}, 'C5': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 94.0, 'y': 111.0, 'rotation': 180.0}, 'C1': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 77.89259, 'y': 118.0, 'rotation': 0.0}},
    netlist_checks={'C4': {'1': '+5V', '2': 'GND'}, 'C5': {'1': '+3V3', '2': 'GND'}, 'C1': {'1': '+3V3', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
