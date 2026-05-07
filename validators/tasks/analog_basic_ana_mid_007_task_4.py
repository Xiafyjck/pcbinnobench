from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-MID-007_task_4',
    project_files=['ANA-MID-007.kicad_pcb', 'ANA-MID-007.kicad_pro', 'ANA-MID-007.kicad_sch'],
    golden_hashes={'ANA-MID-007.kicad_pcb': 'e0754c5ed9c996ede4ba98251ed17a8d1515c056646c50b4ddbdf9681d6469dc', 'ANA-MID-007.kicad_pro': '266ffcb414bd84dff59a640f5c1e7643bdc9d905e4ac088d2631e90da8511f8c', 'ANA-MID-007.kicad_sch': '4ba01193d420f3cb70cee181736d05645a95e2e662a7d98c2194b2468e379d7b'},
    source_hashes={'ANA-MID-007.kicad_pcb': 'e233692bd3a3e65a6a1e102797e426a82f73ce9025ebd6cb5cdf9b4f845f441e', 'ANA-MID-007.kicad_pro': '266ffcb414bd84dff59a640f5c1e7643bdc9d905e4ac088d2631e90da8511f8c', 'ANA-MID-007.kicad_sch': '700c65228c28149087606bc89f38db9e889e37fe7e3aca52ce9247c451493c73'},
    schematic_file='ANA-MID-007.kicad_sch',
    pcb_file='ANA-MID-007.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'J2': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Horizontal', 'x': 92.959, 'y': 54.423, 'rotation': 90.0}, 'C3': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 76.2, 'y': 68.326, 'rotation': -90.0}, 'R5': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 98.552, 'y': 70.612, 'rotation': 0.0}},
    netlist_checks={'J2': {'1': '+5V', '2': 'GND'}, 'C3': {'1': 'Net-(D2-K)', '2': 'GND'}, 'R5': {'1': 'Net-(U2-AIN1)', '2': '/3V3'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
