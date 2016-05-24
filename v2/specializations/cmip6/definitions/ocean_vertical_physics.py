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
ID = 'cmip6.ocean.vertical_physics'

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
DESCRIPTION = 'Characteristics of ocean vertical physics'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['vertical_physics_details'] = {
    'description': 'Properties of vertical physics in ocean',
    'properties': [
        ('convection_type', 'ENUM:vertphys_convection_types', '1.1',
         'Type of vertical convection in ocean'),
        ('tide_induced_mixing', 'str', '1.1',
        'Describe how tide induced mixing is modelled (barotropic, baroclinic, none)'),
        ('langmuir_cells_mixing', 'bool', '1.1',
        'Is there Langmuir cells mixing in upper ocean ?'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['ocean_bndlayer_mixing'] = {
    'description': 'Properties of boundary layer mixing in the ocean (aka mixed layer)',
    'details': ['bndlayer_mixing_tracers',
                'bndlayer_mixing_momentum'],
}

SUB_PROCESSES['ocean_interior_mixing'] = {
    'description': 'Properties of interior vertical mixing in the ocean',
    'details': ['interior_mixing_tracers',
                'interior_mixing_momentum'],
}


# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES: DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['bndlayer_mixing_tracers'] = {
    'description': 'Properties of boundary layer (BL) mixing on tracers in the ocean ',
    'properties': [
        ('type', 'ENUM:bndlayer_mixing_types', '1.1',
            'Type of boundary layer mixing for tracers in ocean'),
        ('closure_order', 'float','0.1',
            'If turbulent BL mixing of tracers, specific order of closure (0, 1, 2.5, 3)'),
        ('constant', 'int','0.1',
            'If constant BL mixing of tracers, specific coefficient (m2/s)'),
        ('background', 'str','1.1',
            'Background BL mixing of tracers coefficient, (schema and value in m2/s - may by none)'),
    ]
}

SUB_PROCESS_DETAILS['bndlayer_momentum_tracers'] = {
    'description': 'Properties of boundary layer (BL) mixing on momentum in the ocean ',
    'properties': [
        ('type', 'ENUM:bndlayer_mixing_types', '1.1',
            'Type of boundary layer mixing for momentum in ocean'),
        ('closure_order', 'float','0.1',
            'If turbulent BL mixing of momentum, specific order of closure (0, 1, 2.5, 3)'),
        ('constant', 'int','0.1',
            'If constant BL mixing of momentum, specific coefficient (m2/s)'),
        ('background', 'str','1.1',
            'Background BL mixing of momentum coefficient, (schema and value in m2/s - may by none)'),
    ]
}

SUB_PROCESS_DETAILS['interior_mixing_tracers'] = {
    'description': 'Properties of interior mixing on tracers in the ocean ',
    'properties': [
        ('type', 'ENUM:interior_mixing_types', '1.1',
         'Type of interior mixing for tracers in ocean'),
        ('constant', 'int','0.1',
            'If constant interior mixing of tracers, specific coefficient (m2/s)'),
        ('profile', 'str','1.1',
            'Is the background interior mixing using a vertical profile for tracers (i.e is NOT constant) ?'),
        ('background', 'str','1.1',
            'Background interior mixing of tracers coefficient, (schema and value in m2/s - may by none)'),
    ]
}

SUB_PROCESS_DETAILS['interior_mixing_momentum'] = {
    'description': 'Properties of interior mixing on momentum in the ocean ',
    'properties': [
        ('type', 'ENUM:interior_mixing_types', '1.1',
         'Type of interior mixing for momentum in ocean'),
        ('constant', 'int','0.1',
            'If constant interior mixing of momentum, specific coefficient (m2/s)'),
        ('profile', 'str','1.1',
            'Is the background interior mixing using a vertical profile for momentum (i.e is NOT constant) ?'),
        ('background', 'str','1.1',
            'Background interior mixing of momentum coefficient, (schema and value in m2/s - may by none)'),
    ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['vertphys_convection_types'] = {
    'description': 'Types of convection scheme in ocean',
    'members': [
        ('Non-penetrative convective adjustment', 'tbd'),
        ('Enhanced vertical diffusion', 'tbd'),
        ('Included in turbulence closure', 'tbd'),
        ('Other', 'tbd'),
     ]
}

ENUMERATIONS['bndlayer_mixing_types'] = {
    'description': 'Types of boundary layer mixing in ocean',
    'members': [
        ('Constant value', 'tbd'),
        ('Turbulent closure - TKE', 'tbd'),
        ('Turbulent closure - KPP', 'tbd'),
        ('Turbulent closure - Mellor-Yamada', 'tbd'),
        ('Turbulent closure - Bulk Mixed Layer', 'tbd'),
        ('Richardson number dependent - PP', 'tbd'),
        ('Richardson number dependent - KT', 'tbd'),
        ('Imbeded as isopycnic vertical coordinate', 'tbd'),
        ('Other', 'tbd'),
     ]
}

ENUMERATIONS['interior_mixing_types'] = {
    'description': 'Types of interior mixing in ocean',
    'members': [
        ('Constant value', 'tbd'),
        ('Turbulent closure - TKE', 'tbd'),
        ('Turbulent closure - Mellor-Yamada', 'tbd'),
        ('Richardson number dependent - PP', 'tbd'),
        ('Richardson number dependent - KT', 'tbd'),
        ('Imbeded as isopycnic vertical coordinate', 'tbd'),
        ('Other', 'tbd'),
     ]
}

