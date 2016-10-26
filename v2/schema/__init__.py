"""
.. module:: esdoc_mp.ontologies.schemas.cim.v2.__init__.py
   :license: GPL/CeCIL
   :platform: Unix, Windows
   :synopsis: CIM v2 ontology schema.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
from esdoc_mp.ontologies.schemas.cim.v2 import activity_classes
from esdoc_mp.ontologies.schemas.cim.v2 import data_classes
from esdoc_mp.ontologies.schemas.cim.v2 import designing_classes
from esdoc_mp.ontologies.schemas.cim.v2 import drs_entities
from esdoc_mp.ontologies.schemas.cim.v2 import platform_classes
from esdoc_mp.ontologies.schemas.cim.v2 import science_classes
from esdoc_mp.ontologies.schemas.cim.v2 import science_enums
from esdoc_mp.ontologies.schemas.cim.v2 import shared_classes
from esdoc_mp.ontologies.schemas.cim.v2 import shared_classes_doc
from esdoc_mp.ontologies.schemas.cim.v2 import software_classes
from esdoc_mp.ontologies.schemas.cim.v2 import software_enums
from esdoc_mp.ontologies.schemas.cim.v2 import time as time_classes



# Ontology name.
NAME = 'cim'

# Ontology version.
VERSION = '2'

# Ontology doc string.
DOC = 'Metafor CIM ontology schema - version 2'


def activity():
    """Types that describe context against which climate models are run.

    """
    return {
        activity_classes
    }


def data():
    """Types that describe output that climate models emit.

    """
    return {
        data_classes
    }


def designing():
    """Types that describe project design features.

    """
    return {
        designing_classes
    }


def drs():
    """Types that describe the directory structures to which climate model output is written.

    """
    return {
        drs_entities
    }


def platform():
    """Types that describe hardware upon which climate models are run.

    """
    return {
        platform_classes
    }


def science():
    """Types that describe the science being performed.

    """
    return {
        science_classes,
        science_enums
    }


def shared():
    """Shared types that might be imported from other packages within the ontology.

    """
    return {
        shared_classes,
        shared_classes_doc
    }


def software():
    """Types that describe the software that constiutes a climate model.

    """
    return {
        software_classes,
        software_enums
    }

def time():
    """Types that describe the software that constiutes a climate model.

    """
    return {
        time_classes
    }