from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='industrial_bus_basic_BUS-RS485-004_task_4',
    project_files=['RS485_5V.kicad_sch', 'groundtruth.kicad_pcb', 'groundtruth.kicad_pro', 'groundtruth.kicad_sch', 'stm32f1.kicad_sch', 'untitled2.kicad_sch'],
    golden_hashes={'RS485_5V.kicad_sch': '6e2586b9409f19e9f1b952f6887b5a8a6224d74adc6d9bd9414f7d97c099cf4a', 'groundtruth.kicad_pcb': '7a898e82ab1a4c522936e9c0600508d94c07d7aa46aaab289897a1fabacb082d', 'groundtruth.kicad_pro': 'e4d4b40ad694d3b33001dc072e53c77cbb6af31b2303863d86e4c2ddb323a9c4', 'groundtruth.kicad_sch': '77154132618263c7c2c3a9ae8a78a5e49a90a9fdff8f35412957dcd684ab3293', 'stm32f1.kicad_sch': 'e0ec82bd0c0ce3bc1ae75a6f95bf8a496dfbe3187b1303cb6b849bfc547e9c13', 'untitled2.kicad_sch': '3051c117e629d9ede99519795b633926d6826fbfc5a76f40b75aded13253f5f3'},
    source_hashes={'RS485_5V.kicad_sch': '8d64d1b4deb43739fd4314b7381305bb562801dc114389241e19a27528cc3c29', 'groundtruth.kicad_pcb': '54faa1127c901f19191e1fa7761101b0e6ba9127acc20ffbe7379236d9b3a9ed', 'groundtruth.kicad_pro': 'e4d4b40ad694d3b33001dc072e53c77cbb6af31b2303863d86e4c2ddb323a9c4', 'groundtruth.kicad_sch': '77154132618263c7c2c3a9ae8a78a5e49a90a9fdff8f35412957dcd684ab3293', 'stm32f1.kicad_sch': 'e0ec82bd0c0ce3bc1ae75a6f95bf8a496dfbe3187b1303cb6b849bfc547e9c13', 'untitled2.kicad_sch': '845dfbd03d14a3d3cba22d486d3b55402e07b01d6f78570fe2bc0b154c2dab95'},
    schematic_file='groundtruth.kicad_sch',
    pcb_file='groundtruth.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'R6': {'footprint': 'Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder', 'x': 108.5, 'y': 121.5, 'rotation': 90.0}, 'C6': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 104.45, 'y': 122.5, 'rotation': 0.0}, 'C1': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 77.89259, 'y': 118.0, 'rotation': 0.0}},
    netlist_checks={'R6': {'1': 'GND', '2': '/RS485_5V/RS485_2B'}, 'C6': {'1': 'GND', '2': '+5V'}, 'C1': {'1': '+3V3', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
