import pygame
from pygame.locals import RESIZABLE

class Renderer:
    """ Clase de renderizador. """

    def __init__(self, width, height):
        """ Constructor: """

        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height), RESIZABLE)
        self.world = None


    def render(self):
        """ Renderiza y actualiza la ventana. """

        self.screen.fill(pygame.Color("black"))

        #self.screen.blit(*self.world.draw()) ARREGLAR AQUI

        self.screen.blit(*self.world.player.draw())
        # self.screen.blit(*self.world.player.draw_rect()) # DIBUJAR EL RECTANGULO DE POSICIÓN
        self.screen.blit(*self.world.player.properties())

        pygame.display.flip()