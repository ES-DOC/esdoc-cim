
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.extended_schema_for_software_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def component():
	"""A SofwareComponent is an abstract component from which all other components derive. It represents an element that takes input data and generates output data. A SoftwareCompnent can include nested "child" components. Every component can have "componentProperties" which describe the scientific properties that a component simulates (for example, temperature, pressure, etc.) and the numerical properties that influence how a component performs its simulation (for example, the force of gravity). A SoftwareComponent can also have a Deployment, which describes how software is deployed onto computing resources. And a SoftwareComponent can have a composition, which describes how ComponentProperties are coupled together either to/from other SoftwareComponents or external data files. The properties specified by a component's composition must be owned by that component or a child of that component; child components cannot couple together their parents' properties.

	"""
    return {
        'type': 'class',
        'base': "shared.data_source",
        'base-hierarchy': [
            'shared.data_source'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'software.model_component',
            'software.processor_component',
            'software.statistical_model_component'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                ""),
            ('code_access', 'str', '0.1',
                "Instructions on how to access the source code for this component."),
            ('composition', 'software.composition', '0.1',
                ""),
            ('coupling_framework', 'software.coupling_framework_type', '0.1',
                "The coupling framework that this entire component conforms to."),
            ('dependencies', 'software.entry_point', '0.N',
                ""),
            ('deployments', 'software.deployment', '0.N',
                ""),
            ('description', 'str', '0.1',
                "A free-text description of the component."),
            ('funding_sources', 'str', '0.N',
                "The entities that funded this software component."),
            ('grid', 'grids.grid_spec', '0.1',
                "A reference to the grid that is used by this component."),
            ('is_embedded', 'bool', '0.1',
                "An embedded component cannot exist on its own as an atomic piece of software; instead it is embedded within another (parent) component. When embedded equals "true", the SoftwareComponent has a corresponding piece of software (otherwise it is acting as a "virtual" component which may be inexorably nested within a piece of software along with several other virtual components)."),
            ('language', 'software.component_language', '0.1',
                ""),
            ('license', 'shared.license', '0.1',
                "The license held by this piece of software."),
            ('long_name', 'str', '0.1',
                "The name of the model (that is recognized externally)."),
            ('online_resource', 'uri', '0.1',
                "Provides a URL location for this model."),
            ('parent', 'software.component', '0.1',
                ""),
            ('previous_version', 'str', '0.1',
                ""),
            ('properties', 'software.component_property', '0.N',
                "The properties that this model simulates and/or couples."),
            ('release_date', 'datetime', '0.1',
                "The date of publication of the software component code (as opposed to the date of publication of the metadata document, or the date of deployment of the model)"),
            ('responsible_parties', 'shared.responsible_party', '0.N',
                ""),
            ('short_name', 'str', '1.1',
                "The name of the model (that is used internally)."),
            ('sub_components', 'software.component', '0.N',
                ""),
            ('version', 'str', '0.1',
                "A free text description of the component version #."),
            ],
        'properties-all': [
            'citations',
            'code_access',
            'composition',
            'coupling_framework',
            'dependencies',
            'deployments',
            'description',
            'funding_sources',
            'grid',
            'is_embedded',
            'language',
            'license',
            'long_name',
            'online_resource',
            'parent',
            'previous_version',
            'properties',
            'purpose',
            'release_date',
            'responsible_parties',
            'short_name',
            'sub_components',
            'version',
            ],
        'properties-inherited': [
            'purpose :: shared.data_source',
            ]
    }


def component_language():
	"""Details of the programming language a component is written in. There is an assumption that all EntryPoints use the same ComponentLanguage.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('name', 'str', '1.1',
                "The name of the language."),
            ('properties', 'software.component_language_property', '0.N',
                ""),
            ]
    }


def component_language_property():
	"""This provides a place to include language-specific information. Every property is basically a name/value pair, where the names are things like: moduleName, reservedUnits, reservedNames (these are all examples of Fortran-specific properties).

	"""
    return {
        'type': 'class',
        'base': "shared.property",
        'base-hierarchy': [
            'shared.property'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'name',
            'value',
            ],
        'properties-inherited': [
            'name :: shared.property',
            'value :: shared.property',
            ]
    }


def component_property():
	"""ComponentProperties include things that a component simulates (ie: pressure, humidity) and things that prescribe that simulation (ie: gravity, choice of advection scheme). Note that this is a specialisation of shared::DataSource. data::DataObject is also a specialisation of shared::DataSource. This allows software::Connections and/or activity::Conformance to refer to either ComponentProperties or DataObjects.

	"""
    return {
        'type': 'class',
        'base': "shared.data_source",
        'base-hierarchy': [
            'shared.data_source'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('citations', 'shared.citation', '0.N',
                ""),
            ('description', 'str', '0.1',
                ""),
            ('grid', 'str', '0.1',
                "A reference to the grid that is used by this component."),
            ('intent', 'software.component_property_intent_type', '0.1',
                "The direction that this property is intended to be coupled: in, out, or inout."),
            ('is_represented', 'bool', '1.1',
                "When set to false, means that this property is not used by the component. Covers the case when, for instance, a modeler chooses not to represent some property in their model. (But still allows meaningful comparisons between components which _do_ model this property.)"),
            ('long_name', 'str', '0.1',
                ""),
            ('short_name', 'str', '1.1',
                ""),
            ('standard_names', 'str', '0.N',
                ""),
            ('sub_properties', 'software.component_property', '0.N',
                ""),
            ('units', 'shared.unit_type', '0.1',
                "The standard name that this property is known as (for example, its CF name)."),
            ('values', 'str', '0.N',
                "The value of the property (not applicable to fields)."),
            ],
        'properties-all': [
            'citations',
            'description',
            'grid',
            'intent',
            'is_represented',
            'long_name',
            'purpose',
            'short_name',
            'standard_names',
            'sub_properties',
            'units',
            'values',
            ],
        'properties-inherited': [
            'purpose :: shared.data_source',
            ]
    }


def composition():
	"""The set of Couplings used by a Component. Couplings can only occur between child components. That is, a composition must belong to an ancestor component of the components whose fields are being connected.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('couplings', 'str', '0.N',
                ""),
            ('description', 'str', '0.1',
                ""),
            ]
    }


def connection():
	"""A Connection represents a link from a source DataSource to a target DataSource.  These can either be ComponentProperties (ie: the values come from an internal component) or DataObjects (ie: the values come from an external file).   It can be associated with another software component (a transformer).  If present, the rate, lag, timeTransformation, and spatialRegridding override that of the parent coupling.  Note that there is the potential for multiple connectionSource & connectionTarget and multiple couplingSources & couplingTargets.  This may lead users to wonder how to match up a connection source (a ComponentProperty) with its coupling source (a SoftwareComponent). Clever logic is not required though; because the sources and targets are listed by reference, they can be found in a CIM document and the parent can be navigated to from there - there is no need to consult the source or target of the coupling.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('priming', 'shared.data_source', '0.1',
                "A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created."),
            ('properties', 'software.connection_property', '0.N',
                ""),
            ('sources', 'software.connection_endpoint', '0.N',
                "The source property being connected.  (note that there can be multiple sources)  This is optional; the file/component source may have already been specified by the couplingSource."),
            ('spatial_regridding', 'software.spatial_regridding', '0.N',
                "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)"),
            ('target', 'software.connection_endpoint', '0.1',
                "The target property being connected.  This is optional to support the way that input is handled in the CMIP5 questionnaire."),
            ('time_lag', 'str', '0.1',
                "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time."),
            ('time_profile', 'software.timing', '0.1',
                "All information having to do with the rate of this connection; the times that it is active.  This overrides any rate of a Coupling."),
            ('time_transformation', 'software.time_transformation', '0.1',
                "Temporal transformation performed on the coupling field before or after regridding onto the target grid."),
            ('transformers', 'software.processor_component', '0.N',
                "An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here."),
            ('type', 'software.connection_type', '0.1',
                "The type of Connection"),
            ]
    }


def connection_endpoint():
	"""The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('data_source', 'shared.data_source', '0.1',
                ""),
            ('instance_id', 'str', '0.1',
                "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG)."),
            ('properties', 'software.connection_property', '0.N',
                "The place to describe features specific to the source/target of a connection."),
            ]
    }


def connection_property():
	"""A ConnectionProperty is a name/value pair used to specify OASIS-specific properties.

	"""
    return {
        'type': 'class',
        'base': "shared.property",
        'base-hierarchy': [
            'shared.property'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'name',
            'value',
            ],
        'properties-inherited': [
            'name :: shared.property',
            'value :: shared.property',
            ]
    }


def coupling():
	"""A coupling represents a set of Connections between a source and target component. Couplings can be complete or incomplete. If they are complete then they must include all Connections between model properties. If they are incomplete then the connections can be underspecified or not listed at all.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('connections', 'software.connection', '0.N',
                ""),
            ('description', 'str', '0.1',
                "A free-text description of the coupling."),
            ('is_fully_specified', 'bool', '1.1',
                "If true then the coupling is fully-specified.  If false then not every Connection has been described within the coupling."),
            ('priming', 'shared.data_source', '0.1',
                "A priming source is one that is active on the first available timestep only (before "proper" coupling can ocurr). It can either be described here explicitly, or else a separate coupling/connection with a timing profile that is active on only the first timestep can be created."),
            ('properties', 'software.coupling_property', '0.N',
                ""),
            ('purpose', 'shared.data_purpose', '1.1',
                ""),
            ('sources', 'software.coupling_endpoint', '1.N',
                "The source component of the coupling. (note that there can be multiple sources)."),
            ('spatial_regriddings', 'software.spatial_regridding', '0.N',
                "Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid)."),
            ('target', 'software.coupling_endpoint', '1.1',
                "The target component of the coupling."),
            ('time_lag', 'software.time_lag', '0.1',
                "The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time."),
            ('time_profile', 'software.timing', '0.1',
                "Describes how often the coupling takes place."),
            ('time_transformation', 'software.time_transformation', '0.1',
                "Temporal transformation performed on the coupling field before or after regridding onto the target grid."),
            ('transformers', 'software.processor_component', '0.N',
                "An "in-line" transformer. This references a fully-described transformer (typically that forms part of the top-level composition) used in the context of this coupling. It is used instead of separately specifying a spatialRegridding, timeTransformation, etc. here."),
            ('type', 'software.connection_type', '0.1',
                "Describes the method of coupling."),
            ]
    }


def coupling_endpoint():
	"""The source/target of a coupling.  This is a DataSource (a SoftwareComponent or DataObject).  This is a separate class in order to associate an instanceID with the DataSource; this is used to identify which particular instance is being coupled in case the same DataSource is used more than once in a coupled model (this may be required for BFG).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('data_source', 'shared.data_source', '0.1',
                ""),
            ('instance_id', 'str', '0.1',
                "If the same datasource is used more than once in a coupled model then a method for identifying which particular instance is being referenced is needed (for BFG)."),
            ('properties', 'software.coupling_property', '0.N',
                "A place to describe features specific to the source/target of a coupling"),
            ]
    }


def coupling_property():
	"""A CouplingProperty is a name/value pair used to specify OASIS-specific properties.

	"""
    return {
        'type': 'class',
        'base': "shared.property",
        'base-hierarchy': [
            'shared.property'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'name',
            'value',
            ],
        'properties-inherited': [
            'name :: shared.property',
            'value :: shared.property',
            ]
    }


def deployment():
	"""Gives information about the technical properties of a component: what machine it was run on, which compilers were used, how it was parallised, etc. A deployment basically associates a deploymentDate with a Platform. A deployment only exists if something has been deployed. A platform, in contrast, can exist independently, waiting to be used in deployments.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('deployment_date', 'datetime', '0.1',
                ""),
            ('description', 'str', '0.1',
                ""),
            ('executable_arguments', 'str', '0.N',
                ""),
            ('executable_name', 'str', '0.1',
                ""),
            ('parallelisation', 'software.parallelisation', '0.1',
                ""),
            ('platform', 'shared.platform', '0.1',
                "The platform that this deployment has been run on. It is optional to allow for "unconfigured" models, that nonetheless specify their parallelisation constraints (a feature needed by OASIS)."),
            ]
    }


def entry_point():
	"""Describes a function or subroutine of a SoftwareComponent. BFG will use these EntryPoints to define a schedule of subroutine calls for a coupled model. Currently, a very basic schedule can be approximated by using the "proceeds" and "follows" attributes, however a more complete system is required for full BFG compatibility. Every EntryPoint can have a set of arguments associated with it. These reference (previously defined) ComponentProperties.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('name', 'str', '0.1',
                ""),
            ]
    }


def model_component():
	"""A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

	"""
    return {
        'type': 'class',
        'base': "software.component",
        'base-hierarchy': [
            'software.component',
            'shared.data_source'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('activity', 'activity.activity', '0.1',
                ""),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('timing', 'software.timing', '0.1',
                "Describes information about how this component simulates time."),
            ('type', 'software.model_component_type', '0.1',
                "Describes the type of component. There can be multiple types."),
            ('types', 'software.model_component_type', '1.N',
                "Describes the type of component. There can be multiple types."),
            ],
        'properties-all': [
            'activity',
            'citations',
            'code_access',
            'composition',
            'coupling_framework',
            'dependencies',
            'deployments',
            'description',
            'funding_sources',
            'grid',
            'is_embedded',
            'language',
            'license',
            'long_name',
            'meta',
            'online_resource',
            'parent',
            'previous_version',
            'properties',
            'purpose',
            'release_date',
            'responsible_parties',
            'short_name',
            'sub_components',
            'timing',
            'type',
            'types',
            'version',
            ],
        'properties-inherited': [
            'citations :: software.component',
            'code_access :: software.component',
            'composition :: software.component',
            'coupling_framework :: software.component',
            'dependencies :: software.component',
            'deployments :: software.component',
            'description :: software.component',
            'funding_sources :: software.component',
            'grid :: software.component',
            'is_embedded :: software.component',
            'language :: software.component',
            'license :: software.component',
            'long_name :: software.component',
            'online_resource :: software.component',
            'parent :: software.component',
            'previous_version :: software.component',
            'properties :: software.component',
            'purpose :: shared.data_source',
            'release_date :: software.component',
            'responsible_parties :: software.component',
            'short_name :: software.component',
            'sub_components :: software.component',
            'version :: software.component',
            ]
    }


def parallelisation():
	"""Describes how a deployment has been parallelised across a computing platform.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('processes', 'int', '1.1',
                ""),
            ('ranks', 'software.rank', '0.N',
                ""),
            ]
    }


def processor_component():
	"""A ModelComponent is a scientific model; it represents code which models some physical phenomena for a particular length of time.

	"""
    return {
        'type': 'class',
        'base': "software.component",
        'base-hierarchy': [
            'software.component',
            'shared.data_source'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ],
        'properties-all': [
            'citations',
            'code_access',
            'composition',
            'coupling_framework',
            'dependencies',
            'deployments',
            'description',
            'funding_sources',
            'grid',
            'is_embedded',
            'language',
            'license',
            'long_name',
            'meta',
            'online_resource',
            'parent',
            'previous_version',
            'properties',
            'purpose',
            'release_date',
            'responsible_parties',
            'short_name',
            'sub_components',
            'version',
            ],
        'properties-inherited': [
            'citations :: software.component',
            'code_access :: software.component',
            'composition :: software.component',
            'coupling_framework :: software.component',
            'dependencies :: software.component',
            'deployments :: software.component',
            'description :: software.component',
            'funding_sources :: software.component',
            'grid :: software.component',
            'is_embedded :: software.component',
            'language :: software.component',
            'license :: software.component',
            'long_name :: software.component',
            'online_resource :: software.component',
            'parent :: software.component',
            'previous_version :: software.component',
            'properties :: software.component',
            'purpose :: shared.data_source',
            'release_date :: software.component',
            'responsible_parties :: software.component',
            'short_name :: software.component',
            'sub_components :: software.component',
            'version :: software.component',
            ]
    }


def rank():
	"""Creates and returns instance of rank class.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('increment', 'int', '0.1',
                ""),
            ('max', 'int', '0.1',
                ""),
            ('min', 'int', '0.1',
                ""),
            ('value', 'int', '0.1',
                ""),
            ]
    }


def spatial_regridding():
	"""Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('dimension', 'software.spatial_regridding_dimension_type', '0.1',
                ""),
            ('properties', 'software.spatial_regridding_property', '0.N',
                ""),
            ('standard_method', 'software.spatial_regridding_standard_method_type', '0.1',
                ""),
            ('user_method', 'software.spatial_regridding_user_method', '0.1',
                ""),
            ]
    }


def spatial_regridding_property():
	"""Used for OASIS-specific regridding information (ie: masked, order, normalisation, etc.)

	"""
    return {
        'type': 'class',
        'base': "shared.property",
        'base-hierarchy': [
            'shared.property'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'name',
            'value',
            ],
        'properties-inherited': [
            'name :: shared.property',
            'value :: shared.property',
            ]
    }


def spatial_regridding_user_method():
	"""Characteristics of the scheme used to interpolate a field from one grid (source grid) to another (target grid).  Documents should use either the spatialRegriddingStandardMethod _or_ the spatialRegriddingUserMethod, but not both.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('file', 'data.data_object', '0.1',
                ""),
            ('name', 'str', '1.1',
                ""),
            ]
    }


def statistical_model_component():
	"""Creates and returns instance of statistical_model_component class.

	"""
    return {
        'type': 'class',
        'base': "software.component",
        'base-hierarchy': [
            'software.component',
            'shared.data_source'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('timing', 'software.timing', '0.1',
                "Describes information about how this component simulates time."),
            ('type', 'software.statistical_model_component_type', '0.1',
                "Describes the type of component. There can be multiple types."),
            ('types', 'software.statistical_model_component_type', '1.N',
                "Describes the type of component. There can be multiple types."),
            ],
        'properties-all': [
            'citations',
            'code_access',
            'composition',
            'coupling_framework',
            'dependencies',
            'deployments',
            'description',
            'funding_sources',
            'grid',
            'is_embedded',
            'language',
            'license',
            'long_name',
            'meta',
            'online_resource',
            'parent',
            'previous_version',
            'properties',
            'purpose',
            'release_date',
            'responsible_parties',
            'short_name',
            'sub_components',
            'timing',
            'type',
            'types',
            'version',
            ],
        'properties-inherited': [
            'citations :: software.component',
            'code_access :: software.component',
            'composition :: software.component',
            'coupling_framework :: software.component',
            'dependencies :: software.component',
            'deployments :: software.component',
            'description :: software.component',
            'funding_sources :: software.component',
            'grid :: software.component',
            'is_embedded :: software.component',
            'language :: software.component',
            'license :: software.component',
            'long_name :: software.component',
            'online_resource :: software.component',
            'parent :: software.component',
            'previous_version :: software.component',
            'properties :: software.component',
            'purpose :: shared.data_source',
            'release_date :: software.component',
            'responsible_parties :: software.component',
            'short_name :: software.component',
            'sub_components :: software.component',
            'version :: software.component',
            ]
    }


def time_lag():
	"""The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('units', 'software.timing_units', '0.1',
                ""),
            ('value', 'int', '0.1',
                ""),
            ]
    }


def time_transformation():
	"""The coupling field used in the target at a given time corresponds to a field produced by the source at a previous time. This lag specifies the difference in time.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('mapping_type', 'software.time_mapping_type', '1.1',
                ""),
            ]
    }


def timing():
	"""Provides information about the rate of couplings and connections and/or the timing characteristics of individual components - for example, the start and stop times that the component was run for or the units of time that a component is able to model (in a single timestep).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('end', 'datetime', '0.1',
                ""),
            ('is_variable_rate', 'bool', '0.1',
                "Describes whether or not the model supports a variable timestep. If set to true, then rate should not be specified."),
            ('rate', 'int', '0.1',
                ""),
            ('start', 'datetime', '0.1',
                ""),
            ('units', 'software.timing_units', '0.1',
                ""),
            ]
    }




