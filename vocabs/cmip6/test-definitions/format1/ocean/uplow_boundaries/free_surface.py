"""Key properties of free surface in the ocean'.

type: science.sub_process

"""


def props():
    """Properties of free surface in ocean.

    type: science.process_detail

    """
    return {
        "scheme": {
            "help": "Type of free surface in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Linear implicit', 'tbd'),
                ('Linear filtered', 'tbd'),
                ('Linear semi-explicit', 'tbd'),
                ('Non-linear implicit', 'tbd'),
                ('Non-linear filtered', 'tbd'),
                ('Non-linear semi-explicit', 'tbd'),
                ('Other', 'tbd'),
            ]
        },
        "embedded_seaice": {
            "help": "Is the sea-ice embeded in the ocean model (instead of levitating) ?",
            "type": "bool",
            "cardinality": "1.1"
        }
    }
