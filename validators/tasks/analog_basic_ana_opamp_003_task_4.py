from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-OPAMP-003_task_4',
    project_files=['ANA-OPAMP-003.kicad_pcb', 'ANA-OPAMP-003.kicad_pro', 'ANA-OPAMP-003.kicad_sch'],
    golden_hashes={'ANA-OPAMP-003.kicad_pcb': 'cf66ebc4b999ee00f6366ee8db3c2b6774995420a491905515094b9bf475f76e', 'ANA-OPAMP-003.kicad_pro': 'e6d9b6a709223579c7f48fb0766efaca7b355a68818150b0b630294c848e83f5', 'ANA-OPAMP-003.kicad_sch': '54fadb3266acafa5b7a0578cc2b61e384403c37421c424467cfaaf574918e91d'},
    source_hashes={'ANA-OPAMP-003.kicad_pcb': 'ca05227230615cda9e3d6980b3ed2e2c4f65118695d66b11d2127d4947ad2b7b', 'ANA-OPAMP-003.kicad_pro': 'e6d9b6a709223579c7f48fb0766efaca7b355a68818150b0b630294c848e83f5', 'ANA-OPAMP-003.kicad_sch': '79f41f16045455682645271d71ae8d224dc4e029fac6d3abd8f2b599c07e1b57'},
    schematic_file='ANA-OPAMP-003.kicad_sch',
    pcb_file='ANA-OPAMP-003.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'R4': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 84.836, 'y': 73.406, 'rotation': -90.0}, 'R5': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 84.836, 'y': 77.47, 'rotation': -90.0}, 'R1': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 87.884, 'y': 74.93, 'rotation': 180.0}},
    netlist_checks={'R4': {'1': '+5V', '2': 'Net-(U1-+)'}, 'R5': {'1': 'Net-(U1-+)', '2': 'GND'}, 'R1': {'1': 'Net-(U1--)', '2': 'Net-(C3-Pad2)'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
