# -*- coding: utf-8 -*-

"""
.. module:: shared_classes.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def cimtext():
    """Provides a text class which supports plaintext, html, and
    friends (or will do).

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}', ('content',)),
        'properties': [
            ('content', 'str', '1.1',
                "Raw content (including markup)."),
            ('content_type', 'shared.text_code', '1.1',
                "Type of content.")
        ]
    }


def citation_target():
    """A real world document, could be a book, a journal article, a manual, a web page ... it might or might
    not be online, although preferably it would be.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'pstr': ('{}', ('name',)),
        'properties': [
            ('citation_detail', 'str', '0.1',
                "Complete citation string as would appear in a bibliography."),
            ('doi', 'str', '0.1',
                "Digital Object Identifier, if it exists."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata about the creation of this document description."),
            ('name', 'str', '1.1',
                "A name for the citation: short hand description, e.g. Meehl et al (2014)."),
            ('online_at', 'shared.online_resource', '0.1',
                "Location of electronic version."),
            ('title', 'str', '1.1',
                "Title or name of the document.")
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
                "Universal document identifier (normally a UUID)."),
            ('institute', 'str', '0.1',
                "Name of institute with which instance is associated with."),
            ('language', 'str', '1.1',
                "Language with which instance is associated with."),
            ('project', 'str', '1.1',
                "Name of project with which instance is associated with."),
            ('sort_key', 'str', '0.1',
                "Document sort key."),
            ('source', 'str', '1.1',
                "Name of application that created the instance."),
            ('source_key', 'str', '0.1',
                "Key of application that created the instance."),
            ('sub_project', 'str', '1.1',
                "Name of sub-project with which instance is associated with."),
            ('type', 'str', '1.1',
                "Document ontology type."),
            ('type_display_name', 'str', '0.1',
                "Document type display name."),
            ('type_sort_key', 'str', '0.1',
                "Document type sort key."),
            ('update_date', 'datetime', '1.1',
                "Date upon which the instance was last updated."),
            ('version', 'int', '1.1',
                "Document version identifier.")
        ]
    }


def doc_reference():
    """Specialisation of online resource for link between CIM documents, whether the
    remote document exists when complete, or not.

    """
    return {
        'type': 'class',
        'base': 'shared.online_resource',
        'is_abstract': False,
        'properties': [
            ('constraint_vocabulary', 'str', '0.1',
                "A constraint vocabulary for the relationship."),
            ('context', 'str', '0.1',
                "Information about remote record in context of reference."),
            ('id', 'str', '0.1',
                "Identifier of remote resource, if known."),
            ('relationship', 'str', '0.1',
                "Predicate - relationship of the object target as seen from the subject resource."),
            ('type', 'str', '1.1',
                "The type of the remote record."),
            ('version', 'int', '0.1',
                "The version of the remote record.")
        ]
    }


def document_types():
    """The complete set of CIM document types, that is, all classes which carry the
    document metadata attributes.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Conformance", "Used to hold information about how simulations and ensemble met experimental requirements"),
            ("Dataset", "An Atomic Dataset description, that is the minimal set of files with common publication characteristics."),
            ("DomainProperties", "SpatioTemporal domain requirements for a numerical experiment."),
            ("Downscaling", "Description of the techniques and software used to downscale data."),
            ("Ensemble", "Parent  description for set of runs conforming to a numerical experiment."),
            ("EnsembleRequirement", "Description of the ensemble requirements of a numerical experiment."),
            ("ExternalDocument", "A document held outside of es-doc."),
            ("ForcingConstraint", "A constraint on how a model must be forced to meet the requirements of a numerical experiment."),
            ("Grid", "The sampling discretisation used by a model or dataset."),
            ("Machine", "A computer used for numerical experimentation (and/or post-processing)."),
            ("Model", "A piece of software used to carry out simulations."),
            ("MultiEnsemble", "An ensemble requirement describing multiple ensemble axes."),
            ("MultiTimeEnsemble", "An ensemble requirement with multple time axes."),
            ("NumericalExperiment", "The scientific description of a numerical experiment"),
            ("NumericalRequirement", "A numerical requirement of a numerical experiment."),
            ("OutputTemporalRequirement", "The output requirements for one or more numerical experiments"),
            ("Party", "A person or organisation which has a role in the documentation of the simulation workflow"),
            ("Performance", "A formal set of criteria describing how a model performed on a given machine."),
            ("Project", "An umbrella for a set of numerical experiments (e.g. a MIP)"),
            ("QualityReview", "A quality control assessment for another CIM artifact"),
            ("ScientificDomain", "A scientifically coherent realm of a numerical model (typically modelled independently)."),
            ("Simulation", "A simulation carried out as part of an ensemble for a numerical experiment."),
            ("SimulationPlan", "A plan to carry out a simulations for a numerical experiment."),
            ("TemporalConstraint", "A constraint on the real time simulations need to represent for a numerical experiment."),
            ("UberEnsemble", "An ensemble description that crosses multiple modelling groups.")
        ]
    }


def nil_reason():
    """Provides an enumeration of possible reasons why a property has not been defined
    Based on GML nilReason as discussed here: https://www.seegrid.csiro.au/wiki/AppSchemas/NilValues.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("nil:inapplicable", "There is no value"),
            ("nil:missing", "The correct value is not available. Furthermore, a correct value may not exist"),
            ("nil:template", "The value will be available later"),
            ("nil:unknown", "The correct value is not known at this time. However, a correct value probably exists"),
            ("nil:withheld", "The value is not divulged")
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
        'properties': [
            ('description', 'str', '0.1',
                "Detail of how to access the resource."),
            ('linkage', 'str', '1.1',
                "A URL."),
            ('name', 'str', '1.1',
                "Name of online resource."),
            ('protocol', 'str', '0.1',
                "Protocol to use at the linkage.")
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
        'properties': [
            ('address', 'str', '0.1',
                "Institutional address."),
            ('email', 'str', '0.1',
                "Email address."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Provides a unique identifier for the party."),
            ('name', 'str', '0.1',
                "Name of person or organisation."),
            ('orcid_id', 'str', '0.1',
                "Orcid ID if available."),
            ('organisation', 'bool', '0.1',
                "True if an organisation not a person."),
            ('url', 'shared.online_resource', '0.1',
                "URL of person or institution.")
        ]
    }


def quality_review():
    """Assertions as to the completeness and quality of a document.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('date', 'str', '1.1',
                "Date upon which review was made."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Metadata about the creation of this document description."),
            ('metadata_reviewer', 'linked_to(shared.party)', '1.1',
                "Party who made the metadata quality assessment."),
            ('quality_description', 'str', '1.1',
                "Assessment of quality of target document."),
            ('quality_status', 'shared.quality_status', '0.1',
                "Status from a controlled vocabulary."),
            ('target_document', 'linked_to(shared.doc_reference)', '1.1',
                "This is the document about which quality is asserted.")
        ]
    }


def quality_status():
    """Assertion as to the review status of document.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("incomplete", "Currently being worked on"),
            ("finalised", "Author has completed document, prior to review"),
            ("under_review", "Document is being reviewed"),
            ("reviewed", "Document has been formally reviewed and assessed as complete and accurate")
        ]
    }


def reference():
    """An external citation target which can have a context associated with it.

    """
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'properties': [
            ('context', 'str', '0.1',
                "Brief text description of why this resource is being cited."),
            ('document', 'shared.citation_target', '1.1',
                "Reference Target.")
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
        'pstr': ('{}:{}', ('role', 'party')),
        'properties': [
            ('party', 'linked_to(shared.party)', '1.N',
                "Parties delivering responsibility."),
            ('role', 'shared.role_code', '1.1',
                "Role that the party plays or played."),
            ('when', 'time.time_period', '0.1',
                "Period when role was active, if no longer.")
        ]
    }


def role_code():
    """Responsibility role codes: roles that a party may play in delivering a responsibility.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Principal Investigator", "Key party responsible for the existence of the resource"),
            ("originator", "Original source for the resource if obtained from elsewhere"),
            ("author", "Party who created (or co-created) resource"),
            ("collaborator", "Contributor to the production of the resource"),
            ("publisher", "Party who published the resource"),
            ("owner", "Party with legal ownership of the resource"),
            ("processor", "Party who has taken part in the workflow that resulted in this resource"),
            ("distributor", "Party who distributes the resource"),
            ("sponsor", "Party who has invested in the production of the resource"),
            ("user", "Party who uses the resource"),
            ("point of contact", "Party who can be contacted for acquiring knowledge about or acquisition of the resource"),
            ("resource provider", "Party that supplies the resource"),
            ("custodian", "Party that accepts accountability and responsibility for the source resource"),
            ("metadata_reviewer", "Party who carried out an independent review of (this) documentation"),
            ("metadata_author", "Party who created (this) documentation")
        ]
    }


def text_code():
    """Types of text understood by the CIM notebook. Currently only
    plaintext, but we expect safe HTML to be supported as soon as practicable.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("plaintext", "Normal plain text")
        ]
    }
