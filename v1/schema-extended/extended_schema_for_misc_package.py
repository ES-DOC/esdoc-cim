
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.extended_schema_for_misc_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def document_set():
    """Represents a bundled set of documents.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('data', 'data.data_object', '0.N',
                "Associated input/output data."),
            ('ensembles', 'activity.ensemble', '0.N',
                "Associated ensemble runs."),
            ('experiment', 'activity.numerical_experiment', '0.1',
                "Associated numerical experiment."),
            ('grids', 'grids.grid_spec', '0.N',
                "Associated grid-spec."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('model', 'software.model_component', '0.1',
                "Associated model component."),
            ('platform', 'shared.platform', '0.1',
                "Associated simulation execution platform."),
            ('simulation', 'activity.simulation_run', '0.1',
                "Associated simulation run."),
            ]
    }




