CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere.turbulance_convection'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.process'

from collections import OrderedDict

# ====================================================================
# PROCESS: PROPERTIES
# ====================================================================
DESCRIPTION = 'Atmosphere Convective Turbulence and Clouds'

# ====================================================================
# PROCESS: DETAILS
#
# URL of #details
# ====================================================================
DETAILS = OrderedDict()

# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['boundary_layer_turbulence_scheme'] = {        
    'description': 'Boundary layer turbulence scheme',
    'details': ['boundary_layer_turbulence_scheme_details']
}

SUB_PROCESSES['deep_convection_scheme'] = {
    'description': 'Deep convection scheme',
    'details': ['deep_convection_scheme_details']
}
        
SUB_PROCESSES['shallow_convection_scheme'] = {
    'description': 'Shallow convection scheme',
    'details': ['shallow_convection_scheme_details']
}

SUB_PROCESSES['other_convection_scheme_details'] = {
    'description': 'Other convection scheme.',
    'details': ['other_convection_scheme_details']
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = OrderedDict()
 
SUB_PROCESS_DETAILS['boundary_layer_turbulence_scheme_details'] = {
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
}
    
SUB_PROCESS_DETAILS['deep_convection_scheme_details'] = {
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
}
        
SUB_PROCESS_DETAILS['shallow_convection_scheme_details'] = {
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
}

SUB_PROCESS_DETAILS['other_convection_scheme_details'] = {
    'properties': [
        ('scheme_name', 'str', '1.1',
         'Other convection scheme name'),
        ('scheme_type', 'ENUM:other_convection_scheme_type', '1.1', 
         'Other convection scheme type'),
    ]
}

# ====================================================================
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================
ENUMERATIONS = OrderedDict()

ENUMERATIONS['boundary_layer_turbulence_scheme_name'] = {
    'description': 'Commonly used name for the boundary layer turbulence scheme.',
    'members': [
        ('Mellor-Yamada', None),
        ('other', None),
    ]
}

ENUMERATIONS['boundary_layer_turbulence_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of turbulence in the boundary layer.',
    'members': [
        ('TKE prognostic', None),
        ('TKE diagnostic', None),
        ('TKE coupled with water', None),
        ('vertical profile of Kz', None),
        ('other', None),
    ]
}

ENUMERATIONS['deep_convection_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of deep convection.',
    'members': [
        ('mass-flux', None),
        ('adjustment', None),
        ('other', None),
    ]
}

ENUMERATIONS['deep_convection_scheme_method'] = {
    'description': 'If deep convection uses a mass-flux scheme enter the method used.',
    'members': [
        ('CAPE', 'Mass flux determined by CAPE'),
        ('bulk', 'A bulk mass flux scheme is used'),
        ('other', None),
    ]
}

ENUMERATIONS['shallow_convection_scheme_method'] = {
    'description': 'Method used for shallow convection.',
    'members': [
        ('same as deep (unified)', None),
        ('included in boundary layer turbulence', None),
        ('separated', None),
    ]
}

ENUMERATIONS['shallow_convection_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of shallow convection.',
    'members': [
        ('mass-flux', None),
        ('other', None),
        ('none', None),
    ]
}

ENUMERATIONS['deep_convection_scheme_processes_attributes'] = {
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
}
