
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def dataset():
    """Dataset discovery information.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('availability', 'shared.online_resource', '0.N',
                "Where the data is located, and how it is accessed."),
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '0.1',
                "Textural description of dataset."),
            ('drs_datasets', 'drs.drs_publication_dataset', '0.N',
                "Data available in the DRS."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "Name of dataset."),
            ('produced_by', 'data.simulation', '0.1',
                "Makes a link back to originating activity."),
            ('related_to_dataset', 'shared.online_resource', '0.N',
                "Related dataset."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "Individuals and organisations reponsible for the data."),
            ]
    }


def downscaling():
    """Defines a downscaling activity.

	"""
    return {
        'type': 'class',
        'base': "data.simulation",
        'base-hierarchy': [
            'data.simulation',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('downscaled_from', 'data.simulation', '1.1',
                "The simulation that was downscaled by this downscaling activity."),
            ],
        'properties-all': [
            'alternative_names',
            'calendar',
            'canonical_name',
            'citations',
            'description',
            'downscaled_from',
            'duration',
            'end_time',
            'extra_attributes',
            'forcing_index',
            'further_info_url',
            'initialization_index',
            'insitution',
            'internal_name',
            'keywords',
            'long_name',
            'meta',
            'name',
            'parent_simulation',
            'part_of_project',
            'physics_index',
            'previously_known_as',
            'primary_ensemble',
            'ran_for_experiments',
            'rationale',
            'realization_index',
            'responsible_parties',
            'start_time',
            'sub_experiment',
            'used',
            'variant_info',
            ],
        'properties-inherited': [
            'alternative_names :: activity.activity',
            'calendar :: data.simulation',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'end_time :: data.simulation',
            'extra_attributes :: data.simulation',
            'forcing_index :: data.simulation',
            'further_info_url :: data.simulation',
            'initialization_index :: data.simulation',
            'insitution :: data.simulation',
            'internal_name :: activity.activity',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'parent_simulation :: data.simulation',
            'part_of_project :: data.simulation',
            'physics_index :: data.simulation',
            'previously_known_as :: activity.activity',
            'primary_ensemble :: data.simulation',
            'ran_for_experiments :: data.simulation',
            'rationale :: activity.activity',
            'realization_index :: data.simulation',
            'responsible_parties :: activity.activity',
            'start_time :: data.simulation',
            'sub_experiment :: data.simulation',
            'used :: data.simulation',
            'variant_info :: data.simulation',
            ]
    }


def input_dataset():
    """An input dataset is used as within another component (such as a
model). It comprises an original, source dataset plus any
modifications requirted to use it in the relevant component.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('modifications_applied', 'str', '1.1',
                "Describe modifications (if any) applied to the dataset prior to use. E.g. spatial interpolation, temporal averaging, etc."),
            ('original_data', 'data.dataset', '1.1',
                "The source dataset, prior to any modifications"),
            ]
    }


def simulation():
    """Simulation class provides the integrating link about what models
    were run and wny.  In many cases this should be auto-generated
    from output file headers.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'data.downscaling'
        ],
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('calendar', 'time.calendar', '0.1',
                "The calendar used in the simulation"),
            ('end_time', 'time.date_time', '0.1',
                "The start date-time of the simulation. e.g. 2087-11-30 12:00:00"),
            ('extra_attributes', 'shared.extra_attribute', '0.N',
                "Additional attributes provided with simulation."),
            ('forcing_index', 'int', '0.1',
                "index for variant of forcing, e.g. 2"),
            ('further_info_url', 'str', '0.1',
                "On-line location of documentation"),
            ('initialization_index', 'int', '0.1',
                "Index variant of initialization method, e.g. 1"),
            ('insitution', 'shared.party', '0.1',
                "institution which carried out the simulation"),
            ('parent_simulation', 'activity.parent_simulation', '0.1',
                "If appropriate, detailed information about how this simulation branched from a previous one"),
            ('part_of_project', 'designing.project', '1.N',
                "Project or projects for which simulation was run"),
            ('physics_index', 'int', '0.1',
                "index for model physics, e.g. 3"),
            ('primary_ensemble', 'activity.ensemble', '0.1',
                "Primary Ensemble (ensemble for which this simulation was first run)."),
            ('ran_for_experiments', 'designing.numerical_experiment', '1.N',
                "One or more experiments with which the simulation is associated"),
            ('realization_index', 'int', '0.1',
                "realization number, e.g. 5"),
            ('start_time', 'time.date_time', '0.1',
                "The start date-time of the simulation. e.g. 2012-04-01 00:00:00"),
            ('sub_experiment', 'designing.numerical_experiment', '0.1',
                "For start-date ensembles, this will indicate the beginning year; for offline models driven by output from another model, this will provide the source_id and variant_label for the 'driving' model."),
            ('used', 'science.model', '1.1',
                "The model used to run the simulation"),
            ('variant_info', 'str', '0.1',
                "description of run variant differences, e.g. forcing: black carbon aerosol only"),
            ],
        'properties-all': [
            'alternative_names',
            'calendar',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'end_time',
            'extra_attributes',
            'forcing_index',
            'further_info_url',
            'initialization_index',
            'insitution',
            'internal_name',
            'keywords',
            'long_name',
            'meta',
            'name',
            'parent_simulation',
            'part_of_project',
            'physics_index',
            'previously_known_as',
            'primary_ensemble',
            'ran_for_experiments',
            'rationale',
            'realization_index',
            'responsible_parties',
            'start_time',
            'sub_experiment',
            'used',
            'variant_info',
            ],
        'properties-inherited': [
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            ]
    }


def variable_collection():
    """A collection of variables within the scope of a code or process element.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('collection_name', 'str', '0.1',
                "Name for this variable collection."),
            ('variables', 'str', '1.N',
                "Set of variable names."),
            ]
    }




