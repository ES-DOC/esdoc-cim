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
DESCRIPTION = 'Atmosphere Convective Turbulence and Clouds'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------

# DEFINE HERE IF REQUIRED

# --------------------------------------------------------------------
# SUB-PROCESS: boundary_layer_turbulence_scheme
# --------------------------------------------------------------------
DETAILS['boundary_layer_turbulence_scheme'] = {
    'description': 'Boundary layer turbulence scheme',
    'properties': [
        ('scheme_name', 'ENUM:boundary_layer_turbulence_scheme_name', '1.1',
             'Boundary layer turbulence scheme name'),
        ('scheme_type', 'ENUM:boundary_layer_turbulence_scheme_type', '1.1',
             'Boundary layer turbulence scheme type'),
        ('closure_order', 'int', '1.1',
             'Boundary layer turbulence scheme closure order'),
        ('counter_gradient', 'bool', '1.1',
            'Uses boundary layer turbulence scheme counter gradient'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: deep_convection_scheme
# --------------------------------------------------------------------
DETAILS['deep_convection_scheme'] = {
    'description': 'Deep convection scheme',
    'properties': [
        ('scheme_name', 'str', '1.1',
             'Deep convection scheme name'),
        ('scheme_type', 'ENUM:deep_convection_scheme_type', '1.1',
             'Deep convection scheme type'),
        ('scheme_method', 'ENUM:deep_convection_scheme_method', '1.N',
             'Deep convection scheme method'),
        ('processes', 'ENUM:deep_convection_scheme_processes_attributes', '1.N',
            'Deep convection scheme processes'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: shallow_convection_scheme
# --------------------------------------------------------------------
DETAILS['shallow_convection_scheme'] = {
    'description': 'Shallow convection scheme',
    'properties': [
        ('selection', 'ENUM:shallow_convection_scheme_method', '1.1',
             'shallow convection scheme method'),
        ('scheme_type', 'ENUM:shallow_convection_scheme_type', '1.1',
             'shallow convection scheme type'),
        ('scheme_name', 'str', '1.1',
             'Shallow convection scheme name'),
        ('processes', 'ENUM:shallow_convection_scheme_processes_attributes', '1.N',
            'Physical processes taken into account in the parameterisation of shallow convection'),
        ]
    }

# --------------------------------------------------------------------
# SUB-PROCESS: other_convection_scheme_details
# --------------------------------------------------------------------
DETAILS['other_convection_scheme_details'] = {
    'description': 'Other convection scheme.',
    'properties': [
        ('scheme_name', 'str', '1.1',
             'Other convection scheme name'),
        ('scheme_type', 'ENUM:other_convection_scheme_type', '1.1',
             'Other convection scheme type'),
        ]
    }

# --------------------------------------------------------------------
# PROCESS: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['boundary_layer_turbulence_scheme_name'] = {
    'description': 'Commonly used name for the boundary layer turbulence scheme.',
    'is_open': True,
    'members': [
        ('Mellor-Yamada', None),
        ]
    }

ENUMERATIONS['boundary_layer_turbulence_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of turbulence in the boundary layer.',
    'is_open': True,
    'members': [
        ('TKE prognostic', None),
        ('TKE diagnostic', None),
        ('TKE coupled with water', None),
        ('vertical profile of Kz', None),
        ]
    }

ENUMERATIONS['deep_convection_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of deep convection.',
    'is_open': True,
    'members': [
        ('mass-flux', None),
        ('adjustment', None),
        ]
    }

ENUMERATIONS['deep_convection_scheme_method'] = {
    'description': 'If deep convection uses a mass-flux scheme enter the method used.',
    'is_open': True,
    'members': [
        ('CAPE', 'Mass flux determined by CAPE'),
        ('bulk', 'A bulk mass flux scheme is used'),
        ]
    }

ENUMERATIONS['shallow_convection_scheme_method'] = {
    'description': 'Method used for shallow convection.',
    'is_open': False,
    'members': [
        ('same as deep (unified)', None),
        ('included in boundary layer turbulence', None),
        ('separated', None),
        ]
    }

ENUMERATIONS['shallow_convection_scheme_type'] = {
    'description': 'Type of scheme used for the parameterisation of shallow convection.',
    'is_open': True,
    'members': [
        ('mass-flux', None),
        ]
    }

ENUMERATIONS['deep_convection_scheme_processes_attributes'] = {
    'description': 'deep_convection_scheme_processes_attributes',
    'is_open': True,
    'members': [
        ('vertical momentum transport', None),
        ('convective momentum transport', None),
        ('entrainment', None),
        ('detrainment', None),
        ('penetrative convection', None),
        ('updrafts and downdrafts', None),
        ('radiative effect of anvils', None),
        ]
    }

# TODO: define as this was added simply to pass validation
ENUMERATIONS['shallow_convection_scheme_processes_attributes'] = {
    'description': 'shallow_convection_scheme_processes_attributes',
    'is_open': True,
    'members': []
    }

# TODO: define as this was added simply to pass validation
ENUMERATIONS['other_convection_scheme_type'] = {
    'description': 'other_convection_scheme_type',
    'is_open': True,
    'members': []
    }
