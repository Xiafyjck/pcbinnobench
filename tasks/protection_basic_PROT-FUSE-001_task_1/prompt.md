Directly revise the KiCad project in the current workspace.

This is an overcurrent/surge protection KiCad project for a USB 5V input, using a unidirectional TVS (SM6T15A) + series fuse (F1, Device:Fuse) to protect the downstream 5V path. Please review the project files, project description, and `datasheets/` to determine whether the operating margin and package current-carrying capability of the fuse under the highest ambient temperature and actual load current are consistent, and complete any necessary schematic or PCB modifications.

This task focuses on whether F1's current package/landing pattern can carry the steady-state current on the USB 5V path and meet thermal derating requirements, and whether this package matches a fuse rather than another SMD component.
