ID = 'cmip6.atmosphere.turbulance_convection'

TYPE = 'science.process'

CIM = '2.0'

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
    'short_name': 'Atmosphere Convective Turbulence and Clouds',              
    'description': 'Atmosphere Convective Turbulence and Clouds',             

    'sub_process': ['boundary_layer_turbulence_scheme',
                    'deep_convection_scheme',
                    'shallow_convection_scheme',
                    'other_convection_scheme',
                ],
                    
    # ----------------------------------------------------------------
    # DETAILS
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # SUB-PROCESSES
    # ----------------------------------------------------------------
    'boundary_layer_turbulence_scheme': {        
        'short_name': 'Boundary layer turbulence scheme',
        'description': 'Boundary layer turbulence scheme',
        'details': [('boundary_layer_turbulence_scheme_details',
                     'scheme_name',
                     'scheme_type',
                     'closure_order',
                     'counter_gradient'),
                ],
    },
    
    'deep_convection_scheme': {
        'short_name': 'Deep convection scheme',
        'description': 'Deep convection scheme',
        'details': [('deep_convection_scheme_details',
                     'scheme_name',
                     'scheme_type',
                     'scheme_method',
                     'processes'),
                ],
    },
        
    'shallow_convection_scheme': {
        'short_name': 'Shallow convection scheme',
        'description': 'Shallow convection scheme',
        'details': [('shallow_convection_scheme_details',
                     'selection',                     
                     'scheme_type',                     
                     'scheme_name',
                     'processes'),
                ],
    },

    'other_convection_scheme_details': {
        'short_name': 'Other convection scheme.',
        'description': 'Other convection scheme.',
        'details': [('other_convection_scheme_details',
                     'scheme_name',
                     'scheme_type'),
                ],
    },        

    # ----------------------------------------------------------------
    # SUB-PROCESS DETAILS
    # ----------------------------------------------------------------
    'boundary_layer_turbulence_scheme_details': {        
        'short_name': 'Properties of boundary layer turbulence scheme',
        'description': 'Properties of boundary layer turbulence scheme',
        'scheme_name': (
            'ENUM:boundary_layer_turbulence_scheme_name', '1.1',
            'Boundary layer turbulence scheme name'),
        'scheme_type': (
            'ENUM:boundary_layer_turbulence_scheme_type', '1.1',
            'Boundary layer turbulence scheme type'),
        'closure_order': (
            'int', '1.1',
            'Boundary layer turbulence scheme closure order'),
        'counter_gradient': (
            'bool', '1.1',
            'Uses boundary layer turbulence scheme counter gradient'),        
    },
    
    'deep_convection_scheme_details': {
        'short_name': 'Properties of deep convection scheme',
        'description': 'Properties of deep convection scheme',
        'scheme_name': (
            'str', '1.1',
            'Deep convection scheme name'),
        'scheme_type': (
            'ENUM:deep_convection_scheme_type', '1.1',
            'Deep convection scheme type'),
        'scheme_method': (
            'ENUM:deep_convection_scheme_method', '1.N', 
            'Deep convection scheme method'),
        'processes': (
            'ENUM:deep_convection_scheme_processes_attributes', '1.N',
            'Deep convection scheme processes'),
    },
        
    'shallow_convection_scheme_details': {
        'short_name': 'Properties of shallow convection scheme',
        'description': 'Properties of shallow convection scheme',
        'selection': (
            'ENUM:shallow_convection_scheme_method', '1.1',
            'shallow convection scheme method'),
        'scheme_type': (
            'ENUM:shallow_convection_scheme_type', '1.1',
            'shallow convection scheme type'),
        'scheme_name': (
            'str', '1.1',
            'Shallow convection scheme name'),
        'processes': (
            'ENUM:shallow_convection_scheme_processes_attributes', '1.N',
            'Physical processes taken into account in the parameterisation of shallow convection'),
    },

    'other_convection_scheme_details': {
        'short_name': 'Properties of other convection scheme',
        'description': 'Properties of other convection scheme',
        'scheme_name': (
            'str', '1.1',
            'Other convection scheme name'),
        'scheme_type': (
            'ENUM:other_convection_scheme_type', '1.1', 
            'Other convection scheme type'),
    },        
}

# ====================================================================
# ENUMERATIONS
# ====================================================================
ENUMERATIONS = {

    'boundary_layer_turbulence_scheme_name': {
        'short_name': '',
        'description': 'Commonly used name for the boundary layer turbulence scheme.',
        'members': [
            ('Mellor-Yamada', None),
            ('other', None),
        ]
    },

    'boundary_layer_turbulence_scheme_type': {
        'short_name': 'Boundary layer turbulence scheme type',
        'description': 'Type of scheme used for the parameterisation of turbulence in the boundary layer.',
        'members': [
            ('TKE prognostic', None),
            ('TKE diagnostic', None),
            ('TKE coupled with water', None),
            ('vertical profile of Kz', None),
            ('other', None),
        ]
    },

    'deep_convection_scheme_type': {
        'short_name': 'Deep convection scheme type',
        'description': 'Type of scheme used for the parameterisation of deep convection.'  ,
        'members': [
            ('mass-flux', None),
            ('adjustment', None),
            ('other', None),
        ]
    },

    'deep_convection_scheme_method': {
        'short_name': 'Deep convection scheme method',
        'description': 'If deep convection uses a mass-flux scheme enter the method used.',
        'members': [
            ('CAPE', 'Mass flux determined by CAPE'),
            ('bulk', 'A bulk mass flux scheme is used'),
            ('other', None),
        ]
    },

    'shallow_convection_scheme_method': {
        'short_name': 'Shallow convection scheme method',
        'description': 'Method used for shallow convection.',
        'members': [
            ('same as deep (unified)', None),
            ('included in boundary layer turbulence', None),
            ('separated', None),
        ]
    },

    'shallow_convection_scheme_type': {
        'short_name': 'Shallow convection scheme type',
        'description': 'Type of scheme used for the parameterisation of shallow convection.',
        'members': [
            ('mass-flux', None),
            ('other', None),
            ('none', None),
        ]
    },


    'deep_convection_scheme_processes_attributes': {
        'short_name': 'deep_convection_scheme_processes_attributes',
        'description': 'deep_convection_scheme_processes_attributes',
        'members': [
            ('vertical momentum transport', None),
            ('convective momentum transport', None),
            ('entrainment', None),
            ('detrainment', None),
            ('penetrative convection', None),
            ('updrafts and downdrafts', None),
            ('radiative effect of anvils', None),
            ('other', None),
        ]
    },

}
