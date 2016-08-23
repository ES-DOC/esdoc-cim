# -*- coding: utf-8 -*-

"""
.. module:: platform_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def component_performance():
    """Describes the simulation rate of a component in seconds per model day.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('speed {} s/day', ('speed',)),
        'properties': [
            ('component', 'software.software_component', '0.1',
                "Link to a CIM software component description."),
            ('component_name', 'str', '1.1',
                "Short name of component."),
            ('cores_used', 'int', '0.1',
                "Number of cores used for this component."),
            ('nodes_used', 'int', '0.1',
                "Number of nodes used for this component."),
            ('speed', 'float', '1.1',
                "Time taken to simulate one real day (s).")
        ]
    }


def compute_pool():
    """Homogeneous pool of nodes within a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('accelerator_type', 'str', '0.1',
                "Type of accelerator."),
            ('accelerators_per_node', 'int', '0.1',
                "Number of accelerator units on a node."),
            ('clock_cycle_concurrency', 'int', '0.1',
                 'The number of operations which can be carried out concurrently in a single clock cycle of a single core. E.g. 4.'),
            ('clock_speed', 'float', '0.1',
                 'The clock speed of a single core, in units of GHz. E.g. 3.6.'),
            ('compute_cores_per_node', 'int', '0.1',
                "Number of CPU cores per node."),
            ('cpu_type', 'str', '0.1',
                "CPU type."),
            ('description', 'str', '0.1',
                "Textural description of pool."),
            ('interconnect', 'str', '0.1',
                "Interconnect used."),
            ('memory_per_node', 'platform.storage_volume', '0.1',
                "Memory per node."),
            ('model_number', 'str', '0.1',
                "Model/Board number/type."),
            ('name', 'str', '0.1',
                "Name of compute pool within a machine."),
            ('number_of_nodes', 'int', '0.1',
                "Number of nodes."),
            ('operating_system', 'str', '0.1',
                "Operating system.")
        ],
        'derived': [
            ('total_cores', 'compute_cores_per_node * number_of_nodes'),
            ('total_memory', 'memory_per_node * number_of_nodes')
        ]
    }


def machine():
    """A computer/system/platform/machine which is used for simulation.

    """
    return {
        'type': 'class',
        'base': 'platform.partition',
        'is_abstract': False,
        'properties': [
            ('meta', 'shared.doc_meta_info', '1.1',
                "Document description.")
        ]
    }


def partition():
    """A major partition (component) of a computing system (aka machine).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('compute_pools', 'platform.compute_pool', '1.N',
                "Layout of compute nodes."),
            ('description', 'str', '0.1',
                "Textural description of machine."),
            ('institution', 'linked_to(shared.party)', '1.1',
                "Institutional location."),
            ('model_number', 'str', '0.1',
                "Vendor's model number/name - if it exists."),
            ('name', 'str', '1.1',
                "Name of partition (or machine)."),
            ('online_documentation', 'shared.online_resource', '0.N',
                "Links to documentation."),
            ('partition', 'platform.partition', '0.N',
                "If machine is partitioned, treat subpartitions as machines."),
            ('storage_pools', 'platform.storage_pool', '0.N',
                "Storage resource available."),
            ('vendor', 'linked_to(shared.party)', '0.1',
                "The system integrator or vendor."),
            ('when_used', 'time.time_period', '0.1',
                "If no longer in use, the time period it was in use.")
        ]
    }


def performance_org():
    """Describes the properties of a performance of a configured model on a particular system/machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{} (sypd:{})', ('name', 'sypd')),
        'properties': [
            ('asypd', 'float', '0.1',
                "Actual simulated years per wall-clock day, all-in."),
            ('chsy', 'float', '0.1',
                "Core-Hours per simulated year."),
            ('compiler', 'str', '0.1',
                "Compiler used."),
            ('coupler_load', 'float', '0.1',
                "Percentage of time spent in coupler."),
            ('io_load', 'float', '0.1',
                "Percentage of time spent in I/O."),
            ('load_imbalance', 'float', '0.1',
                "Load imbalance."),
            ('memory_bloat', 'float', '0.1',
                "Percentage of extra memory needed."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Document metadata."),
            ('model', 'linked_to(science.model)', '1.1',
                "Model for which performance was tested."),
            ('name', 'str', '0.1',
                "Short name for performance (experiment/test/whatever)."),
            ('platform', 'linked_to(platform.machine)', '1.1',
                "Platform on which performance was tested."),
            ('subcomponent_performance', 'platform.component_performance', '0.1',
                "Describes the performance of each subcomponent."),
            ('sypd', 'float', '0.1',
                "Simulated years per wall-clock day."),
            ('total_nodes_used', 'int', '0.1',
                "Number of nodes used.")
        ]
    }

def performance():
    """Describes the properties of a performance of a configured model on a particular system/machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{} (sypd:{})', ('name', 'sypd')),
        'properties': [
            # CPMIP model and platform
            ('resolution', 'int', '0.1', 
                 'Resolution measured as the number of gridpoints (or more generally, spatial degrees of freedom) NX x NY x NZ per component with an independent discretization'),
            ('complexity', 'int', '0.1', 
                 'Complexity measured as the number of prognostic variables per component with an independent discretization'),
            ('platform', 'platform.machine', '1.1',
                 'Platform on which performance was tested.'),

            # CPMIP computational cost
            ('simulated_years_per_day', 'float', '0.1',
                 'Simulated years per day (SYPD) in a 24h period on the given platform'),
            ('actual_simulated_years_per_day', 'float', '0.1',
                 'Actual simulated years per day (ASYPD) in a 24h period on the given platform obtained from a typical long-running simulation with the model. Inclusive of system interruptions, queue wait time, or issues with the model workflow, etc.'),
            ('core_hours_per_simulated_year', 'float', '0.1',
                 'Core-hours per simulated year (CHSY). This is measured as the product of the model runtime for 1 SY, and the numbers of cores allocated. Note that if allocations are done on a node basis then all cores on a node are charged against the allocation, regardless of whether or not they are used.'),
            ('parallelization', 'float', '0.1',
                 'Parallelization measured as the total number of cores (NP) allocated for the run, regardless of whether or or all cores were used. Note that NP=CHSY*SYPD/24.'),
            ('joules_per_simulated_year', 'float', '0.1',
                 'The energy cost of a simulation, measured in joules per simulated year (JPSY). Given the energy E in joules consumed over a budgeting interval T (generally 1 month or 1 year, in units of hours), JPSY=CHSY*E*T/NP'),

            # CPMIP coupling, memory, I/O
            ('coupling_cost', 'float', '0.1',
                 'Coupling cost measures the overhead caused by coupling. This can include the cost of the coupling algorithm itself (which may involve grid interpolation and computation of transfer coefficients for conservative coupling) as well as load imbalance. It is the normalized difference between the time-processor integral for the whole model versus the sum of individual concurrent components'),
            ('memory_bloat', 'float', '0.1',
                 'Memory bloat is the ratio of the actual memory size to the ideal memory size (the size of the complete model state, which in theory is all you need to hold in memory)Mi, defined below.'),
            ('data_output_cost', 'float', '0.1',
                 'Data output cost is the cost of performing I/O, and is the ratio of CHSY with and without I/O.'),
            ('data_intensity', 'float', '0.1',
                 'Data intensity the amount of data produced per compute-hour, in units GB per compute-hour.'),

            ('asypd', 'float', '0.1',
                "Actual simulated years per wall-clock day, all-in."),
            ('chsy', 'float', '0.1',
                "Core-Hours per simulated year."),
            ('compiler', 'str', '0.1',
                "Compiler used."),
            ('coupler_load', 'float', '0.1',
                "Percentage of time spent in coupler."),
            ('io_load', 'float', '0.1',
                "Percentage of time spent in I/O."),
            ('load_imbalance', 'float', '0.1',
                "Load imbalance."),
            ('memory_bloat', 'float', '0.1',
                "Percentage of extra memory needed."),
            ('model', 'linked_to(science.model)', '1.1',
                "Model for which performance was tested."),
            ('name', 'str', '0.1',
                "Short name for performance (experiment/test/whatever)."),
            ('subcomponent_performance', 'platform.component_performance', '0.1',
                "Describes the performance of each subcomponent."),

            ('meta', 'shared.doc_meta_info', '1.1',
                "Document metadata."),
        ]
    }


def storage_pool():
    """Homogeneous storage pool on a computing machine.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('description', 'str', '0.1',
                "Description of the technology used."),
            ('name', 'str', '1.1',
                "Name of storage pool."),
            ('type', 'platform.storage_systems', '0.1',
                "Type of storage."),
            ('vendor', 'linked_to(shared.party)', '0.1',
                "Vendor of storage hardware.")
        ]
    }


def storage_systems():
    """Controlled vocabulary for storage  types (including filesystems).

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Lustre", "Lustre parallel file system"),
            ("GPFS", "IBM GPFS (also known as IBM Spectral Scale"),
            ("isilon", "The EMC scaleout NAS solution"),
            ("NFS", "Generic Network File System"),
            ("S3", "Object file system exposing the AWS S3 interface"),
            ("PanFS", "Panasas Parallel File system"),
            ("Other Disk", "Other disk based file system"),
            ("Tape - MARS", "Tape storage system using ECMWF MARS"),
            ("Tape - MASS", "Tape storage system using Met Office MASS"),
            ("Tape - Castor", "Tape storage sytsem using CERN Castor"),
            ("Tape - Other", "Other tape based system")
        ]
    }


def storage_volume():
    """Platform storage volume and units.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{} {}', ('volume', 'units')),
        'properties': [
            ('units', 'platform.volume_units', '1.1',
                "Volume units."),
            ('volume', 'int', '1.1',
                "Numeric value.")
        ]
    }


def volume_units():
    """Appropriate storage volume units.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("GB", "Gigabytes (1000^3)"),
            ("TB", "Terabytes (1000^4)"),
            ("PB", "Petabytes (1000^5)"),
            ("EB", "Exabytes (1000^6)"),
            ("TiB", "Tebibytes (1024^4)"),
            ("PiB", "Pebibytes (1024^5)"),
            ("EiB", "Exbibytes (1024^6)")
        ]
    }
