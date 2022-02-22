
"""
.. module:: cim.v2.extended_schema_for_cmip_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def cmip_dataset():
    """A CMIP dataset.

	"""
    return {
        'type': 'class',
        'base': "data.dataset",
        'base-hierarchy': [
            'data.dataset'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('drs_location', 'drs.drs_publication_dataset', '0.N',
                "DRS identifier of dataset."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('originating_simulation', 'activity.simulation', '0.1',
                "Makes a link back to originating activity."),
            ],
        'properties-all': [
            'availability',
            'citations',
            'contains',
            'description',
            'drs_location',
            'further_attributes',
            'keywords',
            'lineage',
            'meta',
            'meta',
            'name',
            'originating_simulation',
            'progress',
            'related_to_dataset',
            'responsible_parties',
            'type',
            ],
        'properties-inherited': [
            'availability :: data.dataset',
            'citations :: data.dataset',
            'contains :: data.dataset',
            'description :: data.dataset',
            'further_attributes :: data.dataset',
            'keywords :: data.dataset',
            'lineage :: data.dataset',
            'meta :: data.dataset',
            'name :: data.dataset',
            'progress :: data.dataset',
            'related_to_dataset :: data.dataset',
            'responsible_parties :: data.dataset',
            'type :: data.dataset',
            ]
    }


def cmip_simulation():
    """A CMIP simulation.

    In most CMIP cases this should be auto-generated from output dataset
    file headers.

	"""
    return {
        'type': 'class',
        'base': "activity.simulation",
        'base-hierarchy': [
            'activity.simulation',
            'iso.process_step'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('forcing_index', 'int', '1.1',
                "index for variant of forcing, e.g. 2"),
            ('initialization_index', 'int', '1.1',
                "Index variant of initialization method, e.g. 1"),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('physics_index', 'int', '1.1',
                "index for model physics, e.g. 3"),
            ('realization_index', 'int', '1.1',
                "realization number, e.g. 5"),
            ('variant_info', 'str', '0.1',
                "description of run variant differences, e.g. forcing: black carbon aerosol only"),
            ],
        'properties-all': [
            'calendar',
            'description',
            'documentation',
            'end_time',
            'ensemble_id',
            'errata',
            'execution_date_time',
            'extra_attributes',
            'forcing_index',
            'had_performance',
            'initialization_index',
            'institution',
            'meta',
            'meta',
            'parent_of',
            'part_of_project',
            'physics_index',
            'primary_ensemble',
            'processing_information',
            'processor',
            'produced',
            'ran_for_experiments',
            'ran_on',
            'rationale',
            'realization_index',
            'reference',
            'report',
            'source',
            'start_time',
            'sub_experiment',
            'used',
            'variant_info',
            ],
        'properties-inherited': [
            'calendar :: activity.simulation',
            'description :: iso.process_step',
            'documentation :: activity.simulation',
            'end_time :: activity.simulation',
            'ensemble_id :: activity.simulation',
            'errata :: activity.simulation',
            'execution_date_time :: iso.process_step',
            'extra_attributes :: activity.simulation',
            'had_performance :: activity.simulation',
            'institution :: activity.simulation',
            'meta :: activity.simulation',
            'parent_of :: activity.simulation',
            'part_of_project :: activity.simulation',
            'primary_ensemble :: activity.simulation',
            'processing_information :: iso.process_step',
            'processor :: iso.process_step',
            'produced :: activity.simulation',
            'ran_for_experiments :: activity.simulation',
            'ran_on :: activity.simulation',
            'rationale :: iso.process_step',
            'reference :: iso.process_step',
            'report :: iso.process_step',
            'source :: iso.process_step',
            'start_time :: activity.simulation',
            'sub_experiment :: activity.simulation',
            'used :: activity.simulation',
            ]
    }




