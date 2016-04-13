ID = 'cmip6.atmosphere.microphysics_precipitation'

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
    'short_name': 'Cloud Microphysics and Precipitation',              
    'description': 'Cloud Microphysics and Precipitation',

    'details': [],               
    
    'sub_process': ['large_scale_precipitation',
                    'cloud_microphysics',
                ],

    # ----------------------------------------------------------------
    # DETAILS
    # ----------------------------------------------------------------

    # ----------------------------------------------------------------
    # SUB-PROCESSES
    # ----------------------------------------------------------------
    'large_scale_precipitation': {
        'short_name': 'Large scale precipitation scheme',
        'description': 'Large scale precipitation scheme',
        'details': [('large_scale_precipitation_details',
                     'scheme', 'hydrometeors'),
                ],
    },
    

    'cloud_microphysics': { 
        'short_name': 'Cloud microphysics',
        'description': 'Cloud microphysics',
        'details': [('cloud_microphysics_details',
                    'scheme', 'processes'),
                ],               
    },

    # ----------------------------------------------------------------
    # SUB-PROCESS DETAILS
    # ----------------------------------------------------------------
    'large_scale_precipitation_details': {
        'short_name': 'Large scale precipitation scheme properties',
        'description': 'Large scale precipitation scheme properties',
        'scheme': (
            'str', '1.1',
            'Commonly used name of the large scale precipitation parameterisation scheme'),
        'hydrometeors': (
            'ENUM:large_scale_precipitation_hydrometeor_types', '1.N',
            'Precipitating hydrometeors taken into account in the large scale precipitation scheme'),
    },
    

    'cloud_microphysics_details': { 
        'short_name': 'Cloud microphysics properties',
        'description': 'Cloud microphysics properties',
        'scheme': (
            'str', '1.1',
            'Commonly used name of the microphysics parameterisation scheme.'),
        'processes': (
            'ENUM:cloud_microphysics_processes_attributes', '1.N',
            'Cloud microphysics processes'),
    },
}


# ====================================================================
# ENUMERATIONS
# ====================================================================
ENUMERATIONS = {

    'large_scale_precipitation_hydrometeor_types': {
        'short_name': 'Large scale precipitation hydrometeor types',
        'description': 'Precipitating hydrometeors taken into account in the large scale precipitation scheme',
        'members': [
            ('liquid rain', None),
            ('snow', None),
            ('hail', None),
            ('graupel', None),
            ('other', None),
        ]
    },

    'cloud_microphysics_processes_attributes': {
        'short_name': 'Cloud microphysics processes',
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

