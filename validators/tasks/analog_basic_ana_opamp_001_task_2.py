from validators.common import TaskSpec, validate_against_ground_truth

SPEC = TaskSpec(
    task_id='analog_basic_ANA-OPAMP-001_task_2',
    project_files=['ANA-OPAMP-001.kicad_pcb', 'ANA-OPAMP-001.kicad_pro', 'ANA-OPAMP-001.kicad_sch'],
    golden_hashes={'ANA-OPAMP-001.kicad_pcb': '8228dff26152bafd629a0928cd965c7a006deb258693a9799e29365f6f9905b7', 'ANA-OPAMP-001.kicad_pro': '7caf60912dbd153c33bb32030f37bb25127f98a3d262f06fa04037784eccc2da', 'ANA-OPAMP-001.kicad_sch': 'd284bd785efe00222be251b28f1700721b671bd39facec8c48cdbd05a31324d7'},
    source_hashes={'ANA-OPAMP-001.kicad_pcb': 'f5ef55c26e8d7c706dbb5296252ac0c618baabec00e0e06d2323b442ec91bfc0', 'ANA-OPAMP-001.kicad_pro': '7caf60912dbd153c33bb32030f37bb25127f98a3d262f06fa04037784eccc2da', 'ANA-OPAMP-001.kicad_sch': 'af0eed8726a0bed987358789aec9b8836e38f3ed96ef1de4e22676d7d2f6cddf'},
    schematic_file='ANA-OPAMP-001.kicad_sch',
    pcb_file='ANA-OPAMP-001.kicad_pcb',
    kicad_cli_checks=('netlist_export',),
    position_checks={'U1': {'footprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'x': 71.882, 'y': 75.946, 'rotation': 0.0}, 'D2': {'footprint': 'Diode_SMD:D_SOD-323F', 'x': 65.532, 'y': 69.85, 'rotation': -90.0}, 'R2': {'footprint': 'Resistor_SMD:R_0805_2012Metric', 'x': 62.738, 'y': 69.85, 'rotation': 90.0}},
    netlist_checks={'U1': {'1': 'unconnected-(U1-NC-Pad1)', '2': 'Net-(J3-Pin_1)', '3': 'Net-(U1-+)', '4': 'GND', '5': 'unconnected-(U1-NC-Pad5)', '6': 'Net-(J3-Pin_1)'}, 'D2': {'1': '+5V', '2': 'Net-(D1-K)'}, 'R2': {'1': 'Net-(D1-K)', '2': '+5V'}},
)

def validate(workspace_dir, repo_root=None):
    return validate_against_ground_truth(SPEC, workspace_dir, repo_root=repo_root)
