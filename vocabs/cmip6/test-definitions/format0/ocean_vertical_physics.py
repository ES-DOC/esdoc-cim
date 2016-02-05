__author__ = 'eguil'

owner = "Eric Guilyard"
version = '0.0.1'
science_contributors = [
    "Paul Durack"
]


#
# CMIP6 ocean vertical physics CV
#
# Version history on git/bitbucket#
#
# Top level process
#
ocean_vertical_physics = {
    'base': 'science.process',
    'values': {
        'name': 'Ocean vertical physics',
        'context': 'Properties of  vertical physics within the ocean component',
        'id': 'cmip6.ocean.vertphys',
        'sub-processes': ['ocean_vertphys_attributes',
                          'ocean_bndlayer_mixing',
                          'ocean_interior_mixing'],
        }
    }
#
# Sub-processes
#

ocean_vertphys_attributes = {
    'base': 'science.sub_process',
    'values': {
        'name': 'Ocean vertical physics attributes',
        'context': 'General properties of vertical physics in the ocean',
        'id': 'cmip6.ocean.vertphys.attributes',
        'details': ['ocean_vertphys_props',],
        }
    }

ocean_bndlayer_mixing = {
    'base': 'science.sub_process',
    'values': {
        'name': 'Ocean boundary layer mixing',
        'context': 'Key properties of boundary layer mixing in the ocean (aka mixed layer)',
        'id': 'cmip6.ocean.vertphys.bndlayer.mixing',
        'details': ['ocean_bndlayer_mixing_tracers','ocean_bndlayer_mixing_momentum'],
        }
    }

ocean_interior_mixing = {
    'base': 'science.sub_process',
    'values': {
        'name': 'Ocean interior mixing',
        'context': 'Key properties of interior mixing in the ocean',
        'id': 'cmip6.ocean.vertphys.interior.mixing',
        'details': ['ocean_interior_mixing_tracers','ocean_interior_mixing_momentum'],
        }
    }

#
# Detailed processes properties
# NB: The difference between names and contexts is that the name is the name
# of the property detail, the context is the scientific context of the
# particular detail (which might just be a definition of the name).

ocean_vertphys_props = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of vertical physics in ocean',
         'id': 'cmip6.ocean.vertphys.attributes.props',
         'name': 'Properties of vertical physics in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.vertphys.convection.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_tide_induced_mixing','char','1.1',
          'Describe how tide induced mixing is modelled (barotropic, baroclinic, none)'),
         ('ocean_langmuir_cells_mixing','bool','1.1',
          'Is there Langmuir cells mixing in upper ocean ?'),
         ]
    }

ocean_bndlayer_mixing_tracers = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of boundary layer mixing on tracers in ocean',
         'id': 'cmip6.ocean.vertphys.bndlayer.mixing.tracers',
         'name': 'Properties of boundary layer mixing on tracers in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.vertphys.bndlayer.mixing.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_OML_tracers_turbulent_closure_order','float','0.1',
          'If turbulent BL mixing of tracers, specific order of closure (0, 1, 2.5, 3)'),
         ('ocean_OML_tracers_constant','int','0.1',
          'If constant BL mixing of tracers, specific coefficient (m2/s)'),
         ('ocean_OML_tracers_background','char','1.1',
          'Background BL mixing of tracers coefficient, (schema and value in m2/s - may by none)'),
         ]
    }

ocean_bndlayer_mixing_momentum = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of boundary layer mixing on momentum in ocean',
         'id': 'cmip6.ocean.vertphys.bndlayer.mixing.momentum',
         'name': 'Properties of boundary layer mixing on momentum in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.vertphys.bndlayer.mixing.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_OML_momentum_turbulent_closure_order','float','0.1',
          'If turbulent BL mixing of momentum, specific order of closure (0, 1, 2.5, 3)'),
         ('ocean_OML_momentum_constant','int','0.1',
          'If constant BL mixing of momentum, specific coefficient (m2/s)'),
         ('ocean_OML_momentum_background','char','1.1',
          'Background BL mixing of momentum coefficient, (schema and value in m2/s - may by none)'),
         ]
    }

ocean_interior_mixing_tracers = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of interior mixing on tracers in ocean',
         'id': 'cmip6.ocean.vertphys.interior.mixing.tracers',
         'name': 'Properties of interior mixing on tracers in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.vertphys.interior.mixing.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_interior_tracers_constant','int','0.1',
          'If constant interior mixing of tracers, specific coefficient (m2/s)'),
         ('ocean_interior_tracers_profile','char','1.1',
          'Is the background interior mixing using a vertical profile for tracers (i.e is NOT constant) ?'),
         ('ocean_interior_tracers_background','char','1.1',
          'Background interior mixing of tracers, (schema and coeff. value in m2/s - may by none)'),
         ]
    }

ocean_interior_mixing_momentum = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of interior mixing on momentum in ocean',
         'id': 'cmip6.ocean.vertphys.interior.mixing.momentum',
         'name': 'Properties of interior mixing on momentum in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.vertphys.interior.mixing.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_interior_momentum_constant','int','0.1',
          'If constant interior mixing of momentum, specific coefficient (m2/s)'),
         ('ocean_interior_momentum_profile','char','1.1',
          'Is the background interior mixing using a vertical profile for momentum (i.e is NOT constant) ?'),
         ('ocean_interior_momentum_background','char','1.1',
          'Background interior mixing of momentum, (schema and coeff. value in m2/s - may by none)'),
         ]
    }

#
# CV for enumerated lists
#


ocean_vertphys_convection_types = {
    'name': 'Types of convection scheme in ocean',
    'id': 'cmip6.ocean.vertphys.convection.types',
    'members': [
        ('Non-penetrative convective adjustment', 'tbd'),
        ('Enhanced vertical diffusion', 'tbd'),
        ('Included in turbulence closure', 'tbd'),
        ('Other', 'tbd'),
        ]
    }


ocean_bndayer_mixing_types = {
    'name': 'Types of boundary layer mixing in ocean',
    'id': 'cmip6.ocean.vertphys.bndlayer.mixing.types',
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

ocean_interior_mixing_types = {
    'name': 'Types of boundary layer mixing in ocean',
    'id': 'cmip6.ocean.vertphys.interior.mixing.types',
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