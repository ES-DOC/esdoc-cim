
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.extended_schema_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def calendar():
	"""Describes a method of calculating a span of dates.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'shared.daily_360',
            'shared.perpetual_period',
            'shared.real_calendar'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "Describes the finer details of the calendar, in case they are not-obvious.  For example, if an experiment has changing conditions within it (ie: 1% CO2 increase until 2100, then hold fixed for the remaining period of the  experment)"),
            ('length', 'int', '0.1',
                ""),
            ('range', 'shared.date_range', '0.1',
                ""),
            ]
    }


def change():
	"""A description of [a set of] changes applied at a particular time, by a particular party, to a particular unit of metadata.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('author', 'shared.responsible_party', '0.1',
                "The person that made the change."),
            ('date', 'datetime', '0.1',
                "The date the change was implemented."),
            ('description', 'str', '0.1',
                ""),
            ('details', 'shared.change_property', '1.N',
                ""),
            ('name', 'str', '0.1',
                "A mnemonic for describing a particular change."),
            ('type', 'shared.change_property_type', '0.1',
                ""),
            ]
    }


def change_property():
	"""A description of a single change applied to a single target.  Every ChangeProperty has a description, and may also have a name from a controlled vocabulary and a value.

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
            ('description', 'str', '0.1',
                "A text description of the change.  May be used in addition to, or instead of, the more formal description provided by the "value" attribute."),
            ('id', 'str', '0.1',
                ""),
            ],
        'properties-all': [
            'description',
            'id',
            'name',
            'value',
            ],
        'properties-inherited': [
            'name :: shared.property',
            'value :: shared.property',
            ]
    }


def citation():
	"""An academic reference to published work.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('alternative_title', 'str', '0.1',
                ""),
            ('collective_title', 'str', '0.1',
                ""),
            ('date', 'datetime', '0.1',
                ""),
            ('date_type', 'str', '0.1',
                ""),
            ('location', 'str', '0.1',
                ""),
            ('organisation', 'str', '0.1',
                ""),
            ('role', 'str', '0.1',
                ""),
            ('title', 'str', '0.1',
                ""),
            ('type', 'str', '0.1',
                ""),
            ]
    }


def closed_date_range():
	"""A date range with specified start and end points.

	"""
    return {
        'type': 'class',
        'base': "shared.date_range",
        'base-hierarchy': [
            'shared.date_range'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('end', 'datetime', '0.1',
                "End date is optional becuase the length of a ClosedDateRange can be calculated from the StartDate plus the Duration element."),
            ('start', 'datetime', '1.1',
                ""),
            ],
        'properties-all': [
            'duration',
            'end',
            'start',
            ],
        'properties-inherited': [
            'duration :: shared.date_range',
            ]
    }


def compiler():
	"""A description of a compiler used on a particular platform.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('environment_variables', 'str', '0.1',
                "The set of environment_variables used during compilation (recorded here as a single string rather than separate elements)"),
            ('language', 'str', '0.1',
                ""),
            ('name', 'str', '1.1',
                ""),
            ('options', 'str', '0.1',
                "The set of options used during compilation (recorded here as a single string rather than separate elements)"),
            ('type', 'shared.compiler_type', '0.1',
                ""),
            ('version', 'str', '1.1',
                ""),
            ]
    }


def daily_360():
	"""Creates and returns instance of daily_360 class.

	"""
    return {
        'type': 'class',
        'base': "shared.calendar",
        'base-hierarchy': [
            'shared.calendar'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'length',
            'range',
            ],
        'properties-inherited': [
            'description :: shared.calendar',
            'length :: shared.calendar',
            'range :: shared.calendar',
            ]
    }


def data_source():
	"""A DataSource can be realised by either a DataObject (file), a DataContent (variable), a Component (model), or a ComponentProperty (variable); all of those can supply data.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'software.component',
            'software.component_property',
            'data.data_content',
            'data.data_object',
            'software.model_component',
            'software.processor_component',
            'software.statistical_model_component'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('purpose', 'shared.data_purpose', '0.1',
                ""),
            ]
    }


def date_range():
	"""Creates and returns instance of date_range class.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'shared.closed_date_range',
            'shared.open_date_range'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('duration', 'str', '0.1',
                ""),
            ]
    }


def doc_meta_info():
	"""Encapsulates document meta information used by es-doc machinery. Will not normally be
    populated by humans. May duplicate information held in 'visible' metadata.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('author', 'shared.responsible_party', '0.1',
                "Author of the metadata in the parent document."),
            ('create_date', 'datetime', '1.1',
                "Date upon which the instance was created."),
            ('drs_keys', 'str', '0.N',
                "DRS related keys to support correlation of documents with datasets."),
            ('drs_path', 'str', '0.1',
                "DRS related path to support documents with datasets."),
            ('external_ids', 'str', '0.N',
                "Set of identifiers used to reference the document by external parties."),
            ('id', 'str', '1.1',
                "Universal document identifier (must be a valid UUID)."),
            ('institute', 'str', '0.1',
                "Name of institute with which instance is associated."),
            ('project', 'str', '0.1',
                "Name of project with which instance is associated."),
            ('sort_key', 'str', '0.1',
                "Document sort key."),
            ('source', 'str', '1.1',
                "Name of application that created the instance."),
            ('source_key', 'str', '0.1',
                "Key of application that created the instance."),
            ('sub_projects', 'str', '0.N',
                "Set of sub-projects with which instance is associated."),
            ('type', 'str', '1.1',
                "Document ontology type key."),
            ('type_display_name', 'str', '0.1',
                "Document type display name."),
            ('type_sort_key', 'str', '0.1',
                "Document type sort key."),
            ('update_date', 'datetime', '0.1',
                "Date upon which the instance was last updated."),
            ('version', 'int', '1.1',
                "Document version identifier."),
            ]
    }


def doc_reference():
	"""A reference to another cim entity.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('changes', 'shared.change', '0.N',
                "An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances."),
            ('constraint_vocabulary', 'str', '0.1',
                "A constraint vocabulary for the relationship."),
            ('context', 'str', '0.1',
                "Information about remote record in context of reference."),
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('external_id', 'str', '0.1',
                "External identifier of remote resource, if known."),
            ('id', 'str', '0.1',
                "Identifier of remote resource, if known."),
            ('institute', 'str', '0.1',
                "Canonical institute name of referenced document."),
            ('linkage', 'str', '1.1',
                "A URL."),
            ('name', 'str', '1.1',
                "Name of online resource."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage."),
            ('relationship', 'str', '0.1',
                "Predicate - relationship of the object target as seen from the subject resource."),
            ('type', 'str', '1.1',
                "The type of remote document."),
            ('url', 'str', '0.1',
                "The URL of the remote document."),
            ('version', 'int', '0.1',
                "The version of the remote document."),
            ]
    }


def license():
	"""A description of a license restricting access to a unit of data or software.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('contact', 'str', '0.1',
                "The point of contact for access to this artifact; may be either a person or an institution."),
            ('description', 'str', '0.1',
                "A textual description of the license; might be the full text of the license, more likely to be a brief summary"),
            ('is_unrestricted', 'bool', '0.1',
                "If unrestricted="true" then the artifact can be downloaded with no restrictions (ie: there are no administrative steps for the user to deal with; code or data can be downloaded and used directly)."),
            ('name', 'str', '0.1',
                "The name that the license goes by (ie: "GPL")"),
            ]
    }


def machine():
	"""A description of a machine used by a particular platform.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('cores_per_processor', 'int', '0.1',
                ""),
            ('description', 'str', '0.1',
                ""),
            ('interconnect', 'shared.interconnect_type', '0.1',
                ""),
            ('libraries', 'str', '0.N',
                "The libraries residing on this machine."),
            ('location', 'str', '0.1',
                ""),
            ('maximum_processors', 'int', '0.1',
                ""),
            ('name', 'str', '1.1',
                ""),
            ('operating_system', 'shared.operating_system_type', '0.1',
                ""),
            ('processor_type', 'shared.processor_type', '0.1',
                ""),
            ('system', 'str', '0.1',
                ""),
            ('type', 'shared.machine_type', '0.1',
                ""),
            ('vendor', 'shared.machine_vendor_type', '0.1',
                ""),
            ]
    }


def machine_compiler_unit():
	"""Associates a machine with a [set of] compilers.  This is a separate class in case a platform needs to specify more than one machine/compiler pair.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('compilers', 'shared.compiler', '0.N',
                ""),
            ('machine', 'shared.machine', '1.1',
                ""),
            ]
    }


def open_date_range():
	"""A date range without a specified start and/or end point.

	"""
    return {
        'type': 'class',
        'base': "shared.date_range",
        'base-hierarchy': [
            'shared.date_range'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('end', 'datetime', '0.1',
                ""),
            ('start', 'datetime', '0.1',
                ""),
            ],
        'properties-all': [
            'duration',
            'end',
            'start',
            ],
        'properties-inherited': [
            'duration :: shared.date_range',
            ]
    }


def perpetual_period():
	"""Creates and returns instance of perpetual_period class.

	"""
    return {
        'type': 'class',
        'base': "shared.calendar",
        'base-hierarchy': [
            'shared.calendar'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'length',
            'range',
            ],
        'properties-inherited': [
            'description :: shared.calendar',
            'length :: shared.calendar',
            'range :: shared.calendar',
            ]
    }


def platform():
	"""A platform is a description of resources used to deploy a component/simulation.  A platform pairs a machine with a (set of) compilers.  There is also a point of contact for the platform.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('contacts', 'shared.responsible_party', '0.N',
                ""),
            ('description', 'str', '0.1',
                ""),
            ('long_name', 'str', '0.1',
                ""),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('short_name', 'str', '1.1',
                ""),
            ('units', 'shared.machine_compiler_unit', '1.N',
                ""),
            ]
    }


def property():
	"""A simple name/value pair representing a property of some entity or other.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'shared.change_property',
            'software.component_language_property',
            'software.connection_property',
            'software.coupling_property',
            'data.data_property',
            'grids.grid_property',
            'software.spatial_regridding_property'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('name', 'str', '0.1',
                ""),
            ('value', 'str', '0.1',
                ""),
            ]
    }


def real_calendar():
	"""Creates and returns instance of real_calendar class.

	"""
    return {
        'type': 'class',
        'base': "shared.calendar",
        'base-hierarchy': [
            'shared.calendar'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'length',
            'range',
            ],
        'properties-inherited': [
            'description :: shared.calendar',
            'length :: shared.calendar',
            'range :: shared.calendar',
            ]
    }


def relationship():
	"""A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document's genealogy.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'activity.experiment_relationship',
            'activity.simulation_relationship'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ]
    }


def responsible_party():
	"""A person/organsiation responsible for some aspect of a climate science artefact.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('abbreviation', 'str', '0.1',
                ""),
            ('address', 'str', '0.1',
                ""),
            ('email', 'str', '0.1',
                ""),
            ('individual_name', 'str', '0.1',
                ""),
            ('organisation_name', 'str', '0.1',
                ""),
            ('role', 'str', '0.1',
                ""),
            ('url', 'str', '0.1',
                ""),
            ]
    }


def standard():
	"""Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "The version of the standard"),
            ('name', 'str', '1.1',
                "The name of the standard"),
            ('version', 'str', '0.1',
                "The version of the standard"),
            ]
    }


def standard_name():
	"""Describes a name given to an entity from a recognised standard.  The CIM records the standard and the name.  For example, the standard might be CF and the name might be atmospheric_pressure.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('is_open', 'bool', '1.1',
                ""),
            ('standards', 'shared.standard', '0.N',
                "Details of the standard being used."),
            ('value', 'str', '1.1',
                ""),
            ]
    }




