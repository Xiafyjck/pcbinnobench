Please directly revise the KiCad project in the current workspace.

This is a Hall-effect current sensor front-end KiCad project using an ACS712 and OPA333 to perform ±20A current acquisition. The analog front end is powered from 5V, and its output is sampled by a downstream 3.3V ADC. Please review the current design against the engineering goals for output noise, zero-point stability, and sampling accuracy, using the project files, project description, and `datasheets/`, and complete any necessary schematic or PCB modifications.

This task focuses on whether the power integrity, noise ingress paths, and related PCB layout of the ACS712 and OPA333 analog front end are sufficient to support stable downstream sampling.
