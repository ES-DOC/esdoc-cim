# -*- coding: utf-8 -*-

"""
.. module:: science_enums.py
   :synopsis: Set of CIM v2 ontology type definitions.

"""


def model_types():
    """Defines a set of gross model classes.

    """
    return {
        'type': 'enum',
        'is_open': False,
        'members': [
            ("Atm Only", "Atmosphere Only"),
            ("Ocean Only", "Ocean Only"),
            ("Regional", "Regional Model"),
            ("GCM", "Global Climate Model (Atmosphere, Ocean, no carbon cycle)"),
            ("IGCM", "Intermediate Complexity GCM"),
            ("GCM-MLO", "GCM with mixed layer ocean"),
            ("Mesoscale", "Mesoscale Model"),
            ("Process", "Limited Area process model"),
            ("Planetary", "Non-Earth model")
        ]
    }
