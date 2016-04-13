AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.grid'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.grid'

QC_STATUS = 'draft'

# ====================================================================
# GRID: PROPERTIES
# ====================================================================
DESCRIPTION = ''

# ====================================================================
# GRID: DISCRETISATION
# ====================================================================
DISCRETISATION = {
    'description': '',
    'details': ['horizontal_discretisation',]
},

# ====================================================================
# GRID: DISCRETISATION: DETAILS
#
# URL of #details
# ====================================================================
DISCRETISATION_DETAILS = {    
    'horizontal_discretisation': {
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
    },
}

# ====================================================================
# GRID: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================
ENUMERATIONS = {
    'dynamical_core_discretisation_horizontal_type': {
        'description': 'Type of horizontal discretisation scheme',
        'members': [
            ('spectral', None),
            ('fixed grid', None),
            ('other', None),
        ]
    },

    'dynamical_core_discretisation_horizontal_method': {
        'description': 'If the scheme type is fixed grid, describe the scheme method for the horizontal discretisation scheme',
        'members': [
            ('finite elements', None),
            ('finite volumes', None),
            ('finite difference', None),
            ('centered finte difference', None),
        ]
    },

    'dynamical_core_discretisation_horizontal_order': {
        'description': 'If the scheme method is finite difference or centered finite difference describe the scheme ' +
                       'order of the finite difference method used by the horizontal discretisation scheme',
        'members': [
        ]
    },

    'dynamical_core_discretisation_horizontal_pole': {
        'description': 'Method used to handle the pole singularities',
        'members': [
            ('filter', None),
            ('pole rotation', None),
            ('artificial island', None),
            ('none', None),
            ('other', None),
        ]
    },

}
