from sys import exit

import sdl2
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "../img")

from rendering import TextureRenderer
import entities
import systems


def main():
    sdl2.ext.init()
    window = sdl2.ext.Window("Reptilian Control Center", size=(854, 480))
    window.show()

    world = sdl2.ext.World()
    rendersystem = TextureRenderer(window)
    world.add_system(rendersystem)
    world.add_system(systems.DevelopmentSystem())
    earth = entities.Earth(world)

    factory = sdl2.ext.SpriteFactory(sdl2.ext.TEXTURE,
                                     renderer=rendersystem)
    sprite = factory.from_image(RESOURCES.get_path("controlCenter.png"))

    control_center = entities.ControlCenter(world, sprite)
    

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False

        world.process()
        print(earth.developmentfactor.value)
        
    return 0

if __name__ == "__main__":
    exit(main())
