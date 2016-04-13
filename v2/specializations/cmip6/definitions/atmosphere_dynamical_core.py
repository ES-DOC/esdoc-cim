AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.dynamical_core'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.process'

QC_STATUS = 'draft'

# ====================================================================
# PROCESS: PROPERTIES
# ====================================================================
DESCRIPTION = ''

# ====================================================================
# PROCESS: DETAILS
#
# URL of #details
# ====================================================================
DETAILS = {
    'timestepping_framework': {
        'description': 'Timestepping framework',
        'properties': [
            ('timestepping_type', 'ENUM:timestepping_type', '1.1',
             'Timestepping framework type'),
        ]
    },

    'prognostic_variables': {
        'description': 'List of the model prognostic variables',
        'properties': [
            ('prognostic_variables', 'ENUM:_prognostic_variables', '1.N',
             'prognostic variables'),
        ]
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================
SUB_PROCESSES = {    
    'top_boundary': {
        'description': 'Type of boundary layer at the top of the model',
        'details': ['top_boundary_details']
    },

    'lateral_boundary': {
        'description': 'Type of lateral boundary condition (if the model is a regional model)',
        'details': ['lateral_boundary_details']
    },

    'diffusion_horizontal': {
        'description': 'Horizontal diffusion scheme',
        'details': ['diffusion_horizontal_details'],
    },

    'advection_tracers': {
        'description': 'Tracer advection scheme',
        'details': ['advection_tracers_details']
    },
    
    'advection_momentum': {
        'description': 'Momentum advection scheme',
        'details': ['advection_momentum_details'],
    },
    
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = {   
    'top_boundary_details': {
        'description': 'Properties of boundary layer at the top of the model',
        'properties': [
            ('top_boundary_condition', 'ENUM:top_boundary_condition', '1.1',
             'Top boundary condition'),
            ('top_heat', 'str', '1.1',
             'Top boundary heat treatment'),
            ('top_wind', 'str', '1.1',
             'Top boundary wind treatment'),
        ]
    },

    'lateral_boundary_details': {
        'description': 'Type of lateral boundary condition',
        'properties': [
            ('lateral_boundary_condition', 'ENUM:lateral_boundary', '0.1',
             'Lateral boundary condition'),
        ]
    },

    'diffusion_horizontal_details': {
        'description': 'Horizontal diffusion scheme details',
        'properties': [
            ('scheme_name', 'ENUM:diffusion_horizontal_scheme_name ', '1.1',
             'Horizontal diffusion scheme name'),
            ('scheme_method', 'ENUM:diffusion_horizontal_scheme_method', '1.1',
             'Horizontal diffusion scheme method'),
        ]
    },

    'advection_tracers_details': {
        'description': 'Tracer advection scheme',
        'properties': [
            ('scheme_name', 'ENUM:advection_tracers_scheme_name ', '1.1',
             'Tracer advection scheme name'),
            ('scheme_characteristics', 'ENUM:advection_tracers_scheme_characteristics', '1.N',
             'Tracer advection scheme characteristics'),
            ('conserved_quantities', 'ENUM:advection_tracers_conserved_quantities', '1.N',
             'Tracer advection scheme conserved quantities'),
            ('conservation_method', 'ENUM:advection_tracers_conservation_method', '1.1',
             'Tracer advection scheme conservation method'),
        ]
    },
    
    'advection_momentum_details': {
        'description': 'Momentum advection scheme',
        'properties': [
            ('scheme_name', 'ENUM:advection_momentum_scheme_name ', '1.1',
             'Momentum advection schemes name'),
            ('scheme_characteristics', 'ENUM:advection_momentum_scheme_characteristics', '1.N',
             'Momentum advection scheme characteristics'),
            ('scheme_staggering_type', 'ENUM:advection_momentum_scheme_staggering_type', '1.1',
             'Momentum advection scheme staggering type'),
            ('conserved_quantities', 'ENUM:advection_momentum_conserved_quantities', '1.N',
            'Momentum advection scheme conserved quantities'),
            ('conservation_method', 'ENUM:advection_momentum_conservation_method', '1.1',
             'Momentum advection scheme conservation method'),
        ]
    },
}

# ====================================================================
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================
ENUMERATIONS = {

    'timestepping_type': {
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

    'top_boundary_condition': {
        'description': 'Type of boundary layer at the top of the model',
        'members': [
            ('sponge layer', None),
            ('radiation boundary condition', None),
            ('other', None),
        ]
    },

    'lateral_boundary_attribute': {
        'description': 'Type of lateral boundary condition (if the model is a regional model)',
        'members': [
            ('sponge layer', None),
            ('radiation boundary condition', None),
            ('none', None),
            ('other', None),
        ]
    },

    'prognostic_variables_attributes': {
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

    'diffusion_horizontal_scheme_name': {
        'description': 'Commonly used name for the horizontal diffusion scheme',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'diffusion_horizontal_scheme_method': {
        'description': 'Numerical method used by the horizontal diffusion scheme',
        'members': [
            ('iterated Laplacian', None),
            ('other', None),
        ]
    },

    'advection_tracers_scheme_name': {
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

    'advection_tracers_scheme_characteistics': {
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

    'advection_tracers_conserved_quantities': {
        'description': 'Quantities conserved through the tracers advection scheme',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'advection_tracers_conservation_method': {
        'description': 'Method used to ensure conservation in the tracers advection scheme',
        'members': [
            ('conservation fixer', None),
            ('other', None),
        ]
    },
   
    'advection_momentum_scheme_name': {
        'description': 'Commonly used name for the momentum advection scheme',
        'members': [
            ('VanLeer', None),
            ('Janjic', None),
            ('SUPG (Streamline Upwind Petrov-Galerkin)', None),
            ('other', None),
        ]
    },

    'advection_momentum_scheme_characteristics': {
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

    'advection_momentum_scheme_staggering_type': {
        'description': 'If scheme characteristics specify staggered grid, describe the type of staggering',
        'members': [
            ('Arakawa B-grid', None),
            ('Arakawa C-grid', None),
            ('Arakawa D-grid', None),
            ('Arakawa E-grid', None),
            ('other', None),
        ]
    },

    'advection_momentum_conserved_quantities': {
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

    'advection_momentum_conservation_method': {    
        'description': 'Method used to ensure conservation in the tracers advection scheme',
        'members': [
            ('conservation fixer', None),
            ('other', None),
        ]
    },

}
