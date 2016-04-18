# --------------------------------------------------------------------
# See http://wordpress.es-doc.org for documentation on how to create
# CMIP6 specialisations
# --------------------------------------------------------------------

CONTACT = None

AUTHORS = None

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# GRID IDENTIFIER
#
# Set to 'cmip6.grid' or 'cmip6.<REALM>.grid',
# e.g. 'cmip6.atmosphere.grid'
# --------------------------------------------------------------------
ID = None

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.grid'

from collections import OrderedDict

# --------------------------------------------------------------------
# GRID: PROPERTIES
# --------------------------------------------------------------------
DESCRIPTION = None

# --------------------------------------------------------------------
# GRID: DETAILS
#
# URL of #details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# GRID: DISCRETISATION
# --------------------------------------------------------------------
DISCRETISATION = OrderedDict()

# --------------------------------------------------------------------
# GRID: DISCRETISATION: DETAILS
#
# URL of #details
# --------------------------------------------------------------------
DISCRETISATION_DETAILS = OrderedDict()

# --------------------------------------------------------------------
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()
