import sdl2.ext


class TextureRenderer(sdl2.ext.TextureSpriteRenderSystem):
    def __init__(self, window):
        super(TextureRenderer, self).__init__(window)

    def render(self, components):
        super(TextureRenderer, self).render(components)
