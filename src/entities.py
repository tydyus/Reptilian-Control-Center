import sdl2.ext
import components


class Earth(sdl2.ext.Entity):
    def __init__(self, world):
        self.developmentfactor = components.DevelopmentFactor()
