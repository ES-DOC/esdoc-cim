"""Ocean vertical physics attributes.

type: science.sub_process

"""


def props():
    """Properties of vertical physics in ocean.

    type: science.process_detail

    """
    return {
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
        }
    }
