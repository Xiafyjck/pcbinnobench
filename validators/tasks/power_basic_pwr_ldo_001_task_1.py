from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='Power_basic_PWR-LDO-001_task_1',
    project_files=['PWR-LDO-001.kicad_pcb', 'PWR-LDO-001.kicad_pro', 'PWR-LDO-001.kicad_sch'],
    golden_hashes={'PWR-LDO-001.kicad_pcb': '6c5d642b35083dbf7b7e650bdf2ddd6c75d07a8280bbd774f535c2ab4c34219c', 'PWR-LDO-001.kicad_pro': 'deca61ff05280c442397c5770a61b0dfb9ab69e4bbf87ee422f703e8904ac96c', 'PWR-LDO-001.kicad_sch': 'ba7fed2175f446037277add13e31d0affa861d3eb0b754b158b61271410ff09a'},
    source_hashes={'PWR-LDO-001.kicad_pcb': 'd0b988183b1380e403a4c026ca795234b8e84355582e85481cff2ff928c3f5f6', 'PWR-LDO-001.kicad_pro': 'deca61ff05280c442397c5770a61b0dfb9ab69e4bbf87ee422f703e8904ac96c', 'PWR-LDO-001.kicad_sch': 'ba7fed2175f446037277add13e31d0affa861d3eb0b754b158b61271410ff09a'},
    schematic_file='PWR-LDO-001.kicad_sch',
    pcb_file='PWR-LDO-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'C3': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 83.82, 'y': 63.5, 'rotation': -90.0}, 'C4': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 80.264, 'y': 63.5, 'rotation': -90.0}, 'J2': {'footprint': 'Connector_JST:JST_XH_B2B-XH-AM_1x02_P2.50mm_Vertical', 'x': 90.424, 'y': 62.25, 'rotation': -90.0}},
    netlist_checks={'C3': {'1': '+3.3V', '2': 'GND'}, 'C4': {'1': '+3.3V', '2': 'GND'}, 'J2': {'1': '+3.3V', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
