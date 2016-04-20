# --------------------------------------------------------------------
# See http://wordpress.es-doc.org for documentation on how to create
# CMIP6 specialisations
# --------------------------------------------------------------------

CONTACT = None

AUTHORS = None

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# REALM IDENTIFIER
#
# Set to 'cmip6.<REALM>', e.g. 'cmip6.atmosphere'
# --------------------------------------------------------------------
ID = None

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.scientific_realm'

from collections import OrderedDict

# --------------------------------------------------------------------
# REALM: PROPERTIES
# --------------------------------------------------------------------

# Scientific context of the realm
DESCRIPTION = None

# Name of the scientific realm
NAME = None

# Canonical name for the domain of this scientific area.
REALM = None

# Free text overview of the realm 
OVERVIEW = None

# The grid used to layout the variables
GRID = []

# Key properties for the domain which differ from model defaults
KEY_PROPERTIES = []

# Processes simulated within the realm
PROCESSES = []
