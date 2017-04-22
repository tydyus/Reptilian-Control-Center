import sdl2.ext
import components


class ControlCenter(sdl2.ext.Entity):
    def __init__(self, world, sprite):
        self.sprite = sprite

class Earth(sdl2.ext.Entity):
    def __init__(self, world):
        self.developmentfactor = components.DevelopmentFactor()
