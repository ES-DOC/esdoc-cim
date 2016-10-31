
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.extended_schema_for_data_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def data_content():
	"""The contents of the data object; like ISO: MD_ContentInformation.

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
            ('aggregation', 'str', '0.1',
                "Describes how the content has been aggregated together: sum, min, mean, max, ..."),
            ('frequency', 'str', '0.1',
                "Describes the frequency of the data content: daily, hourly, ..."),
            ('topic', 'data.data_topic', '1.1',
                ""),
            ],
        'properties-all': [
            'aggregation',
            'frequency',
            'purpose',
            'topic',
            ],
        'properties-inherited': [
            'purpose :: shared.data_source',
            ]
    }


def data_distribution():
	"""Describes how a DataObject is distributed.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('access', 'str', '0.1',
                ""),
            ('fee', 'str', '0.1',
                ""),
            ('format', 'str', '0.1',
                ""),
            ('responsible_party', 'shared.responsible_party', '0.1',
                ""),
            ]
    }


def data_extent():
	"""A data object extent represents the geographical and temporal coverage associated with a data object.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('geographical', 'data.data_extent_geographical', '1.1',
                ""),
            ('temporal', 'data.data_extent_temporal', '1.1',
                ""),
            ]
    }


def data_extent_geographical():
	"""A data object geographical extent represents the geographical coverage associated with a data object.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('east', 'float', '0.1',
                ""),
            ('north', 'float', '0.1',
                ""),
            ('south', 'float', '0.1',
                ""),
            ('west', 'float', '0.1',
                ""),
            ]
    }


def data_extent_temporal():
	"""A data object temporal extent represents the temporal coverage associated with a data object.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('begin', 'date', '0.1',
                ""),
            ('end', 'date', '0.1',
                ""),
            ('time_interval', 'data.data_extent_time_interval', '0.1',
                ""),
            ]
    }


def data_extent_time_interval():
	"""A data object temporal extent represents the temporal coverage associated with a data object.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('factor', 'int', '0.1',
                ""),
            ('radix', 'int', '0.1',
                ""),
            ('unit', 'str', '0.1',
                ""),
            ]
    }


def data_hierarchy_level():
	"""The type of data object that is grouped together into a particular hierarchy.  Currently, this is made up of terms describing how the Met Office splits up archived data and how THREDDS categorises variables.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('is_open', 'bool', '0.1',
                ""),
            ('name', 'data.data_hierarchy_type', '0.1',
                "What level in the data hierarchy (constructed by the self-referential parent/child aggregations) is this DataObject."),
            ('value', 'str', '0.1',
                "What is the name of the specific HierarchyLevel this DataObject is being organised at (ie: if the HierarchyLevel is "run" then the name might be the runid)."),
            ]
    }


def data_object():
	"""A DataObject describes a unit of data.  DataObjects can be grouped hierarchically.  The attributes hierarchyLevelName and hierarchyLevelValue describe how objects are grouped.

	"""
    return {
        'type': 'class',
        'base': "shared.data_source",
        'base-hierarchy': [
            'shared.data_source'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('acronym', 'str', '0.1',
                ""),
            ('child_object', 'data.data_object', '0.N',
                ""),
            ('citations', 'shared.citation', '0.N',
                ""),
            ('content', 'data.data_content', '0.N',
                "The content of a DataObject corresponds to a variable (in THREDDS, ...etc.)"),
            ('data_status', 'data.data_status_type', '0.1',
                ""),
            ('description', 'str', '0.1',
                ""),
            ('distribution', 'data.data_distribution', '0.1',
                ""),
            ('extent', 'data.data_extent', '0.1',
                ""),
            ('geometry_model', 'str', '0.1',
                ""),
            ('hierarchy_level', 'data.data_hierarchy_level', '0.1',
                ""),
            ('keyword', 'str', '0.1',
                ""),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('parent_object', 'data.data_object', '0.1',
                ""),
            ('properties', 'data.data_property', '0.N',
                ""),
            ('purpose', 'str', '0.1',
                ""),
            ('restriction', 'data.data_restriction', '0.N',
                ""),
            ('source_simulation', 'str', '0.1',
                ""),
            ('storage', 'data.data_storage', '0.N',
                ""),
            ],
        'properties-all': [
            'acronym',
            'child_object',
            'citations',
            'content',
            'data_status',
            'description',
            'distribution',
            'extent',
            'geometry_model',
            'hierarchy_level',
            'keyword',
            'meta',
            'parent_object',
            'properties',
            'purpose',
            'purpose',
            'restriction',
            'source_simulation',
            'storage',
            ],
        'properties-inherited': [
            'purpose :: shared.data_source',
            ]
    }


def data_property():
	"""A property of a DataObject. Currently this is intended to be used to record CF specific information (like packing, scaling, etc.) for OASIS4.

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
                ""),
            ],
        'properties-all': [
            'description',
            'name',
            'value',
            ],
        'properties-inherited': [
            'name :: shared.property',
            'value :: shared.property',
            ]
    }


def data_restriction():
	"""An access or use restriction on some element of the DataObject actual data.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('license', 'shared.license', '0.1',
                "The thing (data or metadata, access or use) that this restriction is applied to."),
            ('restriction', 'str', '0.1',
                "The thing (data or metadata, access or use) that this restriction is applied to."),
            ('scope', 'str', '0.1',
                "The thing (data or metadata, access or use) that this restriction is applied to."),
            ]
    }


def data_storage():
	"""Describes the method that the DataObject is stored. An abstract class with specific child classes for each supported method.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'data.data_storage_db',
            'data.data_storage_file',
            'data.data_storage_ip'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('format', 'str', '0.1',
                ""),
            ('location', 'str', '0.1',
                ""),
            ('modification_date', 'datetime', '0.1',
                ""),
            ('size', 'int', '0.1',
                ""),
            ]
    }


def data_storage_db():
	"""Contains attributes to describe a DataObject stored as a database file.

	"""
    return {
        'type': 'class',
        'base': "data.data_storage",
        'base-hierarchy': [
            'data.data_storage'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('access_string', 'str', '0.1',
                ""),
            ('name', 'str', '0.1',
                ""),
            ('owner', 'str', '0.1',
                ""),
            ('table', 'str', '0.1',
                ""),
            ],
        'properties-all': [
            'access_string',
            'format',
            'location',
            'modification_date',
            'name',
            'owner',
            'size',
            'table',
            ],
        'properties-inherited': [
            'format :: data.data_storage',
            'location :: data.data_storage',
            'modification_date :: data.data_storage',
            'size :: data.data_storage',
            ]
    }


def data_storage_file():
	"""Contains attributes to describe a DataObject stored as a single file.

	"""
    return {
        'type': 'class',
        'base': "data.data_storage",
        'base-hierarchy': [
            'data.data_storage'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('file_name', 'str', '0.1',
                ""),
            ('file_system', 'str', '0.1',
                ""),
            ('path', 'str', '0.1',
                ""),
            ],
        'properties-all': [
            'file_name',
            'file_system',
            'format',
            'location',
            'modification_date',
            'path',
            'size',
            ],
        'properties-inherited': [
            'format :: data.data_storage',
            'location :: data.data_storage',
            'modification_date :: data.data_storage',
            'size :: data.data_storage',
            ]
    }


def data_storage_ip():
	"""Contains attributes to describe a DataObject stored as a database file.

	"""
    return {
        'type': 'class',
        'base': "data.data_storage",
        'base-hierarchy': [
            'data.data_storage'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('file_name', 'str', '0.1',
                ""),
            ('host', 'str', '0.1',
                ""),
            ('path', 'str', '0.1',
                ""),
            ('protocol', 'str', '0.1',
                ""),
            ],
        'properties-all': [
            'file_name',
            'format',
            'host',
            'location',
            'modification_date',
            'path',
            'protocol',
            'size',
            ],
        'properties-inherited': [
            'format :: data.data_storage',
            'location :: data.data_storage',
            'modification_date :: data.data_storage',
            'size :: data.data_storage',
            ]
    }


def data_topic():
	"""Describes the content of a data object: the variable name, units, etc.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('name', 'str', '0.1',
                ""),
            ('unit', 'str', '0.1',
                ""),
            ]
    }




