ID = 'cmip6.grid'

TYPE = 'science.grid'

CIM = '2.0'

CONTACT = 'David Hassell (e-mail)'

AUTHORS = 'David Hassell'

DATE = '2016-03-11'

VERSION = ''

# ====================================================================
# PROPERTIES
# ====================================================================
PROPERTIES = {

    # ----------------------------------------------------------------
    # MANIFEST
    # ----------------------------------------------------------------
    'name': '',
    'description': '',

    'discretisation': ['discretisation',
                   ],

    # ----------------------------------------------------------------
    # DETAILS
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # DISCRETISATION
    # ----------------------------------------------------------------
    'discretisation': {
        'short_name': '',
        'description': '',
        'details': [('horizontal_discretisation',
                     'scheme_type', 'scheme_method', 'scheme_order', 'horizontal_pole'),
                ],
    },
    
    # ----------------------------------------------------------------
    # DISCRETISATION DETAILS
    # ----------------------------------------------------------------
    'horizontal_discretisation': {
        'short_name': 'Horizontal discretisation scheme',
        'description': 'Horizontal discretisation scheme',
        'scheme_type': (
            'ENUM:dynamical_core_discretisation_horizontal_type', '1.1',
            'Horizontal discretisation type'),
        'scheme_method': (
            'ENUM:dynamical_core_discretisation_horizontal_method', '1.1',
            'Horizontal discretisation method'),
        'scheme_order': (
            'ENUM:dynamical_core_discretisation_horizontal_order', '1.1',
            'Horizontal discretisation function order'),
        'horizontal_pole': (
            'ENUM:dynamical_core_discretisation_horizontal_pole', '1.1',
            'Horizontal discretisation pole singularity treatment'),
    },
    
}

# ====================================================================
# ENUMERATIONS
# ====================================================================
ENUMS = {

    'dynamical_core_discretisation_horizontal_type': {
        'short_name': 'Dynamical core discretisation horizontal type',
        'description': 'Type of horizontal discretisation scheme',
        'members': [
            ('spectral', None),
            ('fixed grid', None),
            ('other', None),
        ]
    },

    'dynamical_core_discretisation_horizontal_method': {
        'short_name': 'Dynamical core discretisation horizontal method',
        'description': 'If the scheme type is fixed grid, describe the scheme method for the horizontal discretisation scheme',
        'members': [
            ('finite elements', None),
            ('finite volumes', None),
            ('finite difference', None),
            ('centered finte difference', None),
        ]
    },

    'dynamical_core_discretisation_horizontal_order': {
        'short_name': 'Dynamical core discretisation horizontal order',
        'description': 'If the scheme method is finite difference or centered finite difference describe the scheme ' +
                       'order of the finite difference method used by the horizontal discretisation scheme',
        'members': [
        ]
    },

    'dynamical_core_discretisation_horizontal_pole': {
        'short_name': 'Dynamical core discretisation horizontal pole',
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
