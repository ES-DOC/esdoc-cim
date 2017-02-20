
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_shared_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def citation():
    """An academic reference to published work.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('abstract', 'str', '0.1',
                "Abstract providing high level reference overview."),
            ('citation_detail', 'str', '0.1',
                "Complete citation string as would appear in a bibliography."),
            ('collective_title', 'str', '0.1',
                "Citation collective title, i.e. with all authors declared."),
            ('context', 'str', '0.1',
                "Brief text description of why this resource is being cited."),
            ('doi', 'str', '0.1',
                "Digital Object Identifier, if it exists."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('title', 'str', '0.1',
                "Citation short title."),
            ('type', 'str', '0.1',
                "Citation type."),
            ('url', 'shared.online_resource', '0.1',
                "Location of electronic version."),
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
            ('author', 'shared.party', '0.1',
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
            ('canonical_name', 'str', '0.1',
                "Canonical name given to document."),
            ('constraint_vocabulary', 'str', '0.1',
                "A constraint vocabulary for the relationship."),
            ('context', 'str', '0.1',
                "Information about remote record in context of reference."),
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('external_id', 'str', '0.1',
                "External identifier of remote resource, if known."),
            ('further_info', 'str', '0.1',
                "A further piece of information used in ad-hoc contexts."),
            ('id', 'str', '0.1',
                "Identifier of remote resource, if known."),
            ('institute', 'str', '0.1',
                "Canonical institute name of referenced document."),
            ('linkage', 'str', '0.1',
                "A URL."),
            ('name', 'str', '0.1',
                "A user friendly name given to document."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage."),
            ('relationship', 'str', '0.1',
                "Relationship of the object target as seen from the subject resource."),
            ('type', 'str', '0.1',
                "The type of remote document."),
            ('url', 'str', '0.1',
                "The URL of the remote document."),
            ('version', 'int', '0.1',
                "The version of the remote document."),
            ]
    }


def extra_attribute():
    """An extra attribute with key and value needed to encode further information
    not in the CIM2 domain model or specialisation. Typical use case: in parsing
    data and encoding attributes found in data.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('doc', 'str', '0.1',
                "Documentation associated with this key."),
            ('key', 'str', '1.1',
                "Name of attribute."),
            ('type', 'str', '0.1',
                "If a non-string type, provide type."),
            ('value', 'str', '1.1',
                "Value associated with key."),
            ]
    }


def online_resource():
    """A minimal approximation of ISO19115 CI_ONLINERESOURCE, provides a link and details
    of how to use that link.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('linkage', 'str', '1.1',
                "A URL."),
            ('name', 'str', '1.1',
                "Name of online resource."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage."),
            ]
    }


def party():
    """Implements minimal material for an ISO19115-1 (2014) compliant party.
    For our purposes this is a much better animal than the previous responsibleParty 
    which munged roles together with people. Note we have collapsed CI_Contact,
    CI_Individual and CI_Organisation as well as the abstract CI_Party.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('address', 'str', '0.1',
                "Institutional address."),
            ('email', 'str', '0.1',
                "Email address."),
            ('is_organisation', 'bool', '0.1',
                "True if an organisation not a person."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '0.1',
                "Name of person or organisation."),
            ('orcid_id', 'str', '0.1',
                "Orcid ID if available."),
            ('url', 'shared.online_resource', '0.1',
                "URL of person or institution."),
            ]
    }


def quality_review():
    """Assertions as to the completeness and quality of a document.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('date', 'str', '1.1',
                "Date upon which review was made."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('metadata_reviewer', 'shared.party', '1.1',
                "Party who made the metadata quality assessment."),
            ('quality_description', 'str', '1.1',
                "Assessment of quality of target document."),
            ('quality_status', 'shared.quality_status', '0.1',
                "Status from a controlled vocabulary."),
            ('target_document', 'shared.doc_reference', '1.1',
                "This is the document about which quality is asserted."),
            ]
    }


def responsibility():
    """Implements the ISO19115-1 (2014) CI_Responsibility (which replaces
    responsibleParty). Combines a person and their role in doing something.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('parties', 'shared.party', '1.N',
                "Parties delivering responsibility."),
            ('role', 'shared.role_code', '1.1',
                "Role that the party plays or played."),
            ('when', 'time.time_period', '0.1',
                "Period when role was active, if no longer."),
            ]
    }


def text_blob():
    """Provides a text class which supports plaintext, html, and
    friends (or will do).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('content', 'str', '1.1',
                "Raw content (including markup)."),
            ('encoding', 'shared.text_blob_encoding', '1.1',
                "Content encoding."),
            ]
    }




