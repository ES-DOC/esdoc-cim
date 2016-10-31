
# -*- coding: utf-8 -*-

"""
.. module:: cim.v1.extended_schema_for_quality_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v1 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the esdoc-mp framework.

"""


def cim_quality():
	"""The starting point for a quality record.  It can contain any number of issues and reports.  An issue is an open-ended description of some issue about a CIM instance.  A record is a prescribed description of some specific quantitative measure that has been applied to a CIM instance.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': True,
        'properties': [
            ('meta', 'shared.doc_meta_info', '1.1',
                "Injected document metadata."),
            ('reports', 'quality.report', '0.N',
                ""),
            ]
    }


def evaluation():
	"""Creates and returns instance of evaluation class.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('date', 'datetime', '0.1',
                ""),
            ('description', 'str', '0.1',
                ""),
            ('did_pass', 'bool', '0.1',
                ""),
            ('explanation', 'str', '0.1',
                ""),
            ('specification', 'str', '0.1',
                ""),
            ('specification_hyperlink', 'str', '0.1',
                ""),
            ('title', 'str', '0.1',
                ""),
            ('type', 'str', '0.1',
                ""),
            ('type_hyperlink', 'str', '0.1',
                ""),
            ]
    }


def measure():
	"""Creates and returns instance of measure class.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                ""),
            ('identification', 'str', '0.1',
                ""),
            ('name', 'str', '0.1',
                ""),
            ]
    }


def report():
	"""Creates and returns instance of report class.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('date', 'datetime', '0.1',
                ""),
            ('evaluation', 'quality.evaluation', '1.1',
                ""),
            ('evaluator', 'shared.responsible_party', '0.1',
                ""),
            ('measure', 'quality.measure', '1.1',
                ""),
            ]
    }




