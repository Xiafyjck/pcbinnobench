from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='protection_basic_PROT-FUSE-001_task_1',
    project_files=['PROT-FUSE-001.kicad_pcb', 'PROT-FUSE-001.kicad_pro', 'PROT-FUSE-001.kicad_sch'],
    golden_hashes={'PROT-FUSE-001.kicad_pcb': '2e6aa2a40e6fc747e5525abdfda7dc6387f57101b910bb21ea827c371559415f', 'PROT-FUSE-001.kicad_pro': '477ebf548ca65eb653d22b64dc319acf1175615e76fd4c986c486499edf54109', 'PROT-FUSE-001.kicad_sch': '85e2b7433160be07b419453e09556b0bd3c509804395340fcd83b0e8c2fc2e18'},
    source_hashes={'PROT-FUSE-001.kicad_pcb': '78216fbe27dba3bf2bb430bf4d6f9e56fcdeada14da74f28a3f7933cb5d5f6b2', 'PROT-FUSE-001.kicad_pro': '477ebf548ca65eb653d22b64dc319acf1175615e76fd4c986c486499edf54109', 'PROT-FUSE-001.kicad_sch': '1b72d4d4dc2efb7d430109af3548acfca95ce55fffc85ec12e254ae5386ac8e6'},
    schematic_file='PROT-FUSE-001.kicad_sch',
    pcb_file='PROT-FUSE-001.kicad_pcb',
    kicad_cli_checks=('drc',),
    position_checks={'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 142.7, 'y': 45.7, 'rotation': -90.0}, 'C1': {'footprint': 'Capacitor_THT:C_Disc_D9.0mm_W5.0mm_P10.00mm', 'x': 127.5, 'y': 44.5, 'rotation': -90.0}, 'D3': {'footprint': 'Diode_SMD:D_SMB', 'x': 135.7, 'y': 47.4, 'rotation': -90.0}},
    netlist_checks={'R1': {'1': 'Net-(D3-A1)', '2': 'GND'}, 'C1': {'1': 'Net-(D3-A1)', '2': 'GND'}, 'D3': {'1': 'Net-(D3-A1)', '2': 'GND'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
