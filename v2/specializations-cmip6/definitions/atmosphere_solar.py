"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""

from collections import OrderedDict
DETAILS = OrderedDict()
PROCESS = OrderedDict()
SUB_PROCESSES = OrderedDict()
ENUMERATIONS = OrderedDict()


# --------------------------------------------------------------------
# CONTACT
#
# Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'Charlotte Pascoe'

# --------------------------------------------------------------------
# AUTHORS
#
# Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'


# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------

DETAILS['top_insolation_solar_constant'] = {
    'description': 'Top of atmosphere insolation',
    'properties': [
        ('type', 'ENUM:top_insolation_solar_constant_type', '1.1',
         'Time adaptation of the solar constant.'),
        ('fixed_value', 'float', '0.1',
         'If the solar constant is fixed, enter the value of the solar constant (W m-2).'),
        ('transient_characteristics', 'str', '1.1',
         'solar constant transient characteristics (W m-2)'),
    ],
}

DETAILS['top_insolation_orbital_parameters'] = {
    'description': 'Orbit and insolation characteristics',
    'properties': [
        ('type', 'ENUM:top_insolation_orbital_parameters_type', '1.1',
         'Time adaptation of orbital parameters'),
        ('fixed_reference_date', 'int', '1.1',
         'fixed orbital parameters reference date (yyyy)'),
        ('solar_constant_transient_characteristics', 'str', '1.1',
         'transient orbital parameters characteristics'),
        ('computation_method', 'ENUM:top_insolation_orbital_parameters_computation_method', '1.1',
         'Method used for computing orbital parameters.')
    ],
}

DETAILS['top_insolation_ozone'] = {
    'description': 'Impact of solar insolation on stratospheric ozone',
    'properties': [
        ('solar_ozone_impact', 'bool', '1.1',
    'Impact of top of atmosphere insolation on stratospheric ozone'),
    ],
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration
# --------------------------------------------------------------------

ENUMERATIONS['top_insolation_solar_constant_type'] = {
    'description': 'Time adaptation of the solar constant.',
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
    ],
}

ENUMERATIONS['top_insolation_orbital_parameters_type'] = {
    'description': 'Time adaptation of orbital parameters',
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
    ],
}

ENUMERATIONS['top_insolation_orbital_parameters_computation_method'] = {
    'description': 'Method used for computing orbital parameters.',
    'is_open': True,
    'members': [
        ('Berger 1978', None),
        ('Laskar 2004', None),
    ],
}

