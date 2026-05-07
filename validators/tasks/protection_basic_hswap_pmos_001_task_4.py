from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='protection_basic_HSWAP-PMOS-001_task_4',
    project_files=['HSWAP-PMOS-001.kicad_pcb', 'HSWAP-PMOS-001.kicad_pro', 'HSWAP-PMOS-001.kicad_sch'],
    golden_hashes={'HSWAP-PMOS-001.kicad_pcb': 'ba9054c4f01d10c9986aff1f560b46b6f214688903997d2dc5fc41fca835fa22', 'HSWAP-PMOS-001.kicad_pro': 'acb9a13c213fb497d755b06b7d9979afc0c17008ffd71d75a48d99b97bd48de5', 'HSWAP-PMOS-001.kicad_sch': '2cc9f24742813469034345042280caeb91ee3b3a87973729d4b06a74fbbdb88a'},
    source_hashes={'HSWAP-PMOS-001.kicad_pcb': 'c148b14f6272d9d872359e62d49c3c6cab78e2d4581c75cb148ce44b329409d5', 'HSWAP-PMOS-001.kicad_pro': 'acb9a13c213fb497d755b06b7d9979afc0c17008ffd71d75a48d99b97bd48de5', 'HSWAP-PMOS-001.kicad_sch': 'c68f747685987121ce5b8873d8f43ffc3634aa4a2d644ffd136b8335b67909bb'},
    schematic_file='HSWAP-PMOS-001.kicad_sch',
    pcb_file='HSWAP-PMOS-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'J2': {'footprint': 'Connector_JST:JST_NV_B02P-NV_1x02_P5.00mm_Vertical', 'x': 138.4, 'y': 55.6, 'rotation': -90.0}, 'Q1': {'footprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'x': 113.55, 'y': 60.14, 'rotation': 90.0}, 'C2': {'footprint': 'Capacitor_THT:C_Disc_D7.5mm_W5.0mm_P10.00mm', 'x': 128.8, 'y': 53.2, 'rotation': -90.0}},
    netlist_checks={'J2': {'1': 'VCC_OUT', '2': 'GND'}, 'Q1': {'1': 'Net-(D1-A)', '2': 'VCC', '3': 'VCC_OUT'}, 'C2': {'1': 'VCC_OUT', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
