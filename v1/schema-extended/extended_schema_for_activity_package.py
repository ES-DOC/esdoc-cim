
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.extended_schema_for_activity_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def activity():
    """An abstract class used as the parent of MeasurementCampaigns, Projects, Experiments, and NumericalActivities.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'activity.downscaling_simulation',
            'activity.ensemble',
            'activity.ensemble_member',
            'activity.experiment',
            'activity.measurement_campaign',
            'activity.numerical_activity',
            'activity.numerical_experiment',
            'activity.simulation',
            'activity.simulation_composite',
            'activity.simulation_run'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('funding_sources', 'str', '0.N',
                "The entities that funded this activity."),
            ('projects', 'activity.project_type', '0.N',
                "The project(s) that this activity is associated with (ie: CMIP5, AMIP, etc)."),
            ('rationales', 'str', '0.N',
                "For what purpose is this activity being performed?"),
            ('responsible_parties', 'shared.responsible_party', '0.N',
                "The point of contact(s) for this activity.This includes, among others, the principle investigator."),
            ]
    }


def boundary_condition():
    """A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_requirement",
        'base-hierarchy': [
            'activity.numerical_requirement'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'id',
            'name',
            'options',
            'requirement_type',
            'source',
            ],
        'properties-inherited': [
            'description :: activity.numerical_requirement',
            'id :: activity.numerical_requirement',
            'name :: activity.numerical_requirement',
            'options :: activity.numerical_requirement',
            'requirement_type :: activity.numerical_requirement',
            'source :: activity.numerical_requirement',
            ]
    }


def conformance():
    """A conformance class maps how a configured model component met a specific numerical requirement.  For example, for a double CO2 boundary condition, a model component might read a CO2 dataset in which CO2 has been doubled, or it might modify a parameterisation (presumably with a factor of two somewhere).  So, the conformance links a requirement to a DataSource (which can be either an actual DataObject or a property of a model component).  In some cases a model/simulation may _naturally_ conform to a requirement.  In this case there would be no reference to a DataSource but the conformant attribute would be true.  If something is purpopsefully non-conformant then the conformant attribute would be false.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'activity.physical_modification'
        ],
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('frequency', 'activity.frequency_type', '0.1',
                ""),
            ('is_conformant', 'bool', '1.1',
                "Records whether or not this conformance satisfies the requirement.  A simulation should have at least one conformance mapping to every experimental requirement.  If a simulation satisfies the requirement - the usual case - then conformant should have a value of true.  If conformant is true but there is no reference to a source for the conformance, then we can assume that the simulation conforms to the requirement _naturally_, that is without having to modify code or inputs. If a simulation does not conform to a requirement then conformant should be set to false."),
            ('requirements', 'activity.numerical_requirement', '1.N',
                "Points to the NumericalRequirement that the simulation in question is conforming to."),
            ('sources', 'shared.data_source', '0.N',
                "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute."),
            ('type', 'activity.conformance_type', '0.1',
                "Describes the method that this simulation conforms to an experimental requirement (in case it is not specified by the change property of the reference to the source of this conformance)"),
            ]
    }


def downscaling_simulation():
    """A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_activity",
        'base-hierarchy': [
            'activity.numerical_activity',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': True,
        'is_document': True,
        'properties': [
            ('calendar', 'shared.calendar', '1.1',
                ""),
            ('downscaled_from', 'shared.data_source', '1.1',
                ""),
            ('downscaling_id', 'str', '0.1',
                ""),
            ('downscaling_type', 'activity.downscaling_type', '0.1',
                ""),
            ('inputs', 'software.coupling', '0.N',
                "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('outputs', 'data.data_object', '0.N',
                ""),
            ],
        'properties-all': [
            'calendar',
            'description',
            'downscaled_from',
            'downscaling_id',
            'downscaling_type',
            'funding_sources',
            'inputs',
            'long_name',
            'meta',
            'outputs',
            'projects',
            'rationales',
            'responsible_parties',
            'short_name',
            'supports',
            ],
        'properties-inherited': [
            'description :: activity.numerical_activity',
            'funding_sources :: activity.activity',
            'long_name :: activity.numerical_activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            'short_name :: activity.numerical_activity',
            'supports :: activity.numerical_activity',
            ]
    }


def ensemble():
    """An ensemble is made up of two or more simulations which are to be compared against each other to create ensemble statistics. Ensemble members can differ in terms of initial conditions, physical parameterisation and the model used. An ensemble bundles together sets of ensembleMembers, all of which reference the same Simulation(Run) and include one or more changes.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_activity",
        'base-hierarchy': [
            'activity.numerical_activity',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('members', 'activity.ensemble_member', '1.N',
                ""),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('outputs', 'shared.data_source', '0.N',
                "Points to the DataSource used to conform to a particular Requirement.   This may be part of an activity::simulation or a software::component.  It can be either a DataObject or a SoftwareComponent or a ComponentProperty.  It could also be by using particular attributes of, say, a SoftwareComponent, but in that case the recommended practise is to reference the component and add appropriate text in the conformance description attribute."),
            ('types', 'activity.ensemble_type', '1.N',
                ""),
            ],
        'properties-all': [
            'description',
            'funding_sources',
            'long_name',
            'members',
            'meta',
            'outputs',
            'projects',
            'rationales',
            'responsible_parties',
            'short_name',
            'supports',
            'types',
            ],
        'properties-inherited': [
            'description :: activity.numerical_activity',
            'funding_sources :: activity.activity',
            'long_name :: activity.numerical_activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            'short_name :: activity.numerical_activity',
            'supports :: activity.numerical_activity',
            ]
    }


def ensemble_member():
    """A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_activity",
        'base-hierarchy': [
            'activity.numerical_activity',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('ensemble', 'activity.ensemble', '0.1',
                ""),
            ('ensemble_ids', 'shared.standard_name', '0.N',
                ""),
            ('simulation', 'activity.simulation', '0.1',
                ""),
            ],
        'properties-all': [
            'description',
            'ensemble',
            'ensemble_ids',
            'funding_sources',
            'long_name',
            'projects',
            'rationales',
            'responsible_parties',
            'short_name',
            'simulation',
            'supports',
            ],
        'properties-inherited': [
            'description :: activity.numerical_activity',
            'funding_sources :: activity.activity',
            'long_name :: activity.numerical_activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            'short_name :: activity.numerical_activity',
            'supports :: activity.numerical_activity',
            ]
    }


def experiment():
    """An experiment might be an activity which is both observational and numerical in focus, for example, a measurement campaign and numerical experiments for an alpine experiment.  It is a place for the scientific description of the reason why an experiment was made.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'activity.numerical_experiment'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('generates', 'str', '0.N',
                ""),
            ('measurement_campaigns', 'activity.measurement_campaign', '0.N',
                ""),
            ('requires', 'activity.numerical_activity', '0.N',
                ""),
            ('supports', 'str', '0.N',
                ""),
            ],
        'properties-all': [
            'funding_sources',
            'generates',
            'measurement_campaigns',
            'projects',
            'rationales',
            'requires',
            'responsible_parties',
            'supports',
            ],
        'properties-inherited': [
            'funding_sources :: activity.activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            ]
    }


def experiment_relationship():
    """Contains a set of relationship types specific to a experiment document that can be used to describe its genealogy.

	"""
    return {
        'type': 'class',
        'base': "shared.relationship",
        'base-hierarchy': [
            'shared.relationship'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('target', 'activity.experiment_relationship_target', '1.1',
                ""),
            ('type', 'activity.experiment_relationship_type', '1.1',
                ""),
            ],
        'properties-all': [
            'description',
            'target',
            'type',
            ],
        'properties-inherited': [
            'description :: shared.relationship',
            ]
    }


def experiment_relationship_target():
    """Creates and returns instance of experiment_relationship_target class.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('numerical_experiment', 'activity.numerical_experiment', '0.1',
                ""),
            ]
    }


def initial_condition():
    """An initial condition is a numerical requirement on a model prognostic variable value at time zero.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_requirement",
        'base-hierarchy': [
            'activity.numerical_requirement'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'id',
            'name',
            'options',
            'requirement_type',
            'source',
            ],
        'properties-inherited': [
            'description :: activity.numerical_requirement',
            'id :: activity.numerical_requirement',
            'name :: activity.numerical_requirement',
            'options :: activity.numerical_requirement',
            'requirement_type :: activity.numerical_requirement',
            'source :: activity.numerical_requirement',
            ]
    }


def lateral_boundary_condition():
    """A boundary condition is a numerical requirement which looks like a variable imposed on the model evolution (i.e. it might - or might not - evolve with time, but is seen by the model at various times during its evolution) as opposed to an initial condition (at model time zero).

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_requirement",
        'base-hierarchy': [
            'activity.numerical_requirement'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'id',
            'name',
            'options',
            'requirement_type',
            'source',
            ],
        'properties-inherited': [
            'description :: activity.numerical_requirement',
            'id :: activity.numerical_requirement',
            'name :: activity.numerical_requirement',
            'options :: activity.numerical_requirement',
            'requirement_type :: activity.numerical_requirement',
            'source :: activity.numerical_requirement',
            ]
    }


def measurement_campaign():
    """Creates and returns instance of measurement_campaign class.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('duration', 'int', '1.1',
                ""),
            ],
        'properties-all': [
            'duration',
            'funding_sources',
            'projects',
            'rationales',
            'responsible_parties',
            ],
        'properties-inherited': [
            'funding_sources :: activity.activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            ]
    }


def numerical_activity():
    """Creates and returns instance of numerical_activity class.

	"""
    return {
        'type': 'class',
        'base': "activity.activity",
        'base-hierarchy': [
            'activity.activity'
            ],
        'base-hierarchy-depth': 1,
        'sub-classes': [
            'activity.downscaling_simulation',
            'activity.ensemble',
            'activity.ensemble_member',
            'activity.simulation',
            'activity.simulation_composite',
            'activity.simulation_run'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "A free-text description of the experiment."),
            ('long_name', 'str', '0.1',
                "The name of the experiment (that is recognized externally)."),
            ('short_name', 'str', '1.1',
                "The name of the experiment (that is used internally)."),
            ('supports', 'activity.experiment', '0.N',
                ""),
            ],
        'properties-all': [
            'description',
            'funding_sources',
            'long_name',
            'projects',
            'rationales',
            'responsible_parties',
            'short_name',
            'supports',
            ],
        'properties-inherited': [
            'funding_sources :: activity.activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            ]
    }


def numerical_experiment():
    """A numerical experiment may be generated by an experiment, in which case it is inSupportOf the experiment. But a numerical experiment may also exist as an activity in its own right (as it might be if it were needed for a MIP). Examples: AR4 individual experiments, AR5 individual experiments, RAPID THC experiments etc.

	"""
    return {
        'type': 'class',
        'base': "activity.experiment",
        'base-hierarchy': [
            'activity.experiment',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('description', 'str', '0.1',
                "A free-text description of the experiment."),
            ('experiment_id', 'str', '0.1',
                "An experiment ID takes the form <number>.<number>[-<letter>]."),
            ('long_name', 'str', '0.1',
                "The name of the experiment (that is recognized externally)."),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('requirements', 'activity.numerical_requirement', '0.N',
                "The name of the experiment (that is used internally)."),
            ('short_name', 'str', '1.1',
                "The name of the experiment (that is used internally)."),
            ],
        'properties-all': [
            'description',
            'experiment_id',
            'funding_sources',
            'generates',
            'long_name',
            'measurement_campaigns',
            'meta',
            'projects',
            'rationales',
            'requirements',
            'requires',
            'responsible_parties',
            'short_name',
            'supports',
            ],
        'properties-inherited': [
            'funding_sources :: activity.activity',
            'generates :: activity.experiment',
            'measurement_campaigns :: activity.experiment',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'requires :: activity.experiment',
            'responsible_parties :: activity.activity',
            'supports :: activity.experiment',
            ]
    }


def numerical_requirement():
    """A description of the requirements of particular experiments.  Numerical Requirements can be initial conditions, boundary conditions, or physical modificiations.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'activity.boundary_condition',
            'activity.initial_condition',
            'activity.lateral_boundary_condition',
            'activity.output_requirement',
            'activity.spatio_temporal_constraint'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('id', 'str', '0.1',
                ""),
            ('name', 'str', '1.1',
                ""),
            ('options', 'activity.numerical_requirement_option', '0.N',
                ""),
            ('requirement_type', 'str', '1.1',
                "Type of reqirement to which the experiment must conform."),
            ('source', 'shared.data_source', '0.1',
                ""),
            ]
    }


def numerical_requirement_option():
    """A NumericalRequirement that is being used as a set of related requirements; For example if a requirement is to use 1 of 3 boundary conditions, then that "parent" requirement would have three "child" RequirmentOptions (each of one with the XOR optionRelationship).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('id', 'str', '0.1',
                ""),
            ('name', 'str', '1.1',
                ""),
            ('relationship', 'str', '0.1',
                "Describes how this optional (child) requirement is related to its sibling requirements.  For example, a NumericalRequirement could consist of a set of optional requirements each with an "OR" relationship meaning use this boundary condition _or_ that one."),
            ('sub_options', 'activity.numerical_requirement_option', '0.N',
                ""),
            ]
    }


def output_requirement():
    """Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_requirement",
        'base-hierarchy': [
            'activity.numerical_requirement'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'id',
            'name',
            'options',
            'requirement_type',
            'source',
            ],
        'properties-inherited': [
            'description :: activity.numerical_requirement',
            'id :: activity.numerical_requirement',
            'name :: activity.numerical_requirement',
            'options :: activity.numerical_requirement',
            'requirement_type :: activity.numerical_requirement',
            'source :: activity.numerical_requirement',
            ]
    }


def physical_modification():
    """Physical modification is the implementation of a boundary condition numerical requirement that is achieved within the model code rather than from some external source file. It  might include, for example,  a specific rate constant within a chemical reaction, or coefficient value(s) in a parameterisation.  For example, one might require a numerical experiment where specific chemical reactions were turned off - e.g. no heterogeneous chemistry.

	"""
    return {
        'type': 'class',
        'base': "activity.conformance",
        'base-hierarchy': [
            'activity.conformance'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ],
        'properties-all': [
            'description',
            'frequency',
            'is_conformant',
            'requirements',
            'sources',
            'type',
            ],
        'properties-inherited': [
            'description :: activity.conformance',
            'frequency :: activity.conformance',
            'is_conformant :: activity.conformance',
            'requirements :: activity.conformance',
            'sources :: activity.conformance',
            'type :: activity.conformance',
            ]
    }


def simulation():
    """A simulation is the implementation of a numerical experiment.  A simulation can be made up of "child" simulations aggregated together to form a simulation composite.  The parent simulation can be made up of whole or partial child simulations, the simulation attributes need to be able to capture this.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_activity",
        'base-hierarchy': [
            'activity.numerical_activity',
            'activity.activity'
            ],
        'base-hierarchy-depth': 2,
        'sub-classes': [
            'activity.simulation_composite',
            'activity.simulation_run'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('authors', 'str', '0.1',
                "List of associated authors."),
            ('calendar', 'shared.calendar', '1.1',
                ""),
            ('conformances', 'activity.conformance', '0.N',
                ""),
            ('control_simulation', 'activity.simulation', '0.1',
                "Points to a simulation being used as the basis (control) run.  Note that only "derived" simulations can describe something as being control; a simulation should not know if it is being used itself as the control of some other run."),
            ('deployments', 'software.deployment', '0.N',
                ""),
            ('inputs', 'software.coupling', '0.N',
                "Implemented as a mapping from a source to target; can be a forcing file, a boundary condition, etc."),
            ('outputs', 'data.data_object', '0.N',
                ""),
            ('restarts', 'data.data_object', '0.N',
                ""),
            ('simulation_id', 'str', '0.1',
                ""),
            ('spinup_date_range', 'shared.closed_date_range', '0.1',
                "The date range that a simulation is engaged in spinup."),
            ('spinup_simulation', 'activity.simulation', '0.1',
                "The (external) simulation used during "spinup."  Note that this element can be used in conjuntion with spinupDateRange.  If a simulation has the latter but not the former, then one can assume that the simulation is performing its own spinup."),
            ],
        'properties-all': [
            'authors',
            'calendar',
            'conformances',
            'control_simulation',
            'deployments',
            'description',
            'funding_sources',
            'inputs',
            'long_name',
            'outputs',
            'projects',
            'rationales',
            'responsible_parties',
            'restarts',
            'short_name',
            'simulation_id',
            'spinup_date_range',
            'spinup_simulation',
            'supports',
            ],
        'properties-inherited': [
            'description :: activity.numerical_activity',
            'funding_sources :: activity.activity',
            'long_name :: activity.numerical_activity',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            'short_name :: activity.numerical_activity',
            'supports :: activity.numerical_activity',
            ]
    }


def simulation_composite():
    """A SimulationComposite is an aggregation of Simulations. With the aggreation connector between Simulation and SimulationComposite(SC) the SC can be made up of both SimulationRuns and SCs. The SimulationComposite is the new name for the concept of SimulationCollection: A simulation can be made up of "child" simulations aggregated together to form a "simulation composite".  The "parent" simulation can be made up of whole or partial child simulations and the SimulationComposite attributes need to be able to capture this.

	"""
    return {
        'type': 'class',
        'base': "activity.simulation",
        'base-hierarchy': [
            'activity.simulation',
            'activity.numerical_activity',
            'activity.activity'
            ],
        'base-hierarchy-depth': 3,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('child', 'activity.simulation', '0.N',
                ""),
            ('date_range', 'shared.date_range', '1.1',
                ""),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('rank', 'int', '1.1',
                "Position of a simulation in the SimulationComposite timeline. eg:  Is this the first (rank = 1) or second (rank = 2) simulation"),
            ],
        'properties-all': [
            'authors',
            'calendar',
            'child',
            'conformances',
            'control_simulation',
            'date_range',
            'deployments',
            'description',
            'funding_sources',
            'inputs',
            'long_name',
            'meta',
            'outputs',
            'projects',
            'rank',
            'rationales',
            'responsible_parties',
            'restarts',
            'short_name',
            'simulation_id',
            'spinup_date_range',
            'spinup_simulation',
            'supports',
            ],
        'properties-inherited': [
            'authors :: activity.simulation',
            'calendar :: activity.simulation',
            'conformances :: activity.simulation',
            'control_simulation :: activity.simulation',
            'deployments :: activity.simulation',
            'description :: activity.numerical_activity',
            'funding_sources :: activity.activity',
            'inputs :: activity.simulation',
            'long_name :: activity.numerical_activity',
            'outputs :: activity.simulation',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            'restarts :: activity.simulation',
            'short_name :: activity.numerical_activity',
            'simulation_id :: activity.simulation',
            'spinup_date_range :: activity.simulation',
            'spinup_simulation :: activity.simulation',
            'supports :: activity.numerical_activity',
            ]
    }


def simulation_relationship():
    """Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

	"""
    return {
        'type': 'class',
        'base': "shared.relationship",
        'base-hierarchy': [
            'shared.relationship'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('target', 'activity.simulation_relationship_target', '1.1',
                ""),
            ('type', 'activity.simulation_relationship_type', '1.1',
                ""),
            ],
        'properties-all': [
            'description',
            'target',
            'type',
            ],
        'properties-inherited': [
            'description :: shared.relationship',
            ]
    }


def simulation_relationship_target():
    """Creates and returns instance of simulation_relationship_target class.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('simulation', 'shared.doc_reference', '0.1',
                ""),
            ('target', 'activity.simulation_type', '0.1',
                ""),
            ]
    }


def simulation_run():
    """A SimulationRun is, as the name implies, one single model run. A SimulationRun is a Simulation. There is a one to one association between SimulationRun and (a top-level) SoftwarePackage::ModelComponent.

	"""
    return {
        'type': 'class',
        'base': "activity.simulation",
        'base-hierarchy': [
            'activity.simulation',
            'activity.numerical_activity',
            'activity.activity'
            ],
        'base-hierarchy-depth': 3,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('date_range', 'shared.date_range', '1.1',
                ""),
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('model', 'software.model_component', '0.1',
                ""),
            ],
        'properties-all': [
            'authors',
            'calendar',
            'conformances',
            'control_simulation',
            'date_range',
            'deployments',
            'description',
            'funding_sources',
            'inputs',
            'long_name',
            'meta',
            'model',
            'outputs',
            'projects',
            'rationales',
            'responsible_parties',
            'restarts',
            'short_name',
            'simulation_id',
            'spinup_date_range',
            'spinup_simulation',
            'supports',
            ],
        'properties-inherited': [
            'authors :: activity.simulation',
            'calendar :: activity.simulation',
            'conformances :: activity.simulation',
            'control_simulation :: activity.simulation',
            'deployments :: activity.simulation',
            'description :: activity.numerical_activity',
            'funding_sources :: activity.activity',
            'inputs :: activity.simulation',
            'long_name :: activity.numerical_activity',
            'outputs :: activity.simulation',
            'projects :: activity.activity',
            'rationales :: activity.activity',
            'responsible_parties :: activity.activity',
            'restarts :: activity.simulation',
            'short_name :: activity.numerical_activity',
            'simulation_id :: activity.simulation',
            'spinup_date_range :: activity.simulation',
            'spinup_simulation :: activity.simulation',
            'supports :: activity.numerical_activity',
            ]
    }


def spatio_temporal_constraint():
    """Contains a set of relationship types specific to a simulation document that can be used to describe its genealogy.

	"""
    return {
        'type': 'class',
        'base': "activity.numerical_requirement",
        'base-hierarchy': [
            'activity.numerical_requirement'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('date_range', 'shared.date_range', '0.1',
                ""),
            ('spatial_resolution', 'activity.resolution_type', '0.1',
                ""),
            ],
        'properties-all': [
            'date_range',
            'description',
            'id',
            'name',
            'options',
            'requirement_type',
            'source',
            'spatial_resolution',
            ],
        'properties-inherited': [
            'description :: activity.numerical_requirement',
            'id :: activity.numerical_requirement',
            'name :: activity.numerical_requirement',
            'options :: activity.numerical_requirement',
            'requirement_type :: activity.numerical_requirement',
            'source :: activity.numerical_requirement',
            ]
    }




