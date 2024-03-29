
"""
.. module:: cim.v2.extended_schema_for_designing_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def domain_requirements():
    """Properties of the domain which needs to be simulated, extent
    and/or resolution.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('required_extent', 'science.topic', '0.1',
                "Constraint on extent of domain to be simulated."),
            ('required_resolution', 'science.topic', '0.1',
                "Constraint on resolution required in simulated domain."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'required_extent',
            'required_resolution',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def ensemble_requirement():
    """Defines an experiment ensemble.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('ensemble_member', 'designing.numerical_requirement', '0.N',
                "Constraint on each ensemble member."),
            ('ensemble_type', 'designing.ensemble_types', '1.1',
                "Type of ensemble."),
            ('minimum_size', 'int', '1.1',
                "Minimum number of members."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'ensemble_member',
            'ensemble_type',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'minimum_size',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def forcing_constraint():
    """Identifies a model forcing constraint.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('additional_constraint', 'str', '0.1',
                "Additional information, e.g. hold constant from 2100-01-01."),
            ('category', 'str', '0.1',
                "Category to which this belongs (from a CV, e.g. GASES)."),
            ('code', 'str', '0.1',
                "Programme wide code from a controlled vocabulary (e.g. N2O)."),
            ('data_link', 'data.dataset', '0.1',
                "A data record used by the forcing "),
            ('forcing_type', 'designing.forcing_types', '1.1',
                "Type of integration."),
            ('group', 'str', '0.1',
                "Sub-Category (e.g. GHG)."),
            ('origin', 'shared.citation', '0.1',
                "Pointer to origin, e.g. CMIP6 RCP database."),
            ],
        'properties-all': [
            'additional_constraint',
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'category',
            'citations',
            'code',
            'data_link',
            'description',
            'duration',
            'forcing_type',
            'group',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'origin',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def initialisation_requirement():
    """A requirement on how a particular simulation should be
    initialised.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('branch_time_in_initialisation_source', 'time.date_time', '0.1',
                "If appropriate,  the time in the initialisation_source (whether observed or simulated)."),
            ('initialise_from_data', 'data.dataset', '0.1',
                "Initialisation should use this primary dataset."),
            ('initialise_from_experiment', 'designing.numerical_experiment', '0.1',
                "This experiment should be initialised from the output of this experiment."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'branch_time_in_initialisation_source',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'initialise_from_data',
            'initialise_from_experiment',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def multi_ensemble():
    """In the case of multiple ensemble axes, defines how they are set
    up and ordered.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('ensemble_axis', 'designing.ensemble_requirement', '1.N',
                "List of orthogonal ensembles."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'ensemble_axis',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def numerical_experiment():
    """Defines a numerical experiment.

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
            ('governing_mips', 'designing.project', '0.N',
                "MIP(s) overseeing experimental design protocol."),
            ('related_experiments', 'designing.numerical_experiment', '0.N',
                "Other experiments which have defined relationships to this one."),
            ('related_mips', 'designing.project', '0.N',
                "MIP's that require this experiment."),
            ('related_objectives', 'str', '0.N',
                "Set of objective identifiers (which should appear within the related experiments)"),
            ('required_period', 'designing.temporal_constraint', '1.1',
                "Constraint on start date and duration."),
            ('requirements', 'designing.numerical_requirement', '0.N',
                "Additional requirements that conformant simulations need to satisfy."),
            ('tier', 'int', '0.1',
                "Relative importance of experiment within a MIP."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'governing_mips',
            'internal_name',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'related_experiments',
            'related_mips',
            'related_objectives',
            'required_period',
            'requirements',
            'responsible_parties',
            'tier',
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


def numerical_requirement():
    """A numerical requirement associated with a numerical
    experiment.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'designing.domain_requirements',
            'designing.ensemble_requirement',
            'designing.forcing_constraint',
            'designing.initialisation_requirement',
            'designing.multi_ensemble',
            'designing.output_requirement',
            'designing.start_date_ensemble',
            'designing.temporal_constraint'
        ],
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('additional_requirements', 'designing.numerical_requirement', '0.N',
                "Additional detail for this requirement."),
            ('is_conformance_info_required', 'bool', '1.1',
                "Indicator as to whether an institute is expected to provide informationas to how it confirmed."),
            ('is_conformance_requested', 'bool', '1.1',
                "Indicator as to whether ensemble documentation should include conformance information for this requirement."),
            ('scope', 'designing.numerical_requirement_scope', '0.1',
                "Scope allows us to categorise a requirement in terms of how widely it is shared."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
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


def objective():
    """Describes a specific scientific objective within a project, and
    any necessary outputs from the experiment needed to meet this
    objective.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('description', 'str', '0.1',
                " Short summary of the objective"),
            ('identifier', 'str', '0.1',
                "Provides a hook to which experiments can link"),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('name', 'str', '1.1',
                "Name of this objective"),
            ('required_outputs', 'data.variable_collection', '0.N',
                "Set of required outputs associated with this objective"),
            ]
    }


def output_requirement():
    """Provides details of what output is required and when from an
    experiment.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('formal_data_request', 'shared.online_resource', '0.1',
                "If available, link to a 'cmip' style online request."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'formal_data_request',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def project():
    """Describes a scientific project.

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
            ('governed_experiments', 'designing.numerical_experiment', '0.N',
                "Experiments governed by this project."),
            ('homepage', 'shared.online_resource', '0.1',
                "Project homepage."),
            ('objectives', 'designing.objective', '0.N',
                "Project objectives."),
            ('previous_projects', 'designing.project', '0.N',
                "Previous projects with similar aims."),
            ('required_experiments', 'designing.numerical_experiment', '0.N',
                "Experiments required to deliver project."),
            ('sub_projects', 'designing.project', '0.N',
                "Activities within the project with their own name and aim(s)."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'governed_experiments',
            'homepage',
            'internal_name',
            'keywords',
            'long_name',
            'meta',
            'name',
            'objectives',
            'previous_projects',
            'previously_known_as',
            'rationale',
            'required_experiments',
            'responsible_parties',
            'sub_projects',
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


def simulation_plan():
    """Describes a simulation that needs to be run.

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
            ('expected_model', 'science.model', '1.1',
                "The model used to run the simulation."),
            ('expected_performance_sypd', 'float', '0.1',
                "Expected performance in simulated years per real day."),
            ('expected_platform', 'platform.machine', '0.1',
                "The machine on which the simulation will be run."),
            ('will_support_experiments', 'designing.numerical_experiment', '1.N',
                "An experiment with which the planned simulation will be associated."),
            ],
        'properties-all': [
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'expected_model',
            'expected_performance_sypd',
            'expected_platform',
            'internal_name',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'will_support_experiments',
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


def start_date_ensemble():
    """Defines an experiment ensemble with multiple start dates.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('ensemble_members', 'time.datetime_set', '1.1',
                "Description of date or time set of start dates."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'ensemble_members',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'responsible_parties',
            'scope',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }


def temporal_constraint():
    """A spatio-temporal constraint on a numerical experiment.

	"""
    return {
        'type': 'class',
        'base': "designing.numerical_requirement",
        'base-hierarchy': [
            'designing.numerical_requirement',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('required_calendar', 'time.calendar', '0.1',
                "Required calendar (e.g. for paleo simulations)."),
            ('required_duration', 'time.time_period', '0.1',
                "Constraint on time or length of simulation."),
            ('start_date', 'time.date_time', '0.1',
                "Required start date."),
            ('start_flexibility', 'time.time_period', '0.1',
                "Amount of time before required start date that it is permissible to begin integration."),
            ],
        'properties-all': [
            'additional_requirements',
            'alternative_names',
            'canonical_name',
            'citations',
            'description',
            'duration',
            'internal_name',
            'is_conformance_info_required',
            'is_conformance_requested',
            'keywords',
            'long_name',
            'meta',
            'name',
            'previously_known_as',
            'rationale',
            'required_calendar',
            'required_duration',
            'responsible_parties',
            'scope',
            'start_date',
            'start_flexibility',
            ],
        'properties-inherited': [
            'additional_requirements :: designing.numerical_requirement',
            'alternative_names :: activity.activity',
            'canonical_name :: activity.activity',
            'citations :: activity.activity',
            'description :: activity.activity',
            'duration :: activity.activity',
            'internal_name :: activity.activity',
            'is_conformance_info_required :: designing.numerical_requirement',
            'is_conformance_requested :: designing.numerical_requirement',
            'keywords :: activity.activity',
            'long_name :: activity.activity',
            'meta :: activity.activity',
            'name :: activity.activity',
            'previously_known_as :: activity.activity',
            'rationale :: activity.activity',
            'responsible_parties :: activity.activity',
            'scope :: designing.numerical_requirement',
            ]
    }




