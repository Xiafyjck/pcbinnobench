from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='digital_interface_basic_basic_CLK-RTC-001_task_3',
    project_files=['CLK-RTC-001.kicad_pcb', 'CLK-RTC-001.kicad_pro', 'CLK-RTC-001.kicad_sch'],
    golden_hashes={'CLK-RTC-001.kicad_pcb': 'b2eaa3d10863f7d95c384e8e7e4a8b761bf5ce0a06050fa924a4cfd79464c6c1', 'CLK-RTC-001.kicad_pro': '50415771dd8e7b1b560a8238b81c5ef6bf8e113d46204a802b978dc382a9e1d5', 'CLK-RTC-001.kicad_sch': '75a74337714cc589696d5d6e9a1ab1893150f6ff7535d71e62f25ce68541e7de'},
    source_hashes={'CLK-RTC-001.kicad_pcb': '01a60f6f053a689082f02c7c6768f1d971c7a3c61fd0d3d1d17e2e9278653244', 'CLK-RTC-001.kicad_pro': '50415771dd8e7b1b560a8238b81c5ef6bf8e113d46204a802b978dc382a9e1d5', 'CLK-RTC-001.kicad_sch': '75a74337714cc589696d5d6e9a1ab1893150f6ff7535d71e62f25ce68541e7de'},
    schematic_file='CLK-RTC-001.kicad_sch',
    pcb_file='CLK-RTC-001.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'C16': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 114.8, 'y': 62.7, 'rotation': 180.0}, 'C7': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 115.95, 'y': 67.15, 'rotation': 90.0}, 'C3': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 127.9, 'y': 57.4, 'rotation': 90.0}},
    netlist_checks={'C16': {'1': 'GND', '2': 'Net-(U2-PC15)'}, 'C7': {'1': '/NRST', '2': 'GND'}, 'C3': {'1': '+3.3V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
