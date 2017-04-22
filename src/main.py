from sys import exit

import sdl2
import sdl2.ext

from rendering import SoftwareRenderer


def main():
    sdl2.ext.init()
    window = sdl2.ext.Window("Reptilian Control Center", size=(854, 480))
    window.show()

    world = sdl2.ext.World()
    world.add_system(SoftwareRenderer(window))

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False

        world.process()
        
    return 0

if __name__ == "__main__":
    exit(main())
