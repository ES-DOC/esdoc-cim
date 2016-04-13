ID = ''

TYPE = 'science.process'

CIM = ''

CONTACT = ''

AUTHORS = ''

DATE = ''

VERSION = ''

# ====================================================================
# PROPERTIES
# ====================================================================
PROPERTIES = {

    # ----------------------------------------------------------------
    # MANIFEST
    # ----------------------------------------------------------------
    'short_name': 'atmosphere dynamical core',
    'description': '',

    'details': [('timestepping_framework',
                 'timestepping_type'),
                ('prognostic_variables',
                 'prognostic_variables'),
            ],               
    
    'sub_process': ['top_boundary', 
                    'lateral_boundary',
                    'diffusion_horizontal',
                    'advection_tracers',
                    'advection_momentum',
                ],

    # ----------------------------------------------------------------
    # DETAILS
    # ----------------------------------------------------------------
    'timestepping_framework': {
        'short_name': 'Timestepping framework',
        'description': 'Timestepping framework',
        'timestepping_type': (
            'ENUM:dynamical_core_timestepping_type', '1.1',
            'Timestepping framework type'),
    },

    'prognostic_variables': {
        'short_name': 'Dynamical core prognostic variables',
        'description': 'List of the model prognostic variables',
        'prognostic_variables': (
            'ENUM:dynamical_core_prognostic_variables', '1.N',
            'prognostic variables'),
    },

    # ----------------------------------------------------------------
    # SUB-PROCESSES
    # ----------------------------------------------------------------
    'dynamical_core_top_boundary': {
        'short_name': 'Type of boundary layer at the top of the model',
        'description': 'Type of boundary layer at the top of the model',
        'details': [('dynamical_core_top_boundary_details',
                     'top_boundary_condition', 'top_heat', 'top_wind')
                ],
    },

    'lateral_boundary': {
        'short_name': 'Type of lateral boundary condition (if the model is a regional model)',
        'description': 'Type of lateral boundary condition (if the model is a regional model)',
        'details': [('lateral_boundary_details',
                     'lateral_boundary_condition'),
                ],
    },

    'diffusion_horizontal': {
        'short_name': 'Horizontal diffusion scheme',
        'description': 'Horizontal diffusion scheme',
        'details': [('diffusion_horizontal_details',
                     'scheme_name', 'scheme_method'),
                ],
    },

    'advection_tracers': {
        'short_name': 'Tracer advection scheme',
        'description': 'Tracer advection scheme',
        'details': [('advection_tracers_details',
                     'scheme_name', 'scheme_characteristics', 'conserved_quantities', 'conservation_method'),
                ],
    },
    
    'dynamical_core_advection_momentum': {
        'short_name': 'Momentum advection scheme',
        'description': 'Momentum advection scheme',
        'details': [('dynamical_core_advection_momentum_details',
                     'scheme_name', 'scheme_characteristics', 'scheme_staggering_type', 'conserved_quantities', 'conservation_method'),
                ],
    },
    
    # ----------------------------------------------------------------
    # SUB-PROCESS DETAILS
    # ----------------------------------------------------------------
    'dynamical_core_top_boundary_details': {
        'short_name': 'Properties of boundary layer at the top of the model',
        'description': 'Properties of boundary layer at the top of the model',
        'top_boundary_condition': (
            'ENUM:top_boundary_condition', '1.1',
            'Top boundary condition'),
        'top_heat': (
            'str', '1.1',
            'Top boundary heat treatment'),
        'top_wind': (
            'str', '1.1',
            'Top boundary wind treatment'),
    },

    'lateral_boundary_details': {
        'short_name': 'Type of lateral boundary condition',
        'description': 'Type of lateral boundary condition',
        'lateral_boundary_condition': (
            'ENUM:dynamical_core_lateral_boundary', '0.1',
            'Lateral boundary condition'),
    },

    'diffusion_horizontal_details': {
        'short_name': 'Horizontal diffusion scheme details',
        'description': 'Horizontal diffusion scheme details',
        'scheme_name': (
            'ENUM:dynamical_core_diffusion_horizontal_scheme_name ', '1.1',
            'Horizontal diffusion scheme name'),
        'scheme_method': (
            'ENUM:dynamical_core_diffusion_horizontal_scheme_method', '1.1',
            'Horizontal diffusion scheme method'),
    },

    'advection_tracers_details': {
        'short_name': 'Tracer advection scheme',
        'description': 'Tracer advection scheme',
        'scheme_name': (
            'ENUM:dynamical_core_advection_tracers_scheme_name ', '1.1',
            'Tracer advection scheme name'),
        'scheme_characteristics': (
            'ENUM:dynamical_core_advection_tracers_scheme_characteristics', '1.N',
            'Tracer advection scheme characteristics'),
        'conserved_quantities': (
            'ENUM:dynamical_core_advection_tracers_conserved_quantities', '1.N',
            'Tracer advection scheme conserved quantities'),
        'conservation_method': (
            'ENUM:dynamical_core_advection_tracers_conservation_method', '1.1',
            'Tracer advection scheme conservation method'),
    },
    
    'dynamical_core_advection_momentum_details': {
        'short_name': 'Momentum advection scheme',
        'description': 'Momentum advection scheme',
        'scheme_name': (
            'ENUM:dynamical_core_advection_momentum_scheme_name ', '1.1',
            'Momentum advection schemes name'),
        'scheme_characteristics': (
            'ENUM:dynamical_core_advection_momentum_scheme_characteristics', '1.N',
            'Momentum advection scheme characteristics'),
        'scheme_staggering_type': (
            'ENUM:dynamical_core_advection_momentum_scheme_staggering_type', '1.1',
            'Momentum advection scheme staggering type'),
        'conserved_quantities': (
            'ENUM:dynamical_core_advection_momentum_conserved_quantities', '1.N',
            'Momentum advection scheme conserved quantities'),
        'conservation_method': (
            'ENUM:dynamical_core_advection_momentum_conservation_method', '1.1',
            'Momentum advection scheme conservation method'),
    },

}

# ====================================================================
# ENUMERATIONS
# ====================================================================
ENUMERATIONS = {

    'dynamical_core_timestepping_type': {
        'short_name': 'Type of time stepping scheme',
        'description': 'Type of time stepping scheme',
        'members': [
            ('Adam Bashford', None),
            ('explicit', None),
            ('implicit', None),
            ('semi-implicit', None),
            ('leap frog', None),
            ('multi-step', None),
            ('Runge Kutta fifth order', None),
            ('Runge Kutta second order', None),
            ('Runge Kutta third order', None),
            ('other', None),
        ]
    },

    'dynamical_core_top_boundary_condition': {
        'short_name': 'Type of boundary layer at the top of the model',
        'description': 'Type of boundary layer at the top of the model',
        'members': [
            ('sponge layer', None),
            ('radiation boundary condition', None),
            ('other', None),
        ]
    },

    'dynamical_core_lateral_boundary_attribute': {
        'shoirt_name': 'Type of lateral boundary condition (if the model is a regional model)',
        'description': 'Type of lateral boundary condition (if the model is a regional model)',
        'members': [
            ('sponge layer', None),
            ('radiation boundary condition', None),
            ('none', None),
            ('other', None),
        ]
    },

    'dynamical_core_prognostic_variables_attributes': {
        'short_name': 'Dynamical core prognostic variables attributes',
        'description': 'List of the model prognostic variables',
        'members': [
            ('surface pressure', None),
            ('wind components', None),
            ('divergence/curl', None),
            ('temperature', None),
            ('potential temperature', None),
            ('total water', None),
            ('water vapour', None),
            ('water liquid', None),
            ('water ice', None),
            ('total water moments', None),
            ('clouds', None),
            ('radiation', None),
            ('other', None),
        ]
    },

    'dynamical_core_diffusion_horizontal_scheme_name': {
        'short_name': 'Dynamical core diffusion horizontal scheme name',
        'description': 'Commonly used name for the horizontal diffusion scheme',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'dynamical_core_diffusion_horizontal_scheme_method': {
        'short_name': 'Dynamical core diffusion horizontal scheme method',
        'description': 'Numerical method used by the horizontal diffusion scheme',
        'members': [
            ('iterated Laplacian', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_tracers_scheme_name': {
        'short_name': 'Dynamical core advection tracers scheme name',
        'description': 'Commonly used name for the tracer advection scheme',
        'members': [
            ('Heun', None),
            ('Roe and VanLeer', None),
            ('Roe and Superbee', None),
            ('Prather', None),
            ('UTOPIA', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_tracers_scheme_characteistics': {
        'short_name': 'Dynamical core advection tracers scheme characteistics',
        'description': 'Characteristics of the numerical scheme used for the advection of tracers',
        'members': [
            ('Eulerian', None),
            ('modified Euler', None),
            ('Lagrangian', None),
            ('semi-Lagrangian', None),
            ('cubic semi-Lagrangian', None),
            ('quintic semi-Lagrangian', None),
            ('mass-conserving', None),
            ('finite volume', None),
            ('flux-corrected', None),
            ('linear', None),
            ('quadratic', None),
            ('quartic', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_tracers_conserved_quantities': {
        'short_name': 'Dynamical core advection tracers conserved quantities',
        'description': 'Quantities conserved through the tracers advection scheme',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_tracers_conservation_method': {
        'short_name': 'Dynamical core advection tracers conservation method',
        'description': 'Method used to ensure conservation in the tracers advection scheme',
        'members': [
            ('conservation fixer', None),
            ('other', None),
        ]
    },
   
    'dynamical_core_advection_momentum_scheme_name': {
        'short_name': 'Dynamical core advection momentum scheme name',
        'description': 'Commonly used name for the momentum advection scheme',
        'members': [
            ('VanLeer', None),
            ('Janjic', None),
            ('SUPG (Streamline Upwind Petrov-Galerkin)', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_momentum_scheme_characteristics': {
        'short_name': 'Dynamical core advection momentum scheme characteistics',
        'description': 'Characteristics of the numerical scheme used for the advection of momentum',
        'members': [
            ('2nd order', None),
            ('4th order', None),
            ('cell-centred', None),
            ('staggered grid', None),
            ('semi-staggered grid', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_momentum_scheme_staggering_type': {
        'short_name': 'dynamical_core_advection_momentum_scheme_staggering_type',
        'description': 'If scheme characteristics specify staggered grid, describe the type of staggering',
        'members': [
            ('Arakawa B-grid', None),
            ('Arakawa C-grid', None),
            ('Arakawa D-grid', None),
            ('Arakawa E-grid', None),
            ('other', None),
        ]
    },

    'dynamical_core_advection_momentum_conserved_quantities': {
        'short_name': 'Dynamical core advection momentum conserved quantities',
        'description': 'Quantities conserved through the tracers advection scheme',
        'members': [
            ("Angular momentum", None),
            ("Horizontal momentum", None),
            ("Enstrophy", None),
            ("Mass", None),
            ("Total energy", None),
            ("Vorticity", None),
            ('Other', None)
        ]
    },

    'dynamical_core_advection_momentum_conservation_method': {    
        'short_name': 'Dynamical core advection momentum conservation method',
        'description': 'Method used to ensure conservation in the tracers advection scheme',
        'members': [
            ('conservation fixer', None),
            ('other', None),
        ]
    },

}
