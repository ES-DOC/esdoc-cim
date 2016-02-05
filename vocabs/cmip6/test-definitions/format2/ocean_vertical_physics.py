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

_enum_interior_mixing_types = [
        ('Constant value', 'tbd'),
        ('Turbulent closure - TKE', 'tbd'),
        ('Turbulent closure - Mellor-Yamada', 'tbd'),
        ('Richardson number dependent - PP', 'tbd'),
        ('Richardson number dependent - KT', 'tbd'),
        ('Imbeded as isopycnic vertical coordinate', 'tbd'),
        ('Other', 'tbd'),
    ]


vertical_physics = {
    "help": "Properties of  vertical physics within the ocean component",
    "type": "science.process",

    "attributes": {
        "description": "General properties of vertical physics in the ocean",
        "type": "science.sub_process",
        "cardinality": "1.1",

        "scheme": {
            "help": "Types of convection scheme in ocean",
            "type": "enum",
            "cardinality": "1.1",
            "choices": [
                ('Non-penetrative convective adjustment', 'tbd'),
                ('Enhanced vertical diffusion', 'tbd'),
                ('Included in turbulence closure', 'tbd'),
                ('Other', 'tbd'),
            ]
        },
        "tide_induced_mixing": {
            "help": "Describe how tide induced mixing is modelled (barotropic, baroclinic, none)",
            "type": "str",
            "cardinality": "1.1"
        },
        "langmuir_cells_mixing": {
            "help": "Is there Langmuir cells mixing in upper ocean ?",
            "type": "str",
            "cardinality": "1.1"
        },
    },

    "boundary_layer_mixing": {
        "help": "Key properties of boundary layer mixing in the ocean (aka mixed layer)",
        "type": "science.sub_process",
        "cardinality": "1.1",

        "tracers": {
            "help": "Properties of boundary layer mixing on tracers in ocean",
            "type": "science.process_detail",
            "cardinality": "1.1",

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
        },

        "momentum": {
            "help": "Properties of boundary layer mixing on momentum in ocean",
            "type": "science.process_detail",
            "cardinality": "1.1",

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
    },

    "interior_mixing": {
        "help": "Key properties of interior mixing in the ocean",
        "type": "science.sub_process",
        "cardinality": "1.1",

        "tracers": {
            "help": "Properties of interior mixing on tracers in ocean",
            "type": "science.process_detail",
            "cardinality": "1.1",

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
        },

        "momentum": {
            "help": "Properties of interior mixing on momentum in ocean",
            "type": "science.process_detail",
            "cardinality": "1.1",

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
    }
}