CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.grid', e.g. 'cmip6.atmosphere.grid'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere.grid'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.grid'

from collections import OrderedDict

# ====================================================================
# GRID: PROPERTIES
# ====================================================================
DESCRIPTION = ''

# ====================================================================
# GRID: DISCRETISATION
# ====================================================================
DISCRETISATION = OrderedDict()

DISCRETISATION['grid_discretisation'] = {
    'description': '',
    'details': ['horizontal_discretisation',]
},

# ====================================================================
# GRID: DISCRETISATION: DETAILS
#
# URL of #details
# ====================================================================
DISCRETISATION_DETAILS = OrderedDict()

DISCRETISATION_DETAILS['horizontal_discretisation'] = {
    'description': 'Horizontal discretisation scheme',
    'properties': [
        ('scheme_type', 'ENUM:dynamical_core_discretisation_horizontal_type', '1.1',
         'Horizontal discretisation type'),
        ('scheme_method', 'ENUM:dynamical_core_discretisation_horizontal_method', '1.1',
         'Horizontal discretisation method'),
        ('scheme_order', 'ENUM:dynamical_core_discretisation_horizontal_order', '1.1',
         'Horizontal discretisation function order'),
        ('horizontal_pole', 'ENUM:dynamical_core_discretisation_horizontal_pole', '1.1',
         'Horizontal discretisation pole singularity treatment'),
    ]
}

# ====================================================================
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================
ENUMERATIONS = OrderedDict()

ENUMERATIONS['dynamical_core_discretisation_horizontal_type'] = {
    'description': 'Type of horizontal discretisation scheme',
    'members': [
        ('spectral', None),
        ('fixed grid', None),
        ('other', None),
    ]
}

ENUMERATIONS['dynamical_core_discretisation_horizontal_method'] = {
    'description': 'If the scheme type is fixed grid, describe the scheme method for the horizontal discretisation scheme',
    'members': [
        ('finite elements', None),
        ('finite volumes', None),
        ('finite difference', None),
        ('centered finte difference', None),
    ]
}

ENUMERATIONS['dynamical_core_discretisation_horizontal_order'] = {
    'description': 'If the scheme method is finite difference or centered finite difference describe the scheme ' +
    'order of the finite difference method used by the horizontal discretisation scheme',
    'members': [
    ]
}

ENUMERATIONS['dynamical_core_discretisation_horizontal_pole'] = {
    'description': 'Method used to handle the pole singularities',
    'members': [
        ('filter', None),
        ('pole rotation', None),
        ('artificial island', None),
        ('none', None),
        ('other', None),
    ]
}
