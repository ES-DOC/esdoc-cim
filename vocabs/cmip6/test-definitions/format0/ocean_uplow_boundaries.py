__author__ = 'eguil'
version = '0.0.1'

#
# CMIP6 ocean upper and lower boundaries CV
#
# Version history on git/bitbucket#
#
# Top level process
#
ocean_uplow_boundaries = {
    'base': 'science.process',
    'values': {
        'name': 'Ocean upper and lower boundaries',
        'context': 'Properties of upper and lower boundaries within the ocean component',
        'id': 'cmip6.ocean.uplowbound',
        'sub-processes': ['ocean_free_surface',
                          'ocean_bottom_boundary_layer',
                          ],
        }
    }
#
# Sub-processes
#

ocean_free_surface = {
    'base': 'science.sub_process',
    'values': {
        'name': 'Ocean free surface',
        'context': 'Key properties of free surface in the ocean',
        'id': 'cmip6.ocean.uplowbound.free.surface',
        'details': ['ocean_free_surface_props',],
        }
    }

ocean_bottom_boundary_layer = {
    'base': 'science.sub_process',
    'values': {
        'name': 'Ocean bottom boundary layer',
        'context': 'Key properties of bottom boundary layer in the ocean',
        'id': 'cmip6.ocean.uplowbound.bottom.bl',
        'details': ['ocean_bottom_bl_props',],
        }
    }

#
# Detailed processes properties
# NB: The difference between names and contexts is that the name is the name
# of the property detail, the context is the scientific context of the
# particular detail (which might just be a definition of the name).

ocean_free_surface_props = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of free surface in ocean',
         'id': 'cmip6.ocean.uplowbound.free.surface.details',
         'name': 'Properties of free surface in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.free.surface.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_embeded_seaice','bool','1.1',
          'Is the sea-ice embeded in the ocean model (instead of levitating) ?'),
         ]
    }

ocean_bottom_bl_props = {
    'base': 'science.process_detail',
    'values':
        {'context': 'Properties of bottom boundary layer in ocean',
         'id': 'cmip6.ocean.uplowbound.bottom.bl.details',
         'name': 'Properties of bottom boundary layer in ocean',
         'select': 'scheme',
         'from_vocab': 'cmip6.ocean.bottom.bl.types.%s' % version,
         'with_cardinality':'1.1',
         },
    'properties':
        [('ocean_bbl_lateral_mixing_coef','int','0.1',
          'If bottom BL is diffusive, specify value of lateral mixing coefficient (in m2/s)'),
         ('ocean_sill_overflow','char','1.1',
          'Describe any specific treatment of sill overflows')
         ]
    }

#
# CV for enumerated lists
#


ocean_free_surface_types = {
    'name': 'Type of free surface in ocean',
    'id': 'cmip6.ocean.free.surface.types',
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

ocean_bottom_bl_types = {
    'name': 'Type of bottom boundary layer in ocean',
    'id': 'cmip6.ocean.bottom.bl.types',
    'members': [
        ('Diffusive', 'tbd'),
        ('Acvective', 'tbd'),
        ('Other', 'tbd'),
        ]
    }
