from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='rf_wireless_basic_RF-BLE-001_task_2',
    project_files=['RF-BLE-001.kicad_pcb', 'RF-BLE-001.kicad_pro', 'RF-BLE-001.kicad_sch'],
    golden_hashes={'RF-BLE-001.kicad_pcb': '43d5fade006a99b351983614fa95ec4fb675f45dea165d1a4fbee402b8e3e1a0', 'RF-BLE-001.kicad_pro': '81b9bd027656387b670b2605fcc87af9f5ac75d3e039517aca3ca5080cd3242b', 'RF-BLE-001.kicad_sch': 'fbc34648d17cb67cab05b622f8ca5af8bbaab679fc63487312aab334649ab276'},
    source_hashes={'RF-BLE-001.kicad_pcb': '830e57f1adfc24f96799f38a3e27c36dfb87a98a340ac8b666428fe9d90eab9c', 'RF-BLE-001.kicad_pro': '81b9bd027656387b670b2605fcc87af9f5ac75d3e039517aca3ca5080cd3242b', 'RF-BLE-001.kicad_sch': '1eadf1d5a052b083fa113a86b33b3ed8e4560b5692a906e7a1e72dd4d478afef'},
    schematic_file='RF-BLE-001.kicad_sch',
    pcb_file='RF-BLE-001.kicad_pcb',
    kicad_cli_checks=('erc',),
    position_checks={'C1': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 94.75, 'y': 33.0, 'rotation': 0.0}, 'Y1': {'footprint': 'Crystal:Crystal_SMD_Abracon_ABM8AIG-4Pin_3.2x2.5mm', 'x': 125.25, 'y': 24.0, 'rotation': 90.0}, 'L1': {'footprint': 'Capacitor_SMD:C_0402_1005Metric', 'x': 128.75, 'y': 39.75, 'rotation': 0.0}},
    netlist_checks={'C1': {'1': '+3.3V', '2': 'GND'}, 'Y1': {'1': 'Net-(U1-XC1)', '2': 'GND', '3': 'Net-(U1-XC2)', '4': 'unconnected-(Y1-Pad4)'}, 'L1': {'1': 'Net-(U1-ANT)', '2': 'Net-(AE1-A)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
