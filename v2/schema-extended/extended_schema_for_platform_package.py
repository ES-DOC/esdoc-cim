
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_platform_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def component_performance():
	"""Describes the simulation rate of a component in seconds per model
day.

Based on "CPMIP: Measurements of Real Computational Performance of
Earth System Models" (Balaji et. al.)

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('actual_simulated_years_per_day', 'float', '0.1',
                "Actual simulated years per day (ASYPD) in a 24h period on the given platform obtained from a typical long-running simulation with the component. Inclusive of system interruptions, queue wait time, or issues with the model workflow, etc."),
            ('component', 'software.software_component', '0.1',
                "Link to a CIM software component description."),
            ('component_name', 'str', '1.1',
                "Short name of component."),
            ('core_hours_per_simulated_year', 'float', '0.1',
                "Core-hours per simulated year (CHSY). This is measured as the product of the component runtime for 1 SY, and the numbers of cores allocated. Note that if allocations are done on a node basis then all cores on a node are charged against the allocation, regardless of whether or not they are used."),
            ('parallelization', 'float', '0.1',
                "Parallelization measured as the total number of cores (NP) allocated for the component, regardless of whether or or all cores were used. Note that NP=CHSY*SYPD/24."),
            ('simulated_years_per_day', 'float', '0.1',
                "Simulated years per day (SYPD) in a 24h period on the given platform"),
            ]
    }


def compute_pool():
	"""Homogeneous pool of nodes within a computing machine.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('accelerator_type', 'str', '0.1',
                "Type of accelerator."),
            ('accelerators_per_node', 'int', '0.1',
                "Number of accelerator units on a node."),
            ('clock_cycle_concurrency', 'int', '0.1',
                "The number of operations which can be carried out concurrently in a single clock cycle of a single core. E.g. 4."),
            ('clock_speed', 'float', '0.1',
                "The clock speed of a single core, in units of GHz. E.g. 3.6."),
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
                "Operating system."),
            ]
    }


def machine():
	"""A computer/system/platform/machine which is used for simulation.

	"""
    return {
        'type': 'class',
        'base': "platform.partition",
        'base-hierarchy': [
            'platform.partition'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ],
        'properties-all': [
            'compute_pools',
            'description',
            'institution',
            'meta',
            'model_number',
            'name',
            'online_documentation',
            'partition',
            'storage_pools',
            'vendor',
            'when_used',
            ],
        'properties-inherited': [
            'compute_pools :: platform.partition',
            'description :: platform.partition',
            'institution :: platform.partition',
            'model_number :: platform.partition',
            'name :: platform.partition',
            'online_documentation :: platform.partition',
            'partition :: platform.partition',
            'storage_pools :: platform.partition',
            'vendor :: platform.partition',
            'when_used :: platform.partition',
            ]
    }


def partition():
	"""A major partition (component) of a computing system (aka machine).

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'platform.machine'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('compute_pools', 'platform.compute_pool', '1.N',
                "Layout of compute nodes."),
            ('description', 'str', '0.1',
                "Textural description of machine."),
            ('institution', 'shared.party', '1.1',
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
            ('vendor', 'shared.party', '0.1',
                "The system integrator or vendor."),
            ('when_used', 'time.time_period', '0.1',
                "If no longer in use, the time period it was in use."),
            ]
    }


def performance():
	"""Describes the properties of a performance of a configured model on
a particular system/machine.

Based on "CPMIP: Measurements of Real Computational Performance of
Earth System Models" (Balaji et. al. 2016, doi:10.5194/gmd-2016-197,
http://www.geosci-model-dev-discuss.net/gmd-2016-197/)

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('actual_simulated_years_per_day', 'float', '0.1',
                "Actual simulated years per day (ASYPD) in a 24h period on the given platform obtained from a typical long-running simulation with the model. Inclusive of system interruptions, queue wait time, or issues with the model workflow, etc."),
            ('compiler', 'str', '0.1',
                "Compiler used for performance test."),
            ('complexity', 'int', '0.1',
                "Complexity measured as the number of prognostic variables per component with an independent discretization"),
            ('core_hours_per_simulated_year', 'float', '0.1',
                "Core-hours per simulated year (CHSY). This is measured as the product of the model runtime for 1 SY, and the numbers of cores allocated. Note that if allocations are done on a node basis then all cores on a node are charged against the allocation, regardless of whether or not they are used."),
            ('coupling_cost', 'float', '0.1',
                "Coupling cost measures the overhead caused by coupling. This can include the cost of the coupling algorithm itself (which may involve grid interpolation and computation of transfer coefficients for conservative coupling) as well as load imbalance. It is the normalized difference between the time-processor integral for the whole model versus the sum of individual concurrent components"),
            ('data_intensity', 'float', '0.1',
                "Data intensity the amount of data produced per compute-hour, in units GB per compute-hour."),
            ('data_output_cost', 'float', '0.1',
                "Data output cost is the cost of performing I/O, and is the ratio of CHSY with and without I/O."),
            ('joules_per_simulated_year', 'float', '0.1',
                "The energy cost of a simulation, measured in joules per simulated year (JPSY). Given the energy E in joules consumed over a budgeting interval T (generally 1 month or 1 year, in units of hours), JPSY=CHSY*E*T/NP"),
            ('memory_bloat', 'float', '0.1',
                "Memory bloat is the ratio of the actual memory size to the ideal memory size (the size of the complete model state, which in theory is all you need to hold in memory)Mi, defined below."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('model', 'science.model', '1.1',
                "Model for which performance was tested."),
            ('name', 'str', '0.1',
                "Name for performance (experiment/test/whatever)."),
            ('parallelization', 'float', '0.1',
                "Parallelization measured as the total number of cores (NP) allocated for the run, regardless of whether or or all cores were used. Note that NP=CHSY*SYPD/24."),
            ('platform', 'platform.machine', '1.1',
                "Platform on which performance was tested."),
            ('resolution', 'int', '0.1',
                "Resolution measured as the number of gridpoints (or more generally, spatial degrees of freedom) NX x NY x NZ per component with an independent discretization"),
            ('simulated_years_per_day', 'float', '0.1',
                "Simulated years per day (SYPD) in a 24h period on the given platform"),
            ('subcomponent_performance', 'platform.component_performance', '0.N',
                "Describes the performance of each subcomponent."),
            ]
    }


def storage_pool():
	"""Homogeneous storage pool on a computing machine.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "Description of the technology used."),
            ('name', 'str', '1.1',
                "Name of storage pool."),
            ('type', 'platform.storage_systems', '0.1',
                "Type of storage."),
            ('vendor', 'shared.party', '0.1',
                "Vendor of storage hardware."),
            ]
    }


def storage_volume():
	"""Platform storage volume and units.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('units', 'platform.volume_units', '1.1',
                "Volume units."),
            ('volume', 'int', '1.1',
                "Numeric value."),
            ]
    }




