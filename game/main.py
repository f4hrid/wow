
import pygame
import sys
from game.world import World
from game.player import Player
from typing import Any
from pygame._sdl2 import Window
from game.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=[SCREEN_WIDTH, SCREEN_HEIGHT], flags=pygame.RESIZABLE)
        self.clock = pygame.time.Clock()

        self.world: World = World()
        self.player: Player = Player(self.world)

        #Window.from_display_module().maximize() # ventana completa


    def loop(self):
        while True:
            input_events: list[Any] = pygame.event.get()
            for event in input_events:
                if event.type == pygame.QUIT:
                    Game.quit()

            self.input()
            self.update()
            self.draw()
            self.clock.tick(FPS)

            pygame.display.flip()

    def input(self):
        self.player.handle_input()

    def update(self):
        self.world.update()
        self.player.update()

    def draw(self):
        self.world.draw(self.screen)
        self.player.draw(self.screen)

    def start(self):
        self.loop()

    @staticmethod
    def quit() -> None:
        pygame.quit()
        sys.exit()