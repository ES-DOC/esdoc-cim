# -*- coding: utf-8 -*-

"""
.. module:: esdoc_mp.ontologies.schemas.cim.v1.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: Sub-package initializer.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""

from esdoc_mp.ontologies.schemas.cim.v1 import activity_classes
from esdoc_mp.ontologies.schemas.cim.v1 import activity_enums
from esdoc_mp.ontologies.schemas.cim.v1 import data_classes
from esdoc_mp.ontologies.schemas.cim.v1 import data_enums
from esdoc_mp.ontologies.schemas.cim.v1 import grids_classes
from esdoc_mp.ontologies.schemas.cim.v1 import grids_enums
from esdoc_mp.ontologies.schemas.cim.v1 import misc_classes
from esdoc_mp.ontologies.schemas.cim.v1 import quality_classes
from esdoc_mp.ontologies.schemas.cim.v1 import quality_enums
from esdoc_mp.ontologies.schemas.cim.v1 import shared_classes
from esdoc_mp.ontologies.schemas.cim.v1 import shared_classes_time
from esdoc_mp.ontologies.schemas.cim.v1 import shared_enums
from esdoc_mp.ontologies.schemas.cim.v1 import software_classes
from esdoc_mp.ontologies.schemas.cim.v1 import software_enums


# Ontology name.
NAME = 'cim'

# Ontology version.
VERSION = '1'

# Ontology doc string.
DOC = 'Metafor CIM ontology schema - version 1'




def activity():
    """Types that describe context against which climate models are run.

    """
    return {
        activity_classes,
        activity_enums
    }


def data():
    """Types that describe output that climate models emit.

    """
    return {
        data_classes,
        data_enums
    }


def grids():
    """Types that describe the grids that climate models plot.

    """
    return {
        grids_classes,
        grids_enums
    }


def misc():
    """Miscellaneous types.

    """
    return {
        misc_classes
    }


def quality():
    """Types that describe the quailty of output that climate models emit.

    """
    return {
        quality_classes,
        quality_enums
    }


def shared():
    """Shared types that might be imported from other packages within the ontology.

    """
    return {
        shared_classes,
        shared_classes_time,
        shared_enums
    }


def software():
    """Types that describe the climate models software.

    """
    return {
        software_classes,
        software_enums
    }
