AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.cloud_scheme'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.process'

QC_STATUS = 'draft'

# ====================================================================
# PROCESS PROPERTIES
# ====================================================================
DESCRIPTION = 'Characteristics of the cloud scheme'

# ====================================================================
# PROCESS: DETAILS
#
# URL of #details
# ====================================================================
DETAILS = {
    'separate_treatment': {
        'description': 'Different cloud schemes for the different types of clouds (convective, stratiform and boundary layer clouds).',
        'properties': [
            ('uses_separate_treatment', 'bool', '1.1',
             'Separate schemes for different cloud types'),
        ]
    },

    'cloud_overlap': {
        'description': 'Method for taking into account overlapping of cloud layers.',
        'properties': [
            ('method', 'ENUM:cloud_overlap_method', '1.1',
             'Cloud scheme cloud overlap method'),
        ]
    },
    
    'processes': {
        'description': 'Processes included in the cloud scheme.',
        'properties': [
            ('processes_attributes', 'ENUM:processes_attributes', '1.N', 
             'Cloud scheme processes'),
        ]
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================
SUB_PROCESSES = {
    'sub_grid_scale_water_distribution': {
        'description': 'Sub-grid scale water distribution',
        'details': ['sub_grid_scale_water_distribution_properties',],
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = {
    'sub_grid_scale_water_distribution_properties': {
        'properties': [
            ('type', 'ENUM:sub_grid_scale_water_distribution_type', '1.1',
             'Sub-grid scale water distribution type'),
            ('function_name', 'str', '1.1',
             'Sub-grid scale water distribution function name'),
            ('function_order', 'int', '1.1',
             'Sub-grid scale water distribution function type'),
            ('convection_coupling','ENUM:sub_grid_scale_water_distribution_convection', '1.N',
             'Sub-grid scale water distribution coupling with convection'),
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
    'sub_grid_scale_water_distribution_type': {
        'description': 'Approach used for cloud water content and fractional cloud cover',
        'members': [
            ('prognostic', None),
            ('diagnostic', None),
        ]
    },

    'sub_grid_scale_water_distribution_convection': {    
        'description': 'Type(s) of convection that the formation of clouds is coupled with',
        'members': [
            ('coupled with deep', None),
            ('coupled with shallow', None),
            ('not coupled with convection', None),
        ]
    },

    'cloud_overlap_method': {
        'description': 'Cloud scheme cloud overlap method',
        'members': [
            ('random', None),
            ('none', None),
            ('other', None),
        ]
    },

    'processes_attributes': {
        'short_name': 'Cloud scheme processes attributes',
        'description': 'Processes included in the cloud scheme.',
        'members': [
            ('entrainment', None),
            ('detrainment', None),
            ('bulk cloud', None),
            ('other', None),
        ]
    },
}
