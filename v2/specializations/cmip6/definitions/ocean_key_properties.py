CONTACT = 'Eric Guilyardi'

AUTHORS = 'Eric Guilyardi'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS
#
# Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# PROCESS IDENTIFIER
#
# Set to 'cmip6.<REALM>.key_properties'
# --------------------------------------------------------------------
ID = 'cmip6.ocean.key_properties'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.key_properties'

from collections import OrderedDict

# --------------------------------------------------------------------
# KEY PROPERTIES: DESCRIPTION
#
# Scientific context of the key properties
# --------------------------------------------------------------------
DESCRIPTION = 'Key properties of the ocean'

# --------------------------------------------------------------------
# KEY PROPERTIES: DETAILS
#
# Sets of details for the key properties
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['general'] = {
    'description': 'General key properties in ocean',
    'properties': [
        ('model_family', 'ENUM:model_family_types', '1.1',
            'Type of ocean model.'),
        ('basic_approximations', 'ENUM:ocean_basic_approx_types', '1.N',
            'Basic approximations made in the ocean.',),
        ('prognostic_variables', 'ENUM:prognostic_vars_types', '1.N',
            'List of prognostic variables in the ocean component.'),
    ]
}

DETAILS['seawater_properties'] = {
    'description': 'Physical properties of seawater in ocean',
    'properties' : [
        ('seawater_eos_type', 'ENUM:seawater_eos_types', '1.1',
            'Type of EOS for sea water'),
        ('ocean_freezing_point', 'str', '1.1',
            'Describe freezing point in ocean (fixed or varying)'),
        ('ocean_specific_heat', 'str', '1.1',
            'Describe specific heat in ocean (fixed or varying)'),
    ]
}

DETAILS['bathymetry'] = {
    'description': 'Properties of bathymetry in ocean',
    'properties' : [
        ('bathymetry_reference_dates', 'ENUM:bathymetry_ref_dates', '1.1',
            'Reference date of bathymetry'),
        ('ocean_bathymetry_type', 'bool', '1.1',
            'Is the bathymetry fixed in time in the ocean ?'),
        ('ocean_smoothing', 'str', '1.1',
            'Describe any smoothing or hand editing of bathymetry in ocean'),
        ('ocean_bathymetry_source', 'str', '1.1',
            'Describe source of bathymetry in ocean'),
    ]
}

DETAILS['nonoceanic_waters'] = (
    'str',
    '0.1',
    'Describe if/how isolated seas and river mouth mixing or other specific treatment is performed'
    )

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTENT
#
# <DESCRIPTION NEEDED>
# --------------------------------------------------------------------
EXTENT = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTENT DETAILS
#
# Sets of details for the extent.
# --------------------------------------------------------------------
EXTENT_DETAILS = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: RESOLUTION
#
# The resolution of the grid.
# --------------------------------------------------------------------
RESOLUTION = OrderedDict()

RESOLUTION['resolution'] = {
    'description': 'Resolution in the ocean grid',
    'details' : ['thickness_of_surface_level'],
}

# --------------------------------------------------------------------
# KEY PROPERTIES: RESOLUTION DETAILS
#
# Sets of details for the resolution
# --------------------------------------------------------------------
RESOLUTION_DETAILS = OrderedDict()

RESOLUTION_DETAILS['thickness_of_surface_level'] = (
    'float', '0.1',
    'Thickness in metres of surface ocean level (e.g. 1)'
    )

# --------------------------------------------------------------------
# KEY PROPERTIES: TUNING APPLIED
#
# Any tuning used to optimise the parameters in this realm
# --------------------------------------------------------------------
TUNING_APPLIED = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: TUNING APPLIED DETAILS
#
# Sets of details for the tuning
# --------------------------------------------------------------------
TUNING_APPLIED_DETAILS  = OrderedDict()

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTRA CONSERVATION PROPERTIES
#
# Details of methodology needed to conserve variables between
# processes
# --------------------------------------------------------------------
EXTRA_CONSERVATION_PROPERTIES = OrderedDict()

EXTRA_CONSERVATION_PROPERTIES['conservation'] = {
    'description': 'Conservation in the ocean component',
    'details': ['conservation_details'],
}

# --------------------------------------------------------------------
# KEY PROPERTIES: EXTRA CONSERVATION PROPERTIES DETAILS
#
# Sets of details for the conservation
# --------------------------------------------------------------------
EXTRA_CONSERVATION_PROPERTIES_DETAILS = OrderedDict()

EXTRA_CONSERVATION_PROPERTIES_DETAILS['conservation_details'] = {
    'description': 'Properties conserved in the ocean component',
    'properties': [
        ('conservation_scheme', 'ENUM:conservation_props_types', '1.N',
         'Conservation scheme in ocean'),
        ('ocean_conservation_method', 'str', '1.1',
         'Describe how conservation properties are ensured in ocean'),
    ]
}

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['model_family_types'] = {
    'description': 'Types of ocean models',
    'members': [
        ('OGCM','tbd'),
        ('slab ocean', 'tbd'),
        ('mixed layer ocean', 'tbd'),
        ('Other', 'tbd'),

    ]
}

ENUMERATIONS['ocean_basic_approx_types'] = {
    'description': 'Types of basic approximation in ocean',
    'members': [
        ('Primitive equations','tbd'),
        ('Non-hydrostatic', 'tbd'),
        ('Boussinesq', 'tbd'),
        ('Other', 'tbd')
    ]
}

ENUMERATIONS['prognostic_vars_types'] = {
    'description': 'Types of basic approximation in ocean',
    'members': [
        ('Potential temperature','tbd'),
        ('Conservative temperature','tbd'),
        ('Salinity','tbd'),
        ('U-velocity','tbd'),
        ('V-velocity','tbd'),
        ('W-velocity','tbd'),
        ('SSH','Sea Surface Height'),
        ('Other', 'Other prognostic variables')
    ]
}

ENUMERATIONS['seawater_eos_types'] = {
    'description': 'Types of seawater Equation of State in ocean',
    'members': [
        ('Linear','tbd'),
        ('Mc Dougall et al.', 'tbd'),
        ('Jackett et al. 2006', 'tbd'),
        ('TEOS 2010', 'tbd'),
        ('Other', 'tbd')
    ]
}

ENUMERATIONS['bathymetry_ref_dates'] = {
    'description': 'List of reference dates for bathymetry in ocean',
    'members': [
        ('Present day','tbd'),
        ('21000 years BP', 'tbd'),
        ('6000 years BP', 'tbd'),
        ('LGM', 'Last Glacial Maximum'),
        ('Pliocene', 'tbd'),
        ('Other', 'tbd')
    ]
}
             
ENUMERATIONS['conservation_props_types'] = {
    'description': 'Types of conservation properties in ocean',
    'members': [
        ('Energy','tbd'),
        ('Enstrophy','tbd'),
        ('Salt', 'tbd'),
        ('Volume of ocean', 'tbd'),
        ('Other', 'tbd')
    ]
}
