# --------------------------------------------------------------------
# See http://wordpress.es-doc.org for documentation on how to create
# CMIP6 process specialisations
# --------------------------------------------------------------------

# ====================================================================
# FILE VARIABLES
# ====================================================================
CONTACT = ''

AUTHORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# GRID IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>'
# --------------------------------------------------------------------
ID = 'cmip6.seaice.dynamics'

# ====================================================================
# INTERNAL VARIABLES (do not change)
# ====================================================================
_TYPE = 'cim.2.science.grid'
from collections import OrderedDict

# ====================================================================
# MODEL DESCRIPTION VARIABLES
# ====================================================================

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the Sea Ice Dynamics'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['horizontal_advection'] = {
    'description': 'Method of horizontal advection',
    'details': ['horizontal_advection_method']
}

SUB_PROCESSES['transport_in_thickness_space'] = {
    'description': 'Method of ice migration in thickness',
    'details': ['transport_in_thickness_space_method']
}

SUB_PROCESSES['redistribution'] = {
    'description': 'Sea Ice Redistribution',
    'details': ['redistribution_details']
}

SUB_PROCESSES['rheology'] = {
    'description': 'Sea ice deformation',
    'details': ['ice_deformation_method']
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESSES_DETAILS = OrderedDict()

SUB_PROCESSES_DETAILS['horizontal_advection_method'] = (
    'ENUM:transport_methods', '0.1',
    'Method of horizontal advection')

SUB_PROCESSES_DETAILS['transport_in_thickness_space_method'] = (
    'ENUM:transport_methods', '0.1',
    'Method of ice migration in thickness')
       
SUB_PROCESSES_DETAILS['redistribution_details'] = {
    'properties': [
        ('processes', 'ENUM:redistribution_types', '0,N',
         'Additional processes which can redistribute sea ice.'),        
        ('ice_strength_formulation', 'str', '0.1',
         'Describe how ice-strength is formulated'),
    ]
}

SUB_PROCESSES_DETAILS['ice_deformation_method'] = (
    'ENUM:rheology_types', '1.1'
    'Ice deformation method')

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['transport_methods'] = {
    'description': 'Transport Methods',
    'members': [
        ('Incremental Re-mapping', '(including Semi-Lagrangian)'),
        ('Prather', None),
        ('Eulerian', None)
    ]
}

ENUMERATIONS['redistribution_types'] = {
    'description':'Sea Ice Redistribution Types',
    'members': [
        ('Rafting', None),
        ('Ridging', None),
    ]
}

ENUMERATIONS['rheology_types'] = {
    'description': 'Sea Ice rheology types',
    'members': [
        ('free-drift', None),
        ('Mohr-Coloumb', None),
        ('visco-plastic', None),
        ('elastic-visco-plastic', 'EVP'),
        ('granular', None),
        ('other', None)
    ]
}


