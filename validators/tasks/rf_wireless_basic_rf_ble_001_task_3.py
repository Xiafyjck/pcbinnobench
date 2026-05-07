from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='rf_wireless_basic_RF-BLE-001_task_3',
    project_files=['RF-BLE-001.kicad_pcb', 'RF-BLE-001.kicad_pro', 'RF-BLE-001.kicad_sch'],
    golden_hashes={'RF-BLE-001.kicad_pcb': '43d5fade006a99b351983614fa95ec4fb675f45dea165d1a4fbee402b8e3e1a0', 'RF-BLE-001.kicad_pro': '81b9bd027656387b670b2605fcc87af9f5ac75d3e039517aca3ca5080cd3242b', 'RF-BLE-001.kicad_sch': 'fbc34648d17cb67cab05b622f8ca5af8bbaab679fc63487312aab334649ab276'},
    source_hashes={'RF-BLE-001.kicad_pcb': 'c13582c2082820173f765ab52807e0e6327b6764537b5273f9a2eeab93f412a9', 'RF-BLE-001.kicad_pro': '81b9bd027656387b670b2605fcc87af9f5ac75d3e039517aca3ca5080cd3242b', 'RF-BLE-001.kicad_sch': 'fbc34648d17cb67cab05b622f8ca5af8bbaab679fc63487312aab334649ab276'},
    schematic_file='RF-BLE-001.kicad_sch',
    pcb_file='RF-BLE-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'AE1': {'footprint': 'RF_Antenna:Texas_SWRA117D_2.4GHz_Right', 'x': 131.75, 'y': 39.75, 'rotation': -90.0}, 'SW2': {'footprint': 'Button_Switch_THT:SW_PUSH_6mm', 'x': 104.0, 'y': 52.25, 'rotation': 180.0}, 'J1': {'footprint': 'Connector_JST:JST_XH_B5B-XH-A_1x05_P2.50mm_Vertical', 'x': 115.0, 'y': 60.25, 'rotation': 0.0}},
    netlist_checks={'AE1': {'1': 'Net-(AE1-A)', '2': 'GND'}, 'SW2': {'1': 'GND', '2': 'Net-(U1-P0.11)'}, 'J1': {'1': '+3.3V', '2': '/swdio', '3': '/swclk', '4': '/NRST', '5': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
