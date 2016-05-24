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
ID = ''

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
DESCRIPTION = ''

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

SUB_PROCESSES['si_radiative_process_methods'] = {
    'description': 'Collected properties of radiation in sea ice thermodynamics',
    'details': ['radiative_process_details',]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESSES_DETAILS = OrderedDict()

SUB_PROCESSES_DETAILS['radiative_process_methods'] = {
    'description':'Additional information about radiative processes in sea ice.',
    'properties': [
        ('surface_albedo', 'str', '0.1',
         'Method used to handle surface albedo'),
        ('ice_radiation_transmission', 'str', '0.1',
         'Method by which solar radiation through ice is handled'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
