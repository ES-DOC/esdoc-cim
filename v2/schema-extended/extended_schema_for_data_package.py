
"""
.. module:: cim.v2.extended_schema_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def dataset():
    """Dataset discovery information.

    This may be further enhanced for ISO (or any other) compliance via
    the extra attributes or project specific sub-classing.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'cmip.cmip_dataset'
        ],
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('availability', 'shared.online_resource', '0.N',
                "Where the data is located, and how it is accessed."),
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('contains', 'data.variable_collection', '0.N',
                "Contents in terms of variables."),
            ('description', 'str', '0.1',
                "Textural description of dataset."),
            ('further_attributes', 'shared.extra_attribute', '0.N',
                "Additional attributes as necessary."),
            ('keywords', 'str', '0.N',
                "Set of additional keywords to aid discovery/classification"),
            ('lineage', 'iso.lineage', '0.1',
                "Provenance of the dataset"),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "Name of dataset."),
            ('progress', 'iso.md_progress_code', '0.1',
                "State of the dataset"),
            ('related_to_dataset', 'shared.formal_association', '0.N',
                "Related dataset."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "Individuals and organisations responsible for the data."),
            ('type', 'data.dataset_type', '1.N',
                "Dataset discovery classifier"),
            ]
    }


def variable_collection():
    """A collection of variables within the scope of a code or process
    element.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('collection_name', 'str', '0.1',
                "Name for this variable collection."),
            ('geometry', 'iso.md_cellgeometry_code', '0.1',
                "Defines whether or not all variables in collection are point or area based"),
            ('variables', 'str', '1.N',
                "Set of variable names."),
            ]
    }




