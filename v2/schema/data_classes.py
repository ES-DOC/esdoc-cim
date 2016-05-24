# -*- coding: utf-8 -*-

"""
.. module:: data_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def data_association_types():
    """Set of possible dataset associations.
    Selected from, and extended from,  ISO19115 (2014) DS_AssociationTypeCode.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("revisonOf", "This dataset was revised from the target"),
            ("partOf", "This dataset forms part of the target"),
            ("isComposedOf", "This dataset is composed from the target")
        ]
    }


def dataset():
    """Dataset discovery information.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('availability', 'shared.online_resource', '0.N',
                "Where the data is located, and how it is accessed."),
            ('description', 'str', '0.1',
                "Textural description of dataset."),
            ('drs_datasets', 'drs.drs_publication_dataset', '0.N',
                "Data available in the DRS."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata describing the creation of this dataset description document."),
            ('name', 'str', '1.1',
                "Name of dataset."),
            ('produced_by', 'linked_to(data.simulation)', '0.1',
                "Makes a link back to originating activity."),
            ('references', 'shared.reference', '0.N',
                "Relevant reference document."),
            ('related_to_dataset', 'shared.online_resource', '0.N',
                "Related dataset."),
            ('responsible_parties', 'linked_to(shared.responsibility)', '0.N',
                "Individuals and organisations reponsible for the data.")
        ]
    }


def downscaling():
    """Defines a downscaling activity.

    """
    return {
        'type': 'class',
        'base': 'data.simulation',
        'is_abstract': False,
        'properties': [
            ('downscaled_from', 'linked_to(data.simulation)', '1.1',
                "The simulation that was downscaled by this downscaling activity.")
        ],
        'constraints': [
            ('cardinality', 'parent_simulation', '0.0')
        ]
    }


def simulation():
    """Simulation class provides the integrating link about what models were run and wny.
    In many cases this should be auto-generated from output file headers.

    """
    return {
        'type': 'class',
        'base': 'activity.activity',
        'is_abstract': False,
        'properties': [
            ('activity_id', 'str', '0.1',
                "activity  labels, e.g. 'CMIP'."),
            ('branch_method', 'str', '0.1',
                "branching procedure, e.g. 'standard'."),
            ('branch_time_in_child', 'float', '0.1',
                "branch time with respect to child time axis, e.g. 365.0."),
            ('branch_time_in_parent', 'float', '0.1',
                "branch time with respect to parent time axis, e.g. 3650.0."),
            ('calendar', 'time.calendar', '0.1',
                "The calendar used in the simulation."),
            ('comment', 'str', '0.1',
                "Miscellaneous information about the data or methods used to produce it."),
            ('contact', 'str', '0.1',
                "None"),
            ('conventions', 'str', '0.1',
                "convention version, e.g. 'CF-1.7 CMIP6-6.0'."),
            ('data_specs_version', 'str', '0.1',
                "version identifier, e.g. '1.3.15'."),
            ('ensemble_identifier', 'str', '1.1',
                "String that can be used to extract ensemble axis membership from the primary ensemble(e.g. cmip6 run_variant_id as in the DRS)."),
            ('experiment_id', 'str', '0.1',
                "root experiment identifier, e.g. 'historical'."),
            ('experisment', 'str', '0.1',
                "short experiment description, e.g. 'pre-industrial control'."),
            ('extra_attributes', 'shared.extra_attribute', '0.N',
                "Additional attributes provided with simulation."),
            ('forcing_index', 'int', '0.1',
                "index for variant of forcing, e.g. 2."),
            ('frequency', 'str', '0.1',
                "sampling frequency, e.g. 'day'."),
            ('further_info_url', 'str', '0.1',
                "location of documentation."),
            ('grid', 'str', '0.1',
                "briefly describes output grid characteristics."),
            ('grid_label', 'str', '0.1',
                "grid identifier, e.g. 'gs1x1'."),
            ('grid_resolution', 'str', '0.1',
                "approximate horizontal resolution, e.g. '50 km'."),
            ('initialization_index', 'int', '0.1',
                "Index variant of initialization method, e.g. 1."),
            ('insitution', 'str', '0.1',
                "institution name, e.g. 'Meteorological Research Institute'."),
            ('institution_id', 'str', '0.1',
                "institution label, e.g. 'IPSL'."),
            ('mip_era', 'str', '0.1',
                "activity's associated CMIP cycle, e.g. 'CMIP6'."),
            ('parent_activity_id', 'str', '0.1',
                "parent activity label, e.g. 'CMIP'."),
            ('parent_experiment_id', 'str', '0.1',
                "parent experiment label, e.g. 'piControl'."),
            ('parent_mip_era', 'str', '0.1',
                "parent\s associated MIP cycle, e.g. 'CMIP6'."),
            ('parent_simulation', 'activity.parent_simulation', '0.1',
                "If appropriate, detailed information about how this simulation branched from a previous one."),
            ('parent_source_id', 'str', '0.1',
                "parent source label, e.g. 'CanCM4'."),
            ('parent_sub_experiment_id', 'str', '0.1',
                "parent sub-experiment label."),
            ('parent_time_units', 'str', '0.1',
                "time units used in parents."),
            ('parent_variant_label', 'str', '0.1',
                "parent variant label, e.g. 'r1i2p22f3'."),
            ('part_of_project', 'linked_to(designing.project)', '1.N',
                "Project or projects for which simulation was run."),
            ('physics_index', 'int', '0.1',
                "index for model physics, e.g. 3."),
            ('primary_ensemble', 'linked_to(activity.ensemble)', '0.1',
                "Primary Ensemble (ensemble for which this simulation was first run)."),
            ('product', 'str', '0.1',
                "product type, e.g. 'output'."),
            ('ran_for_experiments', 'linked_to(designing.numerical_experiment)', '1.N',
                "One or more experiments with which the simulation is associated."),
            ('realization_index', 'int', '0.1',
                "realization number, e.g. 5."),
            ('realm', 'str', '0.1',
                "realm(s) where variable is defined, e.g. 'atmos'."),
            ('references', 'str', '0.1',
                "Published or web-based references that describe the data or methods used to produce it."),
            ('source', 'str', '0.1',
                "source title, e.g. 'GFDL CM2.1: cycle 2.1.14'."),
            ('source_id', 'str', '0.1',
                "source label, e.g. 'GFDL-CM2.1'."),
            ('source_type', 'str', '0.1',
                "type of model used, e.g. 'AOGCM'."),
            ('sub_eperiment', 'str', '0.1',
                "description of sub-experiment."),
            ('sub_eperiment_id', 'str', '0.1',
                "sub-experiment label, e.g. 's1960'."),
            ('table_id', 'str', '0.1',
                "table label, e.g. Amon."),
            ('used', 'linked_to(science.model)', '1.1',
                "The model used to run the simulation."),
            ('variant_info', 'str', '0.1',
                "description of run variant differences, e.g. 'forcing: black carbon aerosol only'."),
            ('variant_label', 'str', '0.1',
                "variant label, e.g. 'r1i1p1f1'.")
        ],
        'constraints': [
            ('cardinality', 'rationale', '0.0')
        ]
    }


def variable_collection():
    """A collection of variables within the scope of a code or process element.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('collection_name', 'str', '0.1',
                "Name for this variable collection."),
            ('variables', 'str', '1.N',
                "Set of variable names.")
        ]
    }
