ID = 'cmip6.atmosphere.radiation'

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
    'short_name': 'Atmosphere Radiation',
    'description': 'Characteristics of the atmosphere radiation process',

    'details': [('aerosol_types',
                 'properties'),
                ('ghg_types',
                 'ghg_types'),
                ('cloud_ice',
                 'properties'),
                ('cloud_liquid',
                 'properties'),
            ],               
    
    'sub_process': ['longwave_scheme',
                    'shortwave_scheme',
                ],

    # ----------------------------------------------------------------
    # DETAILS
    # ----------------------------------------------------------------
    'aerosol_types': {
        'short_name': '',
        'description': '',
        'properties': (
            'ENUM:aerosol_types_attributes', '1.N',
            'Types of aerosols whose radiative effect is taken into account in the atmospheric model'),
    },

    'ghg_types': {
        'short_name': 'GHG types',
        'description': 'Types of greenhouse gases whose radiative effect is taken into account in the atmospheric model',
        'ghg_types': (
            'ENUM:ghg_types_attributes', '1.N', 
            'Radiative greenhouse gases'),
    },

    'cloud_ice': {
        'short_name': 'Radiative properties of ice crystals in clouds',
        'description': 'Radiative properties of ice crystals in clouds',
        'properties': (
            'ENUM:cloud_ice_properties', '1.N',
            'Radiative properties of cloud ice'),
    },

    'cloud_liquid': {
        'description': 'Radiative properties of liquid droplets in clouds',
        'properties': (
            'ENUM:cloud_liquid_properties', '1.N',
            'Radiative properties of cloud droplets'),
    },

    # ----------------------------------------------------------------
    # SUB-PROCESSES
    # ----------------------------------------------------------------
    'longwave_scheme': {
        'short_name': 'Longwave radiation scheme',
        'description': 'Longwave radiation scheme',
        'details': [('longwave_scheme_details',
                     'scheme_type', 'scheme_method', 'spectral_intervals'),
                ],
    },

    'shortwave_scheme': {
        'short_name': 'Shortwave radiation scheme',
        'description': 'Shortwave radiation scheme',
        'details': [('shortwave_scheme_details',                    
                     'scheme_type', 'spectral_intervals'),
                ],
    },

    # ----------------------------------------------------------------
    # SUB-PROCESS DETAILS
    # ----------------------------------------------------------------
    'longwave_scheme_details': {
        'short_name': 'Longwave radiation scheme',
        'description': 'Longwave radiation scheme',
        'scheme_type': (
            'ENUM:longwave_scheme_type', '1.1',
            'Longwave radiation scheme type'),
        'scheme_method': (
            'ENUM:longwave_scheme_method', '1.1', 
            'Longwave radiation scheme method'),
        'spectral_intervals': (
            'int', '1.1',
            'Longwave radiation scheme spectral intervals'),
    },

    'shortwave_scheme_details': {
        'short_name': 'Shortwave radiation scheme',
        'description': 'Shortwave radiation scheme',
        'scheme_type': (
            'ENUM:shortwave_scheme_type', '1.1',
            'Shortwave radiation scheme type'),           
        'spectral_intervals': (
            'int', '1.1',
            'Shortwave radiation scheme spectral intervals'),
    },

}

# ====================================================================
# ENUMERATIONS
# ====================================================================
ENUMERATIONS = {

    'aerosol_types_attributes': {

        'short_name': 'Aerosol types attributes',
        'description': 'Types of aerosols whose radiative effect is taken into account in the atmospheric model.',
        'members': [
            ('sulphate', None),
            ('nitrate', None),
            ('sea salt', None),
            ('dust', None),
            ('ice', None),
            ('organic', None),
            ('BC (black carbon / soot)', None),
            ('SOA (secondary organic aerosols)', None),
            ('POM (particulate organic matter)', None),
            ('polar stratospheric ice', None),
            ('NAT (nitric acid trihydrate)', None),
            ('NAD (nitric acid dihydrate)', None),
            ('STS (supercooled ternary solution aerosol particle)', None),
            ('other', None),
        ]
    },

    'ghg_types_attributes': {
        'short_name': 'GHG types',
        'description': 'Types of greenhouse gases whose radiative effect is taken into account in the atmospheric model',
        'members': [
            ('CO2', None),
            ('CH4', None),
            ('N2O', None),
            ('CFC', None),
            ('H2O', None),
            ('O3', None),
            ('other', None),
        ]
    },

    'cloud_ice_properties': {
        'short_name': 'Cloud ice properties',
        'description': 'Radiative properties of ice crystals in clouds',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'cloud_liquid_properties': {
        'short_name': 'Cloud liquid properties',
        'description': 'Radiative properties of liquid droplets in clouds',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'longwave_scheme_type': {
        'short_name': 'Longwave scheme type',
        'description': 'Type of scheme used for longwave radiation parameterisation',
        'members': [
            ('wide-band model', None),
            ('wide-band model (Morcrette)', None),
            ('K-correlated', None),
            ('K-correlated (RRTM)', None),
            ('other', None),
        ]
    },

    'longwave_scheme_method': {
        'short_name': 'Longwave scheme method',
        'description': 'Method for the radiative transfer calculations used in the longwave scheme',
        'members': [
            ('two-stream', None),
            ('layer interaction', None),
            ('other', None),
        ]
    },

    'shortwave_scheme_type': {
        'short_name': 'Shortwave scheme type',
        'description': 'Type of scheme used for shortwave radiation parameterisation',   
        'members': [
            ('wide-band model', None),
            ('wide-band model (Fouquart)', None),
            ('other', None),
        ]
    },

}
