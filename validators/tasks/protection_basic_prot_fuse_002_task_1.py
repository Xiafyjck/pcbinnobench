from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='protection_basic_PROT-FUSE-002_task_1',
    project_files=['PROT-FUSE-002.kicad_pcb', 'PROT-FUSE-002.kicad_pro', 'PROT-FUSE-002.kicad_sch'],
    golden_hashes={'PROT-FUSE-002.kicad_pcb': '2a67bbcd631355541ffe7b0e42aa999ac59b126e8ca040b49e32294bce8c497e', 'PROT-FUSE-002.kicad_pro': '477ebf548ca65eb653d22b64dc319acf1175615e76fd4c986c486499edf54109', 'PROT-FUSE-002.kicad_sch': 'bb592f5ec723ed62f7f2cdb6731f6784e44ac2d047e265a360a8b6bf747915ea'},
    source_hashes={'PROT-FUSE-002.kicad_pcb': 'a6b2e24f1bdda2e9963c8202b371ae5869cd429295af53c8f2c2b0ad0dfc0818', 'PROT-FUSE-002.kicad_pro': 'f6ea7a76b187d3cdbd8e4587afd0aaf07011cde8db27903340ee908cc8d504de', 'PROT-FUSE-002.kicad_sch': 'd08e35f5c37d9ea58d18dc2dca90beb599171b1ac0c83973efa60830dec72e17'},
    schematic_file='PROT-FUSE-002.kicad_sch',
    pcb_file='PROT-FUSE-002.kicad_pcb',
    kicad_cli_checks=('drc', 'erc', 'netlist_export'),
    position_checks={'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 133.5, 'y': 53.8, 'rotation': 180.0}, 'J2': {'footprint': 'Connector_JST:JST_EH_B2B-EH-A_1x02_P2.50mm_Vertical', 'x': 149.85, 'y': 46.4225, 'rotation': -90.0}, 'F1': {'footprint': 'Fuse:Fuse_1210_3225Metric', 'x': 118.5, 'y': 49.7, 'rotation': 0.0}},
    netlist_checks={'R2': {'1': 'Net-(D2-A)', '2': 'Net-(D3-A1)'}, 'J2': {'1': 'Net-(D3-A1)', '2': 'GND'}, 'F1': {'1': '+12V', '2': 'Net-(D3-A1)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
