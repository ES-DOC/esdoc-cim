AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.microphysics_precipitation'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.process'

QC_STATUS = 'draft'

# ====================================================================
# PROCESS: PROPERTIES
# ====================================================================
DESCRIPTION = 'Cloud Microphysics and Precipitation'

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
    'large_scale_precipitation': {
        'description': 'Large scale precipitation scheme',
        'details': ['large_scale_precipitation_details'],
    },
    
    'cloud_microphysics': { 
        'description': 'Cloud microphysics',
        'details': ['cloud_microphysics_details']
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = {
    'large_scale_precipitation_details': {
        'description': 'Large scale precipitation scheme properties',
        'properties': [
            ('scheme', 'str', '1.1',
             'Commonly used name of the large scale precipitation parameterisation scheme'),
            ('hydrometeors', 'ENUM:hydrometeor_types', '1.N',
             'Precipitating hydrometeors taken into account in the large scale precipitation scheme'),
        ]
    },

    'cloud_microphysics_details': { 
        'description': 'Cloud microphysics properties',
        'properties': [
            ('scheme', 'str', '1.1',
             'Commonly used name of the microphysics parameterisation scheme.'),
            ('processes', 'ENUM:processes_attributes', '1.N',
             'Cloud microphysics processes'),
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

    'hydrometeor_types': {
        'description': 'Precipitating hydrometeors taken into account in the large scale precipitation scheme',
        'members': [
            ('liquid rain', None),
            ('snow', None),
            ('hail', None),
            ('graupel', None),
            ('other', None),
        ]
    },

    'processes_attributes': {
        'description': 'Cloud microphysics processes',
        'members': [
            ('mixed phase', None),
            ('cloud droplets', None),
            ('cloud ice', None),
            ('ice nucleation', None),
            ('water vapour deposition', None),
            ('effect of raindrops', None),
            ('effect of snow', None),
            ('effect of graupel', None),
            ('other', None),
        ]
    },
}

