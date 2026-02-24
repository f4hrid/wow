
import pygame
import sys
from pygame._sdl2 import Window
from game.renderer import Renderer
from game.world import World
from typing import Any
from game.config import MAXIMIZED, WIDTH, HEIGHT, FPS


class Game:
    """ Clase del juego. """

    def __init__(self):
        """ Constructor: """

        self.fps = FPS
        self.maximized = not MAXIMIZED
        self.width, self.height = WIDTH, HEIGHT

        self.renderer: Renderer = Renderer(self.width, self.height)
        self.world: World = World()
        self.renderer.world = self.world


    def loop(self):
        """ Loop del juego. """

        clock = pygame.time.Clock()

        while True:
            if not self.maximized:
                Window.from_display_module().maximize()
                self.maximized = True

            input_events: list[Any] = pygame.event.get()
            for event in input_events:
                if event.type == pygame.QUIT:
                    close()


            self._handle_inputs()

            self.world.update()
            self.renderer.render()
            clock.tick(self.fps)


    def _handle_inputs(self):
        key = pygame.key.get_pressed()
        self.world.player.is_leftward = key[pygame.K_a] and not key[pygame.K_d]
        self.world.player.is_rightward = key[pygame.K_d] and not key[pygame.K_a]
        self.world.player.is_upward = key[pygame.K_w]


def close() -> None:
    """ Cierra el juego. """
    pygame.quit()
    sys.exit()

def main() -> None:
    """ Corre el juego. """
    pygame.init()
    app = Game()
    app.loop()
    close()