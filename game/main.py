
import pygame
import sys
from pygame._sdl2 import Window
from game.renderer import Renderer
from game.world import World
from typing import Any
from game.config import MAXIMIZED, WIDTH, HEIGHT, FPS

def close() -> None:
    """ Cierra el juego. """
    pygame.quit()
    sys.exit()

def main(mode=None) -> None:
    """ Corre el juego. """
    pygame.init()
    app = Game(mode)
    app.loop()
    close()


class Game:
    """ Configuración del juego. """

    def __init__(self, mode):
        """ Constructor: """

        self.fps = FPS
        self.setting = mode
        self.maximized = MAXIMIZED
        self.width, self.height = WIDTH, HEIGHT

        self.renderer: Renderer = Renderer(self.width, self.height)
        self.world: World = World()
        self.renderer.world = self.world


    def loop(self):
        """ Loop del juego. """

        clock = pygame.time.Clock()

        while True:
            if not self.maximized and not self.setting:
                Window.from_display_module().maximize()
                self.maximized = True

            self.input_events()

            self.handle_inputs()

            self.world.update(self.setting)
            self.renderer.render(self.setting)
            clock.tick(self.fps)

    @staticmethod
    def input_events() -> None:
        input_events: list[Any] = pygame.event.get()
        for event in input_events:
            if event.type == pygame.QUIT:
                close()

    def handle_inputs(self):
        key = pygame.key.get_pressed()
        self.world.player.is_leftward = key[pygame.K_a] and not key[pygame.K_d]
        self.world.player.is_rightward = key[pygame.K_d] and not key[pygame.K_a]
        self.world.player.is_upward = key[pygame.K_w]