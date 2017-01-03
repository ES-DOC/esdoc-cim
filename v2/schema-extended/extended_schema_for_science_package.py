
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def model():
    """A model component: can be executed standalone, and has as
    scientific description available via a link to a science.domain
    document. (A configured model can be understood in terms of a
    simulation, a model, and a configuration.).

	"""
    return {
        'type': 'class',
        'base': "software.component_base",
        'base-hierarchy': [
            'software.component_base'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('coupled_components', 'science.model', '0.N',
                "Software components which are linked together using a coupler to deliver this model."),
            ('coupler', 'software.coupling_framework', '0.1',
                "Overarching coupling framework for model."),
            ('internal_software_components', 'software.software_component', '0.N',
                "Software modules which together provide the functionality for this model."),
            ('key_properties', 'science.process', '0.1',
                "Model default key properties (may be over-ridden in coupled component and realm properties)."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('model_type', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('realms', 'science.realm', '0.N',
                "The scientific realms which this model simulates internally, i.e. those which are not linked together using a coupler."),
            ],
        'properties-all': [
            'canonical_id',
            'citations',
            'coupled_components',
            'coupler',
            'description',
            'development_history',
            'internal_software_components',
            'key_properties',
            'long_name',
            'meta',
            'model_type',
            'name',
            'realms',
            'release_date',
            'repository',
            'version',
            ],
        'properties-inherited': [
            'canonical_id :: software.component_base',
            'citations :: software.component_base',
            'description :: software.component_base',
            'development_history :: software.component_base',
            'long_name :: software.component_base',
            'name :: software.component_base',
            'release_date :: software.component_base',
            'repository :: software.component_base',
            'version :: software.component_base',
            ]
    }


def process():
    """Provides structure for description of a process simulated within a
    particular area (or domain/realm/component) of a model. This will
    often be subclassed within a specific implementation so that
    constraints can be used to ensure that the process details
    requested are consistent with project requirements for
    information.

	"""
    return {
        'type': 'class',
        'base': "science.topic",
        'base-hierarchy': [
            'science.topic'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('sub_processes', 'science.topic', '0.N',
                "Discrete portion of a process with common process details."),
            ],
        'properties-all': [
            'citations',
            'description',
            'keywords',
            'overview',
            'properties',
            'property_sets',
            'responsible_parties',
            'short_name',
            'specialization_id',
            'sub_processes',
            ],
        'properties-inherited': [
            'citations :: science.topic',
            'description :: science.topic',
            'keywords :: science.topic',
            'overview :: science.topic',
            'properties :: science.topic',
            'property_sets :: science.topic',
            'responsible_parties :: science.topic',
            'short_name :: science.topic',
            'specialization_id :: science.topic',
            ]
    }


def realm():
    """Scientific area of a numerical model - usually a sub-model or component.

	"""
    return {
        'type': 'class',
        'base': "science.topic",
        'base-hierarchy': [
            'science.topic'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('grid', 'science.process', '0.1',
                "The grid used to layout the variables (e.g. the Global ENDGAME-grid)."),
            ('key_properties', 'science.process', '0.1',
                "Realm key properties which differ from model defaults (grid, timestep etc)."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('processes', 'science.process', '1.N',
                "Processes simulated within the realm."),
            ('realm_type', 'str', '0.1',
                "Canonical name for the realm."),
            ('software_frameworks', 'software.implementation', '0.N',
                "Software framework(s) of the realm."),
            ],
        'properties-all': [
            'citations',
            'description',
            'grid',
            'key_properties',
            'keywords',
            'meta',
            'overview',
            'processes',
            'properties',
            'property_sets',
            'realm_type',
            'responsible_parties',
            'short_name',
            'software_frameworks',
            'specialization_id',
            ],
        'properties-inherited': [
            'citations :: science.topic',
            'description :: science.topic',
            'keywords :: science.topic',
            'overview :: science.topic',
            'properties :: science.topic',
            'property_sets :: science.topic',
            'responsible_parties :: science.topic',
            'short_name :: science.topic',
            'specialization_id :: science.topic',
            ]
    }


def topic():
    """An organized collection of details upon a specific topic, e.g. model key properties.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'science.process',
            'science.realm'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '0.1',
                "A description (possibly derived from specialization)."),
            ('keywords', 'str', '0.N',
                "Keywords to help re-use and discovery of this information."),
            ('overview', 'str', '0.1',
                "General implementation overview."),
            ('properties', 'science.topic_property', '1.N',
                "Set of associated specialized properties."),
            ('property_sets', 'science.topic_property_set', '1.N',
                "Set of associated specialized detail attributes."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for providing this information."),
            ('short_name', 'str', '0.1',
                "A short-name / key (possibly derived from specialization)."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ]
    }


def topic_property():
    """A specialized question asked of the scientic community.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ('value', 'str', '1.1',
                "User value."),
            ]
    }


def topic_property_set():
    """Provides specific details related to a topic (i.e. process, sub-process,
    grid, key properties, etc).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "A description (possibly derived from specialization)."),
            ('properties', 'science.topic_property', '1.N',
                "Set of associated specialized properties."),
            ('short_name', 'str', '0.1',
                "A short-name / key (possibly derived from specialization)."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ]
    }




