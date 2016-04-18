CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# REALM IDENTIFIER
#
# Set to 'cmip6.<REALM>', e.g. 'cmip6.atmosphere'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.scientific_realm'

from collections import OrderedDict

# ====================================================================
# REALM: PROPERTIES
# ====================================================================
DESCRIPTION = ''

NAME = 'atmosphere'

REALM = 'atmosphere'

OVERVIEW = ''

GRID = ['atmosphere_grid']

KEY_PROPERTIES = ['atmosphere_key_properties']

PROCESSES = ['atmosphere_cloud_scheme',
             'atmosphere_cloud_simulator',
             'atmosphere_dynamical_core',
             'atmosphere_gravity_waves',
             'atmosphere_microphysics_precipitation',
             'atmosphere_radiation',
             'atmosphere_turbulence_convection',
         ]
