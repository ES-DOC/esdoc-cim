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
# Set to 'cmip6.<REALM>.grid
# --------------------------------------------------------------------
ID = 'cmip6.ocean.grid'

# --------------------------------------------------------------------
# INTERNAL VARIABLES (do not change)
# --------------------------------------------------------------------
_TYPE = 'cim.2.science.grid'

from collections import OrderedDict

# --------------------------------------------------------------------
# GRID: DESCRIPTION
#
# Scientific context of the grid
# --------------------------------------------------------------------
DESCRIPTION = 'Ocean grid and discretisation'

# --------------------------------------------------------------------
# GRID: DETAILS
#
# Sets of details for the grid
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['vertical_grid'] = {
    'description': 'Properties of vertical coordinate in ocean',
    'properties': [
        ('number_of_levels','int', '1.1',
            'Number of vertical levels'),
    ]
}

DETAILS['horizontal_grid'] = {
    'description': 'Properties of H coordinate in ocean',
    'properties': [
        ('horizontal_grid_type', 'ENUM:horiz_grid_types', '1.1',
            'Horizontal grid type'),
        ('number_of_xy_gridpoints', 'int', '0.1',
            'Total number of horizontal points on computational grid'),
    ]
}

# --------------------------------------------------------------------
# DISCRETISATION
#
# Description of the numerics of the discretisation
# --------------------------------------------------------------------
DISCRETISATION = OrderedDict()

DISCRETISATION['discretisation'] = {
    'description': 'Type of discretisation scheme in ocean',
    'details': [
        'horizontal_discretisation',
        'vertical_discretisation'
        ]
}

# --------------------------------------------------------------------
# DISCRETISATION: DETAILS
#
# Sets of details for the discretisation
# --------------------------------------------------------------------
DISCRETISATION_DETAILS = OrderedDict()

DISCRETISATION_DETAILS['vertical_discretisation'] = {
    'description': 'Properties of vertical coordinate in ocean',
    'properties': [
        ('vertical_coord_type', 'ENUM:vertical_coord_types', '1.1',
            'Type of vertical coordinates in ocean'),
        ('partial_steps', 'bool', '1.1',
            'Using partial steps with Z or Z* vertical coordinate in ocean ?'),
    ]
}

DISCRETISATION_DETAILS['horizontal_discretisation'] = {
    'description': 'Type of horizontal discretisation scheme in ocean',
    'properties': [
        ('horiz_discret_scheme', 'ENUM:horiz_scheme_types', '1.1',
            'Horizontal discretisation scheme in ocean'),
        ('ocean_pole_singularity_treatment', 'str', '1.1',
            'Describe how the North Pole singularity is treated (filter, pole rotation/displacement, artificial island, ...)'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['horiz_grid_types'] = {
    'description': 'Types of horizonal grid in ocean',
    'members': [
        ('Latlon','tbd'),
        ('Rotated north pole','tbd'),
        ('Two north poles (ORCA-style)','tbd'),
        ('Other','tbd'),
    ]
}

ENUMERATIONS['horiz_scheme_types'] = {
    'description': 'Types of horizonal scheme in ocean',
    'members': [
        ('Finite difference / Arakawa B-grid','tbd'),
        ('Finite difference / Arakawa C-grid','tbd'),
        ('Finite difference / Arakawa E-grid','tbd'),
        ('Finite volumes', 'tbd'),
        ('Finite elements', 'tbd'),
        ('Other', 'tbd')
    ]
}

ENUMERATIONS['vertical_coord_types'] = {
    'description': 'Types of vertical coordinates in ocean',
    'members': [
        ('Z-coordinate','tbd'),
        ('Z*-coordinate', 'tbd'),
        ('S-coordinate', 'tbd'),
        ('Isopycnic - sigma 0','Density referenced to the surface'),
        ('Isopycnic - sigma 2','Density referenced to 2000 m'),
        ('Isopycnic - sigma 4','Density referenced to 4000 m'),
        ('Isopycnic - other','Other density-based coordinate'),
        ('Hybrid / Z+S', 'tbd'),
        ('Hybrid / Z+isopycnic', 'tbd'),
        ('Hybrid / ALE', 'tbd'),
        ('Hybrid / other', 'tbd'),
        ('Pressure referenced (P)', 'tbd'),
        ('P*','tbd'),
        ('Z**', 'tbd'),
        ('Other', 'tbd')
    ]
}
