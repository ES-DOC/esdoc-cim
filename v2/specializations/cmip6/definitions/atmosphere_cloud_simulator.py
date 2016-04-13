AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.cloud_simulator'

CONTACT = 'Charlotte Pascoe'

AUTHORS = 'him (ISPL), her (her@ipsl.fr), them'

TYPE = 'cim.2.science.process'

# ====================================================================
# PROCESS: PROPERTIES
# ====================================================================
DESCRIPTION = 'Characteristics of the cloud simulator'

# ====================================================================
# PROCESS: DETAILS
#
# URL of #details
# ====================================================================
DETAILS = {
    'isscp_attributes': {
        'description': 'ISSCP Characteristics', # defaults to derived short_name
        'properties': [
            ('top_height', 'ENUM:isscp_top_height', '1.N',
             'Cloud simulator ISSCP top height'),
            ('top_height_direction', 'ENUM:isscp_top_height_direction', '1.1',
             'Cloud simulator ISSCP top height direction'),
        ],
        'constraints': []
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================
SUB_PROCESSES = {
    'cosp_attributes': {
        'description': 'CFMIP Observational Simulator Package attributes',
        'details': ['cosp_attributes_details'],
    },
    
    'inputs_radar': {
        'descrition': 'Characteristics of the cloud radar simulator',
        'details': ['inputs_radar_details',]
    },
    
    'inputs_lidar': {
        'description': 'Characteristics of the cloud lidar simulator',
        'details': ['inputs_lidar_details',]
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = {
    'cosp_attributes_details': {
        'description': 'OPTIONAL DESCRIPTION'
        'properties': [
            ('run_configuration', 'ENUM:cosp_run_configuration', '1.1',
             'Cloud simulator COSP run configuration'),
            ('number_of_grid_points', 'int', '1.1',
             'Cloud simulator COSP number of grid points'),
            ('number_of_columns', 'int', '1.1',
             'Cloud simulator COSP number of cloumns'),
            ('number_of_levels', 'int', '1.1',
             'Cloud simulator COSP number of levels'),                
        ],
    },
    
    'inputs_radar_details': {
        'properties': [
            ('radar_frequency', 'float', '1.1',
             'Cloud simulator radar frequency'),
            ('radar_type', 'ENUM:inputs_radar_type', '1.1',
             'Cloud simulator radar type'),
            ('gas_absorption', 'bool', '1.1',
             'Cloud simulator radar uses gas absorption'),
            ('effective_radius', 'bool', '1.1',
             'Cloud simulator radar uses effective radius'),
        ],
    },
    
    'inputs_lidar_details': {
        'properties': [
            ('ice_type', 'ENUM:inputs_lidar_ice_type', '1.1',
             'Cloud simulator lidar ice type'),
            ('lidar_overlap', 'ENUM:inputs_lidar_overlap', '1.N',
             'Cloud simulator lidar overlap'),
        ]
`    },
}

# ====================================================================
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# ====================================================================
ENUMERATIONS = {

    'isscp_top_height': {
        'description': 'Cloud top height management',
        'members': [
            ('no adjustment', None),
            ('IR brightness', None),
            ('visible optical depth', None),
        ]
    },

    'isscp_top_height_direction': {
        'description': 'Direction for finding the radiance determined cloud-top pressure. Atmosphere pressure level with interpolated temperature equal to the radiance determined cloud-top pressure.',
        'members': [
            ('lowest altitude level', None),
            ('highest altitude level', None),
        ]
    },

    'cosp_run_configuration': {
        'description': 'Method used to run the CFMIP Observational Simulator Package',
        'members': [
            ('Inline', None),
            ('Offline', None),
            ('None', None),
        ]
    },

    'inputs_radar_type': {
        'description': 'Type of radar',
        'members': [
            ('surface', None),
            ('space borne', None),
        ]
    },

    'inputs_lidar_ice_type': {
        'description': 'Ice particle shape in lidar calculations',
        'members': [
            ('ice spheres', None),
            ('ice non-spherical', None),
        ]
    },

    'inputs_lidar_overlap': {
        'description': 'lidar overlap type',
        'members': [
            ('max', None),
            ('random', None),
            ('other', None),
        ]
    },

}
