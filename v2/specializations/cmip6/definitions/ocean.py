# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.scientific_realm'

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Eric Guilyardi'

# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization authors.
# --------------------------------------------------------------------
AUTHORS = 'Eric Guilyardi'
CONTRIBUTORS = 'David Hassle'
CHANGE_HISTORY = [
{'date':'now', 'what':'ewirfuhgweuyfgewy', 'who':'me'},
{'date':'now', 'what':'ewirfuhgweuyfgewy', 'who':'me'}
    ]

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# REALM IDENTIFIER
#
# Set to 'cmip6.<REALM>'
# --------------------------------------------------------------------
ID = 'cmip6.ocean'

# --------------------------------------------------------------------
# REALM: DESCRIPTION
#
# Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean realm specialization'

# --------------------------------------------------------------------
# REALM: REALM
#
# Canonical name for the domain of this scientific realm
# --------------------------------------------------------------------
REALM = 'ocean'

# --------------------------------------------------------------------
# REALM: GRID
#
# The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'ocean_grid'

# --------------------------------------------------------------------
# REALM: KEY PROPERTIES
#
# Key properties for the domain which differ from model defaults
# (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'ocean_key_properties'

# --------------------------------------------------------------------
# REALM: PROCESSES
#
# Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'ocean_timestepping_framework',
    'ocean_advection',
    'ocean_lateral_physics',
    'ocean_vertical_physics',
    'ocean_uplow_boundaries',
    'ocean_boundary_forcing',
    ]
