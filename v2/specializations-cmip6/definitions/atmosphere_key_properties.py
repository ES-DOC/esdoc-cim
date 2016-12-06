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
            'Basic approximations made in the atmosphere.',)
        ]
    }


DETAILS['orography'] = {
    'description': "Characteristics of the model orography",
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
    'description': "Type of atmospheric model",
    'is_open': True,
    'members': [
        ('AGCM', 'Atmospheric General Circulation Model'),
        ('ARCM', 'Atmospheric Regional Climate Model'),
        ]
    }

ENUMERATIONS['basic_approximations_attributes'] = {
    'description': "Basic approximations made in the atmosphere",
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


ENUMERATIONS['orography_type'] = {
    'description': "Time adaptation of the orography",
    'is_open': False,
    'members': [
        ('present-day', None),
        ('modified', None),
        ]
    }

ENUMERATIONS['orography_changes'] = {
    'description': "If the orography type is modified describe the time adaptation changes",
    'is_open': False,
    'members': [
        ('related to ice sheets', None),
        ('related to tectonics', None),
        ('modified mean', None),
        ('modified variance if taken into account in model (cf gravity waves)', None),
        ]
    }
