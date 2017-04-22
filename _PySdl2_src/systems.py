import sdl2.ext

import components


class DevelopmentSystem(sdl2.ext.System):
    def __init__(self):
        # Yes, the trailing comma is because PYTHON SYNTAX <3
        # Also, pysdl2 has shitty error reporting.
        self.componenttypes = (components.DevelopmentFactor, )

    def process(self, world, development_factors):
        for factor in development_factors:
            factor.value += 2
