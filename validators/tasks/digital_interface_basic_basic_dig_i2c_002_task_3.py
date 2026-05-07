from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='digital_interface_basic_basic_DIG-I2C-002_task_3',
    project_files=['DIG-I2C-002.kicad_pcb', 'DIG-I2C-002.kicad_pro', 'DIG-I2C-002.kicad_sch', 'groundtruth1.kicad_sch', 'groundtruth2.kicad_sch', 'groundtruth3.kicad_sch'],
    golden_hashes={'DIG-I2C-002.kicad_pcb': 'cc5dea6af7cd9a486304f956aa93f1e7735ee57e3526cea7365673044b8d495c', 'DIG-I2C-002.kicad_pro': '235a5db6dff742473c8a534737bba7c13ba44fbe094dfc684da5efc3f5cbf875', 'DIG-I2C-002.kicad_sch': '6facb4b1e2a756330ee6cfd9fd8e479acfb498f37c0400a993070c41f4ef564a', 'groundtruth1.kicad_sch': '4ef795f6994e2d875ef0aa9f41929f2a071d9ca42eb900ad45ae2e60060a516f', 'groundtruth2.kicad_sch': 'ea119ac1f716161d459b47ebb57c414cb923ad74c846d21b67acb5c45c9c4087', 'groundtruth3.kicad_sch': 'bc6f6ecc3459324770afd9d656b8e30a012b6cd9fa704522e422af787846d812'},
    source_hashes={'DIG-I2C-002.kicad_pcb': '0614210ce489fa35922c4f7079ba64045baf83c9ac34d11451bc740c92b5bd0a', 'DIG-I2C-002.kicad_pro': '235a5db6dff742473c8a534737bba7c13ba44fbe094dfc684da5efc3f5cbf875', 'DIG-I2C-002.kicad_sch': '6facb4b1e2a756330ee6cfd9fd8e479acfb498f37c0400a993070c41f4ef564a', 'groundtruth1.kicad_sch': '4ef795f6994e2d875ef0aa9f41929f2a071d9ca42eb900ad45ae2e60060a516f', 'groundtruth2.kicad_sch': 'ea119ac1f716161d459b47ebb57c414cb923ad74c846d21b67acb5c45c9c4087', 'groundtruth3.kicad_sch': 'bc6f6ecc3459324770afd9d656b8e30a012b6cd9fa704522e422af787846d812'},
    schematic_file='DIG-I2C-002.kicad_sch',
    pcb_file='DIG-I2C-002.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'C4': {'footprint': 'Capacitor_SMD:C_0603_1608Metric', 'x': 147.5, 'y': 92.5, 'rotation': 0.0}, 'U3': {'footprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'x': 152.5, 'y': 89.0, 'rotation': 0.0}, 'U1': {'footprint': 'Package_QFP:LQFP-48_7x7mm_P0.5mm', 'x': 142.65, 'y': 87.31, 'rotation': 0.0}},
    netlist_checks={'C4': {'1': '+3V3', '2': 'GND'}, 'U3': {'1': '/groundtruth1/I2C_SDA', '2': '/groundtruth1/I2C_SCL', '3': '/groundtruth1/O.S', '4': 'GND', '5': 'GND', '6': 'GND'}, 'U1': {'1': 'unconnected-(U1-VBAT-Pad1)', '10': 'unconnected-(U1-PA0-Pad10)', '11': 'unconnected-(U1-PA1-Pad11)', '12': 'unconnected-(U1-PA2-Pad12)', '13': 'unconnected-(U1-PA3-Pad13)', '14': 'unconnected-(U1-PA4-Pad14)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
