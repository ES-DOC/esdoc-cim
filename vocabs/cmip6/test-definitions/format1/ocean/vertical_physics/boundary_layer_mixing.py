"""Key properties of boundary layer mixing in the ocean (aka mixed layer).

type: science.sub_process

"""


def tracers():
    """Properties of boundary layer mixing on tracers in ocean.

    type: science.process_detail

    """
    return {
        "background": {
            "help": "Background BL mixing of tracers coefficient, (schema and value in m2/s - may by none)",
            "type": "str",
            "cardinality": "1.1"
        },
        "constant": {
            "help": "'If constant BL mixing of tracers, specific coefficient (m2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "scheme": {
            "help": "Types of boundary layer mixing in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": _enum_boundary_layer_mixing_types
        },
        "turbulent_closure_order": {
            "help": "If turbulent BL mixing of tracers, specific order of closure (0, 1, 2.5, 3)",
            "type": "float",
            "cardinality": "0.1"
        }
    }


def momentum():
    """Properties of boundary layer mixing on momentum in ocean.

    type: science.process_detail

    """
    return {
        "background": {
            "help": "Background BL mixing of momentum coefficient, (schema and value in m2/s - may by none)",
            "type": "str",
            "cardinality": "1.1"
        },
        "constant": {
            "help": "If constant BL mixing of momentum, specific coefficient (m2/s)",
            "type": "int",
            "cardinality": "0.1"
        },
        "scheme": {
            "help": "Types of boundary layer mixing in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": _enum_boundary_layer_mixing_types
        },
        "turbulent_closure_order": {
            "help": "If turbulent BL mixing of momentum, specific order of closure (0, 1, 2.5, 3)",
            "type": "float",
            "cardinality": "0.1"
        }
    }


_enum_boundary_layer_mixing_types = [
    ('Constant value', 'tbd'),
    ('Turbulent closure - TKE', 'tbd'),
    ('Turbulent closure - KPP', 'tbd'),
    ('Turbulent closure - Mellor-Yamada', 'tbd'),
    ('Turbulent closure - Bulk Mixed Layer', 'tbd'),
    ('Richardson number dependent - PP', 'tbd'),
    ('Richardson number dependent - KT', 'tbd'),
    ('Imbeded as isopycnic vertical coordinate', 'tbd'),
    ('Other', 'tbd'),
    ]