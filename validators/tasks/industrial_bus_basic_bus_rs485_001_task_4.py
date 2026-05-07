from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='industrial_bus_basic_BUS-RS485-001_task_4',
    project_files=['groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch'],
    golden_hashes={'groundtruth.kicad_pcb': '7128961f56dcdd0d816732020711ef4f23478f4e5e92b4d2f718742a6afcdfec', 'groundtruth.kicad_pro': '6dac6c784c65dfec3d52e8a52241ced80c6017327c65442f017ad653973413c2', 'groundtruth.kicad_sch': '8689a5997769f5d2301e6b2f84aa51365120fe5bf17b12a651e55b74bd282cd2'},
    source_hashes={'groundtruth.kicad_pcb': 'f337c5dbbe645e61d16505900967a7077b1ae7b246d9b13bfcce5df7a9cac139', 'groundtruth.kicad_pro': '6dac6c784c65dfec3d52e8a52241ced80c6017327c65442f017ad653973413c2', 'groundtruth.kicad_sch': '8689a5997769f5d2301e6b2f84aa51365120fe5bf17b12a651e55b74bd282cd2'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('erc',),
    position_checks={'J4': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical', 'x': 114.0, 'y': 114.5, 'rotation': 0.0}, 'J3': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical', 'x': 86.5, 'y': 112.42, 'rotation': 0.0}, 'J5': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical', 'x': 92.5, 'y': 120.5, 'rotation': 90.0}},
    netlist_checks={'J4': {'1': '/RS485_2B', '2': '/RS485_2A'}, 'J3': {'1': '/RS485_2_RX', '2': '/RS485_2_DE', '3': '/RS485_2_TX', '4': 'GND'}, 'J5': {'1': 'GND', '2': '+3V3'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
