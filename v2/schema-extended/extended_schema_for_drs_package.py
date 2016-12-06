
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_drs_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def drs_atomic_dataset():
    """An entity in a DRS file system.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('frequency', 'drs.drs_frequency_types', '1.1',
                "Frequency at which data is stored."),
            ('geographical_constraint', 'drs.drs_geographical_indicator', '0.1',
                "Identifies geographical subsets and spatial means."),
            ('mip_table', 'str', '1.1',
                "The MIP table, together with the variable defines the physical quantity."),
            ('realm', 'drs.drs_realms', '0.1',
                "Modelling realm."),
            ('temporal_constraint', 'drs.drs_temporal_identifier', '0.1',
                "Identifies temporal subsets or means."),
            ('variable_name', 'str', '1.1',
                "Identifies the physical quantity (when used in conjunction with the MIP table)."),
            ('version_number', 'int', '0.1',
                "Uniquely identifies a particular version of a publication level dataset."),
            ]
    }


def drs_ensemble_identifier():
    """Identifies a 'response ensemble' realisation using the semantic content ofa 'run_variant_id'.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('forcing_number', 'int', '0.1',
                "Identifies possible perturbatinos in forcing."),
            ('initialisation_method_number', 'int', '1.1',
                "Identifies which method of initialisation was used, if multiple methods used."),
            ('perturbation_number', 'int', '1.1',
                "Identifies different members of a perturbed physics ensemble."),
            ('realisation_number', 'int', '1.1',
                "Standard ensemble axis realisation number (usually an initial condition ensemble)."),
            ]
    }


def drs_experiment():
    """An encoding of a drs experiment_id.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('axis_identifer', 'designing.axis_member', '0.1',
                "FIXME."),
            ('axis_type', 'designing.ensemble_types', '0.1',
                "Type of experimental family ensemble required."),
            ('family', 'str', '1.1',
                "Main experimental family."),
            ]
    }


def drs_geographical_indicator():
    """Specifies geographical subsets described by bounding boxes or by named regions.
     One of spatial domain or bounding box must appear.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('bounding_box', 'str', '0.1',
                "DRS bounding box of the form 'latJHJJHHlonMZMMZZ' where H, HH, Z, ZZ are from {NS} {EW} respectively."),
            ('operator', 'drs.drs_geographical_operators', '0.1',
                "Spatial averagin applied to the geographical region."),
            ('spatial_domain', 'str', '0.1',
                "Geographical indicator (currently only 'global' is acceptable)."),
            ]
    }


def drs_publication_dataset():
    """PLACEHOLDER for the real drs_publication_dataset.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ]
    }


def drs_simulation_identifier():
    """That part of the DRS which identifies the response to the experiment: the simulation.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('institute', 'str', '1.1',
                "The institute responsible for this data entity."),
            ('model', 'str', '1.1',
                "A model identifier (sans blanks/periods and parenthesis)."),
            ('run_variant_id', 'drs.drs_ensemble_identifier', '1.1',
                "Also known as ensemble_identifier, unambiguously identifiers ensemble realisation information."),
            ]
    }


def drs_temporal_identifier():
    """Provides information about temporal subsetting and/or averaging.
    If only N1 is present, it a temporal instant,
    If N1-N2 are present with no suffix, it is a temporal subset,
    If N1-N2 with a suffix are present, then some sort of temporal averaging has been applied across
    the period.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('end', 'str', '0.1',
                "N2, required to indicate a period."),
            ('start', 'str', '1.1',
                "N1,  of the form yyyy[MM[dd[hh[mm[ss]]]]]."),
            ('suffix', 'drs.drs_time_suffixes', '0.1',
                "If present, used to indicate climatology or average."),
            ]
    }




