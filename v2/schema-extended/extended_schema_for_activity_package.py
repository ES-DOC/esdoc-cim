
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def activity():
    """Base class for activities.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'activity.conformance',
            'designing.domain_requirements',
            'data.downscaling',
            'activity.ensemble',
            'designing.ensemble_requirement',
            'designing.forcing_constraint',
            'designing.initialisation_requirement',
            'designing.multi_ensemble',
            'designing.numerical_experiment',
            'designing.numerical_requirement',
            'designing.output_requirement',
            'designing.project',
            'data.simulation',
            'designing.simulation_plan',
            'designing.start_date_ensemble',
            'designing.temporal_constraint'
            'activity.uber_ensemble',
        ],
        'is_abstract': True,
        'is_document': True,
        'properties': [
            ('alternative_names', 'str', '0.N',
                "List of names by which the activity is also known."),
            ('canonical_name', 'str', '0.1',
                "Community defined identifier or name."),
            ('citations', 'shared.citation', '0.N',
                "Set of pertinent citations."),
            ('description', 'str', '0.1',
                "Description of what is to be done (or was done)."),
            ('duration', 'time.time_period', '0.1',
                "Time the activity was (or will be) active."),
            ('internal_name', 'str', '0.1',
                "A name used for internal purposes."),
            ('keywords', 'str', '0.1',
                "User defined keywords."),
            ('long_name', 'str', '0.1',
                "Longer version of activity name."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "Short name or abbreviation."),
            ('previously_known_as', 'str', '0.N',
                "List of names by which the activity was formerly known."),
            ('rationale', 'str', '0.1',
                "Explanation of why this activity was carried out and/or what it was intended to achieve."),
            ('responsible_parties', 'shared.responsibility', '0.N',
                "People or organisations responsible for activity."),
            ]
    }


def axis_member():
    """Description of a given ensemble member. It will normally be related to a specific
    ensemble requirement. Note that start dates can be extracted directly from the simulations
    and do not need to be recorded with an axis member description.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '1.1',
                "Description of the member (or name of parameter varied)."),
            ('extra_detail', 'str', '0.1',
                "If necessary: further information about ensemble member conformance."),
            ('index', 'int', '1.1',
                "The ensemble member index."),
            ('value', 'float', '0.1',
                "If parameter varied, value thereof for this member."),
            ]
    }


def conformance():
    """A specific conformance. Describes how a particular numerical requirement has been implemented.
    Will normally be linked from an ensemble descriptor.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('conformance_achieved', 'activity.conformance_type', '1.1',
                "Summary of conformance status."),
            ('datasets', 'data.input_dataset', '0.N',
                "The datasets (including any modifications made to them) used for conforming to the target requirement."),
            ('models', 'science.model', '1.N',
                "The models to which this conformance applies."),
            ('target_requirement', 'designing.numerical_requirement', '1.1',
                "URI of the target numerical requirement."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'citations',
            'conformance_achieved',
            'datasets',
            'description',
            'duration',
            'internal_name',
            'keywords',
            'long_name',
            'meta',
            'models',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'target_requirement',
            ],
        'properties-inherited': [
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            ]
    }


def ensemble():
    """Generic ensemble definition.
    Holds the definition of how the various ensemble members have been configured.
    If ensemble axes are not present, then this is either a single member ensemble,
    or part of an uber ensemble.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'activity.uber_ensemble'
        ],
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('common_conformances', 'activity.conformance', '0.N',
                "Conformance documents for requirements common across ensemble."),
            ('common_performance', 'platform.performance', '0.1',
                "Representative model performance across ensemble."),
            ('documentation', 'shared.online_resource', '0.N',
                "Links to web-pages and other ensemble specific documentation (including workflow descriptions)."),
            ('ensemble_axes', 'activity.ensemble_axis', '0.N',
                "Set of axes for the ensemble."),
            ('experiments', 'designing.numerical_experiment', '1.N',
                "Experiments with which the ensemble is associated (may differ from constituent simulations)."),
            ('members', 'activity.ensemble_member', '1.N',
                "The set of ensemble members."),
            ('uber_ensembles', 'activity.uber_ensemble', '0.N',
                "Link to one or more over-arching ensembles that might includes this one."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'citations',
            'common_conformances',
            'common_performance',
            'description',
            'documentation',
            'duration',
            'ensemble_axes',
            'experiments',
            'internal_name',
            'keywords',
            'long_name',
            'members',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'uber_ensembles',
            ],
        'properties-inherited': [
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            ]
    }


def ensemble_axis():
    """Defines the meaning of r/i/p indices in an ensemble.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('extra_detail', 'str', '1.1',
                "Any extra detail required to describe how this ensemble axis was delivered."),
            ('member', 'activity.axis_member', '1.N',
                "Individual member descriptions along axis."),
            ('short_identifier', 'str', '1.1',
                "e.g. 'r' or 'i' or 'p' to conform with simulation ensemble variant identifiers."),
            ('target_requirement', 'designing.numerical_requirement', '1.1',
                "URI of the target numerical requirement."),
            ]
    }


def ensemble_member():
    """An ensemble may be a complicated interplay of axes, for example, r/i/p, not all of which
    are populated, so we need a list of the actual simulations and how they map onto the ensemble
    axes.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('errata', 'shared.online_resource', '0.1',
                "Link to errata associated with this simulation."),
            ('had_performance', 'platform.performance', '0.1',
                "Performance of the simulation."),
            ('ran_on', 'platform.machine', '0.1',
                "The machine on which the simulation was run."),
            ('simulation', 'data.simulation', '1.1',
                "Actual simulation description for an ensemble member. The variant id is in the simuluation document."),
            ]
    }


def parent_simulation():
    """Defines the relationship between a simulation and its parent.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('branch_method', 'str', '0.1',
                "Description of how the simulation was branched from a parent simualtion, e.g. 'standard', 'none provided'."),
            ('branch_time_in_child', 'time.date_time', '0.1',
                "The time at which the present simulation started in the child calendar."),
            ('branch_time_in_parent', 'time.date_time', '0.1',
                "The time in parent simulation calendar at which this simulation was branched."),
            ('parent', 'data.simulation', '1.1',
                "The parent simulation of this child."),
            ]
    }


def uber_ensemble():
    """An ensemble made up of other ensembles. Often used where parts of an ensemble were run by
    different institutes. Could also be used when a new experiment is designed which can use
    ensemble members from previous experiments and/or projects.

	"""
    return {
        'type': 'class',
        'base': "activity.ensemble",
        'base-hierarchy': [
            'activity.ensemble',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('child_ensembles', 'activity.ensemble', '1.N',
                "Ensemble which are aggregated into this one."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'child_ensembles',
            'citations',
            'common_conformances',
            'common_performance',
            'description',
            'documentation',
            'duration',
            'ensemble_axes',
            'experiments',
            'internal_name',
            'keywords',
            'long_name',
            'members',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'uber_ensembles',
            ],
        'properties-inherited': [
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'common_conformances :: activity.ensemble',
            'common_performance :: activity.ensemble',
            'description :: activity.activity',
            'documentation :: activity.ensemble',
            'duration :: activity.activity',
            'ensemble_axes :: activity.ensemble',
            'experiments :: activity.ensemble',
            'internal_name :: activity.activity',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'members :: activity.ensemble',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'uber_ensembles :: activity.ensemble',
            ]
    }




