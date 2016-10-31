
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_science_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def conservation_properties():
	"""Describes how prognostic variables are conserved.

	"""
    return {
        'type': 'class',
        'base': "science.sub_process",
        'base-hierarchy': [
            'science.sub_process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('corrected_conserved_prognostic_variables', 'data.variable_collection', '0.1',
                "Set of variables which are conserved by *more* than the numerical scheme alone."),
            ('description', 'str', '1.1',
                "Brief description of conservation methodology"),
            ('flux_correction_was_used', 'bool', '0.1',
                "Flag to indicate if correction involved flux correction."),
            ],
        'properties-all': [
            'citations',
            'corrected_conserved_prognostic_variables',
            'description',
            'description',
            'details',
            'flux_correction_was_used',
            'id',
            'implementation_overview',
            'short_name',
            ],
        'properties-inherited': [
            'citations :: science.sub_process',
            'description :: science.science_context',
            'details :: science.sub_process',
            'id :: science.science_context',
            'implementation_overview :: science.sub_process',
            'short_name :: science.science_context',
            ]
    }


def detail():
	"""Provides details of specific properties of a process, sub-process,
    key properties, etc., there are two possible specialisations
    expected: (1) A detail_vocabulary is identified, and a cardinality
    is assigned to that for possible responses, or (2) Detail is used
    to provide a collection for a set of properties which are defined
    in the sub-class. However, those properties must have a type which
    is selected from the classmap (that is, standard 'non-es-doc'
    types).

	"""
    return {
        'type': 'class',
        'base': "science.science_context",
        'base-hierarchy': [
            'science.science_context'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'id',
            'short_name',
            ],
        'properties-inherited': [
            'description :: science.science_context',
            'id :: science.science_context',
            'short_name :: science.science_context',
            ]
    }


def discretisation():
	"""Collection of properties related to method of process discretisation.

	"""
    return {
        'type': 'class',
        'base': "science.sub_process",
        'base-hierarchy': [
            'science.sub_process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'citations',
            'description',
            'details',
            'id',
            'implementation_overview',
            'short_name',
            ],
        'properties-inherited': [
            'citations :: science.sub_process',
            'description :: science.science_context',
            'details :: science.sub_process',
            'id :: science.science_context',
            'implementation_overview :: science.sub_process',
            'short_name :: science.science_context',
            ]
    }


def extent():
	"""Key scientific characteristics of the grid use to simulate a
    specific domain.  Note that the extent does not itself describe a
    grid, so, for example, a polar stereographic grid may have an
    extent of northern boundary 90N, southern boundary 45N, but the
    fact that it is PS comes from the grid_type.

	"""
    return {
        'type': 'class',
        'base': "science.sub_process",
        'base-hierarchy': [
            'science.sub_process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 2,
        'sub-classes': [
            'science.iso_extent'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('is_global', 'bool', '1.1',
                "True if horizontal coverage is global."),
            ('region_known_as', 'str', '0.N',
                "Identifier(s) for the region covered by the extent."),
            ],
        'properties-all': [
            'citations',
            'description',
            'details',
            'id',
            'implementation_overview',
            'is_global',
            'region_known_as',
            'short_name',
            ],
        'properties-inherited': [
            'citations :: science.sub_process',
            'description :: science.science_context',
            'details :: science.sub_process',
            'id :: science.science_context',
            'implementation_overview :: science.sub_process',
            'short_name :: science.science_context',
            ]
    }


def grid():
	"""This describes the numerical grid used for the calculations.  It
    is not necessarily the grid upon which the data is output.  It is
    NOT the resolution, which is a property of a specific domain.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '1.1',
                "Abstract description of grid."),
            ('details', 'science.detail', '0.N',
                "Specific grid properties."),
            ('discretisation', 'science.discretisation', '0.1',
                "Description of the numerics of the discretisation."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "This is a string usually used by the modelling group to describe the overall grid.(e.g. the ENDGAME/New Dynamics dynamical cores have their own grids describing variable layouts."),
            ]
    }


def iso_extent():
	"""Extent on a latitude-longitudinal grid - to aid traditional cartesian discovery.

	"""
    return {
        'type': 'class',
        'base': "science.extent",
        'base-hierarchy': [
            'science.extent',
            'science.sub_process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 3,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('eastern_boundary', 'float', '0.1',
                "Eastern boundary in degrees of longitude."),
            ('northern_boundary', 'float', '0.1',
                "Northern boundary in degrees of latitude."),
            ('southern_boundary', 'float', '0.1',
                "Southern boundary in degrees of latitude."),
            ('western_boundary', 'float', '0.1',
                "Western boundary in degrees of longitude."),
            ],
        'properties-all': [
            'citations',
            'description',
            'details',
            'eastern_boundary',
            'id',
            'implementation_overview',
            'is_global',
            'northern_boundary',
            'region_known_as',
            'short_name',
            'southern_boundary',
            'western_boundary',
            ],
        'properties-inherited': [
            'citations :: science.sub_process',
            'description :: science.science_context',
            'details :: science.sub_process',
            'id :: science.science_context',
            'implementation_overview :: science.sub_process',
            'is_global :: science.extent',
            'region_known_as :: science.extent',
            'short_name :: science.science_context',
            ]
    }


def key_properties():
	"""High level list of key properties. It can be specialised in
    extension packages using the detail extensions.

	"""
    return {
        'type': 'class',
        'base': "science.process",
        'base-hierarchy': [
            'science.process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('extent', 'science.extent', '0.1',
                "DESCRIPTION."),
            ('extra_conservation_properties', 'science.conservation_properties', '0.1',
                "Details of methodology needed to conserve variables between processes."),
            ('resolution', 'science.resolution', '0.1',
                "The resolution of the grid (e.g. N512L180)."),
            ('time_step', 'float', '0.1',
                "Timestep (in seconds) of overall component."),
            ('tuning_applied', 'science.tuning', '0.1',
                "Describe any tuning used to optimise the parameters in this domain."),
            ],
        'properties-all': [
            'citations',
            'description',
            'details',
            'extent',
            'extra_conservation_properties',
            'id',
            'implementation_overview',
            'keywords',
            'resolution',
            'short_name',
            'sub_processes',
            'time_step',
            'tuning_applied',
            ],
        'properties-inherited': [
            'citations :: science.process',
            'description :: science.science_context',
            'details :: science.process',
            'id :: science.science_context',
            'implementation_overview :: science.process',
            'keywords :: science.process',
            'short_name :: science.science_context',
            'sub_processes :: science.process',
            ]
    }


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
            ('category', 'science.model_types', '1.1',
                "Generic type for this model."),
            ('coupled_components', 'science.model', '0.N',
                "Software components which are linked together using a coupler to deliver this model."),
            ('coupler', 'software.coupling_framework', '0.1',
                "Overarching coupling framework for model."),
            ('id', 'str', '0.1',
                "Vocabulary identifier, where this model description was constructed via a controlled vocabulary."),
            ('internal_software_components', 'software.software_component', '0.N',
                "Software modules which together provide the functionality for this model."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('model_key_properties', 'science.key_properties', '0.1',
                "Model default key properties (may be over-ridden in coupled component and scientific realm properties)."),
            ('realms', 'science.scientific_realm', '0.N',
                "The scientific realms which this model simulates internally, i.e. those which are not linked together using a coupler."),
            ],
        'properties-all': [
            'category',
            'citations',
            'coupled_components',
            'coupler',
            'description',
            'development_history',
            'id',
            'internal_software_components',
            'long_name',
            'meta',
            'model_key_properties',
            'name',
            'realms',
            'release_date',
            'repository',
            'version',
            ],
        'properties-inherited': [
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
        'base': "science.science_context",
        'base-hierarchy': [
            'science.science_context'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'science.key_properties'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('details', 'science.detail', '0.N',
                "Sets of properties for this process."),
            ('implementation_overview', 'str', '1.1',
                "General overview description of the implementation of this process."),
            ('keywords', 'str', '0.1',
                "keywords to help re-use and discovery of this information."),
            ('sub_processes', 'science.sub_process', '0.N',
                "Discrete portion of a process with common process details."),
            ],
        'properties-all': [
            'citations',
            'description',
            'details',
            'id',
            'implementation_overview',
            'keywords',
            'short_name',
            'sub_processes',
            ],
        'properties-inherited': [
            'description :: science.science_context',
            'id :: science.science_context',
            'short_name :: science.science_context',
            ]
    }


def resolution():
	"""Describes the computational spatial resolution of a component or
    process.  Not intended to replace or replicate the output grid
    description.  When it appears as part of a process description,
    provide only properties that differ from parent domain.  Note that
    this is supposed to capture gross features of the grid, we expect
    many grids will have different variable layouts, those should be
    described in the grid description, and the exact resolution is not
    required. Note that many properties are not appropriate for
    adaptive grids.

	"""
    return {
        'type': 'class',
        'base': "science.sub_process",
        'base-hierarchy': [
            'science.sub_process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('canonical_horizontal_resolution', 'str', '0.1',
                "Expression quoted for gross comparisons of resolution, eg. 50km or 0.1 degrees etc."),
            ('is_adaptive_grid', 'bool', '0.1',
                "Default is False. Set true if grid resolution changes during execution."),
            ('name', 'str', '1.1',
                "This is a string usually used by the modelling group to describe the resolution of this grid,  e.g. N512L180 or T512L70 etc."),
            ('number_of_horizontal_gridpoints', 'int', '0.1',
                "Total number of horizontal points (or degrees of freedom) on computational grid."),
            ('number_of_vertical_levels', 'int', '0.1',
                "Number of vertical levels resolved on computational grid."),
            ],
        'properties-all': [
            'canonical_horizontal_resolution',
            'citations',
            'description',
            'details',
            'id',
            'implementation_overview',
            'is_adaptive_grid',
            'name',
            'number_of_horizontal_gridpoints',
            'number_of_vertical_levels',
            'short_name',
            ],
        'properties-inherited': [
            'citations :: science.sub_process',
            'description :: science.science_context',
            'details :: science.sub_process',
            'id :: science.science_context',
            'implementation_overview :: science.sub_process',
            'short_name :: science.science_context',
            ]
    }


def science_context():
	"""This is the base class for the science mixins, that is the classes
    which we expect to be specialised and extended by project specific
    vocabularies.  It is expected that values of these will be
    provided within vocabulary definitions.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'science.conservation_properties',
            'science.detail',
            'science.discretisation',
            'science.extent',
            'science.iso_extent'
            'science.key_properties',
            'science.process',
            'science.resolution',
            'science.sub_process',
            'science.tuning',
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('description', 'str', '1.1',
                "Scientific context for which this description is provided."),
            ('id', 'str', '1.1',
                "Identifier for this collection of properties."),
            ('short_name', 'str', '1.1',
                "The name of this process/algorithm/sub-process/detail."),
            ]
    }


def scientific_realm():
	"""Scientific area of a numerical model - usually a sub-model or
    component.  Can also be known as a realm.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('grid', 'science.grid', '0.1',
                "The grid used to layout the variables (e.g. the Global ENDGAME-grid)."),
            ('id', 'str', '0.1',
                "Vocabulary identifier, where this domain description was constructed via a  controlled vocabulary."),
            ('key_properties', 'science.key_properties', '0.1',
                "Key properties for the domain which differ from model defaults (grid, timestep etc)."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "Name of the scientific domain (e.g. ocean)."),
            ('overview', 'str', '0.1',
                "Free text overview description of key properties of domain."),
            ('processes', 'science.process', '1.N',
                "Processes simulated within the domain."),
            ('realm', 'str', '0.1',
                "Canonical name for the domain of this scientific area."),
            ]
    }


def sub_process():
	"""Provides structure for description of part of process simulated
    within a particular area (or domain/realm/component) of a
    model. Typically this will be a part of process which shares
    common properties. It will normally be sub classed within a
    specific implementation so that constraints can be used to ensure
    that the process details requested are consistent with projects
    requirements for information.

	"""
    return {
        'type': 'class',
        'base': "science.science_context",
        'base-hierarchy': [
            'science.science_context'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'science.conservation_properties',
            'science.discretisation',
            'science.extent',
            'science.iso_extent'
            'science.resolution',
            'science.tuning',
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('details', 'science.detail', '0.N',
                "Sets of properties for this process."),
            ('implementation_overview', 'str', '1.1',
                "General overview description of the implementation of this part of the process."),
            ],
        'properties-all': [
            'citations',
            'description',
            'details',
            'id',
            'implementation_overview',
            'short_name',
            ],
        'properties-inherited': [
            'description :: science.science_context',
            'id :: science.science_context',
            'short_name :: science.science_context',
            ]
    }


def tuning():
	"""Method used to optimise equation parameters in model component
    (aka 'tuning').

	"""
    return {
        'type': 'class',
        'base': "science.sub_process",
        'base-hierarchy': [
            'science.sub_process',
            'science.science_context'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '1.1',
                "Brief description of tuning methodology. Include information about observational period(s) used."),
            ('global_mean_metrics_used', 'data.variable_collection', '0.1',
                "Set of metrics of the global mean state used in tuning model parameters."),
            ('regional_metrics_used', 'data.variable_collection', '0.1',
                "Which regional metrics of mean state (e.g Monsoons, tropical means etc) have been used in tuning."),
            ('trend_metrics_used', 'data.variable_collection', '0.1',
                "Which observed trend metrics have been used in tuning model parameters."),
            ],
        'properties-all': [
            'citations',
            'description',
            'description',
            'details',
            'global_mean_metrics_used',
            'id',
            'implementation_overview',
            'regional_metrics_used',
            'short_name',
            'trend_metrics_used',
            ],
        'properties-inherited': [
            'citations :: science.sub_process',
            'description :: science.science_context',
            'details :: science.sub_process',
            'id :: science.science_context',
            'implementation_overview :: science.sub_process',
            'short_name :: science.science_context',
            ]
    }




