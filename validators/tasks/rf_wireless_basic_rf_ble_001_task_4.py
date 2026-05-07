from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='rf_wireless_basic_RF-BLE-001_task_4',
    project_files=['RF-BLE-001.kicad_pcb', 'RF-BLE-001.kicad_pro', 'RF-BLE-001.kicad_sch'],
    golden_hashes={'RF-BLE-001.kicad_pcb': '43d5fade006a99b351983614fa95ec4fb675f45dea165d1a4fbee402b8e3e1a0', 'RF-BLE-001.kicad_pro': '81b9bd027656387b670b2605fcc87af9f5ac75d3e039517aca3ca5080cd3242b', 'RF-BLE-001.kicad_sch': 'fbc34648d17cb67cab05b622f8ca5af8bbaab679fc63487312aab334649ab276'},
    source_hashes={'RF-BLE-001.kicad_pcb': 'bd977556564c3dc566e9d3b7b8ecb5831cbe9e251c87d951b9b3e83233bcada0', 'RF-BLE-001.kicad_pro': '81b9bd027656387b670b2605fcc87af9f5ac75d3e039517aca3ca5080cd3242b', 'RF-BLE-001.kicad_sch': 'fbc34648d17cb67cab05b622f8ca5af8bbaab679fc63487312aab334649ab276'},
    schematic_file='RF-BLE-001.kicad_sch',
    pcb_file='RF-BLE-001.kicad_pcb',
    kicad_cli_checks=('erc', 'netlist_export'),
    position_checks={'SW2': {'footprint': 'Button_Switch_THT:SW_PUSH_6mm', 'x': 104.0, 'y': 52.25, 'rotation': 180.0}, 'C5': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 123.25, 'y': 32.5, 'rotation': 90.0}, 'C15': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 97.8625, 'y': 59.7, 'rotation': 0.0}},
    netlist_checks={'SW2': {'1': 'GND', '2': 'Net-(U1-P0.11)'}, 'C5': {'1': '+3.3V', '2': 'GND'}, 'C15': {'1': '+5V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
