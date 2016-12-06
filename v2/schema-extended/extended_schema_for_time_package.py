
# -*- coding: utf-8 -*-

"""
.. module:: cim.v2.extended_schema_for_time_package.py

   :license: GPL / CeCILL
   :platform: Unix, Windows
   :synopsis: Schema information for the cim v2 ontology.

.. moduleauthor:: Earth System Documentation (ES-DOC) <dev@es-doc.org>
.. note:: Code generated using the pyesdoc framework.

"""


def calendar():
    """Describes the calendar required/used in an experiment/simulation.
    This class is based on the calendar attributes and properties found in the
    CF netCDF conventions.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('description', 'str', '0.1',
                "Extra information about the calendar."),
            ('month_lengths', 'int', '0.N',
                "Used for special calendars to provide month lengths."),
            ('name', 'str', '0.1',
                "Can be used to name a special calendar type."),
            ('standard_name', 'time.calendar_types', '1.1',
                "Type of calendar used."),
            ]
    }


def date_time():
    """A date or time. Either in simulation time with the simulation
    calendar, or with reference to a simulation start, in which
    case the datetime is an interval after the start date.

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('is_offset', 'bool', '0.1',
                "Date is offset from start of an integration."),
            ('value', 'str', '1.1',
                "Date or time - some of (from left to right): yyyy-mm-dd:hh:mm:ss."),
            ]
    }


def datetime_set():
    """A set of times. This is an abstract class which is specialised into
    a periodic or aperiodic (irregular) list.  Note that we assume either a
    periodic set of dates which can be date and/or time, or an irregular set
    which can only be dates.

	"""
    return {
        'type': 'class',
        'base': None,
        'sub-classes': [
            'time.irregular_dateset',
            'time.regular_timeset'
        ],
        'is_abstract': True,
        'is_document': False,
        'properties': [
            ('length', 'int', '1.1',
                "Number of times in set."),
            ]
    }


def irregular_dateset():
    """A set of irregularly spaced times, provided as a comma separated string of yyyy-mm-dd in
     the appropriate calendar.

	"""
    return {
        'type': 'class',
        'base': "time.datetime_set",
        'base-hierarchy': [
            'time.datetime_set'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('date_set', 'str', '1.1',
                "Set of dates, comma separated yyyy-mm-dd."),
            ],
        'properties-all': [
            'date_set',
            'length',
            ],
        'properties-inherited': [
            'length :: time.datetime_set',
            ]
    }


def regular_timeset():
    """A regularly spaced set of times.

	"""
    return {
        'type': 'class',
        'base': "time.datetime_set",
        'base-hierarchy': [
            'time.datetime_set'
            ],
        'base-hierarchy-depth': 1,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('increment', 'time.time_period', '1.1',
                "Interval between members of set."),
            ('length', 'int', '1.1',
                "Number of times in set."),
            ('start_date', 'time.date_time', '1.1',
                "Beginning of time set."),
            ],
        'properties-all': [
            'increment',
            'length',
            'length',
            'start_date',
            ],
        'properties-inherited': [
            'length :: time.datetime_set',
            ]
    }


def time_period():
    """A time period/interval (aka temporal extent).

	"""
    return {
        'type': 'class',
        'base': None,
        'is_abstract': False,
        'is_document': False,
        'properties': [
            ('calendar', 'time.calendar', '0.1',
                "Calendar, default is standard aka gregorian."),
            ('date', 'time.date_time', '0.1',
                "Optional start/end date of time period."),
            ('date_type', 'time.period_date_types', '1.1',
                "Describes how the date is used to define the period."),
            ('length', 'str', '1.1',
                "Duration of the time period."),
            ('units', 'time.time_units', '1.1',
                "Appropriate time units."),
            ]
    }




