"""Key properties of interior mixing in the ocean.

type: science.sub_process

"""


def tracers():
    """Properties of interior mixing on tracers in ocean.

    type: science.process_detail

    """
    return {
        "background": {
            "help": "Background interior mixing of tracers, (schema and coeff. value in m2/s - may by none)",
            "type": "str",
            "cardinality": "1.1"
        },
        "constant": {
            "help": "If constant interior mixing of tracers, specific coefficient (m2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "profile": {
            "help": "Is the background interior mixing using a vertical profile for tracers (i.e is NOT constant) ?",
            "type": "str",
            "cardinality": "1.1"
        },
        "scheme": {
            "help": "Types of boundary layer mixing in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": _enum_interior_mixing_types
        }
    }


def momentum():
    """Properties of interior mixing on momentum in ocean.

    type: science.process_detail

    """
    return {
        "background": {
            "help": "Background interior mixing of momentum, (schema and coeff. value in m2/s - may by none)",
            "type": "str",
            "cardinality": "1.1"
        },
        "constant": {
            "help": "If constant interior mixing of momentum, specific coefficient (m2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "scheme": {
            "help": "Types of interior mixing in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": _enum_interior_mixing_types
        },
        "profile": {
            "help": "Is the background interior mixing using a vertical profile for momentum (i.e is NOT constant) ?",
            "type": "str",
            "cardinality": "1.1"
        }
    }


_enum_interior_mixing_types = [
        ('Constant value', 'tbd'),
        ('Turbulent closure - TKE', 'tbd'),
        ('Turbulent closure - Mellor-Yamada', 'tbd'),
        ('Richardson number dependent - PP', 'tbd'),
        ('Richardson number dependent - KT', 'tbd'),
        ('Imbeded as isopycnic vertical coordinate', 'tbd'),
        ('Other', 'tbd'),
    ]
