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
ID = 'cmip6.ocean.lateral_physics'

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
DESCRIPTION = 'Characteristics of ocean lateral physics'

# --------------------------------------------------------------------
# PROCESS: DETAILS
#
# Sets of details for the process
# --------------------------------------------------------------------
DETAILS = OrderedDict()

DETAILS['ocean_transient_eddy_representation'] = {
    'description': 'Type of transient eddy representation in ocean',
    'properties': [
        ('scheme', 'ENUM:latphys_transient_eddy_types', '1.1',
         'Type of transient eddy representation in ocean'),
    ]
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES
#
# Sets of discrete portions of the process
# --------------------------------------------------------------------
SUB_PROCESSES = OrderedDict()

SUB_PROCESSES['lateral_physics_momentum'] = {
    'description': 'Properties of lateral physics for momentum in ocean',
    'details': ['lateral_physics_momentum_operator',
                'lateral_physics_mom_eddy_viscosity_coeff'],
 }

SUB_PROCESSES['lateral_physics_tracers'] = {
    'description': 'Properties of lateral physics for tracers in ocean',
    'details': ['lateral_physics_tracers_details',
                'lateral_physics_tracers_operator',
                'lateral_physics_tra_eddy_viscosity_coeff',
                'lateral_physics_eddy_induced_velocity'
                ],
}

# --------------------------------------------------------------------
# PROCESS: SUB PROCESSES: DETAILS
#
# Sets of details for the sub processes
# --------------------------------------------------------------------
SUB_PROCESS_DETAILS = OrderedDict()

SUB_PROCESS_DETAILS['lateral_physics_momentum_operator'] = {
    'description': 'Properties of lateral physics operator for momentum in ocean',
    'properties': [
        ('direction', 'ENUM:latphys_operator_direc_types', '1.1',
            'Direction of lateral physics momemtum scheme in the ocean'),
        ('order', 'ENUM:latphys_operator_order_types', '1.1',
            'Order of lateral physics momemtum scheme in the ocean'),
        ('discretisation', 'ENUM:latphys_operator_discret_types', '1.1',
            'Discretisation of lateral physics momemtum scheme in the ocean'),
        ]
}

SUB_PROCESS_DETAILS['lateral_physics_mom_eddy_viscosity_coeff'] = {
    'description': 'Properties of eddy viscosity coeff in lateral physics momemtum scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eddy_visc_coeff_types', '1.1',
            'Lateral physics momemtum eddy viscosity coeff type in the ocean'),
        ('eddy_visc_coeff_cst','int','0.1',
            'If constant, value of eddy viscosity coeff in lateral physics momemtum scheme (in m2/s)'),
        ('eddy_visc_coeff_var','str','0.1',
            'If space-varying, describe variations of eddy viscosity coeff in lateral physics momemtum scheme'),
        ('eddy_visc_coeff_background','int','1.1',
            'Background value of eddy viscosity coeff in lateral physics momemtum scheme (in m2/s)'),
        ('eddy_visc_coeff_backscatter','bool','1.1',
            'Is there backscatter in eddy viscosity coeff in lateral physics momemtum scheme ?')
        ]
}

SUB_PROCESS_DETAILS['lateral_physics_tracers_operator'] = {
    'description': 'Properties of lateral physics for tracers in ocean',
    'properties': [
        ('mesoscale_closure','bool','1.1',
            'Is there a mesoscale closure in the lateral physics tracers scheme ?')
        ]
}

SUB_PROCESS_DETAILS['lateral_physics_tracers_operator'] = {
    'description': 'Properties of lateral physics operator for tracers in ocean',
    'properties': [
        ('direction', 'ENUM:latphys_operator_direc_types', '1.1',
            'Direction of lateral physics tracers scheme in the ocean'),
        ('order', 'ENUM:latphys_operator_order_types', '1.1',
            'Order of lateral physics tracers scheme in the ocean'),
        ('discretisation', 'ENUM:latphys_operator_discret_types', '1.1',
            'Discretisation of lateral physics tracers scheme in the ocean'),
        ]
}

SUB_PROCESS_DETAILS['lateral_physics_tra_eddy_viscosity_coeff'] = {
    'description': 'Properties of eddy viscosity coeff in lateral physics tracers scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eddy_visc_coeff_types', '1.1',
            'Lateral physics tracers eddy viscosity coeff type in the ocean'),
        ('eddy_visc_coeff_cst','int','0.1',
            'If constant, value of eddy viscosity coeff in lateral physics tracers scheme (in m2/s)'),
        ('eddy_visc_coeff_var','str','0.1',
            'If space-varying, describe variations of eddy viscosity coeff in lateral physics tracers scheme'),
        ('eddy_visc_coeff_background','int','1.1',
            'Background value of eddy viscosity coeff in lateral physics tracers scheme (in m2/s)'),
        ('eddy_visc_coeff_backscatter','bool','1.1',
            'Is there backscatter in eddy viscosity coeff in lateral physics tracers scheme ?')
        ]
}

SUB_PROCESS_DETAILS['lateral_physics_eddy_induced_velocity'] = {
    'description': 'Properties of eddy induced velocity (EIV) in lateral physics tracers scheme in the ocean',
    'properties': [
        ('type', 'ENUM:latphys_eiv_types', '1.1',
            'Type of EIV in lateral physics tracers in the ocean'),
        ('eiv_constant_val','int','0.1',
            'If EIV scheme for tracers is constant, specify coefficient value (M2/s)'),
        ('eiv_flux_type','str','1.1',
            'Type of EIV flux (advective or skew)'),
        ('eiv_added_diff','str','1.1',
            'Type of EIV added diffusivity (constant, flow dependent or none)')
        ]
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()

ENUMERATIONS['latphys_transient_eddy_types'] = {
    'description': 'Type of transient eddy representation in ocean',
    'members': [
        ('None','No transient eddies in ocean'),
        ('Eddy active','Full resolution of eddies'),
        ('Eddy admitting', 'Some eddy activity permitted by resolution'),
     ]
}

ENUMERATIONS['latphys_operator_direc_types'] = {
    'description':'Type of lateral physics direction in ocean',
    'members':[
        ('Horizontal', 'tbd'),
        ('Isopycnal', 'tbd'),
        ('Isoneutral', 'tbd'),
        ('Geopotential', 'tbd'),
        ('Iso-level', 'tbd'),
        ('Other', 'tbd'),
     ]
}

ENUMERATIONS['latphys_operator_order_types'] = {
    'description':'Type of lateral physics order in ocean',
    'members':[
        ('Harmonic', 'Second order'),
        ('Bi-harmonic', 'Fourth order'),
        ('Other', 'tbd'),
     ]
}

ENUMERATIONS['latphys_operator_discret_types'] = {
    'description':'Type of lateral physics discretisation in ocean',
    'members':[
        ('Second order', 'Second order'),
        ('Fourth order', 'Fourth order'),
        ('Flux limiter', 'tbd'),
        ('Other', 'tbd'),
     ]
}

ENUMERATIONS['latphys_eddy_visc_coeff_types'] = {
    'description':'Type of lateral physics eddy viscosity coeff in ocean',
    'members':[
        ('Constant', 'tbd'),
        ('Space varying', 'tbd'),
        ('Time + space varying (Smagorinsky)', 'tbd'),
        ('Other', 'tbd'),
     ]
}

ENUMERATIONS['latphys_eiv_types'] = {
    'description':'Type of lateral physics eddy induced velocity in ocean',
    'members':[
        ('GM', 'Gent & McWilliams'),
        ('Other', 'tbd'),
     ]
}