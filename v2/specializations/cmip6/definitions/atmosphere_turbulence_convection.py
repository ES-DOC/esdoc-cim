AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.turbulance_convection'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.process'

QC_STATUS = 'draft'

# ====================================================================
# PROCESS: PROPERTIES
# ====================================================================
DESCRIPTION = 'Atmosphere Convective Turbulence and Clouds'

# ====================================================================
# PROCESS: DETAILS
#
# URL of #details
# ====================================================================
DETAILS = {}

# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================
SUB_PROCESSES = {
    'boundary_layer_turbulence_scheme': {        
        'description': 'Boundary layer turbulence scheme',
        'details': ['boundary_layer_turbulence_scheme_details']
    },
    
    'deep_convection_scheme': {
        'description': 'Deep convection scheme',
        'details': ['deep_convection_scheme_details']
    },
        
    'shallow_convection_scheme': {
        'description': 'Shallow convection scheme',
        'details': ['shallow_convection_scheme_details']
    },

    'other_convection_scheme_details': {
        'description': 'Other convection scheme.',
        'details': ['other_convection_scheme_details']
    },        
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = {    
    'boundary_layer_turbulence_scheme_details': {        
        'description': 'Properties of boundary layer turbulence scheme',
        'properties': [
            ('scheme_name', 'ENUM:boundary_layer_turbulence_scheme_name', '1.1',
             'Boundary layer turbulence scheme name'),
            ('scheme_type', 'ENUM:boundary_layer_turbulence_scheme_type', '1.1',
             'Boundary layer turbulence scheme type'),
            ('closure_order', 'int', '1.1',
             'Boundary layer turbulence scheme closure order'),
            ('counter_gradient', 'bool', '1.1',
            'Uses boundary layer turbulence scheme counter gradient'),        
        ]
    },
    
    'deep_convection_scheme_details': {
        'description': 'Properties of deep convection scheme',
        'properties': [
            ('scheme_name', 'str', '1.1',
             'Deep convection scheme name'),
            ('scheme_type', 'ENUM:deep_convection_scheme_type', '1.1',
             'Deep convection scheme type'),
            ('scheme_method', 'ENUM:deep_convection_scheme_method', '1.N', 
             'Deep convection scheme method'),
            ('processes', 'ENUM:deep_convection_scheme_processes_attributes', '1.N',
             'Deep convection scheme processes'),
        ]
    },
        
    'shallow_convection_scheme_details': {
        'description': 'Properties of shallow convection scheme',
        'properties': [
            ('selection', 'ENUM:shallow_convection_scheme_method', '1.1',
             'shallow convection scheme method'),
            ('scheme_type', 'ENUM:shallow_convection_scheme_type', '1.1',
             'shallow convection scheme type'),
            ('scheme_name', 'str', '1.1',
             'Shallow convection scheme name'),
            ('processes', 'ENUM:shallow_convection_scheme_processes_attributes', '1.N',
             'Physical processes taken into account in the parameterisation of shallow convection'),
        ]
    },

    'other_convection_scheme_details': {
        'description': 'Properties of other convection scheme',
        'properties': [
            ('scheme_name', 'str', '1.1',
             'Other convection scheme name'),
            ('scheme_type', 'ENUM:other_convection_scheme_type', '1.1', 
             'Other convection scheme type'),
        ]
    },        
}

# ====================================================================
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================
ENUMERATIONS = {}

    'boundary_layer_turbulence_scheme_name': {
        'description': 'Commonly used name for the boundary layer turbulence scheme.',
        'members': [
            ('Mellor-Yamada', None),
            ('other', None),
        ]
    },

    'boundary_layer_turbulence_scheme_type': {
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
        'description': 'Type of scheme used for the parameterisation of deep convection.'  ,
        'members': [
            ('mass-flux', None),
            ('adjustment', None),
            ('other', None),
        ]
    },

    'deep_convection_scheme_method': {
        'description': 'If deep convection uses a mass-flux scheme enter the method used.',
        'members': [
            ('CAPE', 'Mass flux determined by CAPE'),
            ('bulk', 'A bulk mass flux scheme is used'),
            ('other', None),
        ]
    },

    'shallow_convection_scheme_method': {
        'description': 'Method used for shallow convection.',
        'members': [
            ('same as deep (unified)', None),
            ('included in boundary layer turbulence', None),
            ('separated', None),
        ]
    },

    'shallow_convection_scheme_type': {
        'description': 'Type of scheme used for the parameterisation of shallow convection.',
        'members': [
            ('mass-flux', None),
            ('other', None),
            ('none', None),
        ]
    },


    'deep_convection_scheme_processes_attributes': {
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
