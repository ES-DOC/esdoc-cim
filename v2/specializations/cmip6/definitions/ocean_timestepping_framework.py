CONTACT = 'Eric Guilyardi'

AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>
# --------------------------------------------------------------------
ID = 'cmip6.ocean.timestepping_framework'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.key_properties'

from collections import OrderedDict

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of ocean time stepping framework'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['timestepping_attributes'] = {
    'description': 'Properties of time stepping in ocean',
    'properties': [
        ('time_step', 'int', '1.1',
         'Ocean time step in seconds'),
        ('diurnal_cycle', 'ENUM:diurnal_cycle_types', '1.1',
         'Diurnal cycle type'),
    ]
}

DETAILS['timestepping_tracers_scheme'] = (
    'ENUM:ocean_timestepping_types','1.1',
    'Time stepping tracer scheme')

DETAILS['barotropic_solver_schem'] = (
    'ENUM:ocean_timestepping_types','1.1',
    'Barotropic solver scheme')

DETAILS['barotropic_momentum_scheme'] = (
    'ENUM:ocean_timestepping_types','1.1',
    'Barotropic momentum scheme')


# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES: DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESSES_DETAILS = OrderedDict()

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['diurnal_cycle_types'] = {
    'description': 'Types of diurnal cycle resolution in ocean',
    'members': [
        ('None','No diurnal cycle in ocean'),
        ('Via coupling','Diurnal cycle via coupling frequency'),
        ('Specific treatment', 'Specific treament'),
    ]
}
    
ENUMERATIONS['ocean_timestepping_types'] = {
    'description': 'Type of timestepping scheme in ocean',
    'members': [
        ('Leap-frog + Asselin filter', 'Leap-frog scheme with Asselin filter'),
        ('Leap-frog + Periodic Euler backward solver', 'Leap-frog scheme with Periodic Euler backward solver'),
        ('Predictor-corrector', 'Predictor-corrector scheme'),
        ('AM3-LF (ROMS)', 'AM3-LF used in ROMS'),
        ('Forward-backward', 'Forward-backward scheme'),
    ]
}
