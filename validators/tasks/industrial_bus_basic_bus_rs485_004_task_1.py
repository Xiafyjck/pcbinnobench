from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='industrial_bus_basic_BUS-RS485-004_task_1',
    project_files=['RS485_5V.kicad_sch', 'groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch', 'stm32f1.kicad_sch', 'untitled2.kicad_sch'],
    golden_hashes={'RS485_5V.kicad_sch': '8d64d1b4deb43739fd4314b7381305bb562801dc114389241e19a27528cc3c29', 'groundtruth.kicad_pcb': '85e186afd97755513c4a3c527b282b8ae66cf1f72dfdaccf7f8b30a91b2e302c', 'groundtruth.kicad_pro': 'e4d4b40ad694d3b33001dc072e53c77cbb6af31b2303863d86e4c2ddb323a9c4', 'groundtruth.kicad_sch': '77154132618263c7c2c3a9ae8a78a5e49a90a9fdff8f35412957dcd684ab3293', 'stm32f1.kicad_sch': 'e0ec82bd0c0ce3bc1ae75a6f95bf8a496dfbe3187b1303cb6b849bfc547e9c13', 'untitled2.kicad_sch': '3051c117e629d9ede99519795b633926d6826fbfc5a76f40b75aded13253f5f3'},
    source_hashes={'RS485_5V.kicad_sch': '8d64d1b4deb43739fd4314b7381305bb562801dc114389241e19a27528cc3c29', 'groundtruth.kicad_pcb': '525bdd03aa8c9e508bdbb566502ce7f9bf7ac1a4c37488f55a5f33431e90bb50', 'groundtruth.kicad_pro': 'a7e5e6fdd63c92763151f88997632280da64bd2d1dff688a8bb62a30c382b46f', 'groundtruth.kicad_sch': 'b721d92518ff5d28d33125afb269ec1fd362b3d21b79311a5011727e6fd99203', 'stm32f1.kicad_sch': 'e0ec82bd0c0ce3bc1ae75a6f95bf8a496dfbe3187b1303cb6b849bfc547e9c13', 'untitled2.kicad_sch': '3051c117e629d9ede99519795b633926d6826fbfc5a76f40b75aded13253f5f3'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 85.5875, 'y': 110.0, 'rotation': 0.0}, 'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 85.73009, 'y': 112.25, 'rotation': 0.0}, 'R3': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 89.5, 'y': 110.0, 'rotation': 0.0}},
    netlist_checks={'R2': {'1': 'Net-(U1-PA9)', '2': '/stm32-uart/TX'}, 'R1': {'1': 'Net-(U1-PA10)', '2': '/stm32-uart/RX'}, 'R3': {'1': '/stm32-uart/TX', '2': '+3V3'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
