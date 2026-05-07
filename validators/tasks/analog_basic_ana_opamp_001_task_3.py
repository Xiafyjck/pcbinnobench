from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-OPAMP-001_task_3',
    project_files=['ANA-OPAMP-001.kicad_pcb', 'ANA-OPAMP-001.kicad_pro', 'ANA-OPAMP-001.kicad_sch'],
    golden_hashes={'ANA-OPAMP-001.kicad_pcb': '8228dff26152bafd629a0928cd965c7a006deb258693a9799e29365f6f9905b7', 'ANA-OPAMP-001.kicad_pro': '7caf60912dbd153c33bb32030f37bb25127f98a3d262f06fa04037784eccc2da', 'ANA-OPAMP-001.kicad_sch': 'd284bd785efe00222be251b28f1700721b671bd39facec8c48cdbd05a31324d7'},
    source_hashes={'ANA-OPAMP-001.kicad_pcb': 'e515f59308eb3055d215fa95f4bc2fd5a0440bdb5f4a1d4b1ee8541cd7db170b', 'ANA-OPAMP-001.kicad_pro': '7caf60912dbd153c33bb32030f37bb25127f98a3d262f06fa04037784eccc2da', 'ANA-OPAMP-001.kicad_sch': 'd284bd785efe00222be251b28f1700721b671bd39facec8c48cdbd05a31324d7'},
    schematic_file='ANA-OPAMP-001.kicad_sch',
    pcb_file='ANA-OPAMP-001.kicad_pcb',
    kicad_cli_checks=('drc',),
    position_checks={'C1': {'footprint': 'Capacitor_SMD:C_0805_2012Metric', 'x': 64.77, 'y': 63.246, 'rotation': 0.0}, 'J1': {'footprint': 'Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Horizontal', 'x': 54.61, 'y': 85.344, 'rotation': 180.0}, 'U1': {'footprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'x': 71.882, 'y': 75.946, 'rotation': 0.0}},
    netlist_checks={'C1': {'1': '+5V', '2': 'GND'}, 'J1': {'1': 'Net-(D1-K)', '2': 'Net-(D1-K)'}, 'U1': {'1': 'unconnected-(U1-NC-Pad1)', '2': 'Net-(J3-Pin_1)', '3': 'Net-(U1-+)', '4': 'GND', '5': 'unconnected-(U1-NC-Pad5)', '6': 'Net-(J3-Pin_1)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
