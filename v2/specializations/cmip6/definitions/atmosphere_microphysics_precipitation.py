CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere.microphysics_precipitation'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.process'

from collections import OrderedDict

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
# --------------------------------------------------------------------
DESCRIPTION = 'Cloud Microphysics and Precipitation'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['large_scale_precipitation'] = {
    'description': 'Large scale precipitation scheme',
    'details': ['large_scale_precipitation_details'],
}

SUB_PROCESSES['cloud_microphysics'] = {
    'description': 'Cloud microphysics',
    'details': ['cloud_microphysics_details']
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['large_scale_precipitation_details'] = {
    'properties': [
        ('scheme', 'str', '1.1',
         'Commonly used name of the large scale precipitation parameterisation scheme'),
        ('hydrometeors', 'ENUM:hydrometeor_types', '1.N',
         'Precipitating hydrometeors taken into account in the large scale precipitation scheme'),
    ]
}

SUB_PROCESS_DETAILS['cloud_microphysics_details'] = {
    'properties': [
        ('scheme', 'str', '1.1',
         'Commonly used name of the microphysics parameterisation scheme.'),
        ('processes', 'ENUM:processes_attributes', '1.N',
         'Cloud microphysics processes'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['hydrometeor_types'] = {
    'description': 'Precipitating hydrometeors taken into account in the large scale precipitation scheme',
    'members': [
        ('liquid rain', None),
        ('snow', None),
        ('hail', None),
        ('graupel', None),
        ('other', None),
    ]
}

ENUMERATIONS['processes_attributes'] = {
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
}

