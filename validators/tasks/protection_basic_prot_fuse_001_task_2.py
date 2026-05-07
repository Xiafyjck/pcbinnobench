from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='protection_basic_PROT-FUSE-001_task_2',
    project_files=['PROT-FUSE-001.kicad_pcb', 'PROT-FUSE-001.kicad_pro', 'PROT-FUSE-001.kicad_sch'],
    golden_hashes={'PROT-FUSE-001.kicad_pcb': '2e6aa2a40e6fc747e5525abdfda7dc6387f57101b910bb21ea827c371559415f', 'PROT-FUSE-001.kicad_pro': '477ebf548ca65eb653d22b64dc319acf1175615e76fd4c986c486499edf54109', 'PROT-FUSE-001.kicad_sch': '85e2b7433160be07b419453e09556b0bd3c509804395340fcd83b0e8c2fc2e18'},
    source_hashes={'PROT-FUSE-001.kicad_pcb': '136b41de42a125b615cc887e89671a33ee7d9dbdbc5e3d4d0af5fd64ce463403', 'PROT-FUSE-001.kicad_pro': '477ebf548ca65eb653d22b64dc319acf1175615e76fd4c986c486499edf54109', 'PROT-FUSE-001.kicad_sch': '8432254620495305d20cee45561581ffc6d69683f31fd4b79b0306b51e9839b2'},
    schematic_file='PROT-FUSE-001.kicad_sch',
    pcb_file='PROT-FUSE-001.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 142.7, 'y': 45.7, 'rotation': -90.0}, 'D3': {'footprint': 'Diode_SMD:D_SMB', 'x': 135.7, 'y': 47.4, 'rotation': -90.0}, 'C2': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 139.9, 'y': 45.7, 'rotation': -90.0}},
    netlist_checks={'R1': {'1': 'Net-(D3-A1)', '2': 'GND'}, 'D3': {'1': 'Net-(D3-A1)', '2': 'GND'}, 'C2': {'1': 'Net-(D3-A1)', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
