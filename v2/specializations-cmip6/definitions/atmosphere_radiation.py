"""

A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.
"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the atmosphere radiation process'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Top level radiation process properties",
    'properties': [
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
# SUB-PROCESS: longwave_scheme
# --------------------------------------------------------------------
DETAILS['longwave_scheme'] = {
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

# --------------------------------------------------------------------
# SUB-PROCESS: shortwave_scheme
# --------------------------------------------------------------------
DETAILS['shortwave_scheme'] = {
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
# --------------------------------------------------------------------
ENUMERATIONS['aerosol_types_attributes'] = {
    'description': 'Types of aerosols whose radiative effect is taken into account in the atmospheric model.',
    'is_open': True,
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
        ]
    }

ENUMERATIONS['ghg_types_attributes'] = {
    'description': 'Types of greenhouse gases whose radiative effect is taken into account in the atmospheric model',
    'is_open': True,
    'members': [
        ('CO2', None),
        ('CH4', None),
        ('N2O', None),
        ('CFC', None),
        ('H2O', None),
        ('O3', None),
        ]
    }

ENUMERATIONS['cloud_ice_properties'] = {
    'description': 'Radiative properties of ice crystals in clouds',
    'is_open': True,
    'members': []
    }

ENUMERATIONS['cloud_liquid_properties'] = {
    'description': 'Radiative properties of liquid droplets in clouds',
    'is_open': True,
    'members': []
    }

ENUMERATIONS['longwave_scheme_type'] = {
    'description': 'Type of scheme used for longwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('wide-band model (Morcrette)', None),
        ('K-correlated', None),
        ('K-correlated (RRTM)', None),
        ]
    }

ENUMERATIONS['longwave_scheme_method'] = {
    'description': 'Method for the radiative transfer calculations used in the longwave scheme',
    'is_open': True,
    'members': [
        ('two-stream', None),
        ('layer interaction', None),
        ]
    }

ENUMERATIONS['shortwave_scheme_type'] = {
    'description': 'Type of scheme used for shortwave radiation parameterisation',
    'is_open': True,
    'members': [
        ('wide-band model', None),
        ('wide-band model (Fouquart)', None),
        ]
    }
