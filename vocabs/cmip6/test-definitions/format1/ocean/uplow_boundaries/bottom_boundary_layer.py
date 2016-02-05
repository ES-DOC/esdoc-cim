"""Key properties of bottom boundary layer in the ocean'.

type: science.sub_process

"""


def props():
    """Properties of bottom boundary layer in ocean.

    type: science.process_detail

    """
    return {
        "scheme": {
            "help": "Type of bottom boundary layer in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Diffusive', 'tbd'),
                ('Acvective', 'tbd'),
                ('Other', 'tbd'),
            ]
        },
        "lateral_mixing_coef": {
            "help": "If bottom BL is diffusive, specify value of lateral mixing coefficient (in m2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "sill_overflow": {
            "help": "Describe any specific treatment of sill overflows",
            "type": "str",
            "cardinality": "1.1"
        }
    }
