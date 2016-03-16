# -*- coding: utf-8 -*-

"""
.. module:: shared_classes_doc.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Set of CIM v1 shared package document related class definitions.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""



def doc_relationship():
    """Contains the set of relationships supported by a Document.

    """
    return {
        'type': 'class',
        'base': 'shared.relationship',
        'is_abstract': False,
        'properties': [
            ('target', 'shared.doc_relationship_target', '1.1'),
            ('type', 'shared.doc_relationship_type', '1.1'),
        ],
        'decodings': [
            ('description', 'child::cim:description'),
            ('direction', 'self::cim:documentRelationship/@direction'),
            ('type', 'self::cim:documentRelationship/@type'),
            ('target', 'child::cim:target'),
        ]
    }


def doc_relationship_target():
    """Creates and returns instance of doc_relationship_target class.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('reference', 'shared.doc_reference', '0.1')
        ],
        'decodings': [
            ('reference', 'child::cim:reference', 'shared.doc_reference')
        ]
    }


def doc_meta_info():
    """Encapsulates document meta information.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('author', 'shared.responsible_party', '0.1'),
            ('create_date', 'datetime', '1.1'),
            ('drs_path', 'str', '0.1'),
            ('drs_keys', 'str', '0.N'),
            ('external_ids', 'shared.standard_name', '0.N'),
            ('genealogy', 'shared.doc_genealogy', '0.1'),
            ('id', 'uuid', '1.1'),
            ('institute', 'str', '0.1'),
            ('language', 'str', '1.1'),
            ('project', 'str', '1.1'),
            ('sort_key', 'str', '0.1'),
            ('source', 'str', '1.1'),
            ('source_key', 'str', '0.1'),
            ('status', 'shared.doc_status_type', '0.1'),
            ('type', 'str', '1.1'),
            ('type_display_name', 'str', '0.1'),
            ('type_sort_key', 'str', '0.1'),
            ('update_date', 'datetime', '1.1'),
            ('version', 'int', '1.1')
        ],
        'constraints': [
            ('source', 'constant', 'scripts'),
        ],
        'doc_strings': {
            'author': 'Associated document author.',
            'create_date': 'Date upon which the instance was created',
            'drs_path': 'DRS related path to support documents with datasets.',
            'drs_keys': 'DRS related keys to support correlation of documents with datasets.',
            'external_ids': 'Set of identifiers used to reference the document by external parties.',
            'genealogy': 'Specifies the relationship of this document with another document. Various relationship types (depending on the type of document; ie: simulation, component, etc.) are supported.',
            'id': 'Universal document identifier.',
            'institute': 'Name of institute with which instance is associated with.',
            'language': 'Language with which instance is associated with.',
            'project': 'Name of project with which instance is associated with.',
            'sort_key': 'Document sort key.',
            'source': 'Application that created the instance.',
            'source_key': 'Key of application that created the instance.',
            'status': "Document status.",
            'type': 'Document ontology type.',
            'type_display_name': 'Document type display name.',
            'type_sort_key': 'Document type sort key.',
            'update_date': 'Date upon which the instance was last updated',
            'version': 'Document version identifier.'
        },
        'decodings': [
            ('author', 'child::cim:documentAuthor'),
            ('create_date', 'child::cim:documentCreationDate'),
            ('external_ids', 'child::cim:externalID'),
            ('genealogy', 'child::cim:documentGenealogy'),
            ('id', 'child::cim:documentID'),
            ('update_date', 'child::cim:documentCreationDate'),
            ('version', 'child::cim:documentVersion'),
            ('version', 'self::cim:numericalExperiment/@documentVersion'),
        ]
    }


def doc_genealogy():
    """A record of a document\'s history. A genealogy element contains a textual description and a set of relationships. Each relationship has a type and a reference to some target. There are different relationships for different document types.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('relationships', 'shared.doc_relationship', '0.N'),
        ],
        'decodings': [
            ('relationships', 'child::cim:relationship/cim:documentRelationship', 'shared.doc_relationship'),
        ]
    }


def doc_reference():
    """A reference to another cim entity.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('changes', 'shared.change', '0.N'),
            ('description', 'str', '0.1'),
            ('external_id', 'str', '0.1'),
            ('id', 'uuid', '0.1'),
            ('name', 'str', '0.1'),
            ('type', 'str', '0.1'),
            ('url', 'str', '0.1'),
            ('version', 'int', '0.1'),
        ],
        'doc_strings': {
            'changes': 'An optional description of how the item being referenced has been modified.  This is particularly useful for dealing with Ensembles (a set of simulations where something about each simulation has changed) or Conformances.',
            'description': 'A description of the element being referenced, in the context of the current class.',
            'external_id': 'A non-CIM (non-GUID) id used to reference the element in question.',
            'id': 'The ID of the element being referenced.',
            'name': 'The name of the element being referenced.',
            'type': 'The type of the element being referenced.',
            'url': 'A URL associated witht he document reference.',
            'version': 'The version of the element being referenced.',
        },
        'decodings': [
            ('changes', 'child::cim:change'),
            ('description', 'child::cim:description'),
            ('external_id', 'child::cim:externalID'),
            ('id', 'child::cim:id'),
            ('name', 'child::cim:name'),
            ('type', 'child::cim:type'),
            ('version', 'child::cim:version'),
        ]
    }


def relationship():
    """A record of a relationship between one document and another. This class is abstract; specific document types must specialise this class for their relationshipTypes to be included in a document\'s genealogy.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': True,
        'properties': [
            ('description', 'str', '0.1'),
            ('direction', 'shared.doc_relationship_direction_type', '1.1'),
        ]
    }

