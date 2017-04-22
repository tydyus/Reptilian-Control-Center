import sdl2.ext
from sdl2 import render


class TextureRenderer(sdl2.ext.TextureSpriteRenderSystem):
    def __init__(self, window):
        super(TextureRenderer, self).__init__(window)
        self.window = window

    def render(self, components):
        render.SDL_RenderClear(self.sdlrenderer)
        super(TextureRenderer, self).render(components)
