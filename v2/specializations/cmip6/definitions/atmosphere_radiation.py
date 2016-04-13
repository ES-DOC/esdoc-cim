AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.radiation'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.process'

QC_STATUS = 'draft'

# ====================================================================
# PROCESS: PROPERTIES
# ====================================================================
DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# ====================================================================
# PROCESS: DETAILS
#
# URL of #details
# ====================================================================
DETAILS = {
    'aerosol_types': {
        'properties': [
            ('properties', 'ENUM:aerosol_types_attributes', '1.N',
             'Types of aerosols whose radiative effect is taken into account in the atmospheric model'),
        ]
    },

    'ghg_types': {
        'description': 'Types of greenhouse gases whose radiative effect is taken into account in the atmospheric model',
        'properties': [
            ('ghg_types', 'ENUM:ghg_types_attributes', '1.N', 
             'Radiative greenhouse gases'),
        ]
    },

    'cloud_ice': {
        'description': 'Radiative properties of ice crystals in clouds',
        'properties': [
            ('properties', 'ENUM:cloud_ice_properties', '1.N',
             'Radiative properties of cloud ice'),
        ]
    },

    'cloud_liquid': {
        'description': 'Radiative properties of liquid droplets in clouds',
        'properties': [
            ('properties', 'ENUM:cloud_liquid_properties', '1.N',
             'Radiative properties of cloud droplets'),
        ]
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# ====================================================================
SUB_PROCESSES = {
    'longwave_scheme': {
        'description': 'Longwave radiation scheme',
        'details': ['longwave_scheme_details']
    },

    'shortwave_scheme': {
        'description': 'Shortwave radiation scheme',
        'details': ['shortwave_scheme_details']
    },
}

# ====================================================================
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# ====================================================================
SUB_PROCESS_DETAILS = {
    'longwave_scheme_details': {
        'description': 'Longwave radiation scheme',
        'properties': [
            ('scheme_type', 'ENUM:longwave_scheme_type', '1.1',
             'Longwave radiation scheme type'),
            ('scheme_method', 'ENUM:longwave_scheme_method', '1.1', 
             'Longwave radiation scheme method'),
            ('spectral_intervals', 'int', '1.1',
             'Longwave radiation scheme spectral intervals'),
        ]
    },

    'shortwave_scheme_details': {
        'description': 'Shortwave radiation scheme',
        'properties': [
            ('scheme_type', 'ENUM:shortwave_scheme_type', '1.1',
             'Shortwave radiation scheme type'),           
            ('spectral_intervals', 'int', '1.1',
             'Shortwave radiation scheme spectral intervals'),
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

    'aerosol_types_attributes': {
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
        'description': 'Radiative properties of ice crystals in clouds',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'cloud_liquid_properties': {
        'description': 'Radiative properties of liquid droplets in clouds',
        'members': [
            ('???', None),
            ('other', None),
        ]
    },

    'longwave_scheme_type': {
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
        'description': 'Method for the radiative transfer calculations used in the longwave scheme',
        'members': [
            ('two-stream', None),
            ('layer interaction', None),
            ('other', None),
        ]
    },

    'shortwave_scheme_type': {
        'description': 'Type of scheme used for shortwave radiation parameterisation',   
        'members': [
            ('wide-band model', None),
            ('wide-band model (Fouquart)', None),
            ('other', None),
        ]
    },

}
