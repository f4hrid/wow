import pygame, typing
from game.config import GRAVITY


class World:
    def __init___(self):
        self.floor = 555

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        surface.fill(pygame.Color("black"))


    @staticmethod
    def apply_gravity(dy: int):
        dy += GRAVITY
        print(dy)
