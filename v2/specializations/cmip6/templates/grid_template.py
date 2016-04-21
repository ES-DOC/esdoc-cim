# --------------------------------------------------------------------
# See http://wordpress.es-doc.org for documentation on how to create
# CMIP6 grid specialisations
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
# Set to 'cmip6.<REALM>.grid'
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
# GRID: DESCRIPTION
#
# Scientific context of the grid
# --------------------------------------------------------------------
DESCRIPTION = ''

# --------------------------------------------------------------------
# GRID: DETAILS
#
# Sets of details for the grid
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# GRID: DISCRETISATION
#
# Description of the numerics of the discretisation
# --------------------------------------------------------------------
DISCRETISATION = OrderedDict()

# --------------------------------------------------------------------
# GRID: DISCRETISATION: DETAILS
#
# Sets of details for the discretisation
# --------------------------------------------------------------------
DISCRETISATION_DETAILS = OrderedDict()

# --------------------------------------------------------------------
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
