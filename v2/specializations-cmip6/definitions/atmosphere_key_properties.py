"""
A realm key-properties sepecialization.
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
DESCRIPTION = 'Atmosphere key properties'

# --------------------------------------------------------------------
# Top level details.
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': "Top level key properties",
    'properties': [
        ('model_family', 'ENUM:model_family_type', '1.1',
            'Type of atmospheric model.'),
        ('basic_approximations', 'ENUM:basic_approximations_attributes', '1.N',
            'Basic approximations made in the atmosphere.',),
        ('volcanoes_implementation', 'ENUM:volcanoes_implementation_method', '1.1',
            'How volcanic effects are modeled in the atmosphere.'),
        ('top_insolation_ozone', 'bool', '1.1',
            'Impact of top of atmosphere insolation on stratospheric ozone')
        ]
    }

DETAILS['top_insolation_solar_constant'] = {
    'description': "TODO: provide a description",
    'properties': [
        ('type', 'ENUM:top_insolation_solar_constant_type', '1.1',
            'Time adaptation of the solar constant.'),
        ('fixed_value', 'float', '0.1',
            'If the solar constant is fixed, enter the value of the solar constant (W m-2).'),
        ('transient_characteristics', 'str', '1.1',
            'solar constant transient characteristics (W m-2)'),
        ('dynamical_core_top_boundary_condition', 'ENUM:dynamical_core_top_boundary_condition', '1.1',
            'Type of boundary layer at the top of the model.'),
        ]
    }

DETAILS['top_insolation_orbital_parameters'] = {
    'description': "TODO: provide a description",
    'properties': [
        ('type', 'ENUM:top_insolation_orbital_parameters_type', '1.1',
            'DESCRIPTION'),
        ('fixed_reference_date', 'int', '1.1',
            'fixed orbital parameters reference date (yyyy)'),
        ('solar_constant_transient_characteristics', 'str', '1.1',
            'transient orbital parameters characteristics'),
        ('computation_method', 'ENUM:top_insolation_orbital_parameters_computation_method', '1.1',
            'Method used for computing orbital parameters.')
        ]
    }

DETAILS['orography'] = {
    'description': "TODO: provide a description",
    'properties': [
        ('type', 'ENUM:orography_type', '1.1',
            'Time adaptation of the orography.',),
        ('changes', 'ENUM:orography_changes', '1.N',
            'If the orography type is modified describe the time adaptation changes.'),
        ]
    }

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['model_family_type'] = {
    'description': 'Type of atmospheric model.',
    'is_open': True,
    'members': [
        ('AGCM', 'Atmospheric General Circulation Model'),
        ('ARCM', 'Atmospheric Regional Climate Model'),
        ]
    }

ENUMERATIONS['basic_approximations_attributes'] = {
    'description': 'Basic approximations made in the atmosphere.',
    'is_open': True,
    'members': [
        ('primitive equations', None),
        ('non-hydrostatic', None),
        ('anelastic', None),
        ('Boussinesq', None),
        ('hydrostatic', None),
        ('quasi-hydrostatic', None),
        ]
    }

ENUMERATIONS['top_insolation_solar_constant_type'] = {
    'description': 'Time adaptation of the solar constant.',
    'is_open': False,
    'members': [
        ('fixed', None),
        ('transient', None),
        ]
    }

ENUMERATIONS['top_insolation_orbital_parameters_type'] = {
    'description': 'TODO: provide a description',
    'is_open': False,
    'members': []
    }

ENUMERATIONS['dynamical_core_top_boundary_condition'] = {
    'description': 'Type of boundary layer at the top of the model.',
    'is_open': True,
    'members': [
        ('sponge layer', None),
        ('radiation boundary condition', None),
        ]
    }

ENUMERATIONS['top_insolation_orbital_parameters_computation_method'] = {
    'description': 'Method used for computing orbital parameters.',
    'is_open': True,
    'members': [
        ('Berger 1978', None),
        ('Laskar 2004', None),
        ]
    }

ENUMERATIONS['orography_type'] = {
    'description': 'Time adaptation of the orography.',
    'is_open': False,
    'members': [
        ('present-day', None),
        ('modified', None),
        ]
    }

ENUMERATIONS['orography_changes'] = {
    'description': 'If the orography type is modified describe the time adaptation changes.',
    'is_open': False,
    'members': [
        ('related to ice sheets', None),
        ('related to tectonics', None),
        ('modified mean', None),
        ('modified variance if taken into account in model (cf gravity waves)', None),
        ]
    }

ENUMERATIONS['volcanoes_implementation_method'] = {
    'description': 'How volcanic effects are modeled in the atmosphere.',
    'is_open': True,
    'members': [
        ('high frequency solar constant anomaly', None),
        ('stratospheric aerosols optical thickness', None),
        ]
    }
