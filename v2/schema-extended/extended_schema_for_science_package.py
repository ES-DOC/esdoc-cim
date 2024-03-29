
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
    document.

    (A configured model can be understood in terms of a simulation, a
    model, and a configuration.).

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
            ('activity_properties', 'science.topic', '0.N',
                "Properties specific to the modelling activity in question, e.g. radiative forcing agents for CMIP6."),
            ('coupled_components', 'science.model', '0.N',
                "Software components which are linked together using a coupler to deliver this model."),
            ('coupler', 'software.coupling_framework', '0.1',
                "Overarching coupling framework for model."),
            ('internal_software_components', 'software.software_component', '0.N',
                "Software modules which together provide the functionality for this model."),
            ('key_properties', 'science.topic', '0.1',
                "Model default key properties (may be over-ridden in coupled component and realm properties)."),
            ('keywords', 'str', '0.N',
                "Keywords to help re-use and discovery of this information."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('model_type', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('realm_coupling', 'science.realm_coupling', '0.N',
                "Description of a coupling between realms"),
            ('realms', 'science.realm', '0.N',
                "The scientific realms which this model simulates internally, i.e. those which are not linked together using a coupler."),
            ],
        'properties-all': [
            'activity_properties',
            'canonical_id',
            'citations',
            'coupled_components',
            'coupler',
            'description',
            'development_history',
            'internal_software_components',
            'key_properties',
            'keywords',
            'long_name',
            'meta',
            'model_type',
            'name',
            'realm_coupling',
            'realms',
            'release_date',
            'repository',
            'responsible_parties',
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
            'responsible_parties :: software.component_base',
            'version :: software.component_base',
            ]
    }


def realm():
    """Scientific area of a numerical model - usually a sub-model or
    component.

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
            ('canonical_name', 'str', '0.1',
                "Canonical name for the realm."),
            ('grid', 'science.topic', '0.1',
                "The grid used to layout the variables (e.g. the Global ENDGAME-grid)."),
            ('key_properties', 'science.topic', '0.1',
                "Realm key properties which differ from model defaults (grid, timestep etc)."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('processes', 'science.topic', '1.N',
                "Processes simulated within the realm."),
            ('software_frameworks', 'software.implementation', '0.N',
                "Software framework(s) of the realm."),
            ],
        'properties-all': [
            'canonical_name',
            'citations',
            'description',
            'grid',
            'key_properties',
            'keywords',
            'meta',
            'name',
            'overview',
            'processes',
            'properties',
            'property_sets',
            'qc_status',
            'responsible_parties',
            'software_frameworks',
            'specialization_id',
            'sub_topics',
            ],
        'properties-inherited': [
            'citations :: science.topic',
            'description :: science.topic',
            'keywords :: science.topic',
            'name :: science.topic',
            'overview :: science.topic',
            'properties :: science.topic',
            'property_sets :: science.topic',
            'qc_status :: science.topic',
            'responsible_parties :: science.topic',
            'specialization_id :: science.topic',
            'sub_topics :: science.topic',
            ]
    }


def realm_coupling():
    """Description of a coupling between realms.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('coupling_details', 'str', '0.1',
                "Description of the coupling algorithm, and any other information (e.g. binlinear interpolation"),
            ('source_realm', 'str', '1.1',
                "The model realm providing the variable (e.g. ocean)"),
            ('target_realm', 'str', '1.1',
                "The model realm receiving the variable (e.g. atmosphere)"),
            ('time_frequency', 'str', '1.1',
                "The time frequency of the coupling (e.g. 1 hour)"),
            ('variable', 'str', '1.1',
                "The variable being coupled (e.g. 10 metre wind)"),
            ]
    }


def topic():
    """An organized collection of details upon a specific topic, e.g.
    model key properties.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'science.realm'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '0.1',
                "A description (derived from specialization)."),
            ('keywords', 'str', '0.N',
                "Keywords to help re-use and discovery of this information."),
            ('name', 'str', '0.1',
                "A short-name / key (derived from specialization)."),
            ('overview', 'str', '0.1',
                "An overview of topic being described."),
            ('properties', 'science.topic_property', '0.N',
                "Set of associated specialized properties."),
            ('property_sets', 'science.topic_property_set', '0.N',
                "Grouped specialized properties."),
            ('qc_status', 'int', '0.1',
                "Quality control status of topic."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for providing this information."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ('sub_topics', 'science.topic', '0.N',
                "Discrete sub-topic with details."),
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
            ('description', 'str', '0.1',
                "User friendly description (derived from specialization)."),
            ('name', 'str', '0.1',
                "A short-name / key (derived from specialization)."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ('values', 'str', '1.N',
                "User value(s)."),
            ]
    }


def topic_property_set():
    """Provides specific details related to a topic (i.e. process, sub-
    process, grid, key properties, etc).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "A description (derived from specialization)."),
            ('name', 'str', '0.1',
                "A short-name / key (derived from specialization)."),
            ('properties', 'science.topic_property', '1.N',
                "Set of associated specialized properties."),
            ('specialization_id', 'str', '0.1',
                "Specialization identifier (derived from specialization)."),
            ]
    }




