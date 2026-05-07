Please directly revise the KiCad project in the current workspace.

This is a 12V input protection KiCad project (industrial applications leave margin to 15V), using a resettable fuse F1 (Polyfuse) + unidirectional TVS combination connected in series between the input connector J1 and the downstream load. Please review whether the actual fuse package/footprint is consistent with its rated current and operating current using the project files, project description, and `datasheets/`, and complete the necessary schematic or PCB modifications.

This task focuses on whether F1's current footprint and pad dimensions can carry the operating current and satisfy thermal derating margin, and whether it really corresponds to a fuse rather than the footprint of some other SMD device.
