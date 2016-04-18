# --------------------------------------------------------------------
# See http://wordpress.es-doc.org for documentation on how to create
# CMIP6 specialisations
# --------------------------------------------------------------------

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere.radiation'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.process'

from collections import OrderedDict

# --------------------------------------------------------------------
# PROCESS: PROPERTIES
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['attributes'] = {
    'properties' = [
        ('aerosol_types', 'ENUM:aerosol_types_attributes', '1.N',
         'Types of aerosols whose radiative effect is taken into account in the atmospheric model'),
        ('ghg_types', 'ENUM:ghg_types_attributes', '1.N', 
         'Types of greenhouse gases whose radiative effect is taken into account in the atmospheric model'),
        ('cloud_ice', 'ENUM:cloud_ice_properties', '1.N',         
         'Radiative properties of ice crystals in clouds'),
        ('cloud_liquid', 'ENUM:cloud_liquid_properties', '1.N',
         'Radiative properties of liquid droplets in clouds'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['longwave_scheme'] = {
    'description': 'Longwave radiation scheme',
    'details': ['longwave_scheme_details']
},

SUB_PROCESSES['shortwave_scheme'] = {
    'description': 'Shortwave radiation scheme',
    'details': ['shortwave_scheme_details']
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES: DETAILS
#   
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict() # Not necesssary, but consistent

SUB_PROCESS_DETAILS['longwave_scheme_details'] = {
    'description': 'Longwave radiation scheme',
    'properties': [
        ('scheme_type', 'ENUM:longwave_scheme_type', '1.1',
         'Longwave radiation scheme type'),
        ('scheme_method', 'ENUM:longwave_scheme_method', '1.1', 
         'Longwave radiation scheme method'),
        ('spectral_intervals', 'int', '1.1',
         'Longwave radiation scheme spectral intervals'),
    ]
}

SUB_PROCESS_DETAILS['shortwave_scheme_details'] = {
    'description': 'Shortwave radiation scheme',
    'properties': [
        ('scheme_type', 'ENUM:shortwave_scheme_type', '1.1',
         'Shortwave radiation scheme type'),           
        ('spectral_intervals', 'int', '1.1',
         'Shortwave radiation scheme spectral intervals'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['aerosol_types_attributes'] = {
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
}

ENUMERATIONS['ghg_types_attributes'] = {
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
}

ENUMERATIONS['cloud_ice_properties'] = {
    'description': 'Radiative properties of ice crystals in clouds',
    'members': [
        ('???', None),
        ('other', None),
    ]
}

ENUMERATIONS['cloud_liquid_properties'] = {
    'description': 'Radiative properties of liquid droplets in clouds',
    'members': [
        ('???', None),
        ('other', None),
    ]
}

ENUMERATIONS['longwave_scheme_type'] = {
    'description': 'Type of scheme used for longwave radiation parameterisation',
    'members': [
        ('wide-band model', None),
        ('wide-band model (Morcrette)', None),
        ('K-correlated', None),
        ('K-correlated (RRTM)', None),
        ('other', None),
    ]
}
             
ENUMERATIONS['longwave_scheme_method'] = {
    'description': 'Method for the radiative transfer calculations used in the longwave scheme',
    'members': [
        ('two-stream', None),
        ('layer interaction', None),
        ('other', None),
    ]
}

ENUMERATIONS['shortwave_scheme_type'] = {
    'description': 'Type of scheme used for shortwave radiation parameterisation',   
    'members': [
        ('wide-band model', None),
        ('wide-band model (Fouquart)', None),
        ('other', None),
    ]
}
