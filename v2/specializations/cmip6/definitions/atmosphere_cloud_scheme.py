CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.<PROCESS>', e.g. 'cmip6.atmosphere.radiation'
# --------------------------------------------------------------------
ID = 'cmip6.atmosphere.cloud_scheme'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.process'

from collections import OrderedDict

# --------------------------------------------------------------------
# PROCESS PROPERTIES
# --------------------------------------------------------------------
DESCRIPTION = 'Characteristics of the cloud scheme'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# URL of #details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['attributes'] = {
    'properties': [
        ('uses_separate_treatment', 'bool', '1.1',
         'Different cloud schemes for the different types of clouds (convective, stratiform and boundary layer clouds'),
        ('cloud_overlap_method', 'ENUM:cloud_overlap_method', '1.1',
         'Method for taking into account overlapping of cloud layers'),
        ('processes', 'ENUM:processes_attributes', '1.N', 
         'Processes included in the cloud scheme'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES
#
# URL of #sub_process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['sub_grid_scale_water_distribution'] = {
    'description': 'Sub-grid scale water distribution',
    'details': ['sub_grid_scale_water_distribution_details',],
}

# --------------------------------------------------------------------
# PROCESS: SUB-PROCESSES: DETAILS
#   
# URL of #details
# Convention: sub-process details start with sub-process name
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['sub_grid_scale_water_distribution_details'] = {
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
}

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
#
# URL of process.html#enuemrations
# Convention: Do not include the process name in the enumeration 
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['sub_grid_scale_water_distribution_type'] = {
    'description': 'Approach used for cloud water content and fractional cloud cover',
    'members': [
        ('prognostic', None),
        ('diagnostic', None),
    ]
}

ENUMERATIONS['sub_grid_scale_water_distribution_convection'] = {
    'description': 'Type(s) of convection that the formation of clouds is coupled with',
    'members': [
        ('coupled with deep', None),
        ('coupled with shallow', None),
        ('not coupled with convection', None),
    ]
}

ENUMERATIONS['cloud_overlap_method'] = {
    'description': 'Cloud scheme cloud overlap method',
    'members': [
        ('random', None),
        ('none', None),
        ('other', None),
    ]
}

ENUMERATIONS['processes_attributes'] = {
    'short_name': 'Cloud scheme processes attributes',
    'description': 'Processes included in the cloud scheme.',
    'members': [
        ('entrainment', None),
        ('detrainment', None),
        ('bulk cloud', None),
        ('other', None),
    ]
}
