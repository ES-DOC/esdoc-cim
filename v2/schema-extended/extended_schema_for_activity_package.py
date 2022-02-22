
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
            'activity.ensemble',
            'designing.ensemble_requirement',
            'designing.forcing_constraint',
            'designing.initialisation_requirement',
            'designing.multi_ensemble',
            'designing.numerical_experiment',
            'designing.numerical_requirement',
            'designing.output_requirement',
            'designing.project',
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
    """Description of a given ensemble member.

    It will normally be related to a specific ensemble requirement. Note
    that start dates can be extracted directly from the simulations and
    do not need to be recorded with an axis member description.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('axis', 'activity.ensemble_axis', '1.1',
                "The parent axis of this ensemble member"),
            ('conformance', 'activity.conformance', '0.1',
                "Conformance document for the target requirement that defines this member, if any."),
            ('description', 'str', '0.1',
                "Description of the member (or name of parameter varied)."),
            ('extra_detail', 'str', '0.1',
                "If necessary: further information about ensemble member conformance."),
            ('index', 'int', '1.1',
                "The ensemble member index."),
            ('value', 'float', '0.1',
                "If parameter varied; value for this member."),
            ]
    }


def child_simulation():
    """Defines the relationship between a simulation and its parent.

	"""
    return {
        'type': 'class',
        'base': "activity.simulation",
        'base-hierarchy': [
            'activity.simulation',
            'iso.process_step'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('branch_method', 'str', '0.1',
                "Description of how the simulation was branched from a parent simulation, e.g. 'standard', 'none provided'."),
            ('branch_time_in_child', 'time.date_time', '0.1',
                "The time at which the present simulation started in the child calendar."),
            ('branch_time_in_parent', 'time.date_time', '0.1',
                "The time in parent simulation calendar at which this simulation was branched."),
            ('parent', 'activity.simulation', '1.1',
                "The parent simulation of this child."),
            ],
        'properties-all': [
            'branch_method',
            'branch_time_in_child',
            'branch_time_in_parent',
            'calendar',
            'description',
            'documentation',
            'end_time',
            'ensemble_id',
            'errata',
            'execution_date_time',
            'extra_attributes',
            'had_performance',
            'institution',
            'meta',
            'parent',
            'parent_of',
            'part_of_project',
            'primary_ensemble',
            'processing_information',
            'processor',
            'produced',
            'ran_for_experiments',
            'ran_on',
            'rationale',
            'reference',
            'report',
            'source',
            'start_time',
            'sub_experiment',
            'used',
            ],
        'properties-inherited': [
            'calendar :: activity.simulation',
            'description :: iso.process_step',
            'documentation :: activity.simulation',
            'end_time :: activity.simulation',
            'ensemble_id :: activity.simulation',
            'errata :: activity.simulation',
            'execution_date_time :: iso.process_step',
            'extra_attributes :: activity.simulation',
            'had_performance :: activity.simulation',
            'institution :: activity.simulation',
            'meta :: activity.simulation',
            'parent_of :: activity.simulation',
            'part_of_project :: activity.simulation',
            'primary_ensemble :: activity.simulation',
            'processing_information :: iso.process_step',
            'processor :: iso.process_step',
            'produced :: activity.simulation',
            'ran_for_experiments :: activity.simulation',
            'ran_on :: activity.simulation',
            'rationale :: iso.process_step',
            'reference :: iso.process_step',
            'report :: iso.process_step',
            'source :: iso.process_step',
            'start_time :: activity.simulation',
            'sub_experiment :: activity.simulation',
            'used :: activity.simulation',
            ]
    }


def conformance():
    """A specific conformance.

    Describes how a particular numerical requirement has been
    implemented.  Will normally be linked from an ensemble descriptor.

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
            ('datasets', 'data.dataset', '0.N',
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

    Holds the definition of how the various ensemble members have been
    configured. If ensemble axes are not present, then this is either a
    single member ensemble, or part of an uber ensemble.

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
            ('documentation', 'shared.online_resource', '0.N',
                "Links to web-pages and other ensemble specific documentation (including workflow descriptions)."),
            ('ensemble_axes', 'activity.ensemble_axis', '0.N',
                "Set of axes for the ensemble."),
            ('experiments', 'designing.numerical_experiment', '1.N',
                "Experiments with which the ensemble is associated (may differ from constituent simulations)."),
            ('members', 'activity.simulation', '0.N',
                "Simulations within ensemble (should only be zero while ensemble is being defined)"),
            ('representative_performance', 'platform.performance', '0.1',
                "Representative model performance across ensemble."),
            ('uber_ensembles', 'activity.uber_ensemble', '0.N',
                "Link to one or more over-arching ensembles that might includes this one."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'citations',
            'common_conformances',
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
            'representative_performance',
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
        'is_document': True,
        'properties': [
            ('extra_detail', 'str', '0.1',
                "Any extra detail required to describe how this ensemble axis was delivered."),
            ('members', 'activity.axis_member', '0.N',
                "Individual member descriptions along axis. 0.N cardinality is only acceptable during design"),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "Short handle/name for the axis"),
            ('short_identifier', 'str', '1.1',
                "e.g. 'r', 'i', 'p' or 'f' to conform with simulation ensemble variant identifiers."),
            ('target_requirement', 'designing.numerical_requirement', '0.1',
                "URI of the target numerical requirement, if any"),
            ]
    }


def simulation():
    """Simulation class provides the integrating link about what models
    were run and wny.

	"""
    return {
        'type': 'class',
        'base': "iso.process_step",
        'base-hierarchy': [
            'iso.process_step'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'activity.child_simulation',
            'cmip.cmip_simulation'
        ],
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('calendar', 'time.calendar', '0.1',
                "The calendar used in the simulation"),
            ('documentation', 'shared.online_resource', '0.1',
                "On-line location of additional documentation"),
            ('end_time', 'time.date_time', '0.1',
                "The end date-time of the simulation. e.g. 2087-11-30 12:00:00"),
            ('ensemble_id', 'activity.axis_member', '0.N',
                "Identification within ensemble axes via axis member. (Multiple axis members within a simulation cannot share the same ensemble_axis.) (There must be an axis_member instance for each ensemble axis in a parent ensemble.)"),
            ('errata', 'shared.online_resource', '0.1',
                "Link to errata associated with this simulation."),
            ('extra_attributes', 'shared.extra_attribute', '0.N',
                "Additional attributes provided with simulation."),
            ('had_performance', 'platform.performance', '0.1',
                "Performance of the simulation."),
            ('institution', 'shared.party', '0.1',
                "institution which carried out the simulation"),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('parent_of', 'activity.child_simulation', '0.N',
                "If appropriate, links to simulations which branched from this one"),
            ('part_of_project', 'designing.project', '1.N',
                "Project or projects for which simulation was run"),
            ('primary_ensemble', 'activity.ensemble', '0.1',
                "Primary Ensemble (ensemble for which this simulation was first run)."),
            ('produced', 'data.dataset', '0.N',
                "Products of the simulation"),
            ('ran_for_experiments', 'designing.numerical_experiment', '1.N',
                "One or more experiments with which the simulation is associated"),
            ('ran_on', 'platform.machine', '0.1',
                "The machine on which the simulation was run."),
            ('start_time', 'time.date_time', '0.1',
                "The start date-time of the simulation. e.g. 2012-04-01 00:00:00"),
            ('sub_experiment', 'designing.numerical_experiment', '0.1',
                "For start-date ensembles, this will indicate the beginning year; for offline models driven by output from another model, this will provide the source_id and variant_label for the 'driving' model."),
            ('used', 'science.model', '1.1',
                "The model used to run the simulation"),
            ],
        'properties-all': [
            'calendar',
            'description',
            'documentation',
            'end_time',
            'ensemble_id',
            'errata',
            'execution_date_time',
            'extra_attributes',
            'had_performance',
            'institution',
            'meta',
            'parent_of',
            'part_of_project',
            'primary_ensemble',
            'processing_information',
            'processor',
            'produced',
            'ran_for_experiments',
            'ran_on',
            'rationale',
            'reference',
            'report',
            'source',
            'start_time',
            'sub_experiment',
            'used',
            ],
        'properties-inherited': [
            'description :: iso.process_step',
            'execution_date_time :: iso.process_step',
            'processing_information :: iso.process_step',
            'processor :: iso.process_step',
            'rationale :: iso.process_step',
            'reference :: iso.process_step',
            'report :: iso.process_step',
            'source :: iso.process_step',
            ]
    }


def uber_ensemble():
    """An ensemble made up of other ensembles.

    Often used where parts of an ensemble were run by different
    institutes. Could also be used when a new experiment is designed
    which can use ensemble members from previous experiments and/or
    projects.

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
            'representative_performance',
            'responsible_parties',
            'uber_ensembles',
            ],
        'properties-inherited': [
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'common_conformances :: activity.ensemble',
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
            'representative_performance :: activity.ensemble',
            'responsible_parties :: activity.activity',
            'uber_ensembles :: activity.ensemble',
            ]
    }




