AUTHOR_GUIDE = 'URL on wordpress site of useful info for authors "CMIP6 specilaisations author guide". This page will be a generic guide on how to fill in a REALM, PROCESS, SUB_PROCESS, SUB_PROCESS_DETAILS, etc. http://cmip6.specialisation.guide/process.html'

ID = 'cmip6.atmosphere.key_properties'

CONTACT = 'Charlotte Pascoe'

AUTHORS = ''

TYPE = 'cim.2.science.key_properties'

QC_STATUS = 'draft'

# ====================================================================
# KEY PROPERTIES: PROPERTIES
# ====================================================================
DESCRIPTION = 'Key properties of the atmosphere'

# ====================================================================
# KEY PROPERTIES: DETAILS
# ====================================================================
DETAILS = {
    'general': {
        'properties': [
            ('model_family','ENUM:model_family_type', '1.1',
             'Type of atmospheric model.'),
            ('basic_approximations', 'ENUM:basic_approximations_attributes', '1.N',
             'Basic approximations made in the atmosphere.',),
            ('volcanoes_implementation', 'ENUM:volcanoes_implementation_method', '1.1',
             'How volcanic effects are modeled in the atmosphere.'),
        ]
    },
    
    'top_insolation_solar_constant': {
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
    },
    
    'top_insolation_orbital_parameters': {
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
    },

    'top_insolation_ozone': {
        'description': 'Top of atmosphere insolation impact on ozone',
        'properties': [           
            ('top_insolation_ozone', 'bool', '1.1',
             'Impact of top of atmosphere insolation on stratospheric ozone'),
        ]
    },
    
    'orography': {
        'properties': [
            ('type', 'ENUM:orography_type', '1.1',
             'Time adaptation of the orography.',),
            ('changes', 'ENUM:orography_changes', '1.N',
             'If the orography type is modified describe the time adaptation changes.'),
        ]
    },
}

# ====================================================================
# KEY PROPERTIES: EXTENT
# ====================================================================
EXTENT = {}

# ====================================================================
# KEY PROPERTIES: RESOLUTION
# ====================================================================
RESOLUTION = {}

# ====================================================================
# KEY PROPERTIES: TUNING APPLIED
# ====================================================================
TUNING_APPLIED = {}

# ====================================================================
# KEY PROPERTIES: EXTRA CONSERVATION PROPERTIES
# ====================================================================
EXTRA_CONSERVATION_PROPERTIES = {}

# ====================================================================
# KEY PROPERTIES: ENUMERATIONS
# ====================================================================
ENUMERATIONS = {

    'model_family_type': {
        'description': 'Type of atmospheric model.',
        'members': [
            ('AGCM', 'Atmospheric General Circulation Model'),
            ('ARCM', 'Atmospheric Regional Climate Model'),
            ('other', None),
        ]
    },
    
    'basic_approximations_attributes': {
        'description': 'Basic approximations made in the atmosphere.',
        'members': [
            ('primitive equations', None),
            ('non-hydrostatic', None),
            ('anelastic', None),
            ('Boussinesq', None),
            ('hydrostatic', None),
            ('quasi-hydrostatic', None),
            ('other', None),
        ],
    },

    'top_insolation_solar_constant_type': {
        'description': 'Time adaptation of the solar constant.',
        'members': [
            ('fixed', None),
            ('transient', None),
        ]
    },

    'dynamical_core_top_boundary_condition': {
        'description': 'Type of boundary layer at the top of the model.',
        'members': [
            ('sponge layer', None),
            ('radiation boundary condition', None),
            ('other', None),
        ]
    },

    'top_insolation_orbital_parameters_computation_method': { 
        'description': 'Method used for computing orbital parameters.',
        'members': [
            ('Berger 1978', None),
            ('Laskar 2004', None),
            ('Other', None),
        ]
    },


    'orography_type': {
        'description': 'Time adaptation of the orography.',
        'members': [
            ('present-day', None),
            ('modified', None),
        ]
    },

    'orography_changes': {
        'description': 'If the orography type is modified describe the time adaptation changes.',
        'members': [
            ('related to ice sheets', None),
            ('related to tectonics', None),
            ('modified mean', None),
            ('modified variance if taken into account in model (cf gravity waves)', None),
        ]
    },

    'volcanoes_implementation_method': {
        'description': 'How volcanic effects are modeled in the atmosphere.',
        'members': [
            ('high frequency solar constant anomaly', None),
            ('stratospheric aerosols optical thickness', None),
            ('other', None),
            ('none', None),
        ]
    },
}
