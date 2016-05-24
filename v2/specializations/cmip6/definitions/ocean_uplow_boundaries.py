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
# Set to 'cmip6.<REALM>.<PROCESS>
# --------------------------------------------------------------------
ID = 'cmip6.ocean.uplow_boundaries'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.process'

from collections import OrderedDict

# --------------------------------------------------------------------
# PROCESS: DESCRIPTION
#
# Scientific context of the process
# --------------------------------------------------------------------
DESCRIPTION = 'Properties of ocean upper and lower boundaries'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['ocean_free_surface'] = {
    'description': 'Properties of free surface in ocean',
    'properties': [
        ('scheme', 'ENUM:free_surface_types', '1.1'
        'Free surface scheme in ocean'),
        ('ocean_embeded_seaice','bool','1.1',
        'Is the sea-ice embeded in the ocean model (instead of levitating) ?'),
     ]
}

DETAILS['ocean_bottom_boundary_layer'] = {
    'description': 'Properties of bottom boundary layer in ocean',
    'properties': [
        ('type', 'ENUM:bottom_bl_types', '1.1'
        'Type of bottom boundary layer in ocean'),
        ('ocean_bbl_lateral_mixing_coef','int','0.1',
        'If bottom BL is diffusive, specify value of lateral mixing coefficient (in m2/s)'),
        ('ocean_sill_overflow','str','1.1',
        'Describe any specific treatment of sill overflows')
     ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['free_surface_types'] = {
    'description': 'Type of free surface in ocean',
    'members': [
        ('Linear implicit', 'tbd'),
        ('Linear filtered', 'tbd'),
        ('Linear semi-explicit', 'tbd'),
        ('Non-linear implicit', 'tbd'),
        ('Non-linear filtered', 'tbd'),
        ('Non-linear semi-explicit', 'tbd'),
        ('Other', 'tbd'),
        ]
}

ENUMERATIONS['bottom_bl_types'] = {
    'description': 'Type of bottom boundary layer in ocean',
    'members': [
        ('Diffusive', 'tbd'),
        ('Acvective', 'tbd'),
        ('Other', 'tbd'),
        ]
}

