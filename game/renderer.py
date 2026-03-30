import pygame
from pygame.locals import RESIZABLE

class Renderer:
    """ Clase de renderizado. """

    def __init__(self, width, height):
        """ Constructor: """

        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height), RESIZABLE)
        self.world = None


    def render(self, mode):
        """ Renderiza y actualiza la ventana. """

        self.screen.fill(pygame.Color("white"))
        #self.screen.blit(*self.world.draw())
        self.screen.blit(*self.world.player.draw())

        pygame.draw.rect(self.screen, "cyan", (0,555,800,-10))

        if mode == "test":
            if hasattr(self.world.player, "hitbox"):
                pygame.draw.rect(self.screen, "gray", self.world.player.position, 1)
                pygame.draw.rect(self.screen, "green", self.world.player.hitbox, 1)

            self.screen.blit(*self.world.player.properties())

        pygame.display.flip()